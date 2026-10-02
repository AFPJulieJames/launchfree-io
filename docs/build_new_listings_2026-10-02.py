#!/usr/bin/env python3
"""
One-off batch builder for the 2026-10-02 LaunchFree.io runway-review batch.
Reuses the render/fix_dashes/related_cards logic pattern from docs/rebuild_listings.py,
adapted to build brand-new pages from submission data rather than re-extracting from
existing HTML. Scratch script: delete from docs/ before finishing the session.

Usage (run from repo root):
    python3 docs/build_new_listings_2026-10-02.py                 # dry run: collision check + report
    python3 docs/build_new_listings_2026-10-02.py --write          # actually write pages + data files

Reads docs/build_manifest_2026-10-02.json for the list of approved submissions.
"""
import json
import os
import re
import sys
import html as htmllib
import unicodedata
from datetime import datetime
from urllib.parse import urlparse, quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if not os.path.exists(os.path.join(ROOT, "listings.json")):
    ROOT = os.getcwd()
WRITE = "--write" in sys.argv

TODAY = "2026-10-02"
TODAY_LONG = "October 2, 2026"

TEMPLATE = open(os.path.join(ROOT, "docs", "LISTING_TEMPLATE_SSR.html"), encoding="utf-8").read()
TEMPLATE = re.sub(r"\n?  <!--\n    LaunchFree\.io canonical listing template.*?-->\n", "\n", TEMPLATE, flags=re.S)

DATA = json.load(open(os.path.join(ROOT, "listings.json"), encoding="utf-8"))
BY_SLUG = {r["slug"]: r for r in DATA}

MANIFEST = json.load(open(os.path.join(ROOT, "docs", "build_manifest_2026-10-02.json"), encoding="utf-8"))

DEFAULT_OG = "https://launchfree.io/og-image.png"


# ------------------------------------------------------------------ shared helpers (ported from rebuild_listings.py)
def fix_dashes(t):
    if not t:
        return t
    t = re.sub(r"(?<=[\d$])\s*[—–]\s*(?=[\d$])", "-", t)
    t = re.sub(r"\s*[—–]\s*", ", ", t)
    t = re.sub(r",\s*,", ",", t)
    t = re.sub(r"\s+,", ",", t)
    return t


def fix_name_dashes(t):
    if not t:
        return t
    t = re.sub(r"(?<=[\d$])\s*[—–]\s*(?=[\d$])", "-", t)
    t = re.sub(r"\s*[—–]\s*", ": ", t)
    return t


def esc(t):
    s = t or ""
    prev = None
    while s != prev:
        prev = s
        s = htmllib.unescape(s)
    return htmllib.escape(s, quote=True)


def urlenc(t):
    return quote(t or "", safe="")


def paragraphs_from_text(text):
    if not text:
        return ""
    parts = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()] or [text.strip()]
    out = []
    for p in parts:
        p = fix_dashes(" ".join(p.split()))
        if p:
            out.append("<p>%s</p>" % esc(p))
    return "".join(out)


def slugify(name):
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    s = s.lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def norm_url(u):
    if not u:
        return ""
    if "//" not in u:
        u = "https://" + u
    p = urlparse(u)
    host = (p.netloc or "").lower()
    if host.startswith("www."):
        host = host[4:]
    path = (p.path or "").rstrip("/")
    query = ("?" + p.query) if p.query else ""
    return host + path + query


EXISTING_URLS = {norm_url(r.get("url", "")): r for r in DATA}

# ------------------------------------------------------------------ related launches (identical pattern to rebuild_listings.py)
by_cat = {}
for r in DATA:
    by_cat.setdefault(r["cat"], []).append(r)
for v in by_cat.values():
    v.sort(key=lambda r: (r.get("date", ""), r["slug"]), reverse=True)
newest = sorted(DATA, key=lambda r: (r.get("date", ""), r["slug"]), reverse=True)


def related_cards(rec):
    picks, seen = [], {rec["slug"]}
    for pool in (by_cat.get(rec["cat"], []), newest):
        for other in pool:
            if len(picks) == 3:
                break
            if other["slug"] in seen:
                continue
            seen.add(other["slug"])
            picks.append(other)
    return "".join(
        '<a href="{s}.html" class="related-card"><div class="related-logo">{e}</div>'
        '<div class="related-info"><div class="related-name">{n}</div>'
        '<div class="related-tag">{c}</div></div></a>'.format(
            s=p["slug"], e=esc(p.get("emoji") or p["name"][:1].upper()),
            n=esc(p["name"]), c=esc(p["cat"]))
        for p in picks)


