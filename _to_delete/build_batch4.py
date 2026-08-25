import json, re, urllib.parse

WD = "."
TEMPLATE = open(f"{WD}/docs/LISTING_TEMPLATE_SSR.html").read()
BUILD_DATE = "2026-08-25"
DATE_LONG = "August 25, 2026"

records = [
    dict(name="Rixin Archive", tagline="Local smart filing and AI-assisted retrieval for Android",
        url="https://rixin-archive.leelele9.chatgpt.site", category="Productivity", stage="Live",
        builder_name="Zhonghai Li",
        builder_bio="I am an independent Android developer at Lexiang Technology, building practical local-first tools for everyday work. Rixin Archive focuses on making scattered documents and media easier to file, understand, and retrieve without forcing AI into the workflow.",
        desc="Rixin Archive is an Android filing system for documents and media received through chat apps, browsers, office suites, Downloads, and file managers. Users share or send a supported file to the app, choose an archive box, and keep an independent local copy with its original extension. Retrieval combines keywords, notes, file types, dates, source apps, tags, archive boxes, and custom dimensions. Optional on-device AI and OCR can suggest titles, summaries, tags, and filing metadata before the user confirms the archive.",
        builder_story="Work files often disappear into separate chat apps, download folders, office tools, and photo albums. I built Rixin Archive after seeing how hard it was to retrieve a contract, quotation, project image, or study PDF once the original conversation was buried. The goal is a practical local archive that keeps filing manual and predictable while using AI only as an optional assistant.",
        logo="https://rixin-archive.leelele9.chatgpt.site/icon-512.png", screenshots=[], linkedin="", twitter=""),
    dict(name="AI Text Watermark Remover", tagline="Detect invisible characters and strip Markdown paste noise from AI text",
        url="https://aitextwatermarkremover.com", category="Productivity", stage="Live",
        builder_name="neo wang",
        builder_bio="An independent builder making small, free browser tools for writers and content teams.",
        desc="AI Text Watermark Remover is a set of free browser tools for anyone who pastes AI-generated text into their own work. It detects invisible/zero-width characters, strips Markdown paste noise, and cleans odd spacing so your text looks human-written and imports cleanly into any editor or CMS. Everything runs in the browser, and an optional Pro rewrite is available. It is not an AI-detector bypass and not an image watermark remover. Just clean, honest text hygiene for writers, marketers, and students.",
        builder_story="I kept finding hidden zero-width characters and broken Markdown artifacts every time I pasted AI drafts into my CMS. Cleaning them by hand was tedious, so I built a fast browser tool that does it in one click.",
        logo="", screenshots=[], linkedin="", twitter=""),
    dict(name="Third-Party API Contract Drift Monitor", tagline="Detect authorized API contract changes with baseline evidence",
        url="https://apify.com/invaluable_rondeau/third-party-api-contract-drift-monitor", category="Developer Tools", stage="Live",
        builder_name="PROOFNEXA",
        builder_bio="I build narrow, evidence-first developer tools for recurring operational checks. Third-Party API Contract Drift Monitor helps API teams detect authorized contract changes with dated fingerprints while avoiding response bodies, login flows, and credential handling.",
        desc="A privacy-bounded monitor for authorized third-party APIs. Provide an OpenAPI 3 spec URL and a baseline state ID, then run bounded GET checks to detect added, removed, or changed contracts. It records fingerprints, timestamps, status codes, and timeout or rate-limit outcomes without POST requests, login flows, proxy rotation, or response bodies. Built for API teams that need scheduled change evidence before integrations break.",
        builder_story="Third-party API contracts can change without notice, and teams need a dated record of what changed before an integration fails. I built this as a narrow, GET-only evidence monitor so teams can check authorized endpoints on a schedule without collecting response bodies or handling credentials.",
        logo="", screenshots=[], linkedin="", twitter="@aaa1487855"),
    dict(name="LyfSkills Discover", tagline="Find trusted classes and activities for children across India",
        url="https://discover.lyfskills.com", category="Education", stage="Live",
        builder_name="Sumit Kapoor",
        builder_bio="I work on LyfSkills, helping families discover trustworthy skill-building classes and activities for children across India. We are making local discovery simpler for parents.",
        desc="LyfSkills Discover helps parents in India find and compare skill-building classes and activities for children across sports, music, dance, performing arts, yoga, academics, STEM, and more. Parents can explore relevant options by category and location.",
        builder_story="We built LyfSkills Discover to reduce the time and uncertainty parents face when searching for trustworthy local classes and activities for their children. Bringing options together by category and location makes comparison much simpler.",
        logo="", screenshots=[], linkedin="https://www.linkedin.com/company/lyfskills", twitter=""),
    dict(name="getgiffgaff", tagline="Chinese giffgaff SIM card guide and service",
        url="https://getgiffgaff.com/", category="Travel", stage="Live",
        builder_name="Xiaowei",
        builder_bio="I am an independent builder creating practical Chinese-language services for international travelers and people moving to the UK. I built getgiffgaff to remove the language and setup friction around UK mobile service.",
        desc="getgiffgaff is an independent Chinese-language guide and SIM card service for giffgaff users. It helps Chinese-speaking travelers and people moving to the UK purchase and activate a giffgaff SIM, choose a plan, understand roaming and troubleshoot common account issues.",
        builder_story="I built getgiffgaff after seeing Chinese-speaking travelers struggle with fragmented English instructions for buying and activating UK mobile service. The goal is to make the entire giffgaff setup process clear in Chinese and provide practical help when something goes wrong.",
        logo="https://getgiffgaff.com/apple-touch-icon.png", screenshots=[], linkedin="", twitter=""),
    dict(name="Vedic Astrology Chart", tagline="Free sidereal Vedic birth chart calculator",
        url="https://vedicastrologychart.net", category="AI / ML", stage="Live",
        builder_name="Vedic Astrology Chart Team",
        builder_bio="The product team behind a free browser-based Vedic astrology chart calculator.",
        desc="Vedic Astrology Chart is a free browser tool that generates a sidereal birth chart from birth date, time, and location, then presents planetary positions and readable Vedic astrology interpretations.",
        builder_story="We built it to make foundational Vedic chart calculations easier to access without requiring paid desktop software or a consultation for every exploratory chart.",
        logo="", screenshots=[], linkedin="", twitter=""),
    dict(name="Unse Nadri: Place Fortune", tagline="Check today's personal fortune with a place already on your plan",
        url="https://play.google.com/store/apps/details?id=com.unsenadri.app&hl=en&gl=US", category="Other", stage="Live",
        builder_name="Jaehoon Lee",
        builder_bio="I am an independent Android developer in South Korea. I build small apps around everyday moments, and Unse Nadri explores the personal curiosity people feel after choosing a place they plan to visit.",
        desc="Unse Nadri is a free Android app for checking today's personal fortune with one place already on your plan. Search a cafe, park, venue, station, neighborhood, or business to see a place-fortune score and a short five-elements and sky-timing reading. Results can be saved and revisited. The app supports six languages and uses localized store screenshots.",
        builder_story="I noticed that most place apps focus on deciding where to go. I wanted to explore the more personal moment that comes afterward: the destination is already chosen, and you are curious about how that place and today may fit you.",
        logo="https://play-lh.googleusercontent.com/DxH87ux3nwPsML4aZXDpWpSCUBybHZe4ZzM10EVyaX8L8m616E8UQIKOdGIwWiA9wZ3uGjEqW4YDt0e41h4MyA=w512-h512-rw",
        screenshots=["https://play-lh.googleusercontent.com/ZjO7W55l9UFwLds-WMKiWFUocNQn8R8Pscu1_vU17wwFii3kqvA9XnvxrbjHRNw4JX5383Ahqty6QLa8oCCj=w1080-h1920-rw"],
        linkedin="", twitter=""),
    dict(name="Kit Ventas en 24h", tagline="Consigue clientes en 24 horas con guiones y prompts listos.",
        url="https://kit-ventas-24h.santoshpandita836517.chatgpt.site", category="Marketing", stage="Live",
        builder_name="Kit Ventas en 24h",
        builder_bio="Kit Ventas en 24h es un recurso digital en espanol para freelancers y pequenos negocios. El proyecto reune guiones, prompts y seguimiento en un sprint de 24 horas para facilitar la primera conversacion comercial.",
        desc="Kit digital en PDF para freelancers y pequenos negocios que necesitan activar ventas sin complicar su proceso. Incluye un sprint de 24 horas, 12 guiones para contacto y seguimiento, 20 prompts de IA, respuestas a objeciones, un tracker y una checklist. Se compra por 9 USD y se entrega como descarga digital despues de confirmar el pago.",
        builder_story="Se diseno para convertir el consejo generico de ventas en una secuencia breve y accionable: una oferta clara, mensajes listos y seguimiento medible para que un profesional independiente pueda empezar hoy.",
        logo="", screenshots=["https://kit-ventas-24h.santoshpandita836517.chatgpt.site/og.png"], linkedin="", twitter=""),
    dict(name="Be The Final Boss Codes, Guides, Wiki & Updates", tagline="Verified Roblox codes, wiki & guides for Be The Final Boss",
        url="https://bethefinalbossgg.wiki/", category="Entertainment", stage="Live",
        builder_name="Blues Keep",
        builder_bio="Independent fan-site maintainer for Roblox game guides.",
        desc="Independent fan wiki for the Roblox tycoon Be The Final Boss: verified redeem codes, unit/weapon databases, skill tree, boss waves, mutations, events, calculators and official update notes. Free, no login.",
        builder_story="Be The Final Boss GG is an independent fan-made wiki and player guide for the Roblox tycoon game Be The Final Boss. The site focuses on verified redeem codes, source-aware game data, and practical progression advice instead of invented stats. Players can browse active codes with one-click copy, check unit and weapon databases, review skill tree nodes and costs, study boss wave checkpoints, and compare mutation multipliers such as Shiny, Cursed, and Demonic.",
        logo="https://bethefinalbossgg.wiki/imgs/game/icon.webp", screenshots=["https://bethefinalbossgg.wiki/imgs/og.jpg"], linkedin="", twitter=""),
    dict(name="Solana Launch Vault", tagline="24 launch frameworks and a distribution playbook for Solana builders",
        url="https://solana-quick-kit.nxtboyiii.chatgpt.site/solana-launch-templates", category="Marketing", stage="Live",
        builder_name="Lucas Wilde",
        builder_bio="Lucas builds focused browser tools for people shipping on Solana. Solana Quick Kit combines practical launch utilities with public-chain payment verification and no mandatory account.",
        desc="Solana Launch Vault is a downloadable Markdown pack for Solana builders. It includes 24 fill-in-the-blank launch frameworks, a six-channel distribution playbook, and a seven-point shipping checklist. Buyers pay once in SOL, verify the public transaction in their browser, and download the file immediately.",
        builder_story="The free launch-copy generator showed that a focused structure helps builders move past a blank page. The Vault packages the reusable frameworks and practical distribution checklist into a portable file that works in any text editor or notes app.",
        logo="https://solana-quick-kit.nxtboyiii.chatgpt.site/solana-quick-kit-social.png", screenshots=[], linkedin="", twitter=""),
    dict(name="Extract.FAST", tagline="Extract images, text, audio, and metadata from documents and media in bulk.",
        url="https://extract.fast", category="SaaS", stage="Live",
        builder_name="Stewart Celani",
        builder_bio="Stewart Celani is the founder of Extract.FAST and the Tools.FAST network, building practical browser tools for turning mixed files into useful outputs.",
        desc="Extract.FAST is a browser-based bulk extraction workspace for pulling images, text, audio, metadata, OCR results, pages, frames, and embedded files from documents and media. Upload PDFs, Word, PowerPoint, Excel, email, archives, audio, or video, choose the outputs you need, and download organized results. It supports real batch workflows rather than one file at a time, with free daily credits to try the product and Pro capacity for larger jobs. Processing uses encrypted transfer and automatic deletion after processing, making it useful for researchers, operations teams, developers, and anyone turning mixed files into usable assets quickly.",
        builder_story="Working with mixed documents and media often meant installing separate utilities or handling one file at a time. Extract.FAST was built to make that workflow simple in a browser: upload a real batch, choose the outputs, and get organized results quickly. We wanted extraction to be useful for researchers, operations teams, developers, and anyone turning mixed files into usable assets.",
        logo="", screenshots=[], linkedin="", twitter="@stewartcelani"),
    dict(name="Conversion Snapshot 24", tagline="A page-specific conversion audit delivered in 24 hours",
        url="https://h7vzkqbo7cap4j2tisuhcuuy5rxvvydz.pastehtml.dev/", category="Service", stage="Live",
        builder_name="AuditForge",
        builder_bio="AuditForge is an independent conversion-research practice focused on SaaS and AI product pages. It turns observable buyer friction into ready-to-paste copy and testable experiments, without fabricating customer metrics.",
        desc="Conversion Snapshot 24 is an independent, page-specific conversion audit for SaaS and AI product teams. It identifies the highest-friction buyer decisions, rewrites the hero and primary CTA, proposes proof and objection fixes, checks the mobile decision path, and supplies three measurable experiments. Buyers receive the completed audit within 24 hours for a one-time USD 129 payment, with a useful-or-refunded guarantee. A public nine-page AI demo-agent benchmark shows the research method before purchase.",
        builder_story="This service started after reviewing AI product pages that promised instant value but routed visitors into vague sales gates. The goal is to give small teams a decision-ready, implementation-ready audit without a meeting, a retainer, or invented benchmarks.",
        logo="", screenshots=[], linkedin="", twitter=""),
    dict(name="BitShovel", tagline="Source-linked product discovery with clear evidence limits.",
        url="https://bitshovel.site/en", category="AI / ML", stage="Live",
        builder_name="BitShovel editorial team",
        builder_bio="I help maintain BitShovel, an independent product discovery site focused on clear context, source links, and honest evidence boundaries.",
        desc="BitShovel is an editorial field guide to products and apps worth noticing. Each profile explains what it solves, where it stands, why it matters, and what the evidence still does not prove.",
        builder_story="The web moves quickly, but launch pages often flatten a product into a headline. BitShovel was built to preserve useful context: the problem, current stage, sources, and limits, so people can decide what to explore next.",
        logo="", screenshots=["https://bitshovel.site/og-en.png"], linkedin="", twitter=""),
    dict(name="AurasPay", tagline="Non-custodial crypto payment acceptance for merchants.",
        url="https://auraspay.com", category="Fintech", stage="Live",
        builder_name="Mazen Zakariya H Alshareef",
        builder_bio="Founder and CEO of AurasPay, building non-custodial merchant payment acceptance and orchestration for on-chain commerce. I focus on practical payment tools that keep settlement under merchant control.",
        desc="AurasPay is a non-custodial merchant payment acceptance and orchestration platform for businesses that want to accept on-chain payments. Merchants can create payment links, QR codes, point-of-sale requests, invoices, API integrations, webhooks, and ecommerce plugins. Customers review and sign transactions from their own wallets, while settlement goes directly to merchant-controlled addresses. AurasPay does not hold customer or merchant funds and does not present itself as a bank, exchange, custodian, card acquirer, or licensed payment service provider. The platform supports multiple blockchain networks, including Solana and BNB Chain, and provides operational tooling for merchant checkout and payment tracking.",
        builder_story="We built AurasPay to give merchants a direct, non-custodial way to accept on-chain payments without handing custody of customer or merchant funds to a payment platform.",
        logo="", screenshots=[], linkedin="", twitter="@auras_pay"),
    dict(name="HawkOVR", tagline="Free Diablo IV event timers and Helltide overlay for Windows",
        url="https://d4builds.ai", category="Developer Tools", stage="Live",
        builder_name="Qiang Fei",
        builder_bio="Independent developer of HawkOVR, a free Windows companion overlay for Diablo IV. I focus on practical local tools, transparent feature documentation, and clear disclosure of update behavior and game-rule risks.",
        desc="HawkOVR is a free Windows x64 desktop overlay companion for Diablo IV. It shows world-event countdowns, Helltide worm and chest indicators, and configurable widgets while playing. Optional pickup automation, skill auto-cast, and Actor/Object display may generate or act on game input; users should review Blizzard's current rules and use those features at their own risk. The launcher connects online for updates. HawkOVR is unofficial and not affiliated with Blizzard.",
        builder_story="I built HawkOVR because switching between Diablo IV and browser trackers during time-sensitive world events was disruptive. The goal is to keep essential timers and Helltide information visible in a small local Windows overlay, while clearly documenting optional automation features and their rule risks so players can make informed choices.",
        logo="https://d4builds.ai/og.png", screenshots=["https://d4builds.ai/screenshots/world-event-countdown.webp"], linkedin="", twitter=""),
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
