import json, re, urllib.parse

WD = "."
TEMPLATE = open(f"{WD}/docs/LISTING_TEMPLATE_SSR.html").read()
BUILD_DATE = "2026-08-25"
DATE_LONG = "August 25, 2026"

records = [
    {
        "name": "3D Animal Coloring",
        "tagline": "Kids color in 2D and see their animals come alive in 3D.",
        "url": "https://h2play.com/animal-coloring",
        "desc": "3D Animal Coloring is a creative app for young children built around one idea: there is no correct color for a child's animal. A child colors an animal or dinosaur in 2D, then taps “View in 3D” to see those exact colors on a movable 3D friend. Finished creations can be kept in a private on-device collection and brought into a small playground. Seven friends are free and one purchase unlocks all 38. There are no ads, tracking, accounts, chat, or public posting.",
        "category": "Education",
        "stage": "Live",
        "builder_name": "Hyunki Hong",
        "builder_bio": "I am an independent developer at H2Play, building small, privacy-conscious creative and observational apps for young children and their grown-ups. I focus on short interactions that encourage making, noticing, and conversation.",
        "builder_story": "I wanted the transition from drawing to 3D to make a child's own choices feel tangible. The product does not generate a picture for the child or score the colors. It keeps the child as the creator and uses 3D as the reward and the next place to explore the result.",
        "logo": "https://h2play.com/launch-assets/3d-animal-coloring/icon-512.png",
        "screenshots": ["https://h2play.com/launch-assets/3d-animal-coloring/gallery-01-color-it.jpg"],
        "linkedin": "",
    },
    {
        "name": "Animal Peekaboo",
        "tagline": "Guess the silhouette, then tap for a joyful 3D reveal.",
        "url": "https://h2play.com/animal-peekaboo",
        "desc": "Animal Peekaboo is a simple 3D silhouette guessing game made for young children and their grown-ups to play together. A child studies an animal's ears, tail, legs, and shape from different viewpoints, talks through a guess, then taps for a cheerful color reveal. Six animals are free and one purchase unlocks all 30. There are no ads, analytics, or accounts.",
        "category": "Education",
        "stage": "Live",
        "builder_name": "Hyunki Hong",
        "builder_bio": "I am an independent developer at H2Play, building small, privacy-conscious creative and observational apps for young children and their grown-ups. I focus on short interactions that encourage making, noticing, and conversation.",
        "builder_story": "I wanted a tiny screen activity that starts a conversation instead of replacing one. The short silhouette-and-reveal loop gives a parent an easy reason to ask what a child notices, what sound the animal might make, and why a guess changed from another angle.",
        "logo": "https://h2play.com/launch-assets/animal-peekaboo/icon-512.png",
        "screenshots": ["https://h2play.com/launch-assets/animal-peekaboo/gallery-01-look-closely.jpg"],
        "linkedin": "",
    },
    {
        "name": "RecipeScan",
        "tagline": "Photograph your fridge. Get dinner instantly.",
        "url": "https://recipescannerapp.com/",
        "desc": "RecipeScan turns a fridge or pantry photo into recipes you can cook tonight, plus a grocery list for what's missing. Import from TikTok, Instagram, YouTube, and Pinterest. Meal planning, calorie tracking, Apple Watch. Free on iPhone and iPad. RecipeScan by Gigabyte LLC (App Store id 6758753386). Not Cooksmart Recipe by Ingredient by Bosc Tech Labs. Not Reciscan by Dustin Runnells.",
        "category": "Lifestyle",
        "stage": "Live",
        "builder_name": "Mats Degerstedt",
        "builder_bio": "Indie developer building RecipeScan, an iPhone and iPad app that turns fridge photos into recipes and grocery lists.",
        "builder_story": "We kept staring at a full fridge with no idea what to cook, and saved recipes were scattered across social apps. RecipeScan was built so a single photo of what you already have turns into dinner options, with a grocery list only for what's missing.",
        "logo": "https://recipescannerapp.com/apple-touch-icon.png",
        "screenshots": ["https://recipescannerapp.com/assets/screenshots/discover.png"],
        "linkedin": "",
    },
    {
        "name": "SuperApp by Devkart",
        "tagline": "One platform. Food, retail, grocery, your brand.",
        "url": "https://www.superapphq.com",
        "desc": "SuperApp is a white-label multi-vertical marketplace platform. One multi-tenant backend launches branded customer, partner, business and dispatcher apps for iOS, Android and web across food delivery, retail and supermarkets. Pricing includes order volume rather than taking a commission on transactions. Available in 100+ countries, 50+ currencies and 25+ languages.",
        "category": "E-commerce",
        "stage": "Live",
        "builder_name": "Pradeep Saran",
        "builder_bio": "I am Pradeep Saran, Technical Architect and Founder of Devkart Technologies LLP. I built SuperApp for operators who want to launch branded food, retail and grocery marketplaces with subscription pricing and the operational tools to run their own network.",
        "builder_story": "SuperApp was built for operators who want to launch and run their own branded marketplace instead of joining someone else's network. Devkart brings customer, merchant, delivery, dispatch and admin operations together so food, retail and grocery businesses can operate under their own brand.",
        "logo": "https://www.superapphq.com/favicon.svg",
        "screenshots": [],
        "linkedin": "https://www.linkedin.com/in/devsaran/",
    },
    {
        "name": "More Good Reviews",
        "tagline": "Your AI Reputation Manager",
        "url": "https://moregoodreviews.com",
        "desc": "More Good Reviews is an AI-powered reputation management platform for local service businesses and agencies. Automate customer review requests via email and SMS, sync Google and Facebook reviews, help customers write reviews, and draft AI replies. Includes branded review pages, widgets, Zapier/HubSpot/Stripe integrations, and an MCP server so you can manage reputation from Claude or ChatGPT.",
        "category": "Marketing",
        "stage": "Live",
        "builder_name": "Scott Vayner",
        "builder_bio": "Founder of More Good Reviews. Building AI reputation tools for local service businesses and the agencies that serve them.",
        "builder_story": "Local shops and agencies were stuck doing manual review outreach. We built More Good Reviews to automate review requests, sync Google and Facebook, and draft AI replies at a price local businesses can actually pay.",
        "logo": "",
        "screenshots": [],
        "linkedin": "",
    },
]

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

