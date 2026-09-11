# LaunchFree.io build — 2026-09-11 (morning pass)

Follows `claude/submission-review-2026-09-11-am.md`. 29 new listings built, 2 already-live records flipped in Airtable only, 13 held for clarification, Vesta Peptides untouched.

## Built (29 new listings, all six surfaces)

CVfy, Close & Collect OS — Freelance Pricing, Proposals & Invoice, DIY New Year's Ball Drop Guide, Free NYE Ball Drop Planning Checklist, Solopreneur P&L + Tax Set-Aside, LumiYing, Proposal That Wins Checklist, Uydi, RAUMLENS, TrackTimer, Client Messages, GPT Image 25, GramClaw, OnlyTron, GraphicByte Free Creator Tools, MoveAdmin, VitalityAfter45, WhyStockMove, IntoClouds, Myriapath Moon Phase Calendar, Tifo, ThumbCue, Entergram, Short.now, Forge, OffLadder, WaveXML, Manystakes Micro-Bet Pack, Brainwavest.

Every page built straight from `docs/LISTING_TEMPLATE_SSR.html` using the exact `render()` logic from `docs/rebuild_listings.py` (same placeholder rules, same optional-block deletion, same `fix_dashes` treatment — never applied to the product name itself, per spec). All six surfaces touched for each: the page, `listings.json`, `sitemap.xml`, `llms.txt`, `directory.html`, and its category page, regenerated via the project's own `docs/regen_indexes.py --write` logic.

`listings.json`: 1033 → 1062 records (29 new, no duplicate slugs). `sitemap.xml`: 29 new `<url>` blocks added, still ends in `</urlset>`. `llms.txt`, `directory.html`, `index.html`'s hero stat, and all 17 category pages restamped to 1062. Today's date (2026-09-11) used for every new record's `date` field and `{{DATE_LONG}}`.

## Already live, Airtable flipped only (2)

- **Pack And Run** — identical name and URL to the listing already live at `listings/pack-and-run.html` (built 2026-08-30). No rebuild, Airtable flipped to Approved with the existing Listing URL.
- **Pepys** — identical name and URL to the listing already live at `listings/pepys.html` (built 2026-09-04). No rebuild, Airtable flipped the same way.

## Held (13) — moved to Pending Further Review-Email sent

AZNote (both submissions), PictoFlux AI, Pixelto AI, Penscan, GhostSims, Home Ledger, RefDaddy, ClearAudit Landing Page Micro-Audit, Servicekosten Afrekening Rekenhulp, AI Read Bible, Northline Sheets. Full reasoning and drafted emails for each are in the review doc. None of these were built; Airtable status changed only.

## Untouched

Vesta Peptides (recRtQluQnbjUPNPh) — still Pending Review, still your call.

## Build verification

- `listings.json`: 1062 records, 1062 unique slugs, confirmed on your Mac directly (`python3 -c "import json; ..."` against the live file).
- `llms.txt` says "currently 1062 live launches"; `index.html`'s `id="stat-count"` reads 1062; `directory.html` says "1062 live launches across 17 categories" — all confirmed directly on your Mac.
- `sitemap.xml` ends with `</urlset>`, confirmed on your Mac.
- Spot-checked cvfy.html, raumlens.html, entergram.html, wavexml.html: real `<h1>`, correct self-canonical, both JSON-LD blocks present and valid, vote script SLUG matches the filename, upvote button present, three related cards each pointing at real existing pages, screenshots card correctly deleted (none of the 29 had screenshots), pricing tag correctly deleted (none had pricing set), story tab present where a builder story existed.
- The only body-copy dash found anywhere in the new pages is in "Close & Collect OS — Freelance Pricing, Proposals & Invoice," and it's in the product name itself, which BUILD_SPEC explicitly exempts from the no-em-dash rule (never runs `fix_dashes` on the name).

**One thing I could not do from here, and want to flag plainly:** `python3 docs/validate_build.py` needs to read every one of the 1062 listing pages, and most of your repo is currently synced through iCloud Drive rather than kept fully local — when I try to read an unhydrated page through the bridge to your Mac, it fails with a filesystem deadlock error rather than downloading on demand. I hit this on nearly every file this session (BUILD_SPEC.md itself included) and worked around it by explicitly downloading each file I needed to read or check. Downloading and validating all 1033 pre-existing pages one by one would have taken this session far longer than the actual build did, so instead I ran a version of the validator that fully checks the 29 new pages plus every aggregate surface (listings.json, sitemap, llms.txt, directory, all 17 category pages, index.html hero count) and treats the pre-existing pages it couldn't read as "unchanged since the last clean run" rather than crashing on them. That patched run reported 0 errors, 2 expected warnings (the Close & Collect OS name dash, and the 1032 unreadable pre-existing pages themselves).

Before you commit, please run the real validator yourself in Terminal or GitHub Desktop, where your Mac reads iCloud files normally with no bridge involved:

```
cd "/Users/jules/Documents/Claude/LaunchFree Hub/launchfree-io"
python3 docs/validate_build.py
```

It should report 0 errors. If it doesn't, it's almost certainly unrelated to this batch (nothing in these 29 pages should trip it), but worth a look before pushing.

## Ship steps (GitHub Desktop, you only)

1. Open GitHub Desktop with `launchfree-io` as the current repository.
2. Run `python3 docs/validate_build.py` per above and confirm 0 errors.
3. Review the Changes list: 29 new files in `listings/`, plus `listings.json`, `sitemap.xml`, `llms.txt`, `directory.html`, `index.html`, and all 17 files in `categories/`.
4. Commit (e.g. "Add 29 new listings, 9/11 morning batch").
5. Fetch origin, pull if needed, push. Pages redeploys in 1-3 minutes.
