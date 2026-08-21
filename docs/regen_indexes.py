#!/usr/bin/env python3
"""
Regenerate every index surface from listings.json:

  categories/*.html   grid, counts, ItemList JSON-LD, other-categories strip
  directory.html      counts, category table of contents, every category section
  llms.txt            live launch count, Recent launches, Categories counts

Design, CSS and copy are preserved. Only the data-driven regions are rewritten. Run from the repo
root, after listings.json has been updated:

    python3 docs/regen_indexes.py            # dry run
    python3 docs/regen_indexes.py --write    # apply

Never touches git.
"""
import html as htmllib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if not os.path.exists(os.path.join(ROOT, "listings.json")):
    ROOT = os.getcwd()
WRITE = "--write" in sys.argv

CATEGORIES = {
    "AI / ML": "ai-ml", "Affiliate": "affiliate", "Community": "community",
    "Creator Tools": "creator-tools", "Developer Tools": "developer-tools",
    "E-commerce": "e-commerce", "Education": "education", "Entertainment": "entertainment",
    "Fintech": "fintech", "Health": "health", "Lifestyle": "lifestyle", "Marketing": "marketing",
    "Other": "other", "Productivity": "productivity", "SaaS": "saas", "Service": "service",
    "Travel": "travel",
}

DATA = json.load(open(os.path.join(ROOT, "listings.json"), encoding="utf-8"))
TOTAL = len(DATA)

by_cat = {}
for r in DATA:
    by_cat.setdefault(r["cat"], []).append(r)
for v in by_cat.values():
    v.sort(key=lambda r: r["name"].lower())
ordered_cats = sorted(CATEGORIES, key=lambda c: (-len(by_cat.get(c, [])), c))
newest = sorted(DATA, key=lambda r: (r.get("date", ""), r["slug"]), reverse=True)

written = []


def e(t):
    return htmllib.escape(t or "", quote=True)


def plural(n, word="launch"):
    return "%d %s" % (n, word if n == 1 else word + "es")


def save(path, old, new):
    if old == new:
        return False
    written.append(path)
    if WRITE:
        open(os.path.join(ROOT, path), "w", encoding="utf-8").write(new)
    return True


# ----------------------------------------------------------------- category pages
def card(r, prefix="../listings/"):
    return ('<a class="card" href="%s%s.html"><span class="nm">%s</span>'
            '<span class="tg">%s</span></a>' % (prefix, r["slug"], e(r["name"]), e(r["tagline"])))


def category_page(cat):
    fname = CATEGORIES[cat]
    path = "categories/%s.html" % fname
    full = os.path.join(ROOT, path)
    if not os.path.exists(full):
        print("  ! missing %s" % path)
        return
    src = open(full, encoding="utf-8").read()
    rows = by_cat.get(cat, [])
    n = len(rows)
    s = src

    desc = ("Browse %d free %s launches on LaunchFree.io (The Runway). Every listing is free, "
            "human-reviewed, and includes a permanent dofollow backlink." % (n, cat))
    if '<meta name="description"' not in s:
        raise SystemExit("%s has no meta description, refusing to write" % path)
    s = re.sub(r'(<meta name="description" content=")[^"]*(">)', lambda m: m.group(1) + desc + m.group(2), s, count=1)
    s = re.sub(r'(<meta property="og:description" content=")[^"]*(">)', lambda m: m.group(1) + desc + m.group(2), s, count=1)
    s = re.sub(r"<title>Free %s Launches &amp; Tools \(\d+\)" % re.escape(cat.replace("&", "&amp;")),
               "<title>Free %s Launches &amp; Tools (%d)" % (cat.replace("&", "&amp;"), n), s, count=1)
    s = re.sub(r"(<title>[^<]*?)\(\d+\)", r"\g<1>(%d)" % n, s, count=1)

    # ItemList JSON-LD
    items = ",".join(
        '{"@type":"ListItem","position":%d,"url":"https://launchfree.io/listings/%s.html","name":"%s"}'
        % (i + 1, r["slug"], e(r["name"])) for i, r in enumerate(rows))
    s = re.sub(r'"description":"All \d+ free %s launches listed on LaunchFree\.io\."' % re.escape(cat),
               '"description":"All %d free %s launches listed on LaunchFree.io."' % (n, cat), s, count=1)
    s = re.sub(r'"mainEntity":\{"@type":"ItemList","numberOfItems":\d+,"itemListElement":\[.*?\]\}',
               '"mainEntity":{"@type":"ItemList","numberOfItems":%d,"itemListElement":[%s]}' % (n, items),
               s, count=1, flags=re.S)

    # visible count line
    s = re.sub(r'<p class="meta">\d+ free launches listed',
               '<p class="meta">%d free launches listed' % n, s, count=1)
    # the grid
    s = re.sub(r'<div class="grid">.*?</div>\n',
               '<div class="grid">%s</div>\n' % "".join(card(r) for r in rows), s, count=1, flags=re.S)
    # other categories strip
    strip = "".join('<a href="%s.html">%s (%d)</a>' % (CATEGORIES[c], e(c), len(by_cat.get(c, [])))
                    for c in ordered_cats if c != cat)
    s = re.sub(r'<div class="othercats">.*?</div>', '<div class="othercats">%s</div>' % strip,
               s, count=1, flags=re.S)
    # dead stylesheet reference
    s = re.sub(r'\s*<link rel="stylesheet" href="[^"]*?/css/content-shared\.css">', "", s)
    save(path, src, s)


