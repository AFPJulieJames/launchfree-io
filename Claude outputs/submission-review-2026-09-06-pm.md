# LaunchFree submission review, 2026-09-06 (afternoon)

Pulled the current `Status = Pending Review` queue: 47 records. 24 are carryover already dispositioned (untouched): the 20 long-standing/09-04/09-05 holds already tracked in `claude/submission-review-2026-09-06.md`, plus the 4 held/rejected from this morning's pass (HJcyberX, HJ CyberX YouTube, Free Grok Spicy Prompt Generator, ApplyTailor App). The remaining 23 are new since this morning's review and were checked live from the sandbox (WebFetch only, parallelized across five review agents, plus direct re-verification on three ambiguous ones).

## Already-live products, resubmitted (skipped, not rebuilt)

- **Humanleap** (humanleap.com) - this exact product was reviewed, built, and approved earlier *today* (slug `humanleap`). The builder resubmitted it again a few hours later. Per the collision-check rule, skipped rather than rebuilt; the duplicate Airtable record was deleted.
- **TrendDesk** (atlas-brave-sky-maple.grok.me) - already built and live under slug `trenddesk` since 2026-08-27. Today's resubmission is an exact duplicate (same URL, same product). Skipped; duplicate record deleted.

## Approved and built (14)

- **One Custom Song** (onecustomsong.com) - live AI music-gift platform, working audio previews, occasion carousel, and create-song flow; matches submission.
- **Grafics MLS Ready** (grafics.com/mls-ready/) - live, real MLS-safe photo cleanup service for realtors with clear scope (banner/watermark/timestamp removal, explicitly no fake staging or invented architecture), pricing tiers, and a free trial.
- **Pitch — New Client Proposal Template (PDF)** (Gumroad) - live $12 fill-in freelance proposal template, matches submission almost verbatim, explicitly not a contract or legal advice.
- **Gojo** (trygojo.com) - live native macOS 14+ notch productivity hub; every claimed feature (dictation, window snapping, clipboard history, file shelf, media/display controls) is genuinely there, free trial with clear pricing after.
- **OfferMath** (offermath-app.vercel.app) - live, working AI compensation calculator (salary, bonus, equity/strike/FMV/vesting inputs), matches submission exactly.
- **BigPipe** (bigpipe.agency) - live, genuinely functional free venture-planning tools (break-even calculator, pricing calculator, business brief templates), usable without an account. The submission is upfront about the paid "Founden" upsell rather than hiding it.
- **ApiLink** (apilink.io) - live, real unified API gateway to 433+ models with working code samples, transparent pricing, docs, and a status page.
- **Calculator Toolkit** (calculator-toolkit.com) - live, genuine browser-based tip/bill-split calculator, no account required, runs locally.
- **Meeting Timezones** (meetingtimezones.com) - live, real time-zone comparison tool: city search, 24-hour grid with color-coded overlap indicators, share-link, matches submission closely.
- **Cierre MX** (Payhip) - live Spanish-language freelancer kit for Mexico (quoting + WhatsApp follow-up scripts + collection), free sample funnels to the MX$179 full kit, standard checkout.
- **Lynqra** (lynqra.com) - live Singapore AI-ops-automation service with a specific consult-build-train methodology, named partners, and a business registration number.
- **Vellum Lane Free Weekly Planner** (itch.io) - live, exactly what was described: a free undated one-page A4 weekly planner PDF, instant digital download.
- **First Dollar Kit** (Polar checkout) - live 48-hour digital-sale runbook with playbook, listing copy, outreach templates, checklist, and pricing ladder; matches submission.
- **Ops Control HQ** (opscontrolhq.com) - live exception-first ops-control toolkit for founders/COOs with free diagnostics and paid one-time tools; matches submission, no red flags.

All six surfaces touched per listing: the page, `listings.json` (725 records going in, see build summary for the out count), `sitemap.xml`, `llms.txt`, `directory.html`, and each item's category page, regenerated via `docs/regen_indexes.py --write`.

