# LaunchFree build summary, 2026-09-06 (afternoon)

Reviewed 23 new submission records since this morning's pass, built 14 approved listings, held 6 for review, rejected 1. Two resubmissions turned out to already be live under their existing slugs and were skipped rather than rebuilt. 24 carryover items (20 from before this morning plus the 4 held/rejected this morning) were left untouched. Full disposition and reasoning in `claude/submission-review-2026-09-06-pm.md`.

## What was built

14 new listing pages, all rendered from `docs/LISTING_TEMPLATE_SSR.html`, dated **2026-09-06**:

one-custom-song, grafics-mls-ready, pitch-new-client-proposal-template-pdf, gojo, offermath, bigpipe, apilink, calculator-toolkit, meeting-timezones, cierre-mx, lynqra, vellum-lane-free-weekly-planner, first-dollar-kit, ops-control-hq.

All six surfaces touched per listing: the page, `listings.json` (725 to 739 records), `sitemap.xml`, `llms.txt`, `directory.html`, and each item's category page, regenerated via `docs/regen_indexes.py --write`.

`python3 docs/validate_build.py` result: **0 errors, 3 warnings** - all three are the familiar false-positive pattern (a product's own name legitimately contains an em dash, which is exempt from the no-em-dash rule). Two are pre-existing (Awkward Client Emails, Proofstamp) and one is new: **Pitch — New Client Proposal Template (PDF)** carries an em dash in its own product name, which shows up in the title, JSON-LD, breadcrumb, and "Visit" link - all name occurrences, not body copy. Verified none of the actual body copy (description/story/bio/tagline) on that page carries a stray dash. Nothing to fix.

## Two resubmissions of already-live products (skipped, not rebuilt)

- **Humanleap** - already built and live (slug `humanleap`) since earlier today's morning batch. The builder resubmitted it again a few hours later. Skipped per the collision-check rule; duplicate Airtable record deleted.
- **TrendDesk** - already built and live (slug `trenddesk`) since 2026-08-27, exact same URL (atlas-brave-sky-maple.grok.me). Today's resubmission was an exact duplicate; skipped, record deleted.

## Airtable changes

- 14 records: `Status -> Approved`, `Listing URL` set to the live page.
- 2 records deleted: the Humanleap and TrendDesk resubmissions (already-live collisions).
- 6 held for review and 1 rejected (Airtable left untouched in Pending Review, your call) plus 24 already-dispositioned carryover items left untouched.

## Held for review (6)

- **North Brief** - real product, but hosted on a throwaway prototype-builder subdomain (here.now) with a disposable mailinator builder email. Needs a permanent domain/contact before committing to a slug that's never renamed.
- **Digital Dignity Copy Kit** - live product is real, but it's actually a niche Amazon-listing copy optimizer for ESL sellers, not the general "sales-copy writing tool" the submission described. Needs a corrected description.
- **Grok Blueprints** - trades on the "Grok" name for an unofficial third-party template marketplace (possible trademark problem), and Stage says "In Development" while the live site looks fully operational.
- **CSV Cleanup Kit** - every sandbox fetch attempt (https and http) failed with a DNS/robots.txt error, so the page couldn't be verified live at all. Separately worth a look once reachable: payment is crypto-only (Base USDC) for what's described as an ordinary file-cleaning utility.
- **Quotepilot** - a JS-rendered SPA; sandbox fetch only returned the title/meta shell, so the actual functionality couldn't be verified. More importantly, the submitted Builder Story describes a totally different product ("I built ReviewPilot...") - a clear copy-paste mismatch needing clarification.
- **CardURL OG debugger** - cardurl.dev is already live under slug `cardurl` as "CardURL," a hosted-OG-image product. This submission is a free debugger tool at a sub-path of that same domain - not an obvious exact duplicate, but also not a shared multi-tenant platform the way BUILD_SPEC's "different app-store path" exception anticipates. Holding for your call on whether this is a legitimate second listing.

## Rejected (1)

- **portfolio** (sarathks.online) - sandbox fetch failed both ways, and everything in the submission (one-word "marketing" builder story, personal-services tagline/description, Stage "Coming Soon") reads as a personal freelance-services page rather than a product. Airtable left in Pending Review, your call per usual.

## Ship steps (GitHub Desktop)

These 14 pages join the 96 from the last several days, so the diff now totals 110 new listing pages plus the six-surface updates across all batches so far.

1. Open GitHub Desktop, review the diff. It should show exactly: 14 new files in `listings/`, plus `listings.json`, `sitemap.xml`, `llms.txt`, `directory.html`, `index.html`, and the category pages touched by this and the morning batch (ai-ml, saas, service, productivity, marketing, developer-tools, education, creator-tools). No stray files - I did not leave any scratch files behind this time.
2. Commit (in one go or split by batch, your call) - e.g. "Add 14 new launches - 2026-09-06 pm."
3. Fetch origin, pull if needed, then push.
4. Spot check a few of the new listing pages live after deploy, plus the homepage and a category page.
5. Confirm the Make "Runway - Approval Email" automation sends for all 14.

## Note on scratch files

Building today's batch as brand-new pages (no existing HTML to extract from) needed a one-off script and its input data. I wrote both temporarily into `docs/` as `_tmp_build_batch.py` and `_tmp_build_records.json`, plus a `listings.json.bak_pre_pm_batch` backup, ran the build, then deleted all three before finishing - so they should not appear in your Changes list. Flagging this so you know why device permissions asked for a delete grant mid-session.
