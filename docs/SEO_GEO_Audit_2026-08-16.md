# LaunchFree.io — SEO / GEO Audit

Date: August 16, 2026. Audited against the live repo and served HTML. House style: no em dashes.

## Bottom line

The site's fundamentals are strong: robots.txt, llms.txt, the homepage, the directory, category pages, and the sitemap are all well built and AI-friendly. There is one high-impact problem: 56 of the 234 listing pages, all the ones built from the current `template.html` (every recent batch), are client-rendered. Crawlers and AI answer engines receive an empty "Loading..." page with a canonical pointing at the homepage. Fixing that is the single biggest SEO and GEO win available right now.

## What is working (keep it)

- **robots.txt is best-in-class for GEO.** It explicitly welcomes every major AI crawler by name: GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-Web, anthropic-ai, PerplexityBot, Perplexity-User, Google-Extended, Applebot-Extended, Amazonbot, Bytespider, CCBot, cohere-ai, Meta-ExternalAgent, Bingbot, plus the social unfurlers. It also points to the sitemap and llms.txt.
- **llms.txt exists and is current.** Structured overview, correct live count (234), key pages, and a recent-launches list. This is exactly what AI answer engines look for.
- **Homepage is fully optimized.** Complete title, meta description, keywords, canonical, Open Graph, Twitter card, and JSON-LD (WebSite + Organization + SearchAction). Bing verification present, GA4 present.
- **Directory and category pages are server-rendered** with real H1s, meta descriptions, proper self-canonicals, and internal links to listings. This gives crawlers a real path in.
- **Sitemap is comprehensive:** 281 URLs, and every listing page is included. HTTPS, custom domain (CNAME), mobile viewport, and analytics are all in place.
- **178 of 234 listing pages are already server-rendered correctly** (the older generation): real title, real H1, correct self-canonical in the raw HTML.

## Issues, by priority

### P0 - 56 listing pages are JavaScript-only (invisible to crawlers and AI)

The raw HTML served for these pages contains:

- Title: `Loading... - LaunchFree.io | The Runway`
- Meta description: empty
- Open Graph title and description: empty
- H1: empty
- JSON-LD schema: empty
- Canonical: `https://launchfree.io` (the homepage, not the page itself)

Every real value (name, tagline, description, schema, canonical) is injected by JavaScript after load. These are the pages generated from the current `template.html`, which means all of our recent batches (for example bifrost, browseract, calisthenai, clean-the-supermarket-tools, runebook, plus the Aug 14 and Aug 15 batches).

Why it matters:

- **Google** can render JavaScript, but it is slower and less reliable, and the raw canonical pointing at the homepage tells Google "this page is a duplicate of the homepage." That risks these 56 listings not getting indexed on their own URLs.
- **AI answer engines** (GPTBot, ClaudeBot, PerplexityBot, CCBot, and most others) generally do not execute JavaScript. They fetch the page and see an empty "Loading..." shell. So your newest 56 launches are effectively invisible to the exact AI crawlers you welcomed in robots.txt. That is a direct GEO loss on the pages builders most want cited.

The fix: bake the content into the static HTML at build time. We already have each product's data when we generate the page, so the generator should write the real title, meta description, canonical (to the page's own URL), Open Graph tags, H1, the description text, and the JSON-LD schema directly into the file. The interactive parts (tabs, upvote, share) can still hydrate with JavaScript. This is exactly how the older 178 pages already work, so it is a proven pattern, not a redesign.

### P1 - directory.html is stale

The directory page is the main server-rendered crawl path to every listing, and it currently says 179 launches while there are 234. The roughly 55 newest listings have no server-rendered internal link anywhere except the sitemap, which compounds the P0 issue. Regenerate `directory.html` from `listings.json` on every build, and add that step to the runbook.

### P2 - Minor

- **Per-listing Open Graph images.** Most listings reuse the builder's favicon or logo (or the default og-image.png) as the share image. It works, but social and AI cards are inconsistent. Optional: generate a branded per-listing OG image.
- **Stale sitemap lastmod dates.** A number of entries still show May to July dates. Harmless, but worth refreshing when a page actually changes.
- **BreadcrumbList schema.** Listing pages have a visible breadcrumb but no BreadcrumbList JSON-LD. Adding it is a small rich-result win.

## Recommended next step

Fix P0 and P1 together: update `template.html` and the page generator to server-render the listing content, regenerate the 56 JavaScript-only pages and the directory, and re-run the pre-flight checklist. That one change makes your newest launches fully visible to both Google and the AI answer engines, and it brings all 234 listing pages onto the same, correct pattern.