## Held for review (6) - Airtable left in Pending Review, not built

- **North Brief** (sunny-yoga-nxyz.here.now) - the live page is a real, coherent product (a paid competitor-analysis brief) that matches the submission, but it's hosted on a throwaway prototype-builder subdomain and the builder used a disposable mailinator address. Slugs are never renamed once built, so this needs a permanent domain and real contact before committing to one.
- **Digital Dignity Copy Kit** (digital-dignity.com/transformation-kit/) - the live product is real and functional, but it's actually a niche Amazon-listing copy optimizer for ESL/international sellers ("turn broken English into US-buyer copy"), not the general "sales-copy writing tool for sales pages, emails, and product copy" the submission described. Needs a corrected description before this gets built as what it actually is.
- **Grok Blueprints** (grokblueprints.whop.site) - the live Whop marketplace has substantial real content (~100 templates, filters, upvotes), but two things need a look: it trades on the "Grok" name for an unofficial third-party template marketplace (possible trademark problem), and the submission lists Stage as "In Development" while the live site looks fully operational with a mature catalog.
- **CSV Cleanup Kit** (csv-cleanup-kit.pages.dev) - every sandbox fetch attempt (https and http) failed with a DNS/robots.txt lookup error, so the live page could not be verified at all. Separately worth flagging once it's reachable: the submission states payment is "$40 per file via Base USDC, no subscription, no signup" - a crypto-only checkout for what's described as an ordinary file-cleaning utility, worth a manual look rather than a reflexive approve.
- **Quotepilot** (quotepilot-saas-plat-9xjs.bolt.host) - this is a JS-rendered single-page app; sandbox fetch only returned the page's title/meta shell, so the actual quote/client/PDF functionality couldn't be verified live. More importantly, the submitted "Builder Story" text describes a completely different product ("I built ReviewPilot because responding to customer reviews...") - a clear copy-paste mismatch that needs the builder to clarify regardless of what the site turns out to contain.
- **CardURL OG debugger** (cardurl.dev/check) - this domain, cardurl.dev, is already live under slug `cardurl` since 2026-09-04 as "CardURL," a hosted-OG-image product. This submission is for a free debugger tool at a sub-path of that same domain. It's a different page with a distinct free-tool value prop, not an obvious exact duplicate, but it's also the same company's own domain rather than a shared multi-tenant platform (the kind of case BUILD_SPEC's "different app-store path" exception is meant for) - holding for your call on whether this is a legitimate second listing or the same product resubmitted.

## Rejected (1) - Airtable left in Pending Review, your call

- **portfolio** (sarathks.online) - sandbox fetch failed on both https and http (robots.txt errors), so the page couldn't be loaded at all. Independent of that, everything in the submission reads as a personal freelance-services page rather than a product: the tagline is a personal claim ("A BEST DIGITAL MARKETER IN KOLLAM"), the description is "get in touch with Sarath KS... for SEO, website development, and digital marketing services," the entire "Builder Story" is the single word "marketing," and Stage is marked "Coming Soon." This matches BUILD_SPEC's "not a product" reject criterion (personal page, no distinct product behind it) rather than something worth an email asking for a fix.

## Collision check (BUILD_SPEC section 4)

All 14 approved slugs and hosts checked against the pre-batch listings.json: no collisions - `bigpipe.agency`, `apilink.io`, `calculator-toolkit.com`, `meetingtimezones.com`, `lynqra.com`, `opscontrolhq.com`, `onecustomsong.com`, `grafics.com`, and `trygojo.com` are all new hosts. `nydaymuse.gumroad.com`, `payhip.com`, and `buy.polar.sh` already host other unrelated products (Gumroad/Payhip/Polar are shared checkout platforms), which is not a collision. Two items (Humanleap, TrendDesk) *were* found to already exist live under their expected slugs and exact URLs - skipped rather than rebuilt, see above.

## Next: see `claude/launchfree-build-2026-09-06-pm.md` for what got shipped.
