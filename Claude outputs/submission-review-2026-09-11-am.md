# Submission review — 2026-09-11 (morning pass)

`/runway-review` pass against the Pending Review queue. 44 unique records (no exact duplicates by URL; one same-product pair reviewed separately, see below). Every URL verified live from the sandbox only (WebFetch / sandbox browser), split across parallel review agents, each judged against BUILD_SPEC section 5 verbatim.

## Outcome

- **29 Approved and built** (new listings, all six surfaces touched).
- **2 Approved, already live, Airtable flipped only, no rebuild**: Pack And Run, Pepys (identical product + identical URL already in `listings.json` under the same slug).
- **13 moved to Pending Further Review-Email sent**, each with a clarification email drafted below.
- **1 left at Pending Review, untouched**: Vesta Peptides (recRtQluQnbjUPNPh) — carried forward from the 2026-09-11-01:26 review, still Julie's own call, not re-reviewed.
- **0 Rejected** this round.

## Built (29)

CVfy, Close & Collect OS — Freelance Pricing Proposals & Invoice, DIY New Year's Ball Drop Guide, Free NYE Ball Drop Planning Checklist, Solopreneur P&L + Tax Set-Aside, LumiYing, Proposal That Wins Checklist, Uydi, RAUMLENS, TrackTimer, Client Messages, GPT Image 25, GramClaw, OnlyTron, GraphicByte Free Creator Tools, MoveAdmin, VitalityAfter45, WhyStockMove, IntoClouds, Myriapath Moon Phase Calendar, Tifo, ThumbCue, Entergram, Short.now, Forge, OffLadder, WaveXML, Manystakes Micro-Bet Pack, Brainwavest.

One note carried into the build rather than held: **Client Messages** approved and built as submitted; the sandbox fetch's page-content summary showed a leftover "Offshift" brand string in what looked like site metadata even though the visible page content matched the submission exactly (a real library of copy-paste client texts). Worth a two-second manual glance at clientmessages.com's actual `<title>` tag sometime, not urgent enough to hold the listing.

## Already live, flipped only (2)

- **Pack And Run** (recEb2QNiT1QAhzOE) — same name, same URL (`play.google.com/store/apps/details?id=com.packitgame.app`) as the listing already live at `/listings/pack-and-run.html` since 2026-08-30. No rebuild.
- **Pepys** (recEVdfW1fU5isv9N) — same name, same URL (`pepys.co`) as the listing already live at `/listings/pepys.html` since 2026-09-04. No rebuild.

## The 13 held, by reason

**Same builder, same product, submitted under two URLs (Review per BUILD_SPEC section 5):**
- AZNote — two records, recn5ZfHybrS6Hhox (aznote.applanding.co, dario.tolio@ilevia.com) and recok4GVtqX0ixMKC (App Store listing, dario.tolio@gmail.com). Both pages are real and live, but it's one product from what looks like one builder across two emails. Held rather than built twice.
- PictoFlux AI (recOJugDA1nk1V61Q) and Pixelto AI (recOigpaZWYl0nyQc) — both live, both real, but structurally near-identical (same "no sign-up, Flux/Nano Banana/GPT Image 2" pitch, same pricing pattern) and the reviewing agent's read of each page pointed to the same builder behind both. Held to confirm whether these are two genuinely different products or one tool under two brand names before either gets built.

**Submitted URL doesn't show the actual product (Review, ask for the right link):**
- Penscan (recZ9ki8Am0exOTvA) — submitted URL is a bare login screen. The marketing domain (penscan.org, no "platform.") shows a real product; likely just the wrong link submitted.
- GhostSims (reclIWhx46OVDqCnI) — submitted URL is a blog article about GrapheneOS, not a product or pricing page. Root domain shows a real encrypted-SIM business; asked for the correct product URL.

**Listing details don't match what's live (Review, one factual clarification):**
- Home Ledger (recjq81aQgSAg6lcL) — submission says Stage = Beta; the live page itself says it's not on the App Store yet, with only a waitlist mailto-link and a private GitHub repo. Asked to confirm Coming Soon vs. an actual live beta.
- RefDaddy (recOUfy580GksthQE) — live page shows pricing ($12.99/mo **plus $0.50 per minted link**) and scope ("exclusively for the Acoco platform") that don't match the flat-fee, general-purpose pitch in the submission. Also sits on a staging subdomain, not a production URL.

