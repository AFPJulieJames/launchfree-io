#!/usr/bin/env python3
"""
LaunchFree.io build validator.

Checks every rule in docs/BUILD_SPEC.md that a machine can check. Run it from the repo root
before every commit:

    python3 docs/validate_build.py

It reads files only. It never touches git, never writes anything, and never talks to the network.
Exit code 0 means clean, 1 means at least one ERROR.

ERROR   = do not commit until fixed.
WARN    = known drift, safe to ship, worth cleaning up.
"""

import json
import os
import re
import sys
import unicodedata
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if not os.path.exists(os.path.join(ROOT, "listings.json")):
    ROOT = os.getcwd()

CATEGORIES = {
    "AI / ML": "ai-ml", "Affiliate": "affiliate", "Community": "community",
    "Creator Tools": "creator-tools", "Developer Tools": "developer-tools",
    "E-commerce": "e-commerce", "Education": "education", "Entertainment": "entertainment",
    "Fintech": "fintech", "Health": "health", "Lifestyle": "lifestyle", "Marketing": "marketing",
    "Other": "other", "Productivity": "productivity", "SaaS": "saas", "Service": "service",
    "Travel": "travel",
}
STAGES = {"Live", "Beta", "Early Access", "Coming Soon", "In Development"}

errors, warns = [], []
def err(m): errors.append(m)
def warn(m): warns.append(m)
def p(path): return os.path.join(ROOT, path)
def read(path):
    with open(p(path), encoding="utf-8", errors="replace") as f:
        return f.read()


def slugify(name):
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    s = s.lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


# ---------------------------------------------------------------- listings.json
try:
    data = json.loads(read("listings.json"))
except Exception as e:
    print(f"ERROR  listings.json is not valid JSON: {e}")
    sys.exit(1)

slugs = [r.get("slug") for r in data]
dupes = [s for s, n in Counter(slugs).items() if n > 1]
if dupes:
    err(f"listings.json has duplicate slugs: {dupes}")

FIELDS = ["id", "name", "tagline", "desc", "emoji", "logo", "cat", "url",
          "stage", "votes", "featured", "slug", "date", "mrr"]

for r in data:
    s = r.get("slug", "?")
    missing = [f for f in FIELDS if f not in r]
    if missing:
        err(f"{s}: listings.json record missing fields {missing}")
    if r.get("id") != r.get("slug"):
        err(f"{s}: id does not equal slug")
    if r.get("votes") != 0:
        err(f"{s}: votes must be 0 in listings.json (real counts live in Supabase)")
    if r.get("mrr"):
        err(f"{s}: mrr must stay empty, it is intake-only data")
    if r.get("cat") not in CATEGORIES:
        err(f"{s}: category '{r.get('cat')}' is not one of the 17 canonical values")
    if r.get("stage") not in STAGES:
        warn(f"{s}: stage '{r.get('stage')}' is not one of {sorted(STAGES)}")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(r.get("date", ""))):
        err(f"{s}: date '{r.get('date')}' is not YYYY-MM-DD")
    if s and not re.fullmatch(r"[a-z0-9-]+", s):
        err(f"{s}: slug contains characters outside a-z 0-9 and hyphen")

# ---------------------------------------------------------------- page files
files = {f[:-5] for f in os.listdir(p("listings")) if f.endswith(".html")}
orphan_files = files - set(slugs)
orphan_records = set(slugs) - files
for s in sorted(orphan_files):
    err(f"{s}: listings/{s}.html exists but has no listings.json record, so nothing links to it")
for s in sorted(orphan_records):
    err(f"{s}: listings.json record has no listings/{s}.html page")

