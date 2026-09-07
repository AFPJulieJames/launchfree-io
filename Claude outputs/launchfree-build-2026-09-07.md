# LaunchFree build summary, 2026-09-07

Reviewed 43 unique new submissions since the last pass (plus one that arrived mid-review), collapsed 9 duplicate/collision resubmissions, built 29 approved listings, held 13 for review, rejected 1. 24 carryover items already dispositioned in prior review docs were left untouched. Full disposition and reasoning in `claude/submission-review-2026-09-07.md`.

## What was built

29 new listing pages, all rendered from `docs/LISTING_TEMPLATE_SSR.html`, dated **2026-09-07**:

signslip, consultant-pharmacist-aichat, solicitor-digital, vibehacker, cash-tracker-template, hourlyratecalc, remind, stash, dance-party, matrix-desktop, ai-ebook-generator, nextfeed, after-hours-web-capture-kit, ayzo, start-this-task, novatik, deposit-back-apartment-move-out-kit, your-i-ching, cosmodex, privro-ai, stokvel-os, neutrixflow, jobfinder-ai, same-day-readme-setup-polish-pack-a, freyavideo, freelance-ai-launch-kit, base2026, appliance-repair-triage-eval-pack, face-swap-ai.

All six surfaces touched per listing: the page, `listings.json` (739 to 768 records), `sitemap.xml`, `llms.txt`, `directory.html`, and each item's category page, regenerated via `docs/regen_indexes.py --write`.

`python3 docs/validate_build.py` result: **0 errors, 3 warnings** - all three are pre-existing false positives from earlier batches (a product's own name legitimately contains an em dash: Awkward Client Emails, Proofstamp, Pitch — New Client Proposal Template). Nothing from today's batch triggered a warning.

## Duplicates collapsed and deleted (9 Airtable records)

- **Kade Studio ZZP rekentools 2026** - 3 exact duplicates of the same tiiny.site URL deleted, plus 1 alternate-host (here.now) resubmission deleted. One record kept in Pending Review, held (see review doc).
- **GetBrazilVisa** - 1 exact duplicate deleted, 1 record kept, held.
- **Your I Ching** - 2 exact duplicates deleted, 1 record kept and built.
- **PepLedger** - 1 duplicate (www vs. bare domain of the same site) deleted, 1 record kept, held.
- **Songtell** - 1 exact duplicate deleted, 1 record kept, held.
- **Lynqra** - already built and live (slug `lynqra`) from the 2026-09-06 afternoon batch; this resubmission was deleted rather than rebuilt.

## Airtable changes

- 29 records: `Status -> Approved`, `Listing URL` set to the live page.
- 9 records deleted: the duplicate/already-live resubmissions above.
- 13 held for review and 1 rejected (Airtable left untouched in Pending Review, your call) plus 24 already-dispositioned carryover items left untouched.

## Held for review (13) - see the review doc for full reasoning

PepLedger - Peptide Tracker, Kade Studio ZZP rekentools 2026, HVAC Intake Eval Pack, AI Agent Business Operator Kit (Grok Bot Edition) / GBO-001, Servicekosten Afrekening, First-Client Paperwork Pack, Deep Swap AI, Songtell, Dianwu.AI Flow, WSUP AI: Free AI Character Chat, GetBrazilVisa, FLASHLAB Pack Offre 24h, and Close the Books: 45-Minute Month-End for Freelancers (name/slug collision with an unrelated already-live listing from 2026-09-02).

## Rejected (1)

- **Avinash Singh - Portfolio** (avinashs.com) - personal developer portfolio/resume, not a product. Note: the same builder's second submission, Privro AI, was a genuinely distinct product and was approved and built.

## Ship steps (GitHub Desktop)

1. Open GitHub Desktop, review the diff. It should show exactly: 29 new files in `listings/`, plus `listings.json`, `sitemap.xml`, `llms.txt`, `directory.html`, `index.html`, and the category pages touched by today's batch (saas, health, service, ai-ml, fintech, productivity, developer-tools, entertainment, e-commerce, creator-tools, lifestyle). No stray files - scratch build files and backups were cleaned up before finishing.
2. Commit (in one go or split, your call) - e.g. "Add 29 new launches - 2026-09-07."
3. Fetch origin, pull if needed, then push.
4. Spot check a few of the new listing pages live after deploy, plus the homepage and a category page.
5. Confirm the Make "Runway - Approval Email" automation sends for all 29.

## Note on scratch files

Building today's batch as brand-new pages needed a one-off script and its input data, plus pre-build backups of `listings.json` and `sitemap.xml`. All of these were written temporarily into `docs/` and the repo root, then deleted after the build and validator passed, so they should not appear in your Changes list.
