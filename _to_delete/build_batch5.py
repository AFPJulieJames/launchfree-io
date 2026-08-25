import json, re, urllib.parse

WD = "."
TEMPLATE = open(f"{WD}/docs/LISTING_TEMPLATE_SSR.html").read()
BUILD_DATE = "2026-08-25"
DATE_LONG = "August 25, 2026"

records = [
    dict(name="Freelance Starter Kit", tagline="Offline invoice, proposal, rate & time tools for freelancers.",
        url="https://cotizadorpro.gumroad.com/l/freelance-starter-kit", category="Productivity", stage="Live",
        builder_name="CotizaPro Labs",
        builder_bio="An independent builder making small offline-first tools that solve boring, expensive problems for freelancers.",
        desc="Four lightweight tools that run entirely offline in your browser: professional invoice generator (print/PDF), proposal generator with scope and pricing, hourly-rate calculator covering expenses/taxes/savings goals, and a billable-hours time tracker with CSV export. No signup, data stays local. Free tools plus a complete $12 kit.",
        builder_story="I kept watching freelancers lose money by underpricing and spending hours on admin instead of paid work. Invoicing templates broke, proposals took whole evenings, and nobody knew their real minimum rate. So I built four small tools that fix exactly those jobs and work offline.",
        logo="", screenshots=[], linkedin="", twitter="@cotizaprolabs"),
    dict(name="Atlas Verified", tagline="AI verification for global trade: certifications, sanctions, FDA, trade data.",
        url="https://atlasverified.ai", category="AI / ML", stage="Live",
        builder_name="Jeremy Crane",
        builder_bio="Jeremy Crane builds Atlas Verified with Mathew Keegan. AI verification for global trade so teams and agents can check certifications, OFAC, FDA, and trade data.",
        desc="Atlas Verified is AI-powered intelligence and verification for global trade: certifications, OFAC, FDA, and trade data. Teams use it for audit-ready checks with cited sources. Agents can connect via remote MCP (Streamable HTTP) at https://api.atlasverified.ai/mcp (OAuth 2.0 + PKCE). Website: https://atlasverified.ai.",
        builder_story="Global trade verification is fragmented across certifications, sanctions lists, and FDA signals. We built Atlas Verified so operators and AI agents can verify counterparties and trade data from one intelligence layer, without inventing stats or relying on opaque blockchain metaphors.",
        logo="", screenshots=[], linkedin="", twitter=""),
]

for r in records:
    for k in ("tagline","desc","builder_story","builder_bio"):
        if "—" in r[k]:
            raise SystemExit(f"EM DASH found in {r['name']} field {k}: {r[k]!r}")
    if re.search(r'\bmaker\b', r["builder_bio"], re.I) or re.search(r'\bmaker\b', r["desc"], re.I) or re.search(r'\bmaker\b', r["builder_story"], re.I):
        raise SystemExit(f"'maker' language found in {r['name']}")

def slugify(name):
    s = name.lower()
    accents = {"á":"a","é":"e","í":"i","ó":"o","ú":"u","ñ":"n"}
    for a,b in accents.items(): s = s.replace(a,b)
    s = s.replace("&", "and")
    s = re.sub(r'[^a-z0-9]+', '-', s)
    s = s.strip('-')
    s = re.sub(r'-+', '-', s)
    return s

listings = json.load(open(f"{WD}/listings.json"))
existing_slugs = {r["slug"] for r in listings}
cat_index = {}
for r in listings:
    cat_index.setdefault(r["cat"], []).append(r)

for rec in records:
    slug = slugify(rec["name"])
    if slug in existing_slugs:
        raise SystemExit(f"COLLISION: {slug} already exists")
    existing_slugs.add(slug)
    rec["slug"] = slug