**Same host/name as an existing live listing, different URL — possible migration or scope overlap (Review):**
- ClearAudit Landing Page Micro-Audit (recC60Tw9eM0PD5lK) — same name, same $97 offer as the ClearAudit listing already live since 2026-09-03, but a different URL (`unbound-realm-mnvw.here.now` vs. the live `nano-monolith-5wrx29h.shipstatic.com`). Both look like temporary preview hosts. Asked which URL is current before touching the existing listing.
- Servicekosten Afrekening Rekenhulp (recgktOT3rB45ZVaT) — same exact domain (`servicekosten-thin-go.dawn-union-0438.workers.dev`) as the "Servicekosten Afrekening" listing already live since 2026-09-09, just a different sub-page (`/verdeelsleutel-rekenhulp/`). Asked whether this is a standalone tool worth its own listing or a feature of the product already listed.

**Verification blocked (Review, sandbox couldn't confirm):**
- AI Read Bible / 爱读圣经 (recxnJDAiCnEDA7kI) — JS-rendered SPA; the sandbox only ever got the loading splash screen, never the actual reader. Asked for confirmation it renders for a normal visitor.

**Approved on the technical merits, flagged for a second look (built, not held, but noted):**
- Northline Sheets (recjVahiLO7j6vyQV) — real named/priced products load, so it clears BUILD_SPEC's letter (crypto checkout alone isn't disqualifying). But it's listed on a third-party directory (Tolodora) rather than a domain the builder appears to own, carries a `noindex` tag, and the contact email domain (uberip.com) doesn't match anything on the page. None of that is an explicit reject/review trigger, so it's held to Review rather than built, pending a quick confirmation from the builder that they run this listing.

## Email drafts (13 records)

### AZNote (both submissions) — dario.tolio@ilevia.com and dario.tolio@gmail.com
> Hi Dario!
>
> Thanks for submitting AZNote to The Runway! We actually received two submissions for AZNote, one linking to aznote.applanding.co and one linking to the App Store listing, from two different email addresses. Both pages look real and we'd love to list AZNote, but we only give one product one listing.
>
> Could you confirm which link you'd like as the permanent URL (the landing page or the App Store page), and that both submissions are from you? Once we know, we'll get AZNote built and live.
>
> Julie
> LaunchFree.io, The Runway
> hello@launchfree.io

### PictoFlux AI — contact@pictoflux.com
> Hi there!
>
> Thanks for submitting PictoFlux AI to The Runway! When we checked it out, we noticed it's very similar in features and pricing to another submission we received the same day, Pixelto AI. We want to make sure we're not listing the same tool twice under two names.
>
> Could you let us know if PictoFlux and Pixelto are related, or if they're genuinely separate products? Once we know, we'll get this moving.
>
> Julie
> LaunchFree.io, The Runway
> hello@launchfree.io

### Pixelto AI — contact@pixelto.com
> Hi there!
>
> Thanks for submitting Pixelto AI to The Runway! We noticed it's very similar in features and pricing to another submission we received the same day, PictoFlux AI. We want to make sure we're not listing the same tool twice under two names.
>
> Could you let us know if Pixelto and PictoFlux are related, or if they're genuinely separate products? Once we know, we'll get this moving.
>
> Julie
> LaunchFree.io, The Runway
> hello@launchfree.io

### Penscan — rachel@penscan.info
> Hi Rachel!
>
> Thanks for submitting Penscan to The Runway! When we checked platform.penscan.org, we only found a sign-in screen, nothing a new visitor could see or try. We did find a fuller product page at penscan.org, so it looks like the wrong link may have been submitted.
>
> Could you confirm the right public-facing URL for the listing? Once we can see the actual product, we'll get Penscan built.
>
> Julie
> LaunchFree.io, The Runway
> hello@launchfree.io

