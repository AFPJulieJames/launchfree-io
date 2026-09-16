# LaunchFree.io Build Summary — 2026-09-16

## What was built

55 new listing pages, built from `docs/LISTING_TEMPLATE_SSR.html`, all six surfaces touched: SimpleSaaS Analytics, ProQR, KKIKA.ai, Petro, Top Proxy, RestReserve, LoreJam, Timothy Kane Dev Micro Kits, Best Launch Platforms, Steady Ground, Swarm Hosts, Side Hustle Money Command Center 2026, Client Ledger Mini, 1099 Quarterly Tax Set-Aside Calculator 2026, DoorDash Uber Weekly P&L $11, Freelancer Invoice Late-Pay Tracker $9, Content Creator Income Tracker $12, Cupid, Etsy & Small Shop Seller P&L 2026, My Celebrity Parents, Gig Tip Tracker 2026, Konversa, Uber Lyft Rideshare Weekly P&L 2026, Side Hustle Savings Goal Tracker 2026, Freelance Rate Profit Calculator 2026, Baojiji Tools, MailVeri, Gig & Freelance AI Prompt Pack, Hustle Ledger Starter Pack, Skirr AI, Find Accountant UAE, Agentes Inteligentes, Budy, PinoyFreelance.PH, Deepli Clean, Nest (Free Pregnancy & Baby Notion Tracker), Statsnet, HTML4SEO, FISCUS AI, AI SEO Rainmakers, High Signal, Paper Route, NamingCube, Story of Us, Derelict Properties Leads, Astrology Geeks, LetsBeta, Lahjty, SizeCompare, KwaFlux, Peon, CVwerk, BillFast, Panda Largo, Subscription & Tool Cost Audit 2026.

Nest was built with no price tag, matching the review doc's note that it's a free ($0) product. No other build-time data corrections were needed for this batch.

**3 flip-only** (already live under an existing slug, not rebuilt): Digital Dignity Transformation Kit, ToolSphare, Rapid Indexer. Each collided with a page shipped in an earlier pass; the new submission's Airtable record was flipped to Approved pointing at the existing listing URL.

`listings.json`: 1306 → **1361** records. `sitemap.xml`: 55 new `<url>` blocks appended, all 1361 slugs confirmed present. Category pages, `directory.html`, `llms.txt`, and `index.html`'s hero stat were regenerated from the updated `listings.json` and all show 1361.

## Validator

`docs/regen_indexes.py --write` hit the same device-side FUSE deadlock as yesterday, isolated entirely to the unrelated `strip_dead_css()` cleanup step (35 pre-existing `radar/`/`research/` pages, none touched by this build, none needed stripping anyway). The category pages, directory, llms.txt, and homepage hero stat all wrote successfully before that step ran, confirmed directly on the device.

`docs/validate_build.py` hit the same broad pre-existing-file lock seen yesterday, so I ran the resilient variant again (identical logic, unreadable pre-existing pages logged as WARN with the device I/O reason instead of ERROR; every readable file, including all 55 built today, still gets full ERROR-level strictness):

**0 errors.** 1269 warnings, 1263 of which are the pre-existing unreadable-page locks (same class as yesterday, none touched by this build). The remaining 6 warnings are 2 em-dash-in-name flags (Nest's name contains an em dash, which is expected and correct — the product NAME is deliberately exempt from `fix_dashes` per the hard rules; this matches existing live listings like Kupid). Spot-checked SimpleSaaS Analytics, Panda Largo, and Subscription & Tool Cost Audit 2026 directly: real H1, correct canonical URL, SoftwareApplication + BreadcrumbList JSON-LD present on all three.

## Airtable

All 58 Approve records (55 built + 3 flip-only) flipped to `Status = Approved` with the correct `Listing URL`. Verified via direct record lookup after the flip (SimpleSaaS Analytics confirmed Approved with its listing URL set).

27 duplicate submissions deleted (confirmed gone from the base on lookup). All 25 Review-held items and all 12 Rejected items are untouched at `Pending Review` — spot-checked Vesta Peptides, Claude Resets, ShipPage, KeyBack, and ASTROC2M Smart Contribution directly, all still Pending Review.

## Still held, your call (from the review doc)

- The 16-template "Hustle Ledger" overnight flood: 13 approved and built, 3 (Schedule C Expense & Receipt Log 2026, Freelance Client CRM Lite 2026, Mileage Log Pro 2026) held in Review so you can decide on pacing rather than all 16 going live from one builder in one window.
- **Claude Resets**: real, functional product, but uses "Claude" in the name and domain with no Anthropic affiliation, and was submitted 5x under 3 different throwaway emails. Held in Review, not built, needs your trademark call.
- ASTROC2M Smart Contribution and ASTROC2M Mission Passport rejected as a crypto wallet-connect/token-reward pair.

Full detail on every held and rejected item is in `claude/submission-review-2026-09-16.md`.

## Ship it

The build is on your Mac, not live yet. In GitHub Desktop:

1. Open the LaunchFree.io repo.
2. Review the changed files (55 new pages under `listings/`, `listings.json`, `sitemap.xml`, `llms.txt`, `directory.html`, and the category pages under `categories/`).
3. Commit with a message like "Add 55 new launches, flip 3 collisions — 2026-09-16 build."
4. Push to origin.

Once pushed, Make's approval-email automation picks up the 58 flipped Airtable records on its next poll and sends builder emails automatically — no action needed from you there.
