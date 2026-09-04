#!/usr/bin/env python3
"""
Rebuild every listing page from docs/LISTING_TEMPLATE_SSR.html.

Reads each existing listings/<slug>.html, extracts its real content, and re-renders it from the
one canonical template so all pages share a single structure. Content, slugs and URLs are
unchanged. Run from the repo root:

    python3 docs/rebuild_listings.py            # dry run, reports what it would do
    python3 docs/rebuild_listings.py --write    # actually rewrite the pages

Never touches git.
"""
import json
import os
import re
import sys
import html as htmllib
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if not os.path.exists(os.path.join(ROOT, "listings.json")):
    ROOT = os.getcwd()
WRITE = "--write" in sys.argv

TEMPLATE = open(os.path.join(ROOT, "docs", "LISTING_TEMPLATE_SSR.html"), encoding="utf-8").read()
# the build-instruction comment does not belong in a built page
TEMPLATE = re.sub(r"\n?  <!--\n    LaunchFree\.io canonical listing template.*?-->\n", "\n", TEMPLATE, flags=re.S)

DATA = json.load(open(os.path.join(ROOT, "listings.json"), encoding="utf-8"))
BY_SLUG = {r["slug"]: r for r in DATA}

DEFAULT_OG = "https://launchfree.io/og-image.png"
VOID = {"img", "br", "hr", "meta", "link", "input", "source", "path", "circle", "line", "rect"}


def inner_html(s, open_tag_match):
    """Return the inner HTML of the element whose opening tag is open_tag_match."""
    tag = re.match(r"<(\w+)", open_tag_match.group(0)).group(1)
    i = open_tag_match.end()
    depth = 1
    pat = re.compile(r"</?%s\b[^>]*>" % tag, re.I)
    while depth:
        m = pat.search(s, i)
        if not m:
            return s[open_tag_match.end():].strip()
        if m.group(0).startswith("</"):
            depth -= 1
            if depth == 0:
                return s[open_tag_match.end():m.start()].strip()
        elif not m.group(0).endswith("/>"):
            depth += 1
        i = m.end()
    return ""


def grab(s, cls, tag=r"\w+"):
    m = re.search(r'<(?:%s)[^>]*class="[^"]*\b%s\b[^"]*"[^>]*>' % (tag, cls), s)
    return inner_html(s, m) if m else None


def text_of(fragment):
    if fragment is None:
        return ""
    t = re.sub(r"<[^>]+>", " ", fragment)
    return " ".join(htmllib.unescape(t).split())


def fix_dashes(t):
    """House style: no em dashes in body copy. Keep the sentence readable."""
    if not t:
        return t
    t = re.sub(r"(?<=[\d$])\s*[—–]\s*(?=[\d$])", "-", t)   # numeric range keeps a hyphen
    t = re.sub(r"\s*[—–]\s*", ", ", t)                    # everything else becomes a comma
    t = re.sub(r",\s*,", ",", t)
    t = re.sub(r"\s+,", ",", t)
    return t


def paragraphs(fragment):
    """Return description HTML as one or more <p> blocks, dashes cleaned."""
    if not fragment:
        return ""
    parts = re.findall(r"<p\b[^>]*>(.*?)</p>", fragment, re.S)
    if not parts:
        raw = text_of(fragment)
        parts = [p.strip() for p in re.split(r"\n\s*\n", raw) if p.strip()] or [raw]
    out = []
    for p in parts:
        p = fix_dashes(" ".join(htmllib.unescape(re.sub(r"<[^>]+>", "", p)).split()))
        if p:
            out.append("<p>%s</p>" % htmllib.escape(p, quote=False))
    return "".join(out)


def long_date(iso):
    try:
        return datetime.strptime(iso, "%Y-%m-%d").strftime("%B %-d, %Y")
    except Exception:
        return iso


def urlenc(t):
    from urllib.parse import quote
    return quote(t or "", safe="")


def esc(t):
    # Decode any pre-existing HTML entities to a fixpoint first, so re-rendering an already-rendered
    # page never stacks &amp;amp; encoding layers. Values from listings.json have no entities, so this
    # is a no-op for them; values read back from prior page HTML get healed instead of re-escaped.
    s = t or ""
    prev = None
    while s != prev:
        prev = s
        s = htmllib.unescape(s)
    return htmllib.escape(s, quote=True)


# ------------------------------------------------------------------ related launches
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