for r in data:
    s = r.get("slug")
    if s not in files:
        continue
    html = read(f"listings/{s}.html")

    if "{{" in html:
        err(f"{s}: unreplaced template placeholder left in the page")
    m = re.search(r"<title>(.*?)</title>", html, re.S)
    title = m.group(1).strip() if m else ""
    if not title or "Loading" in title:
        err(f"{s}: title is missing or still says Loading")
    elif not title.endswith("| LaunchFree.io"):
        warn(f"{s}: title does not end with '| LaunchFree.io'")
    m = re.search(r'rel="canonical" href="([^"]+)"', html)
    want = f"https://launchfree.io/listings/{s}.html"
    if not m:
        err(f"{s}: no canonical link")
    elif m.group(1) != want:
        err(f"{s}: canonical is {m.group(1)}, must be {want}")
    if not re.search(r'name="description" content="[^"]{10,}"', html):
        err(f"{s}: meta description is missing or empty")
    if not re.search(r"<h1[^>]*>\s*\S", html):
        err(f"{s}: no real H1")
    for tag in ('property="og:title"', 'property="og:url"', 'property="og:image"',
                'name="twitter:card"'):
        if tag not in html:
            warn(f"{s}: missing {tag}")
    for schema in ("SoftwareApplication", "BreadcrumbList"):
        if schema not in html:
            err(f"{s}: missing {schema} JSON-LD")
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        try:
            json.loads(block)
        except Exception:
            err(f"{s}: a JSON-LD block is not valid JSON")
    if "data-lf-vote-backend" not in html:
        err(f"{s}: missing the Supabase vote script")
    v = re.search(r"""SLUG\s*=\s*['"]([^'"]+)['"]""", html)
    if not v:
        err(f"{s}: vote script has no SLUG")
    elif v.group(1) != s:
        err(f"{s}: vote script SLUG is '{v.group(1)}' but the file is {s}.html")
    if 'class="upvote-btn"' not in html:
        err(f"{s}: no upvote button for the vote script to bind to")
    if "LF_SLUG" in html:
        warn(f"{s}: legacy LF_SLUG script still present, safe to remove")
    if 'name="robots"' not in html:
        warn(f"{s}: no robots meta tag")
    body = html[html.find("<body"):] if "<body" in html else html
    body = re.sub(r"<script.*?</script>", "", body, flags=re.S)
    if "—" in re.sub(r"<[^>]+>", "", body):
        warn(f"{s}: em dash found in body copy, house style is no em dashes")
    for link in set(re.findall(r'class="related-card"[^>]*', html)):
        pass
    rel = re.findall(r'href="([a-z0-9._-]+\.html)"[^>]*class="related-card"', html)
    rel += re.findall(r'class="related-card"[^>]*href="([a-z0-9._-]+\.html)"', html)
    for target in rel:
        if target[:-5] not in files:
            err(f"{s}: related card points at {target}, which does not exist")

# ---------------------------------------------------------------- sitemap
sitemap = read("sitemap.xml")
if not sitemap.rstrip().endswith("</urlset>"):
    err("sitemap.xml does not end with </urlset>")
in_sitemap = set(re.findall(r"https://launchfree\.io/listings/([a-z0-9._-]+)\.html", sitemap))
for s in sorted(set(slugs) - in_sitemap):
    err(f"{s}: not in sitemap.xml")
for cat, fname in CATEGORIES.items():
    if f"https://launchfree.io/categories/{fname}.html" not in sitemap:
        warn(f"category page {fname}.html is not in sitemap.xml")

# ---------------------------------------------------------------- llms.txt
llms = read("llms.txt")
in_llms = set(re.findall(r"https://launchfree\.io/listings/([a-z0-9._-]+)\.html", llms))
m = re.search(r"currently (\d+) live launches", llms)
if not m:
    err("llms.txt has no 'currently N live launches' sentence")
elif int(m.group(1)) != len(data):
    err(f"llms.txt says {m.group(1)} live launches, listings.json has {len(data)}")

# ---------------------------------------------------------------- directory.html
directory = read("directory.html")
in_dir = set(re.findall(r"listings/([a-z0-9._-]+)\.html", directory))
missing_dir = set(slugs) - in_dir
if missing_dir:
    err(f"directory.html is missing {len(missing_dir)} launches, regenerate it: "
        f"{sorted(missing_dir)[:5]}{' ...' if len(missing_dir) > 5 else ''}")

# ---------------------------------------------------------------- category pages
by_cat = {}
for r in data:
    by_cat.setdefault(r.get("cat"), set()).add(r.get("slug"))
for cat, fname in CATEGORIES.items():
    path = f"categories/{fname}.html"
    if not os.path.exists(p(path)):
        err(f"{path} does not exist but category '{cat}' is in use")
        continue
    page = read(path)
    linked = set(re.findall(r"listings/([a-z0-9._-]+)\.html", page))
    want = by_cat.get(cat, set())
    missing = want - linked
    if missing:
        err(f"{path} is missing {len(missing)} of {len(want)} launches: "
            f"{sorted(missing)[:4]}{' ...' if len(missing) > 4 else ''}")
    m = re.search(r"\((\d+)\)", page[:3000])
    if m and int(m.group(1)) != len(want):
        err(f"{path} claims {m.group(1)} launches, listings.json has {len(want)}")

# ---------------------------------------------------------------- report
print(f"LaunchFree build validator  |  {len(data)} records, {len(files)} pages\n")
for m in errors:
    print(f"ERROR  {m}")
if errors and warns:
    print()
for m in warns:
    print(f"WARN   {m}")
print(f"\n{len(errors)} errors, {len(warns)} warnings")
if not errors:
    print("Pre-flight machine checks passed. Still do the human checks in BUILD_SPEC.md section 10.")
sys.exit(1 if errors else 0)