# ----------------------------------------------------------------- directory.html
def directory_page():
    path = "directory.html"
    src = open(os.path.join(ROOT, path), encoding="utf-8").read()
    s = src
    n_cats = len([c for c in ordered_cats if by_cat.get(c)])

    s = re.sub(r"all \d+ free, human-reviewed launches", "all %d free, human-reviewed launches" % TOTAL, s)
    s = re.sub(r"all \d+ free, human-reviewed", "all %d free, human-reviewed" % TOTAL, s)
    s = re.sub(r"directory of \d+ free launches", "directory of %d free launches" % TOTAL, s)
    s = re.sub(r"<title>Browse All \d+ Launches", "<title>Browse All %d Launches" % TOTAL, s)
    s = re.sub(r'<p class="meta">\d+ live launches across \d+ categories',
               '<p class="meta">%d live launches across %d categories' % (TOTAL, n_cats), s, count=1)

    toc = "".join('<a href="categories/%s.html">%s (%d)</a>' % (CATEGORIES[c], e(c), len(by_cat[c]))
                  for c in ordered_cats if by_cat.get(c))
    s = re.sub(r'<div class="toc">.*?</div>', '<div class="toc">%s</div>' % toc, s, count=1, flags=re.S)

    sections = ""
    for c in ordered_cats:
        rows = by_cat.get(c)
        if not rows:
            continue
        sections += (
            '<h2 class="cat" id="%s"><a href="categories/%s.html">%s</a></h2>'
            '<div class="cat-count">%s &middot; <a href="categories/%s.html">see the %s hub &rarr;</a></div>'
            '<div class="grid">%s</div>'
            % (CATEGORIES[c], CATEGORIES[c], e(c), plural(len(rows)), CATEGORIES[c], e(c),
               "".join(card(r, "listings/") for r in rows)))
    s = re.sub(r'<h2 class="cat".*?(?=\n<div class="cta">)', sections, s, count=1, flags=re.S)

    # ItemList in the CollectionPage schema, if present
    items = ",".join(
        '{"@type": "ListItem", "position": %d, "url": "https://launchfree.io/listings/%s.html", "name": "%s"}'
        % (i + 1, r["slug"], e(r["name"])) for i, r in enumerate(newest[:100]))
    s = re.sub(r'"mainEntity": \{"@type": "ItemList", "numberOfItems": \d+, "itemListElement": \[.*?\]\}',
               '"mainEntity": {"@type": "ItemList", "numberOfItems": %d, "itemListElement": [%s]}'
               % (TOTAL, items), s, count=1, flags=re.S)
    save(path, src, s)


# ----------------------------------------------------------------- llms.txt
def llms_txt():
    path = "llms.txt"
    src = open(os.path.join(ROOT, path), encoding="utf-8").read()
    s = re.sub(r"There are currently \d+ live launches",
               "There are currently %d live launches" % TOTAL, src, count=1)

    recent = "\n".join(
        "- [%s](https://launchfree.io/listings/%s.html): %s (%s)."
        % (r["name"], r["slug"], r["tagline"].rstrip(". "), r["cat"]) for r in newest[:100])
    s = re.sub(r"(## Recent launches\n).*?(\n\n## )", r"\g<1>%s\g<2>" % recent.replace("\\", "\\\\"),
               s, count=1, flags=re.S)

    cats = "\n".join(
        "- [%s](https://launchfree.io/categories/%s.html): %s free %s %s."
        % (c, CATEGORIES[c], len(by_cat[c]), c, "launch" if len(by_cat[c]) == 1 else "launches")
        for c in ordered_cats if by_cat.get(c))
    s = re.sub(r"(## Categories\n).*?(\n\n## )", r"\g<1>%s\g<2>" % cats.replace("\\", "\\\\"),
               s, count=1, flags=re.S)
    save(path, src, s)


# ----------------------------------------------------------------- homepage hero stat
def index_html():
    # index.html fetches listings.json live on page load, so a human sees the right
    # count. Crawlers, AI answer engines and link unfurlers read the static HTML and do
    # not run that JS, so stamp the live catalog length into the hero stat span here.
    # The client-side JS (if LISTINGS.length) stays the fallback; the two always agree.
    path = "index.html"
    src = open(os.path.join(ROOT, path), encoding="utf-8").read()
    s = re.sub(r'(<span[^>]*id="stat-count"[^>]*>)[^<]*(</span>)',
               lambda m: "%s%d%s" % (m.group(1), TOTAL, m.group(2)), src, count=1)
    # the meta description leads with the live count; stamp it too so it never drifts
    s = re.sub(r'(<meta name="description" content=")\d+( free, human-reviewed)',
               lambda m: "%s%d%s" % (m.group(1), TOTAL, m.group(2)), s, count=1)
    save(path, src, s)


# ----------------------------------------------------------------- dead stylesheet elsewhere
def strip_dead_css():
    for folder in ("radar", "research", "categories", "."):
        d = os.path.join(ROOT, folder)
        for f in sorted(os.listdir(d)):
            if not f.endswith(".html"):
                continue
            rel = f if folder == "." else "%s/%s" % (folder, f)
            src = open(os.path.join(ROOT, rel), encoding="utf-8").read()
            if "/css/content-shared.css" not in src:
                continue
            s = re.sub(r'\s*<link rel="stylesheet" href="[^"]*?/css/content-shared\.css">', "", src)
            save(rel, src, s)


for c in CATEGORIES:
    category_page(c)
directory_page()
llms_txt()
index_html()
strip_dead_css()

print("%d files %s" % (len(written), "written" if WRITE else "would change"))
for w in written:
    print("  " + w)
if not WRITE:
    print("Dry run. Re-run with --write to apply.")