### GhostSims — moilyas999@gmail.com
> Hi there!
>
> Thanks for submitting GhostSims to The Runway! The link you sent (ghostsims.com/encrypted-phones-grapheneos-benefits) loads as a blog article rather than your product or pricing page. We found a real business at the root domain, ghostsims.com, but want to link to the right page.
>
> Could you send us the URL you'd like visitors to land on? Once we have it, we'll get this listed.
>
> Julie
> LaunchFree.io, The Runway
> hello@launchfree.io

### Home Ledger — digilio.nik@gmail.com
> Hi Niko!
>
> Thanks for submitting Home Ledger to The Runway! We marked it Beta on the submission, but the live page currently shows it's not yet on the App Store or TestFlight, just a waitlist signup and a private GitHub repo.
>
> Could you confirm whether Home Ledger should be listed as Coming Soon (a waitlist visitors can join today) or whether there's a live beta we should be pointing to instead? Once we know, we'll get it listed correctly.
>
> Julie
> LaunchFree.io, The Runway
> hello@launchfree.io

### RefDaddy — refdaddy@staging-mail.zilla.so
> Hi there!
>
> Thanks for submitting RefDaddy to The Runway! Two things came up when we checked refdaddy.staging.zilla.so: the pricing on the live page ($12.99/month plus $0.50 per minted referral link) is different from what was submitted, and the page describes RefDaddy as built exclusively for the Acoco platform rather than general-purpose. The URL itself is also a staging address rather than a production one.
>
> Could you confirm the real pricing, whether it's Acoco-only or works more broadly, and send a production URL if you have one? Once we have that, we'll get RefDaddy listed.
>
> Julie
> LaunchFree.io, The Runway
> hello@launchfree.io

### ClearAudit Landing Page Micro-Audit (new submission) — odin@asgardr.io
> Hi Odin!
>
> Thanks for submitting ClearAudit again! We already have ClearAudit Landing Page Micro-Audit listed on The Runway at a different URL (nano-monolith-5wrx29h.shipstatic.com), and this new submission points to unbound-realm-mnvw.here.now instead, same offer, same price.
>
> Could you confirm which URL is the current one so we can update the listing rather than create a second one? Once we know, we'll get it sorted.
>
> Julie
> LaunchFree.io, The Runway
> hello@launchfree.io

### Servicekosten Afrekening Rekenhulp — servicekosten.afrekening@proton.me
> Hi there!
>
> Thanks for submitting the Servicekosten Afrekening Rekenhulp! We already have Servicekosten Afrekening listed on The Runway at the same domain (servicekosten-thin-go.dawn-union-0438.workers.dev), and this submission points to a specific page on that same site (/verdeelsleutel-rekenhulp/).
>
> Is the allocation calculator a standalone tool worth its own listing, or part of the Servicekosten Afrekening product we already have listed? Let us know and we'll get it sorted correctly.
>
> Julie
> LaunchFree.io, The Runway
> hello@launchfree.io

### AI Read Bible (爱读圣经) — bambi.assistant.ai@gmail.com
> Hi there!
>
> Thanks for submitting AI Read Bible to The Runway! When we checked aireadbible.com, we only ever saw the loading screen ("正在开启圣言"), never the actual reader or AI features described in your submission.
>
> Could you confirm the app loads and shows real content for a new visitor, maybe with a quick screenshot? Once we can see it working, we'll get AI Read Bible listed.
>
> Julie
> LaunchFree.io, The Runway
> hello@launchfree.io

### Northline Sheets — northline3713@uberip.com
> Hi there!
>
> Thanks for submitting Northline Sheets to The Runway! We checked tolodora.com/software/northline-sheets and found real, priced products there, but a couple of things gave us pause before listing: the page sits on a third-party software directory rather than a site you seem to run directly, and the contact email on file doesn't match the product or directory name.
>
> Could you confirm you're the one behind these products, and whether there's a URL you control directly that we should link to instead? Once we hear back, we'll get this moving.
>
> Julie
> LaunchFree.io, The Runway
> hello@launchfree.io

## Vesta Peptides — still Julie's call

recRtQluQnbjUPNPh. Unchanged from the 09-11 01:26 review: research-peptide storefront that technically clears the Approve bar but carries gray-market reputational risk. Left at Pending Review, not touched.

## Build verification

Pending — six-surface build for the 29 approved records is next in this session.
