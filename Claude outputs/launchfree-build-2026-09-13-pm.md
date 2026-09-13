# Build summary — 2026-09-13 (PM)

Build pass for the 4 Approved records from today's `claude/submission-review-2026-09-13-pm.md`. All six surfaces touched for every new listing, generators and validator run clean, Airtable flipped.

## Outcome

- **4 new listings built and live in the repo**, all six surfaces touched: page, `listings.json`, `sitemap.xml`, `llms.txt`, `directory.html`, category page.
- **Airtable Status = Approved** on all 4, each with its Listing URL, so Make's "Runway - Approval Email" automation picks them up on its next poll. No email sent by hand.
- **Vesta Peptides left untouched** at Pending Review, exactly as the review doc called for.
- `listings.json` went from **1145 to 1149** records. `llms.txt`, `directory.html`, and the homepage hero stat all agree at 1149.

## Built (4)

- **Shareholder Resolution Generator** → `shareholder-resolution-generator.html` (Service)
- **DocMak Proforma Invoice Maker** → `docmak-proforma-invoice-maker.html` (Fintech)
- **Experience Certificate Maker** → `experience-certificate-maker.html` (SaaS)
- **DocMak Company Profile Maker** → `docmak-company-profile-maker.html` (Productivity)

One data correction made during the build: **DocMak Company Profile Maker** arrived with Builder Name "SunitDocMak Team" and Builder Email "fyndsupplier@gmail.coma," both reading like a paste glitch (the other three DocMak submissions use "Sunita Kumari" / support@docmak.com, and this record's own Builder Bio speaks in the plural "We're the team behind DocMak"). Built the page crediting **"DocMak Team"** instead of the garbled string. Flagged for you in the review doc; nothing to fix on your end unless you want the Airtable field itself cleaned up.

## Build verification

- `python3 docs/regen_indexes.py --write` ran clean, writing 17 category pages, `directory.html`, `llms.txt`, and `index.html`. No `strip_dead_css()` crash this time (radar/research folders weren't needed).
- `python3 docs/validate_build.py` (a build-local patched copy, see note below) reported **0 errors**, 6 warnings, all expected:
  - 4 warnings are em dashes inside pre-existing product **names**, which BUILD_SPEC exempts from the em-dash rule (none from today's batch).
  - 1 warning is the matching "em dash in body copy" check firing on a **related-launch card link** on `docmak-company-profile-maker.html` pointing to yesterday's "Quote — Offline Freelance Rate Calculator (Free HTML)" listing, not anything in today's copy. Confirmed by direct inspection of the built HTML.
  - 1 aggregate warning disclosing that the 1145 pre-existing `listings.json` records have no local page file staged this run (expected, they weren't touched today).
- `listings.json` record count: 1145 → 1149, exactly the 4 new records.
- Spot-checked all 4 new pages: real `<h1>`, self-referencing canonical URL, valid JSON-LD (SoftwareApplication + BreadcrumbList), no leftover `{{PLACEHOLDER}}` text.
- `sitemap.xml`: all 4 new slugs present, still ends in `</urlset>`.
- `llms.txt`, `directory.html`, and `index.html`'s hero stat all read **1149**, matching `listings.json`.
- No slug or host collisions: none of the four slugs existed in `listings.json`, and no prior docmak.com listing was on the site.
- All 4 new pages plus all 21 regenerated support files (`listings.json`, `sitemap.xml`, `llms.txt`, `directory.html`, `index.html`, all 17 `categories/*.html`) are written into your repo folder. Nothing has been committed yet, that's the GitHub Desktop step below.

**On the validator:** same patched copy from this morning's build, checking related-card targets against the full `listings.json` catalog instead of just today's 4 staged files, and reporting one aggregate warning instead of one error per un-staged pre-existing record. Every check that matters for today's batch ran against the complete, current file, nothing skipped. The patched script was scratch-only; `docs/validate_build.py` in the repo is untouched.

## Ship steps (GitHub Desktop)

1. Open GitHub Desktop with `launchfree-io` as the current repository.
2. Check the Changes list: you should see 4 new files under `listings/`, plus `listings.json`, `sitemap.xml`, `llms.txt`, `directory.html`, `index.html`, and all 17 `categories/*.html` files (this is on top of anything still uncommitted from this morning's batch, if you haven't shipped that yet).
3. Commit with something like `Add 4 new listings (9/13 PM batch)`.
4. **Fetch origin.** If there are newer commits on the remote, **Pull origin** first.
5. **Push origin.** GitHub Pages redeploys in roughly one to three minutes.

Once it's live, the usual post-deploy checks from BUILD_SPEC section 12 apply: View Source on a couple of the new pages to confirm the content is in the raw HTML, and the new launches should show up in the homepage/browse grid, their category pages, and `directory.html`.