def render(vals):
    page = TEMPLATE
    for k, v in vals.items():
        if k.startswith("_"):
            continue
        page = page.replace("{{%s}}" % k, v)
    if not vals["GALLERY_IMAGES"]:
        page = re.sub(r'\n\s*<!-- OPTIONAL gallery.*?-->\n\s*<div class="section-card">'
                      r'<div class="section-label">Screenshots</div><div class="gallery"></div></div>',
                      "", page, flags=re.S)
    else:
        page = re.sub(r'\n\s*<!-- OPTIONAL gallery.*?-->\n', "\n      ", page, flags=re.S)
    if not vals["BUILDER_STORY"]:
        page = page.replace(
            '<button class="tab" onclick="switchTab(\'story\',this)">Why I Built This</button>', "")
        page = re.sub(r'<div class="tab-panel" id="panel-story">.*?</div></div>\n', "", page, flags=re.S)
    if not vals["PRICING"]:
        page = page.replace('<span class="tag tag-n" id="tag-pricing"></span>', "")
    page = "\n".join(l for l in page.split("\n") if l.strip())
    if vals["_featured"]:
        page = page.replace('<span class="hero-date"',
                            '<span class="tag tag-feat">Featured on The Runway</span>\n      <span class="hero-date"')
    return page


def build_vals(item, slug):
    name = item["name"]
    tagline = fix_dashes(item["tagline"])
    story = fix_dashes(item.get("builder_story", ""))
    bio = fix_dashes(item.get("builder_bio", ""))
    handle = item.get("twitter", "") or ""
    handle_disp = handle if not handle.startswith("http") else ""
    logo = item.get("logo", "") or ""
    screenshots = item.get("screenshots", []) or []
    pricing = item.get("pricing", "") or ""

    rec_stub = {"slug": slug, "cat": item["category"], "name": name,
                "emoji": name[:1].upper()}

    vals = {}
    vals["NAME"] = esc(fix_name_dashes(name))
    vals["SLUG"] = slug
    vals["TAGLINE"] = esc(tagline)
    vals["CATEGORY"] = esc(item["category"])
    vals["STAGE"] = esc(item["stage"])
    vals["DATE_LONG"] = TODAY_LONG
    vals["PRODUCT_URL"] = esc(item["url"])
    vals["TAGLINE_NOSTOP"] = esc(tagline.rstrip(" .!"))
    vals["NAME_URLENC"] = urlenc(name)
    vals["TAGLINE_URLENC"] = urlenc(tagline)
    vals["RELATED_CARDS"] = related_cards(rec_stub)
    vals["DESCRIPTION_HTML"] = paragraphs_from_text(item["description"]) or "<p>%s</p>" % esc(tagline)
    vals["BUILDER_STORY"] = esc(story) if story else ""
    vals["BUILDER_NAME"] = fix_dashes(item.get("builder_name", "")) or name
    vals["BUILDER_BIO"] = esc(bio)
    vals["BUILDER_HANDLE"] = esc(handle_disp)
    vals["BUILDER_INITIAL"] = esc((vals["BUILDER_NAME"] or name)[:1].upper())
    vals["PRICING"] = esc(pricing)

    extra = ""
    linkedin = item.get("linkedin", "") or ""
    if linkedin:
        href = linkedin if linkedin.startswith("http") else "https://" + linkedin
        extra += '<a href="%s" target="_blank" rel="noopener" class="builder-link">LinkedIn</a>' % esc(href)
    if handle.startswith("http"):
        extra += '<a href="%s" target="_blank" rel="noopener" class="builder-link">Twitter / X</a>' % esc(handle)
    vals["BUILDER_EXTRA_LINKS"] = extra

    initial = esc(name[:1].upper())
    if logo:
        vals["LOGO_BLOCK"] = ('<img src="%s" alt="%s" loading="lazy" '
                              'onerror="this.outerHTML=\'%s\'" />' % (esc(logo), esc(name), initial))
    else:
        vals["LOGO_BLOCK"] = initial
    vals["OG_IMAGE_URL"] = esc(logo or DEFAULT_OG)

    imgs = []
    for s in screenshots:
        imgs.append('<div class="gallery-img"><img src="%s" alt="%s screenshot" loading="lazy" /></div>'
                    % (esc(s), esc(name)))
    vals["GALLERY_IMAGES"] = "".join(imgs)

    vals["_featured"] = False
    return vals


