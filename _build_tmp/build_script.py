#!/usr/bin/env python3
"""One-off build script for the 2026-09-23 runway-review batch. Builds fresh
listing pages for the 108 collision-clean Approved records, appends them to
listings.json and sitemap.xml. Delete this file after the build completes."""
import json, re, os, sys, html as htmllib, unicodedata
from datetime import datetime
from urllib.parse import quote

ROOT = os.path.expanduser("~/mnt/launchfree-io")
TODAY = datetime.now().strftime("%Y-%m-%d")
DEFAULT_OG = "https://launchfree.io/og-image.png"

TEMPLATE = open(os.path.join(ROOT, "docs", "LISTING_TEMPLATE_SSR.html"), encoding="utf-8").read()
TEMPLATE = re.sub(r"\n?  <!--\n    LaunchFree\.io canonical listing template.*?-->\n", "\n", TEMPLATE, flags=re.S)

LISTINGS_PATH = os.path.join(ROOT, "listings.json")
DATA = json.load(open(LISTINGS_PATH, encoding="utf-8"))

APPROVED = json.load(open(os.path.join(ROOT, "_build_tmp", "approved_full_corrected.json"), encoding="utf-8"))
APPROVED_BY_ID = {r["id"]: r for r in APPROVED}

COLLISION = json.load(open("/tmp/collision_report2.json", encoding="utf-8"))
CLEAN_IDS = [x["id"] for x in COLLISION["clean"]]
CLEAN_SLUGS = {x["id"]: x["slug"] for x in COLLISION["clean"]}

CATEGORIES = {
    "AI / ML", "Affiliate", "Community", "Creator Tools", "Developer Tools",
    "E-commerce", "Education", "Entertainment", "Fintech", "Health", "Lifestyle",
    "Marketing", "Other", "Productivity", "SaaS", "Service", "Travel",
}
STAGES = {"Live", "Beta", "Coming Soon", "In Development"}


def slugify(name):
    s = name.lower()
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace('&', ' and ')
    s = re.sub(r'[^a-z0-9]+', '-', s)
    s = s.strip('-')
    s = re.sub(r'-+', '-', s)
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
    parts = [p.strip() for p in re.split(r"\n\s*\n", raw) if p.strip()]
    if not parts:
        parts = [raw.strip()]
    out = []
    for p in parts:
        p = fix_dashes(" ".join(p.split()))
        if p:
            out.append("<p>%s</p>" % htmllib.escape(p, quote=False))
    return "".join(out)


def long_date(iso):
    return datetime.strptime(iso, "%Y-%m-%d").strftime("%B %-d, %Y")


def urlenc(t):
    return quote(t or "", safe="")


def truncate_desc(desc):
    d = fix_dashes(" ".join((desc or "").split()))
    if len(d) <= 150:
        return d
    cut = d[:150]
    cut = cut.rsplit(" ", 1)[0]
    return cut + "…"


# ------------------------------------------------------------------ related launches (computed once at start; new records use category pools from existing data, refreshed incrementally)
by_cat = {}
for r in DATA:
    by_cat.setdefault(r["cat"], []).append(r)
for v in by_cat.values():
    v.sort(key=lambda r: (r.get("date", ""), r["slug"]), reverse=True)


def related_cards(rec, all_data):
    cat_pool = [r for r in all_data if r["cat"] == rec["cat"] and r["slug"] != rec["slug"]]
    cat_pool.sort(key=lambda r: (r.get("date", ""), r["slug"]), reverse=True)
    newest_pool = sorted(all_data, key=lambda r: (r.get("date", ""), r["slug"]), reverse=True)
    picks, seen = [], {rec["slug"]}
    for pool in (cat_pool, newest_pool):
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