# ------------------------------------------------------------------ extraction
def extract(slug, src):
    rec = BY_SLUG[slug]
    out = {}

    desc_frag = grab(src, "listing-desc")
    out["DESCRIPTION_HTML"] = paragraphs(desc_frag) or "<p>%s</p>" % esc(rec["tagline"])

    story_frag = grab(src, "story-text")
    out["BUILDER_STORY"] = htmllib.escape(fix_dashes(text_of(story_frag)), quote=False) if story_frag else ""

    out["BUILDER_NAME"] = fix_dashes(text_of(grab(src, "builder-name"))) or rec["name"]
    out["BUILDER_BIO"] = htmllib.escape(fix_dashes(text_of(grab(src, "builder-bio"))), quote=False)
    handle = text_of(grab(src, "builder-handle"))
    out["BUILDER_HANDLE"] = esc(handle)
    avatar = text_of(grab(src, "builder-avatar"))
    out["BUILDER_INITIAL"] = esc((avatar or out["BUILDER_NAME"] or rec["name"])[:1].upper())

    # extra builder links: anything in builder-links that is not the product url
    extra = ""
    links_frag = grab(src, "builder-links") or ""
    for a in re.findall(r"<a\b[^>]*>.*?</a>", links_frag, re.S):
        href = re.search(r'href="([^"]+)"', a)
        if not href:
            continue
        h = href.group(1)
        if h.rstrip("/") == rec["url"].rstrip("/"):
            continue
        label = text_of(a) or h
        extra += ('<a href="%s" target="_blank" rel="noopener" class="builder-link">%s</a>'
                  % (esc(h), esc(label)))
    out["BUILDER_EXTRA_LINKS"] = extra

    # pricing tag, if the old page carried one
    pricing = ""
    hero = grab(src, "hero-meta") or ""
    known = {rec["cat"].lower(), (rec.get("stage") or "").lower()}
    for t in re.findall(r'<span class="tag[^"]*"[^>]*>([^<]*)</span>', hero):
        t = t.strip()
        if not t or t.lower() in known or "featured" in t.lower() or "runway" in t.lower():
            continue
        pricing = t
        break
    out["PRICING"] = esc(pricing)

    # logo and social image
    logo = rec.get("logo") or ""
    if not logo:
        m = re.search(r'<img[^>]*class="[^"]*listing-logo[^"]*"[^>]*src="([^"]+)"', src) \
            or re.search(r'class="listing-logo"[^>]*>\s*<img[^>]*src="([^"]+)"', src)
        if m:
            logo = m.group(1)
    m = re.search(r'class="listing-logo"[^>]*>([^<]{1,4})</div>', src)
    initial = esc((m.group(1).strip() if m else rec.get("emoji") or rec["name"][:1].upper()))
    if logo:
        # if the builder's logo URL ever breaks, fall back to the initial instead of a broken image
        out["LOGO_BLOCK"] = ('<img src="%s" alt="%s" loading="lazy" '
                             'onerror="this.outerHTML=\'%s\'" />' % (esc(logo), esc(rec["name"]), initial))
    else:
        out["LOGO_BLOCK"] = initial
    og = re.search(r'property="og:image" content="([^"]+)"', src)
    out["OG_IMAGE_URL"] = esc(og.group(1) if og and og.group(1) else (logo or DEFAULT_OG))

    # gallery
    imgs = []
    gal = grab(src, "gallery")
    if gal:
        for m in re.finditer(r'<img[^>]*src="([^"]+)"', gal):
            imgs.append('<div class="gallery-img"><img src="%s" alt="%s screenshot" loading="lazy" /></div>'
                        % (esc(m.group(1)), esc(rec["name"])))
    out["GALLERY_IMAGES"] = "".join(imgs)

    out["NAME"] = esc(rec["name"])
    out["SLUG"] = slug
    out["TAGLINE"] = esc(fix_dashes(rec["tagline"]))
    out["CATEGORY"] = esc(rec["cat"])
    out["STAGE"] = esc(rec.get("stage") or "Live")
    out["DATE_LONG"] = long_date(rec.get("date", ""))
    out["PRODUCT_URL"] = esc(rec["url"])
    out["TAGLINE_NOSTOP"] = esc(fix_dashes(rec["tagline"]).rstrip(" .!"))
    out["NAME_URLENC"] = urlenc(rec["name"])
    out["TAGLINE_URLENC"] = urlenc(fix_dashes(rec["tagline"]))
    out["RELATED_CARDS"] = related_cards(rec)
    out["_featured"] = bool(rec.get("featured"))
    return out


def render(vals):
    page = TEMPLATE
    for k, v in vals.items():
        if k.startswith("_"):
            continue
        page = page.replace("{{%s}}" % k, v)

    # optional blocks
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
    changed = problems = 0
    for rec in DATA:
        slug = rec["slug"]
        path = os.path.join(ROOT, "listings", slug + ".html")
        if not os.path.exists(path):
            print("MISSING  %s.html" % slug)
            problems += 1
            continue
        src = open(path, encoding="utf-8").read()
        vals = extract(slug, src)
        for req in ("NAME", "TAGLINE", "DESCRIPTION_HTML", "BUILDER_NAME"):
            if not vals[req]:
                print("EMPTY    %s -> %s" % (slug, req))
                problems += 1
        page = render(vals)
        left = re.findall(r"\{\{[A-Z_]+\}\}", page)
        if left:
            print("UNFILLED %s -> %s" % (slug, set(left)))
            problems += 1
            continue
        if page != src:
            changed += 1
            if WRITE:
                open(path, "w", encoding="utf-8").write(page)
    print("\n%d pages %s, %d problems" % (changed, "rewritten" if WRITE else "would change", problems))
    if not WRITE:
        print("Dry run. Re-run with --write to apply.")
    return 1 if problems else 0


sys.exit(main())
