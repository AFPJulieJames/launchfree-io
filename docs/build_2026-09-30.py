#!/usr/bin/env python3
# One-off build script for the 2026-09-30 batch (71 approved submissions).
# Builds new listing pages from docs/LISTING_TEMPLATE_SSR.html, appends listings.json + sitemap.xml.
# Deleted after use.
import json
import os
import re
import html as htmllib
from datetime import datetime
from urllib.parse import quote

ROOT = os.getcwd()
TEMPLATE = open(os.path.join(ROOT, "docs", "LISTING_TEMPLATE_SSR.html"), encoding="utf-8").read()
TEMPLATE = re.sub(r"\n?  <!--\n    LaunchFree\.io canonical listing template.*?-->\n", "\n", TEMPLATE, flags=re.S)

DATA = json.load(open(os.path.join(ROOT, "listings.json"), encoding="utf-8"))
BY_SLUG = {r["slug"]: r for r in DATA}
DEFAULT_OG = "https://launchfree.io/og-image.png"
TODAY = "2026-09-30"


def slugify(name):
    s = name.lower()
    s = s.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
    s = s.replace("ñ", "n").replace("ü", "u")
    s = s.replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    s = re.sub(r"-{2,}", "-", s)
    return s


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


def paragraphs(raw):
    if not raw:
        return ""
    parts = [p.strip() for p in re.split(r"\n\s*\n", raw) if p.strip()] or [raw]
    out = []
    for p in parts:
        p = fix_dashes(" ".join(p.split()))
        if p:
            out.append("<p>%s</p>" % esc(p))
    return "".join(out)


def long_date(iso):
    return datetime.strptime(iso, "%Y-%m-%d").strftime("%B %-d, %Y")


def urlenc(t):
    return quote(t or "", safe="")


def truncate_desc(t, n=150):
    if not t or len(t) <= n:
        return t or ""
    cut = t[:n]
    cut = cut.rsplit(" ", 1)[0]
    return cut + "…"


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
            s=p["slug"], e=esc(p.get("emoji") or fix_name_dashes(p["name"])[:1].upper()),
            n=esc(fix_name_dashes(p["name"])), c=esc(p["cat"]))
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


SUBMISSIONS = json.load(open(os.path.join(ROOT, "_build_tmp", "submissions.json"), encoding="utf-8"))

built = []
skipped = []
for sub in SUBMISSIONS:
    name_raw = sub["name"]
    slug = slugify(name_raw)
    if slug in BY_SLUG:
        print("COLLISION, skipping:", name_raw, slug)
        skipped.append((name_raw, slug))
        continue

    name_fixed = fix_name_dashes(name_raw)
    tagline_fixed = fix_dashes(sub["tagline"])
    logo = sub.get("logo") or ""
    ss1 = sub.get("screenshot1") or ""
    og_image = logo or ss1 or DEFAULT_OG
    initial = esc(name_fixed[:1].upper())
    if logo:
        logo_block = ('<img src="%s" alt="%s" loading="lazy" '
                     'onerror="this.outerHTML=\'%s\'" />' % (esc(logo), esc(name_fixed), initial))
    else:
        logo_block = initial

    gallery_imgs = []
    for s in (ss1,):
        if s:
            gallery_imgs.append('<div class="gallery-img"><img src="%s" alt="%s screenshot" loading="lazy" /></div>'
                                % (esc(s), esc(name_fixed)))
    gallery_html = "".join(gallery_imgs)

    extra_links = ""
    if sub.get("twitter"):
        handle = sub["twitter"].lstrip("@")
        extra_links += '<a href="https://x.com/%s" target="_blank" rel="noopener" class="builder-link">X / Twitter</a>' % esc(handle)
    if sub.get("linkedin"):
        extra_links += '<a href="%s" target="_blank" rel="noopener" class="builder-link">LinkedIn</a>' % esc(sub["linkedin"])

    builder_handle = esc(sub["twitter"]) if sub.get("twitter") else ""

    stage = sub.get("stage") or "Live"

    vals = {
        "NAME": esc(name_fixed),
        "SLUG": slug,
        "TAGLINE": esc(tagline_fixed),
        "CATEGORY": esc(sub["cat"]),
        "STAGE": esc(stage),
        "DATE_LONG": long_date(TODAY),
        "PRODUCT_URL": esc(sub["url"]),
        "TAGLINE_NOSTOP": esc(tagline_fixed.rstrip(" .!")),
        "NAME_URLENC": urlenc(name_raw),
        "TAGLINE_URLENC": urlenc(tagline_fixed),
        "DESCRIPTION_HTML": paragraphs(sub["description"]) or "<p>%s</p>" % esc(tagline_fixed),
        "BUILDER_STORY": esc(fix_dashes(sub.get("story") or "")),
        "BUILDER_NAME": esc(fix_dashes(sub["builder_name"])),
        "BUILDER_BIO": esc(fix_dashes(sub.get("bio") or "")),
        "BUILDER_HANDLE": builder_handle,
        "BUILDER_INITIAL": esc((sub["builder_name"] or name_fixed)[:1].upper()),
        "BUILDER_EXTRA_LINKS": extra_links,
        "PRICING": esc(sub.get("pricing") or ""),
        "LOGO_BLOCK": logo_block,
        "OG_IMAGE_URL": esc(og_image),
        "GALLERY_IMAGES": gallery_html,
        "RELATED_CARDS": related_cards({"slug": slug, "cat": sub["cat"], "name": name_raw}),
        "_featured": False,
    }

    page = render(vals)
    left = re.findall(r"\{\{[A-Z_]+\}\}", page)
    if left:
        print("UNFILLED", slug, set(left))
        continue

    path = os.path.join(ROOT, "listings", slug + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(page)

    new_rec = {
        "id": slug,
        "name": name_fixed,
        "tagline": tagline_fixed,
        "desc": truncate_desc(sub["description"]),
        "emoji": name_fixed[:1].upper(),
        "logo": logo,
        "cat": sub["cat"],
        "url": sub["url"],
        "stage": stage,
        "votes": 0,
        "featured": False,
        "slug": slug,
        "date": TODAY,
        "mrr": "",
    }
    built.append((name_raw, slug, sub["id"]))
    BY_SLUG[slug] = new_rec
    DATA.append(new_rec)
    by_cat.setdefault(sub["cat"], []).insert(0, new_rec)
    newest.insert(0, new_rec)

with open(os.path.join(ROOT, "listings.json"), "w", encoding="utf-8") as f:
    json.dump(DATA, f, ensure_ascii=False, indent=1)
    f.write("\n")

sitemap_path = os.path.join(ROOT, "sitemap.xml")
sitemap = open(sitemap_path, encoding="utf-8").read()
blocks = "".join(
    '<url><loc>https://launchfree.io/listings/%s.html</loc><lastmod>%s</lastmod>'
    '<changefreq>weekly</changefreq><priority>0.6</priority></url>\n' % (slug, TODAY)
    for _, slug, _ in built
)
sitemap = sitemap.replace("</urlset>", blocks + "</urlset>")
with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(sitemap)

print("\nBUILT %d pages:" % len(built))
for name, slug, _ in built:
    print(" -", name, "->", slug + ".html")

if skipped:
    print("\nSKIPPED (collision) %d:" % len(skipped))
    for name, slug in skipped:
        print(" -", name, "->", slug)

with open(os.path.join(ROOT, "_build_tmp", "build_result.json"), "w", encoding="utf-8") as f:
    json.dump({"built": built, "skipped": skipped}, f, indent=2)