def build_vals(sub, slug, all_data):
    name = sub["name"]
    tagline = sub["tagline"]
    cat = sub["cat"]
    stage = sub.get("stage") or "Live"
    if stage not in STAGES:
        stage = "Live"
    url = sub["url"]
    desc = sub.get("desc") or ""
    bstory = sub.get("bstory") or ""
    bname = sub.get("bname") or name
    bbio = sub.get("bbio") or ""
    twitter = (sub.get("twitter") or "").strip()
    linkedin = (sub.get("linkedin") or "").strip()
    logo = (sub.get("logo") or "").strip()
    pricing = (sub.get("pricing") or "").strip()
    ss = [s for s in (sub.get("ss1"), sub.get("ss2"), sub.get("ss3")) if s and s.strip()]

    vals = {}
    vals["NAME"] = esc(fix_name_dashes(name))
    vals["SLUG"] = slug
    vals["TAGLINE"] = esc(fix_dashes(tagline))
    vals["TAGLINE_NOSTOP"] = esc(fix_dashes(tagline).rstrip(" .!"))
    vals["CATEGORY"] = esc(cat)
    vals["STAGE"] = esc(stage)
    vals["DATE_LONG"] = long_date(TODAY)
    vals["PRODUCT_URL"] = esc(url)
    vals["DESCRIPTION_HTML"] = paragraphs(desc) or "<p>%s</p>" % esc(fix_dashes(tagline))
    vals["BUILDER_STORY"] = htmllib.escape(fix_dashes(" ".join(bstory.split())), quote=False) if bstory.strip() else ""
    vals["BUILDER_NAME"] = esc(fix_dashes(bname))
    vals["BUILDER_BIO"] = htmllib.escape(fix_dashes(" ".join(bbio.split())), quote=False)

    # twitter handle display text
    handle = ""
    twitter_url = ""
    if twitter:
        h = twitter.lstrip("@").strip()
        if h.startswith("http"):
            twitter_url = h
            handle = "@" + h.rstrip("/").split("/")[-1]
        else:
            handle = "@" + h
            twitter_url = "https://twitter.com/" + h
    vals["BUILDER_HANDLE"] = esc(handle)
    vals["BUILDER_INITIAL"] = esc((bname or name)[:1].upper())

    extra = ""
    if twitter_url and twitter_url.rstrip("/") != url.rstrip("/"):
        extra += '<a href="%s" target="_blank" rel="noopener" class="builder-link">Twitter</a>' % esc(twitter_url)
    if linkedin and linkedin.rstrip("/") != url.rstrip("/"):
        extra += '<a href="%s" target="_blank" rel="noopener" class="builder-link">LinkedIn</a>' % esc(linkedin)
    vals["BUILDER_EXTRA_LINKS"] = extra

    vals["PRICING"] = esc(pricing)

    initial = esc((name[:1] or "L").upper())
    if logo:
        vals["LOGO_BLOCK"] = ('<img src="%s" alt="%s" loading="lazy" '
                              'onerror="this.outerHTML=\'%s\'" />' % (esc(logo), esc(name), initial))
    else:
        vals["LOGO_BLOCK"] = initial
    vals["OG_IMAGE_URL"] = esc(logo or DEFAULT_OG)

    imgs = []
    for s in ss:
        imgs.append('<div class="gallery-img"><img src="%s" alt="%s screenshot" loading="lazy" /></div>'
                    % (esc(s), esc(name)))
    vals["GALLERY_IMAGES"] = "".join(imgs)

    vals["NAME_URLENC"] = urlenc(name)
    vals["TAGLINE_URLENC"] = urlenc(fix_dashes(tagline))
    vals["RELATED_CARDS"] = related_cards({"slug": slug, "cat": cat}, all_data)
    vals["_featured"] = False
    return vals


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


def main():
    built = []
    problems = []
    working_data = list(DATA)
    seen_slugs = {r["slug"] for r in DATA}

    for rid in CLEAN_IDS:
        sub = APPROVED_BY_ID[rid]
        slug = CLEAN_SLUGS[rid]
        if slug in seen_slugs:
            problems.append("%s: slug '%s' collides WITHIN this batch, needs manual qualifier" % (rid, slug))
            continue
        seen_slugs.add(slug)

        vals = build_vals(sub, slug, working_data)
        page = render(vals)
        left = re.findall(r"\{\{[A-Z_]+\}\}", page)
        if left:
            problems.append("%s (%s): unfilled placeholders %s" % (rid, slug, set(left)))
            continue

        path = os.path.join(ROOT, "listings", slug + ".html")
        if os.path.exists(path):
            problems.append("%s (%s): listings/%s.html already exists on disk!" % (rid, slug, slug))
            continue
        with open(path, "w", encoding="utf-8") as f:
            f.write(page)

        stage = sub.get("stage") or "Live"
        if stage not in STAGES:
            stage = "Live"
        record = {
            "id": slug,
            "name": sub["name"],
            "tagline": fix_dashes(sub["tagline"]),
            "desc": truncate_desc(sub.get("desc") or ""),
            "emoji": (sub["name"][:1] or "L").upper(),
            "logo": sub.get("logo") or "",
            "cat": sub["cat"],
            "url": sub["url"],
            "stage": stage,
            "votes": 0,
            "featured": False,
            "slug": slug,
            "date": TODAY,
            "mrr": "",
        }
        working_data.append(record)
        by_cat.setdefault(record["cat"], []).append(record)
        built.append({"id": rid, "slug": slug, "name": sub["name"], "url": sub["url"], "cat": sub["cat"]})

    # write listings.json (append all new records)
    json.dump(working_data, open(LISTINGS_PATH, "w", encoding="utf-8"), indent=1, ensure_ascii=False)

    # update sitemap.xml
    sitemap_path = os.path.join(ROOT, "sitemap.xml")
    sitemap = open(sitemap_path, encoding="utf-8").read()
    new_urls = "".join(
        '<url><loc>https://launchfree.io/listings/%s.html</loc><lastmod>%s</lastmod>'
        '<changefreq>weekly</changefreq><priority>0.6</priority></url>' % (b["slug"], TODAY)
        for b in built
    )
    sitemap = sitemap.replace("</urlset>", new_urls + "</urlset>")
    open(sitemap_path, "w", encoding="utf-8").write(sitemap)

    print("BUILT: %d pages" % len(built))
    print("PROBLEMS: %d" % len(problems))
    for p in problems:
        print("  " + p)

    json.dump({"built": built, "problems": problems}, open("/tmp/build_result.json", "w"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
