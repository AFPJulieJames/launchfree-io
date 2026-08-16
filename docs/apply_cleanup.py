#!/usr/bin/env python3
"""
One-time cleanup, 2026-08-16. Brings the repo to a clean baseline before the new build process
takes over. Idempotent: running it twice changes nothing the second time.

  listings.json   normalize drifted stage values, remove an em dash from one product name
  index.html      remove the dead Airtable code path and the stale SEED array
  browse.html     same
  submit.html     replace the two categories that do not exist with the two that were missing
  sitemap.xml     refresh lastmod on every page whose content changed
  template.html   replace the legacy JavaScript-render skeleton with a stub
  docs/RUNBOOK.md replace with a pointer to docs/BUILD_SPEC.md

Run from the repo root:

    python3 docs/apply_cleanup.py            # dry run
    python3 docs/apply_cleanup.py --write    # apply

Never touches git.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if not os.path.exists(os.path.join(ROOT, "listings.json")):
    ROOT = os.getcwd()
WRITE = "--write" in sys.argv
TODAY = "2026-08-16"
changed = []


def fix_dashes(t):
    """House style: no em dashes in copy. Numeric ranges keep a plain hyphen."""
    if not t:
        return t
    t = re.sub(r"(?<=[\d$])\s*[\u2013\u2014]\s*(?=[\d$])", "-", t)
    t = re.sub(r"\s*[\u2013\u2014]\s*", ", ", t)
    t = re.sub(r",\s*,", ",", t)
    t = re.sub(r"\s+,", ",", t)
    return t


def load(p):
    return open(os.path.join(ROOT, p), encoding="utf-8").read()


def save(p, old, new):
    if old == new:
        return
    changed.append(p)
    if WRITE:
        open(os.path.join(ROOT, p), "w", encoding="utf-8").write(new)


# ---------------------------------------------------------------- listings.json
s = load("listings.json")
orig = s
for slug, old, new in [("aituai", "Launched", "Live"),
                       ("creatorcommissions", "Early access", "Beta"),
                       ("liveshoppingcreators", "Early access", "Beta"),
                       ("affiliateliveshopping", "Early access", "Beta")]:
    m = re.search(r'\{\s*"id": "%s".*?\n \}' % re.escape(slug), s, re.S)
    if not m:
        print("  ! record not found: %s" % slug)
        continue
    block = m.group(0)
    s = s[:m.start()] + block.replace('"stage": "%s"' % old, '"stage": "%s"' % new) + s[m.end():]
s = s.replace("Digital Defense Brief \u2014 AI Scam Survival Guide 2026",
              "Digital Defense Brief: AI Scam Survival Guide 2026")
# no em dashes in the catalog copy either, since the grids and category pages render it
for rec in json.loads(s):
    for field in ("name", "tagline", "desc"):
        val = rec.get(field) or ""
        fixed = fix_dashes(val)
        if fixed != val:
            s = s.replace(json.dumps(val, ensure_ascii=False), json.dumps(fixed, ensure_ascii=False))
json.loads(s)  # refuse to write invalid JSON
save("listings.json", orig, s)

# ---------------------------------------------------------------- index.html / browse.html
NEW_FETCH = ("async function fetchListings(){\n"
             "try{\n"
             "const res=await fetch('listings.json',{cache:'no-cache'});\n"
             "if(!res.ok)throw new Error('listings.json '+res.status);\n"
             "LISTINGS=await res.json();\n"
             "}catch(err){\n"
             "console.error('Could not load listings.json',err);\n"
             "LISTINGS=[];\n"
             "}\n"
             "await loadLiveVotes();initVotes();render();\n"
             "}\n")

for path in ("index.html", "browse.html"):
    s = load(path)
    orig = s
    if "AIRTABLE_KEY" not in s:
        continue
    s = re.sub(r"/\* CONFIG \*/\n?", "", s)
    s = re.sub(r"const AIRTABLE_BASE='[^']*';\nconst AIRTABLE_TABLE='[^']*';\n"
               r"const AIRTABLE_KEY='[^']*';\nconst CACHE_KEY='[^']*';\nconst CACHE_TTL=[^;]*;\n", "", s)
    s = re.sub(r"/\* SEED LISTINGS \*/\n?", "", s)
    s = re.sub(r"const SEED=\[.*?\n\];\n", "", s, flags=re.S)
    pat = r"async function fetchListings\(\)\{.*?\n\}\n(\s*)function initVotes"
    s, n = re.subn(pat, lambda m: NEW_FETCH + m.group(1) + "function initVotes", s, count=1, flags=re.S)
    if n != 1 or "AIRTABLE" in s or "SEED" in s:
        print("  ! %s not cleaned, left unchanged" % path)
        continue
    save(path, orig, s)

# ---------------------------------------------------------------- submit.html
s = load("submit.html")
orig = s
s = s.replace('<div class="cat-pill" data-val="Newsletter">Newsletter</div>',
              '<div class="cat-pill" data-val="Entertainment">Entertainment</div>')
s = s.replace('<div class="cat-pill" data-val="Physical Product">Physical Product</div>',
              '<div class="cat-pill" data-val="Lifestyle">Lifestyle</div>')
save("submit.html", orig, s)

# ---------------------------------------------------------------- sitemap lastmod
s = load("sitemap.xml")
orig = s


def bump(m):
    loc = m.group(0)
    if re.search(r"/(listings|categories)/|/directory\.html|/submit\.html|/$", loc):
        return re.sub(r"<lastmod>[^<]*</lastmod>", "<lastmod>%s</lastmod>" % TODAY, loc)
    return loc


s = re.sub(r"<url>.*?</url>", bump, s, flags=re.S)
save("sitemap.xml", orig, s)

# ---------------------------------------------------------------- retired files
STUB_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="robots" content="noindex">
<title>Retired file</title>
</head>
<body>
<!--
  RETIRED 2026-08-16. This was the old JavaScript-rendered listing skeleton. Pages built from it
  shipped with a "Loading..." title, an empty description and a canonical pointing at the homepage,
  which made them invisible to Google and to AI answer engines. Do not build from this file.

  The canonical listing template is docs/LISTING_TEMPLATE_SSR.html.
  The build process is docs/BUILD_SPEC.md.

  This file is safe to delete in GitHub Desktop.
-->
<p>This file is retired. See docs/BUILD_SPEC.md.</p>
</body>
</html>
"""
if "const LISTING" in load("template.html"):
    save("template.html", load("template.html"), STUB_TEMPLATE)