def desc_field(full_desc):
    d = fix_dashes(" ".join(full_desc.split()))
    if len(d) <= 150:
        return d
    cut = d[:150]
    cut = cut.rsplit(" ", 1)[0]
    return cut + "…"


def main():
    report_built = []
    report_skipped = []
    new_records = []
    before_count = len(DATA)
    id_map = []  # (record_id, slug) for airtable follow-up

    for item in MANIFEST:
        name = item["name"]
        slug = slugify(name)
        nurl = norm_url(item["url"])
        collision = None
        if slug in BY_SLUG:
            collision = ("slug", slug, BY_SLUG[slug]["url"])
        elif nurl in EXISTING_URLS:
            collision = ("url", nurl, EXISTING_URLS[nurl]["slug"])

        if collision:
            report_skipped.append((name, slug, collision, item["record_id"]))
            continue

        vals = build_vals(item, slug)
        page = render(vals)
        left = re.findall(r"\{\{[A-Z_]+\}\}", page)
        if left:
            print("UNFILLED %s -> %s" % (slug, set(left)))
            report_skipped.append((name, slug, ("unfilled", left, ""), item["record_id"]))
            continue

        rec = {
            "id": slug,
            "name": name,
            "tagline": fix_dashes(item["tagline"]),
            "desc": desc_field(item["description"]),
            "emoji": name[:1].upper(),
            "logo": item.get("logo", "") or "",
            "cat": item["category"],
            "url": item["url"],
            "stage": item["stage"],
            "votes": 0,
            "featured": False,
            "slug": slug,
            "date": TODAY,
            "mrr": "",
        }

        if WRITE:
            path = os.path.join(ROOT, "listings", slug + ".html")
            with open(path, "w", encoding="utf-8") as f:
                f.write(page)

        new_records.append(rec)
        report_built.append((name, slug))
        id_map.append({"record_id": item["record_id"], "slug": slug, "name": name})
        BY_SLUG[slug] = rec
        EXISTING_URLS[nurl] = rec

    print("=== COLLISIONS (skip) ===")
    for name, slug, c, rid in report_skipped:
        print("SKIP  %-32s slug=%-40s reason=%s  record=%s" % (name, slug, c, rid))
    print()
    print("=== TO BUILD ===")
    for name, slug in report_built:
        print("BUILD %-32s -> %s" % (name, slug))
    print()
    print("%d to build, %d skipped (collisions), %d input items" % (len(report_built), len(report_skipped), len(MANIFEST)))

    if WRITE and new_records:
        DATA.extend(new_records)
        with open(os.path.join(ROOT, "listings.json"), "w", encoding="utf-8") as f:
            json.dump(DATA, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print("\nlistings.json: %d -> %d" % (before_count, len(DATA)))

        sm_path = os.path.join(ROOT, "sitemap.xml")
        sm = open(sm_path, encoding="utf-8").read()
        blocks = "".join(
            "  <url>\n    <loc>https://launchfree.io/listings/%s.html</loc>\n"
            "    <lastmod>%s</lastmod>\n    <changefreq>weekly</changefreq>\n"
            "    <priority>0.6</priority>\n  </url>\n" % (r["slug"], TODAY)
            for r in new_records
        )
        sm = sm.rstrip()
        assert sm.endswith("</urlset>")
        sm = sm[: -len("</urlset>")] + blocks + "</urlset>\n"
        with open(sm_path, "w", encoding="utf-8") as f:
            f.write(sm)
        print("sitemap.xml: +%d urls" % len(new_records))

        with open(os.path.join(ROOT, "docs", "_built_id_map_2026-10-02.json"), "w", encoding="utf-8") as f:
            json.dump(id_map, f, indent=1)
        print("wrote docs/_built_id_map_2026-10-02.json (%d entries) for Airtable follow-up" % len(id_map))

    if not WRITE:
        print("\nDry run. Re-run with --write to apply.")
    return 0


sys.exit(main())