new_entries = []
for rec in records:
    slug = slugify(rec["name"])
    if slug in existing_slugs:
        raise SystemExit(f"COLLISION: {slug} already exists")
    existing_slugs.add(slug)
    rec["slug"] = slug
    new_entries.append(rec)

for rec in new_entries:
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

    desc_html = f"<p>{rec['desc']}</p>"

    if rec["screenshots"]:
        gallery_imgs = "".join(f'<div class="gallery-img"><img src="{u}" alt="{name} screenshot" loading="lazy" /></div>' for u in rec["screenshots"])
        gallery_card = f'<div class="section-card"><div class="section-label">Screenshots</div><div class="gallery">{gallery_imgs}</div></div>'
    else:
        gallery_card = ""

    extra_links = ""
    if rec["linkedin"]:
        extra_links += f'<a href="{rec["linkedin"]}" target="_blank" rel="noopener" class="builder-link">LinkedIn</a>'

    # related cards: 3 from same category, already-live
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
    html = html.replace("{{BUILDER_HANDLE}}", "")
    html = html.replace("{{BUILDER_BIO}}", rec["builder_bio"])
    html = html.replace("{{LOGO_BLOCK}}", logo_block)
    html = html.replace("{{OG_IMAGE_URL}}", og_image)
    html = html.replace("{{NAME_URLENC}}", urllib.parse.quote(name))
    html = html.replace("{{TAGLINE_URLENC}}", urllib.parse.quote(tagline))
    html = html.replace("{{RELATED_CARDS}}", related_html)
    html = html.replace("{{BUILDER_EXTRA_LINKS}}", extra_links)
    html = html.replace("{{GALLERY_IMAGES}}", "")  # placeholder inside gallery card, unused if card removed

    # Screenshots card: template has a fixed gallery card; replace it wholesale
    html = re.sub(
        r'<div class="section-card"><div class="section-label">Screenshots</div><div class="gallery">.*?</div></div>',
        gallery_card, html, flags=re.S
    )

    # Pricing: no Pricing field on any of these 5 -> delete the tag-pricing span
    html = re.sub(r'\s*<span class="tag tag-n" id="tag-pricing">\{\{PRICING\}\}</span>\s*\n?', '\n      ', html)

    assert "{{" not in html, f"Unresolved placeholder in {slug}: " + re.search(r'\{\{[A-Z_]*\}\}', html).group(0)

    open(f"{WD}/listings/{slug}.html", "w").write(html)
    print("wrote", f"listings/{slug}.html")

    # desc field for listings.json: first ~150 chars at word boundary
    d = rec["desc"]
    if len(d) > 150:
        cut = d[:150].rsplit(" ", 1)[0]
        desc_short = cut + "…"
    else:
        desc_short = d

    entry = {
        "id": slug,
        "name": name,
        "tagline": tagline,
        "desc": desc_short,
        "emoji": initial,
        "logo": rec["logo"],
        "cat": rec["category"],
        "url": rec["url"],
        "stage": rec["stage"],
        "votes": 0,
        "featured": False,
        "slug": slug,
        "date": BUILD_DATE,
        "mrr": ""
    }
    listings.append(entry)
    cat_index.setdefault(rec["category"], []).insert(0, entry)

json.dump(listings, open(f"{WD}/listings.json", "w"), indent=1, ensure_ascii=False)
print("listings.json now has", len(listings), "records")

# sitemap.xml
sitemap = open(f"{WD}/sitemap.xml").read()
blocks = "".join(
    f'<url><loc>https://launchfree.io/listings/{r["slug"]}.html</loc><lastmod>{BUILD_DATE}</lastmod><changefreq>weekly</changefreq><priority>0.6</priority></url>\n'
    for r in new_entries
)
sitemap = sitemap.replace("</urlset>", blocks + "</urlset>")
open(f"{WD}/sitemap.xml", "w").write(sitemap)
print("sitemap.xml updated")

print("SLUGS:", [r["slug"] for r in new_entries])