for rec in records:
    name = rec["name"]
    slug = rec["slug"]
    tagline = rec["tagline"]
    tagline_nostop = tagline.rstrip(".")
    initial = name[0].upper()

    if rec["logo"]:
        logo_block = f'<img src="{rec["logo"]}" alt="{name}" loading="lazy" onerror="this.outerHTML=\'{initial}\'" />'
        og_image = rec["logo"]
    else:
        logo_block = initial
        og_image = "https://launchfree.io/og-image.png"

    paras = [p.strip() for p in rec["desc"].split("\n\n") if p.strip()]
    desc_html = "".join(f"<p>{p}</p>" for p in paras)

    if rec["screenshots"]:
        gallery_imgs = "".join(f'<div class="gallery-img"><img src="{u}" alt="{name} screenshot" loading="lazy" /></div>' for u in rec["screenshots"])
        gallery_card = f'<div class="section-card"><div class="section-label">Screenshots</div><div class="gallery">{gallery_imgs}</div></div>'
    else:
        gallery_card = ""

    extra_links = ""
    if rec["linkedin"]:
        extra_links += f'<a href="{rec["linkedin"]}" target="_blank" rel="noopener" class="builder-link">LinkedIn</a>'

    handle = ""
    if rec["twitter"]:
        h = rec["twitter"].strip()
        handle = h if h.startswith("@") else "@" + h

    pool = cat_index.get(rec["category"], [])
    related = pool[:3]
    related_html = "".join(
        f'<a href="{r["slug"]}.html" class="related-card"><div class="related-logo">{r["emoji"]}</div><div class="related-info"><div class="related-name">{r["name"]}</div><div class="related-tag">{r["cat"]}</div></div></a>'
        for r in related
    )

    html = TEMPLATE
    html = html.replace("{{NAME}}", name)
    html = html.replace("{{SLUG}}", slug)
    html = html.replace("{{TAGLINE_NOSTOP}}", tagline_nostop)
    html = html.replace("{{TAGLINE}}", tagline)
    html = html.replace("{{CATEGORY}}", rec["category"])
    html = html.replace("{{STAGE}}", rec["stage"])
    html = html.replace("{{DATE_LONG}}", DATE_LONG)
    html = html.replace("{{PRODUCT_URL}}", rec["url"])
    html = html.replace("{{DESCRIPTION_HTML}}", desc_html)
    html = html.replace("{{BUILDER_STORY}}", rec["builder_story"])
    html = html.replace("{{BUILDER_NAME}}", rec["builder_name"])
    html = html.replace("{{BUILDER_INITIAL}}", rec["builder_name"][0].upper())
    html = html.replace("{{BUILDER_HANDLE}}", handle)
    html = html.replace("{{BUILDER_BIO}}", rec["builder_bio"])
    html = html.replace("{{LOGO_BLOCK}}", logo_block)
    html = html.replace("{{OG_IMAGE_URL}}", og_image)
    html = html.replace("{{NAME_URLENC}}", urllib.parse.quote(name))
    html = html.replace("{{TAGLINE_URLENC}}", urllib.parse.quote(tagline))
    html = html.replace("{{RELATED_CARDS}}", related_html)
    html = html.replace("{{BUILDER_EXTRA_LINKS}}", extra_links)

    html = re.sub(
        r'\s*<!-- OPTIONAL gallery.*?-->\s*\n?', '\n      ', html
    )
    html = re.sub(
        r'<div class="section-card"><div class="section-label">Screenshots</div><div class="gallery">\{\{GALLERY_IMAGES\}\}</div></div>',
        gallery_card, html
    )

    html = re.sub(r'\s*<span class="tag tag-n" id="tag-pricing">\{\{PRICING\}\}</span>\s*\n?', '\n      ', html)

    assert "{{" not in html, f"Unresolved placeholder in {slug}: " + str(re.search(r'\{\{[A-Z_]*\}\}', html))

    open(f"{WD}/listings/{slug}.html", "w").write(html)
    print("wrote", f"listings/{slug}.html")

    d = rec["desc"].replace("\n\n", " ")
    if len(d) > 150:
        cut = d[:150].rsplit(" ", 1)[0]
        desc_short = cut + "…"
    else:
        desc_short = d

    entry = {
        "id": slug, "name": name, "tagline": tagline, "desc": desc_short,
        "emoji": initial, "logo": rec["logo"], "cat": rec["category"], "url": rec["url"],
        "stage": rec["stage"], "votes": 0, "featured": False, "slug": slug,
        "date": BUILD_DATE, "mrr": ""
    }
    listings.append(entry)
    cat_index.setdefault(rec["category"], []).insert(0, entry)

json.dump(listings, open(f"{WD}/listings.json", "w"), indent=1, ensure_ascii=False)
print("listings.json now has", len(listings), "records")

sitemap = open(f"{WD}/sitemap.xml").read()
blocks = "".join(
    f'<url><loc>https://launchfree.io/listings/{r["slug"]}.html</loc><lastmod>{BUILD_DATE}</lastmod><changefreq>weekly</changefreq><priority>0.6</priority></url>\n'
    for r in records
)
sitemap = sitemap.replace("</urlset>", blocks + "</urlset>")
open(f"{WD}/sitemap.xml", "w").write(sitemap)
print("sitemap.xml updated")
print("SLUGS:", [r["slug"] for r in records])
