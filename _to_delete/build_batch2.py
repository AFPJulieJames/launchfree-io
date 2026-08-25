import json, re, urllib.parse

WD = "."
TEMPLATE = open(f"{WD}/docs/LISTING_TEMPLATE_SSR.html").read()
BUILD_DATE = "2026-08-25"
DATE_LONG = "August 25, 2026"

records = [
    dict(name="Cleanup My Phone", tagline="On-device iPhone cleaner with a 30-day undo vault",
        url="https://cleanupmyphone.com", category="Productivity", stage="Live",
        builder_name="Mats Degerstedt",
        builder_bio="Indie iOS maker, Gigabyte LLC.",
        desc="Cleanup My Phone is an iPhone storage cleaner that runs entirely on-device. It finds similar shots, blurry photos, screenshots, and big videos, compresses 4K with HEVC, and cleans Gmail/iCloud/Outlook/IMAP. First cleanup is free. 30-day on-device undo vault. No account, no photo upload. Distinct from MacPaw CleanMyPhone and Codeway Cleanup.",
        builder_story="Other iPhone cleaners upload your camera roll to their servers or lock deletes behind a paywall. I wanted a cleaner that never uploads a photo and lets you undo everything for 30 days, so I built it.",
        logo="", screenshots=[], linkedin="", twitter=""),
    dict(name="creators.vip", tagline="Bid your creator link to the top 10",
        url="https://creators.vip", category="Creator Tools", stage="Live",
        builder_name="Shay Ben Yacov",
        builder_bio="Building consumer products in public. Founder of creators.vip.",
        desc="A live public ranking for creators. Bid for a top-10 slot in podcast, YouTube, Instagram, TikTok, music, books, or X. Stay ranked until someone outbids you. Same pay-to-rank mechanic as recent boards, built for creator links, not generic sites.",
        builder_story="I wanted a public place for creators to be found that is not another feed. I shipped a live board where a bid is a rank, a page, and a badge.",
        logo="", screenshots=[], linkedin="", twitter=""),
    dict(name="PlainQuote", tagline="Quoting app for one-person plumbers. Type the job, print the estimate.",
        url="https://plainquote.online", category="Productivity", stage="Live",
        builder_name="James W",
        builder_bio="Builder of PlainQuote, a quoting app for one-person plumbers.",
        desc="PlainQuote is driveway paperwork for one-person trades. Type the job on the phone. Print an estimate, change order, invoice, or work order PDF. $19.99 once. Not a subscription.",
        builder_story="Built so a one-person plumber can type the job on a phone and print an estimate in the driveway, without a subscription.",
        logo="", screenshots=[], linkedin="", twitter="TurtleAnchor"),
    dict(name="ShipReady", tagline="Production mechanic for Lovable, Bolt, v0, and Cursor apps",
        url="https://creative-kelpie-287826.netlify.app", category="Developer Tools", stage="Live",
        builder_name="Eldar Guliev",
        builder_bio="I'm Eldar, a solo developer. I run ShipReady, a small async service that takes AI-built apps (Lovable, Bolt, v0, Cursor) from a working preview to a safe production deploy: secrets, RLS, Stripe webhooks, and Vercel env. Flat fees, no sales calls.",
        desc="ShipReady helps people who built an app in Lovable, Bolt, v0, or Cursor get it safely into production. Preview works; production is secrets, RLS, Stripe webhooks, and Vercel env. $49 async audit, $39 hardening kit, no call required. Launched 24 Aug 2026, 0 customers so far. An honest shop, not a case-study reel.",
        builder_story="AI builders make a working preview in minutes, then get stuck the moment real users, real money, and real data show up: leaked secrets, missing RLS, broken Stripe webhooks, wrong Vercel env vars. I kept seeing the same short list of production gaps, so I packaged fixing them as a flat-fee async service instead of a sales call.",
        logo="", screenshots=[], linkedin="", twitter=""),
    dict(name="PROXe", tagline="PROXe answers, qualifies, books and follows up on every enquiry, on every channel. You never miss a lead again.",
        url="https://goproxe.com", category="AI / ML", stage="Live",
        builder_name="Thanzeel Ashruf",
        builder_bio="Thanzeel Ashruf. Founder of PROXe.",
        desc="PROXe is the AI that runs the customer side of your business. It answers every enquiry across WhatsApp, Instagram, your website and calls in seconds, qualifies the lead, books the appointment, and keeps following up until they decide, remembering every conversation along the way.",
        builder_story="Built for Indian SMBs already running Meta ads. Local businesses pay for leads and lose them in chat. PROXe replies, qualifies, books, and follows up.",
        logo="https://goproxe.com/proxe/brand/proxe-app-icon-1024-maskable.png", screenshots=[],
        linkedin="https://www.linkedin.com/in/thanzeelashruf", twitter=""),
    dict(name="SEMAPRAX", tagline="Agent-native systems language with replayable semantic patches",
        url="https://wavect.io/semaprax/", category="Developer Tools", stage="In Development",
        builder_name="Kevin Riedl",
        builder_bio="Kevin Riedl is a co-founder of Wavect GmbH, the team building SEMAPRAX as an open-source systems-programming research project. The work explores how compiler-checked semantic identity and independently replayable evidence can make agent-assisted changes easier to inspect and constrain.",
        desc="SEMAPRAX is an Apache-2.0 experimental research language for agent-assisted systems programming. Its Rust compiler combines persistent declaration identities, a deterministic semantic graph, bounded context and impact analysis, replayable evidence-gated semantic patches, and explicit capabilities, effects, and ownership. Human-readable .spx source remains the canonical Git projection while the graph provides a checked compiler-produced interface for tools and coding agents. Current output lanes target native C11/Clang and WebAssembly Core. Version 0.2 is pre-alpha and not production-ready.",
        builder_story="Coding agents can generate large edits quickly, but ordinary text patches bind changes to unstable line positions and often hide semantic impact. Wavect started SEMAPRAX to explore a stricter systems-language workflow: declarations keep persistent identities, meaning is projected as a deterministic graph, and proposed semantic changes can be independently replayed before the compiler-owned mutation authority applies them. Coding agents have been used extensively as development assistants; Wavect GmbH retains human responsibility for the design and its executable evidence gates.",
        logo="", screenshots=[], linkedin="", twitter="@wavect_tech"),
    dict(name="CheckShop", tagline="The search engine for independent digital-product stores.",
        url="https://www.checkshop.io", category="E-commerce", stage="Live",
        builder_name="CheckShop",
        builder_bio="CheckShop is a search engine and directory for independent digital-product stores. Search sellers of software, subscriptions, gaming products and online services, compare listings and accepted payment methods side by side, then head to the seller's own site to buy. Every store is reviewed before it appears, and shoppers can report anything that looks off.",
        desc="Independent digital-product stores are everywhere, and almost impossible to compare. Their catalogues and accepted payment methods are scattered across dozens of storefront platforms, with no easy way to search across them or tell which to trust.\n\nCheckShop fixes that. It's a search engine and directory that indexes independent stores selling software, subscriptions, gaming products and online services, so buyers can search once and compare listings, prices and accepted payment methods shown side by side, then click through to the seller's own site to buy.\n\nEvery store is reviewed before it appears publicly, and shoppers can flag any listing that looks wrong. CheckShop never takes payment or handles delivery: it simply helps buyers find independent stores, and helps legitimate sellers get discovered.",
        builder_story="Find independent digital stores. Compare, then buy direct.",
        logo="", screenshots=[], linkedin="", twitter=""),
    dict(name="Presque", tagline="Your old photographs, turned into introductions.",
        url="https://getpresque.com", category="Travel", stage="Coming Soon",
        builder_name="Presque Labs Inc.",
        builder_bio="Presque is a privacy-first social memory map for iOS. We are building a gentler way to discover shared moments and missed connections through the photos people already have.",
        desc="Presque reads the coordinates and timestamps already inside your camera roll and lays them out as a personal atlas. Run a scan and the app compares that atlas with everyone else who chose to be findable, returning the moments you shared with a stranger, eleven metres apart, nine minutes late. Nothing is public by default and no identity appears until both people accept.",
        builder_story="We wanted to turn private photo metadata into a chance to notice people and places without background tracking or public profiles.",
        logo="", screenshots=[], linkedin="", twitter=""),
    dict(name="Dotallio", tagline="Turn a conversation into a live business app, without app-specific code.",
        url="https://www.dotallio.com", category="AI / ML", stage="Live",
        builder_name="Yonatan Lavy",
        builder_bio="Yonatan Lavy is the founder of Dotallio, an AI work-app builder for non-technical professionals and small teams. He is building a reusable, configuration-driven alternative to fragile one-off generated software.",
        desc="Dotallio is an AI work-app builder for non-technical professionals and small teams. Describe the workflow you need and it assembles a live, editable app with smart boards, forms, dashboards, workflows, and documents on one stable engine. Its black swan is architectural: it turns the conversation into reusable configuration instead of a fragile new pile of app-specific code, so the result stays structured, persistent, and easier to evolve.",
        builder_story="We built Dotallio to remove the gap between describing a business workflow and maintaining custom software. Existing AI tools often stop at an answer or produce one-off code that becomes brittle. Dotallio turns the conversation into a live, editable work app assembled from reusable building blocks, giving small teams custom software without making them become software teams.",
        logo="https://www.dotallio.com/assets/logo.png", screenshots=["https://www.dotallio.com/images/dashboard-light.png"],
        linkedin="", twitter="@dotallio"),
    dict(name="TaxMiles: Mileage Tracker", tagline="Auto-detects business drives, estimates tax savings, IRS-ready mileage log.",
        url="https://taxmilesapp.com/", category="Fintech", stage="Live",
        builder_name="Mats Degerstedt",
        builder_bio="Indie iOS maker at Gigabyte LLC. Also built Cleanup My Phone and RecipeScan.",
        desc="TaxMiles is an iOS mileage tracker for gig drivers, contractors, real estate agents, and rideshare drivers. It auto-detects business drives in the background, estimates tax savings as you go, and produces an IRS-ready mileage log. Version 3.0 adds CarPlay, Home and Lock Screen widgets, Live Activity, Deduction Finder, True Hourly Wage, an odometer log, and an AI tax assistant. Free includes 40 trips per month. Pro is $5.99/month, $39.99/year, or $79.99 lifetime, with a 7-day trial on subscriptions.",
        builder_story="Mats Degerstedt built TaxMiles at Gigabyte LLC for people who drive for work and need a complete IRS-ready mileage log without tapping start and stop on every trip.",
        logo="https://taxmilesapp.com/appicon.png", screenshots=[], linkedin="", twitter=""),
    dict(name="Supaorder", tagline="Your brand, our tech. Zero-commission ordering.",
        url="https://www.supaorder.com", category="E-commerce", stage="Live",
        builder_name="Pradeep Saran",
        builder_bio="I am Pradeep Saran, Technical Architect and Founder of Devkart Technologies LLP. I built Supaorder for restaurant operators who want branded ordering, zero-commission subscription pricing and the operational tools to run their own customer relationship.",
        desc="Supaorder is a white-label online ordering platform for restaurants. Restaurants get branded iOS, Android and web ordering apps for a flat monthly fee with zero commission on orders. POS synchronisation with Clover, Square and Toast, auto-dispatch, loyalty, kitchen display and kiosk workflows are included.",
        builder_story="Supaorder was built for restaurant operators who want to own the ordering relationship instead of paying a commission on every transaction. Devkart runs the platform so each restaurant can operate branded ordering, POS sync, dispatch, loyalty, kiosk and kitchen workflows under its own name.",
        logo="https://www.supaorder.com/favicon.svg", screenshots=[],
        linkedin="https://www.linkedin.com/in/devsaran/", twitter=""),
    dict(name="Size Matters", tagline="AI fish photo editor that turns any catch into a trophy",
        url="https://sizematters.app/go", category="Entertainment", stage="Live",
        builder_name="Westhaven Holdings",
        builder_bio="Westhaven Holdings LLC publishes Size Matters, a live iOS fishing entertainment app. The product is an AI photo editor for catch photos, made for bragging rights and jokes rather than official measurements.",
        desc="Size Matters is a live iOS app (version 1.3.0) that uses AI to resize the fish in a catch photo. Upload a selfie with your catch, slide from 50% to 300%, then save or share a before-and-after or a tabloid-style card. Built for anglers who want bragging rights, jokes, and social posts. It is entertainment, not a tournament measuring tool. Free to download on the App Store with a few free resizes, then optional in-app purchases.",
        builder_story="Every fishing trip ends with someone saying the fish was bigger. Size Matters is a fishing double-entendre brand: a novelty iOS app that lets you enlarge the catch in a photo and share the joke. The app is live on the App Store as version 1.3.0.",
        logo="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/3b/da/b5/3bdab565-8338-a94b-1fa5-7ff53c162e73/AppIcon-0-0-1x_U007epad-0-1-85-220.png/512x512bb.jpg",
        screenshots=[], linkedin="", twitter=""),
]

for r in records:
    for k in ("tagline","desc","builder_story","builder_bio"):
        if "—" in r[k]:
            raise SystemExit(f"EM DASH found in {r['name']} field {k}: {r[k]!r}")

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
