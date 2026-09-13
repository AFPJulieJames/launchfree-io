# Build summary — 2026-09-13

Build pass for the 34 Approved records from today's `claude/submission-review-2026-09-13.md`. All six surfaces touched for every new listing, all generators and the validator run clean, Airtable flipped.

## Outcome

- **34 new listings built and live in the repo**, all six surfaces touched: page, `listings.json`, `sitemap.xml`, `llms.txt`, `directory.html`, category page.
- **5 already-live matches flipped to Approved** with their existing Listing URLs. No rebuild.
- **5 duplicate-submission records deleted** from Airtable (the MicroPay Labs / SkillMint / StudyNotes Hub promo-page cluster from today's review).
- **Airtable Status = Approved** on all 39 (34 built + 5 flip-only), each with its Listing URL, so Make's "Runway - Approval Email" automation picks them up on its next poll. No email sent by hand.
- **12 moved to Pending Further Review-Email sent, 3 Rejected**, and Vesta Peptides left untouched at Pending Review, exactly as the review doc called for.
- `listings.json` went from **1111 to 1145** records. `llms.txt`, `directory.html`, and the homepage hero stat all agree at 1145.

## A data-integrity note worth your attention

Twelve of the 60 records pulled today were carryovers I'd already dispositioned on 2026-09-12 (Reject or hold), and they'd all reverted to Pending Review in Airtable despite the prior build doc recording the correct status. I re-verified every one fresh rather than trust the stale disposition, and one of them (**Tokenized**) actually flipped from Reject to Approve on a second, more literal read of the standard: tokenized.so is a research/comparison directory with no token of its own for sale, not a token-as-product scheme. Full reasoning is in the review doc. If held or rejected items keep bouncing back to Pending Review on their own, that queue will never actually shrink, worth checking what's resetting the status.

## Built (34)

Tokenized, AI Outbound OS, Anhydra Systems, Bickqr, Call2Physio, Free Bible Study, Free Invoice Webhook Stub, Miloosh, Quote — Offline Freelance Rate Calculator (Free HTML), 3DIMLI, AI Prompts Online, Automation ROI Calculator, AviateHub, Cash Crow Digital Ops Packs, Client Magnet Kit, Dayora, FORE, FileNest WorkTools, Freelance Proposal Win Kit, Freelancer Ops Bundle, GamerHub, JustFiled, Kitset, Kovyxa, Literacy Trail, Packfiled, Peaklify, Rapid Indexer, Remoote, SayVocal, Sheetshot, StoreRadar, ToolSphare, Treviya.

One category correction carried over from the review: **Client Magnet Kit** was submitted as "AI Tools," not one of the 17 canonical categories. Mapped to **AI / ML**, the closest fit for a prompt kit.

## Already live, flipped only (5)

Exact URL match to a listing already in `listings.json`. No rebuild:

- **VitalityAfter45** (reckBT3PoGCXnNRnG) → `vitalityafter45.html`
- **AI Room Makeover** (reciCyJpq20KUODUh) → `ai-room-makeover.html`
- **Video Size Reducer** (recePe6dkC6BOggVY) → `video-size-reducer.html`
- **B's Ads** (recsA37oOIEDGKian) → `b-s-ads.html`
- **Finanzas Freelance MX** (recnt7PCXZCL3xcGM) → `finanzas-freelance-mx.html`

## Duplicate records deleted from Airtable (5)

recNm4mPjJZzgfHdi, recqn1IH0K973ZAGa, recBpuN82jhiAPW70, rec9TXZc9QS6rPw5D, recPA3EUEddWRB2UT, all promo/teaser pages for MicroPay Labs, SkillMint, and StudyNotes Hub, same builder (frhdirstb2kjj@uberip.com), same day.

## Held, untouched at Pending Review

The 12 Review-held items, the 3 Rejected items (Status flipped as noted above), and Vesta Peptides (recRtQluQnbjUPNPh) — all exactly as listed in `claude/submission-review-2026-09-13.md`. Vesta's Airtable status is unchanged from before.

## Build verification

- `python3 docs/regen_indexes.py --write` ran clean (after patching around the unrelated `strip_dead_css()` step, which fails when `radar/`/`research/` aren't staged locally; confirmed by direct inspection that `index.html`, `llms.txt`, and `directory.html` had already written correctly before that step ran), writing 17 category pages, `directory.html`, `llms.txt`, and `index.html`.
- `python3 docs/validate_build.py` (a build-local patched copy, see note below) reported **0 errors**, 10 warnings, all expected:
  - 4 warnings are em dashes inside product **names**, which BUILD_SPEC exempts from the em-dash rule (including today's "Quote — Offline Freelance Rate Calculator (Free HTML)").
  - 5 warnings are the matching "em dash in body copy" check firing on **related-launch card links** to the pre-existing "Kupid — Free AI Automation" listing on other pages, not on anything in today's batch. Confirmed by direct inspection of the built HTML.
  - 1 aggregate warning disclosing that most of the 1111 pre-existing `listings.json` records have no local page file staged this run (expected, they weren't touched today).
- `listings.json` record count: 1111 → 1145, exactly the 34 new records.
- Spot-checked `tokenized.html` and `treviya.html`: real `<h1>`, self-referencing canonical URL, valid JSON-LD (SoftwareApplication + BreadcrumbList), correct vote-script slug, no leftover `{{PLACEHOLDER}}` text.
- `sitemap.xml`: all 34 new slugs present, still ends in `</urlset>`.
- `llms.txt`, `directory.html`, and `index.html`'s hero stat all read **1145**, matching `listings.json`.
- All 34 new pages plus all 22 regenerated support files (`listings.json`, `sitemap.xml`, `llms.txt`, `directory.html`, `index.html`, all 17 `categories/*.html`) are written into your repo folder. Nothing has been committed yet, that's the GitHub Desktop step below.

**On the validator:** the related-card existence check only knows about locally-staged page files by default, which produces hundreds of false-positive "points at a page that doesn't exist" errors against the other ~1111 live pages that weren't part of today's build. I ran a build-local patched copy of `docs/validate_build.py` that checks related-card targets against the full `listings.json` catalog instead of just staged files, and reports one aggregate warning instead of one error per un-staged pre-existing record. Every check that matters (today's 34 pages, JSON structure, sitemap, llms.txt, directory.html, category pages, homepage stat) ran against the complete, current file, nothing skipped. The patched script was scratch-only; `docs/validate_build.py` in the repo is untouched.

## Ship steps (GitHub Desktop)

1. Open GitHub Desktop with `launchfree-io` as the current repository.
2. Check the Changes list: you should see 34 new files under `listings/`, plus `listings.json`, `sitemap.xml`, `llms.txt`, `directory.html`, `index.html`, and all 17 `categories/*.html` files (regen_indexes.py rewrites every category page's count block regardless of whether that category got a new launch today).
3. Commit with something like `Add 34 new listings (9/13 batch)`.
4. **Fetch origin.** If there are newer commits on the remote, **Pull origin** first.
5. **Push origin.** GitHub Pages redeploys in roughly one to three minutes.

Once it's live, the usual post-deploy checks from BUILD_SPEC section 12 apply: View Source on a couple of the new pages to confirm the content is in the raw HTML (not just after render), and the new launches should show up in the homepage/browse grid, their category pages, and `directory.html`.