STUB_RUNBOOK = """# Retired: see docs/BUILD_SPEC.md

This runbook is superseded as of 2026-08-16. It contradicted itself: section 3.5 required
server-rendered pages while step 3 still said to build from `template.html`, which is the
JavaScript-render skeleton that caused the problem. It also listed four surfaces when a build
touches six.

The current build process is **`docs/BUILD_SPEC.md`**.
How the whole site works is **`docs/OPERATIONS_MANUAL.md`**.

This file is safe to delete in GitHub Desktop.
"""
if "New Listings Build Runbook" in load("docs/RUNBOOK.md"):
    save("docs/RUNBOOK.md", load("docs/RUNBOOK.md"), STUB_RUNBOOK)

STUB_OLD = """# Retired: see docs/BUILD_SPEC.md

This file was an early draft of the runbook. The current build process is `docs/BUILD_SPEC.md`
and the operations manual is `docs/OPERATIONS_MANUAL.md`.

This file is safe to delete in GitHub Desktop.
"""
p = "The_Runway_New_Listings_Runbook.md"
if os.path.exists(os.path.join(ROOT, p)) and load(p) != STUB_OLD:
    save(p, load(p), STUB_OLD)

print("%d files %s" % (len(changed), "written" if WRITE else "would change"))
for c in changed:
    print("  " + c)
if not WRITE:
    print("Dry run. Re-run with --write to apply.")
