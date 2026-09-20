#!/usr/bin/env python3
"""One-off build script for the 2026-09-20 second-round batch (47 fresh listings).
Standalone: does not import rebuild_listings.py (avoids its main()/sys.exit() side effect
and a prior FUSE deadlock reading existing pages). Inlines only the needed render helpers."""
import json, os, re, sys, html as htmllib
from datetime import datetime
from urllib.parse import quote, urlsplit

ROOT = os.getcwd()
TEMPLATE = open(os.path.join(ROOT, "docs", "LISTING_TEMPLATE_SSR.html"), encoding="utf-8").read()
TEMPLATE = re.sub(r"\n?  <!--\n    LaunchFree\.io canonical listing template.*?-->\n", "\n", TEMPLATE, flags=re.S)

DATA = json.load(open(os.path.join(ROOT, "listings.json"), encoding="utf-8"))
BY_SLUG = {r["slug"]: r for r in DATA}
DEFAULT_OG = "https://launchfree.io/og-image.png"

NEW = json.load(open(os.path.join(ROOT, "docs", "build47_input.json"), encoding="utf-8"))
TODAY = "2026-09-20"

CAT_FIX = {"saas": "SaaS"}

def fix_dashes(t):
    if not t:
        return t
    t = re.sub(r"(?<=[\d$])\s*[—–]\s*(?=[\d$])", "-", t)
    t = re.sub(r"\s*[—–]\s*", ", ", t)
    t = re.sub(r",\s*,", ",", t)
    t = re.sub(r"\s+,", ",", t)
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

def long_date(iso):
    try:
        return datetime.strptime(iso, "%Y-%m-%d").strftime("%B %-d, %Y")
    except Exception:
        return iso

def paragraphs(text):
    if not text:
        return ""
    parts = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()] or [text]
    out = []
    for p in parts:
        p = fix_dashes(" ".join(p.split()))
        if p:
            out.append("<p>%s</p>" % htmllib.escape(p, quote=False))
    return "".join(out)

def slugify(name):
    import unicodedata
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
    s = s.lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    s = re.sub(r"-{2,}", "-", s)
    return s

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
    return page

os.makedirs(os.path.join(ROOT, "listings"), exist_ok=True)

new_listing_records = []
built = []
for rec in NEW:
    name = rec["name"]
    slug = slugify(name)
    if slug in BY_SLUG:
        print("SKIP (slug collision at build time):", slug)
        continue
    cat = CAT_FIX.get(rec["cat"], rec["cat"])
    url = rec["url"]
    tagline = fix_dashes(rec["tagline"] or "")
    desc = rec.get("desc") or ""
    story = fix_dashes(rec.get("builder_story") or "")
    bio = fix_dashes(rec.get("builder_bio") or "")
    builder_name = rec.get("builder_name") or name
    twitter = rec.get("twitter")
    linkedin = rec.get("linkedin")
    logo = rec.get("logo") or ""
    pricing = rec.get("pricing") or ""

    extra_links = ""
    if twitter:
        h = twitter if twitter.startswith("http") else "https://twitter.com/%s" % twitter.lstrip("@")
        extra_links += '<a href="%s" target="_blank" rel="noopener" class="builder-link">Twitter</a>' % esc(h)
    if linkedin:
        h = linkedin if linkedin.startswith("http") else "https://linkedin.com/in/%s" % linkedin
        extra_links += '<a href="%s" target="_blank" rel="noopener" class="builder-link">LinkedIn</a>' % esc(h)

    handle = ""
    if twitter:
        handle = "@" + twitter.lstrip("@") if not twitter.startswith("http") else ""

    vals = {}
    vals["NAME"] = esc(name)
    vals["SLUG"] = slug
    vals["TAGLINE"] = esc(tagline)
    vals["TAGLINE_NOSTOP"] = esc(tagline.rstrip(" .!"))
    vals["CATEGORY"] = esc(cat)
    vals["STAGE"] = esc(rec.get("stage") or "Live")
    vals["PRICING"] = esc(pricing)
    vals["DATE_LONG"] = long_date(TODAY)
    vals["PRODUCT_URL"] = esc(url)
    vals["DESCRIPTION_HTML"] = paragraphs(desc) or "<p>%s</p>" % esc(tagline)
    vals["BUILDER_STORY"] = htmllib.escape(story, quote=False) if story else ""
    vals["BUILDER_NAME"] = esc(builder_name)
    vals["BUILDER_INITIAL"] = esc((builder_name or name)[:1].upper())
    vals["BUILDER_BIO"] = htmllib.escape(bio, quote=False)
    vals["BUILDER_HANDLE"] = esc(handle)
    vals["BUILDER_EXTRA_LINKS"] = extra_links
    if logo:
        initial = esc((builder_name or name)[:1].upper())
        vals["LOGO_BLOCK"] = ('<img src="%s" alt="%s" loading="lazy" '
                              'onerror="this.outerHTML=\'%s\'" />' % (esc(logo), esc(name), initial))
    else:
        vals["LOGO_BLOCK"] = esc(name[:1].upper())
    vals["OG_IMAGE_URL"] = esc(logo or DEFAULT_OG)
    gallery_imgs = []
    for k in ("ss1", "ss2", "ss3"):
        v = rec.get(k)
        if v:
            gallery_imgs.append('<div class="gallery-img"><img src="%s" alt="%s screenshot" loading="lazy" /></div>' % (esc(v), esc(name)))
    vals["GALLERY_IMAGES"] = "".join(gallery_imgs)
    vals["NAME_URLENC"] = urlenc(name)
    vals["TAGLINE_URLENC"] = urlenc(tagline)

    temp_rec = {"slug": slug, "name": name, "cat": cat, "date": TODAY, "emoji": None}
    vals["RELATED_CARDS"] = related_cards(temp_rec)

    page = render(vals)
    left = re.findall(r"\{\{[A-Z_]+\}\}", page)
    if left:
        print("UNFILLED", slug, "->", set(left))
        continue

    path = os.path.join(ROOT, "listings", slug + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(page)

    short = fix_dashes((desc or tagline).split("\n\n")[0])
    if len(short) > 150:
        cut = short[:150].rsplit(" ", 1)[0]
        short = cut + "…"

    new_listing_records.append({
        "id": slug,
        "slug": slug,
        "name": name,
        "tagline": tagline,
        "desc": short,
        "cat": cat,
        "stage": rec.get("stage") or "Live",
        "url": url,
        "date": TODAY,
        "votes": 0,
        "mrr": "",
        "logo": logo,
        "emoji": None,
        "featured": False,
    })
    built.append((rec["id"], slug, name))
    # register into BY_SLUG/by_cat/newest so subsequent related_cards calls see it
    BY_SLUG[slug] = temp_rec
    by_cat.setdefault(cat, []).insert(0, temp_rec)
    newest.insert(0, temp_rec)

DATA.extend(new_listing_records)
with open(os.path.join(ROOT, "listings.json"), "w", encoding="utf-8") as f:
    json.dump(DATA, f, indent=2, ensure_ascii=False)

print("\nBuilt %d pages" % len(built))
for rid, slug, name in built:
    print(" ", rid, "->", slug, "(%s)" % name)

with open(os.path.join(ROOT, "docs", "build47_result.json"), "w") as f:
    json.dump({"built": built}, f, indent=2)
