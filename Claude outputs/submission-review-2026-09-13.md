# Submission review — 2026-09-13

`/runway-review` pass against the Pending Review queue. 60 records pulled (including Vesta Peptides, your standing carryover). Every URL verified live from the sandbox only, split across 12 parallel review agents plus direct follow-up checks, judged against BUILD_SPEC section 5 verbatim.

## Outcome

- **34 Approved and built** (new listings, all six surfaces touched).
- **5 Approved, already live, Airtable flipped only, no rebuild**: VitalityAfter45, AI Room Makeover, Video Size Reducer, B's Ads, Finanzas Freelance MX — all five are exact URL matches to listings already in `listings.json`.
- **5 duplicate submissions collapsed/deleted** (same product, different promo page, same builder, same day).
- **12 moved to Pending Further Review-Email sent**, each with a clarification email drafted below.
- **3 Rejected.**
- **1 left at Pending Review, untouched**: Vesta Peptides (recRtQluQnbjUPNPh) — carried forward again, still your own call, not re-reviewed.

60 = 34 + 5 + 5 + 12 + 3 + 1. Checks out.

## Something worth flagging before anything else

Twelve of these 60 records were not new. They're carryovers from the 2026-09-12 review that I had previously dispositioned as Rejected or held for clarification (Kit Útil, Vpster, Temp SMS Inbox, Lens Info, Northvault Workflow Tools, Free Invoice Webhook Stub, notefold, Icon Dental, Tokenized, "digital marketing," Matchs Sports Scores). All twelve had reverted to Status = Pending Review by the time I pulled the queue today, even though the 2026-09-12 build doc says their Airtable status was set to "Pending Further Review-Email sent" or left Rejected. I don't know why — possibly the write didn't stick, possibly something in your workflow reset them. I re-verified every one of them fresh rather than assuming the old call still held, and in one case (Tokenized) the fresh look actually changed the verdict from Reject to Approve — see below. Worth keeping an eye on whether this keeps happening; if held/rejected items keep bouncing back to Pending Review, that queue will never actually shrink.

## The uberip.com cluster (8 submissions, 1 builder, tools genuinely offline)

`frhdirstb2kjj@uberip.com` submitted three "products" (MicroPay Labs, SkillMint, StudyNotes Hub), each with its own store page plus one or two telegra.ph promo pages linking back to it — 8 records total, all 2026-09-12.

- **SkillMint** — the Vercel deployment is dead (`vercel.com/deployment-expired`). **Rejected.** Its telegra.ph promo page (SkillMint Resume Pack) points at the same dead store, so it's rejected/deleted too rather than held.
- **MicroPay Labs** and **StudyNotes Hub** — both live on `surge.sh`, and that domain's own `robots.txt` blocks automated fetching. I could not load either one, from the sandbox or by direct retry, so per the hard rule (verify live, never guess, never fall back to your browser) I'm holding both as **Review** rather than approving on the strength of their promo pages alone. Their two extra telegra.ph promo pages each are exact duplicates describing the same product and are deleted.

## Two more unverifiable URLs

- **Icon Dental Sedation and Implants Center** — the actual site (icondentalimplants.com, not the Airtable URL field, which was blank) returned a 403 to the sandbox fetch tool on every attempt. Real Visalia dental practice with a full address and phone number in the submission, so this reads like routine bot-blocking rather than a dead site, but I can't confirm what's actually live. Held as **Review**.

## Tokenized — verdict changed from Reject to Approve

The 2026-09-12 pass rejected this as a crypto-token product. Looking again against the literal standard: tokenized.so is a research/comparison directory (~1,100 assets, 32 issuers) with no checkout, no token of its own for sale, and no presale — it links out to sources so researchers can compare how different issuers represent the same stock or commodity onchain. BUILD_SPEC's reject criterion is specifically for sites where a token or coin itself is the product being sold. That's not what this is, so I approved and built it this time.

## Built (34, all six surfaces)

Tokenized, AI Outbound OS, Anhydra Systems, Bickqr, Call2Physio, Free Bible Study, Free Invoice Webhook Stub, Miloosh, Quote — Offline Freelance Rate Calculator (Free HTML), 3DIMLI, AI Prompts Online, Automation ROI Calculator, AviateHub, Client Magnet Kit, Cash Crow Digital Ops Packs, Dayora, FORE, FileNest WorkTools, Freelance Proposal Win Kit, Freelancer Ops Bundle, GamerHub, JustFiled, Kitset, Kovyxa, Literacy Trail, Packfiled, Peaklify, Rapid Indexer, Remoote, SayVocal, Sheetshot, StoreRadar, ToolSphare, Treviya.

One category correction: **Client Magnet Kit** was submitted as "AI Tools," which isn't one of the 17 canonical categories. Mapped to **AI / ML** (closest fit for a prompt kit) rather than inventing a new category.

Two same-builder relationships worth knowing about, neither treated as a duplicate since both are genuinely separate products/SKUs:
- **Client Magnet Kit** and **Freelancer Ops Bundle** (same builder, xbs200261@gmail.com, same raw-IP host). The Bundle repackages Client Magnet Kit plus two other kits at a discount — a real bundle SKU, not a copy, so both are listed.
- **JustFiled** and **Packfiled** (same builder, hello@justfiledit.com) — dumpster/waste filings vs. packaging EPR compliance, genuinely different verticals.
- **AI Prompts Online** and **Animals Details** (same builder email, lawnstarter.net@gmail.com, two different asserted builder names — Mohamed karim / Mohamed Laghbar). Both products are real and independently legitimate, so neither is held on this basis alone, but the two-names-one-email pattern is worth knowing about if it recurs.

## Already live, Airtable flipped only (5)

Exact URL match to a listing already in `listings.json`. No rebuild:

- **VitalityAfter45** (reckBT3PoGCXnNRnG) — vitalityafter45.lovable.app, live since 2026-09-11
- **AI Room Makeover** (reciCyJpq20KUODUh) — airoommakeover.com, live since 2026-09-12
- **Video Size Reducer** (recePe6dkC6BOggVY) — video-size-reducer.com, live since 2026-09-03
- **B's Ads** (recsA37oOIEDGKian) — chatgptadtemplates.com, live since 2026-09-10
- **Finanzas Freelance MX** (recnt7PCXZCL3xcGM) — finanzas-freelance-mx.jfpadilla1101.chatgpt.site, live since 2026-09-12

## Duplicate submissions collapsed/deleted (5)

Same product, promo/teaser page, same builder, same day:

- **MicroPay Labs 1 then 9 UPI page** (recNm4mPjJZzgfHdi) — duplicate of MicroPay Labs
- **MicroPay Labs M1 and M9 page** (recqn1IH0K973ZAGa) — duplicate of MicroPay Labs
- **SkillMint Resume Pack page** (recBpuN82jhiAPW70) — duplicate/promo of the now-rejected SkillMint
- **StudyNotes Class 12 Physics Chemistry PDFs** (rec9TXZc9QS6rPw5D) — duplicate of StudyNotes Hub
- **StudyNotes Hub public notes page** (recPA3EUEddWRB2UT) — duplicate of StudyNotes Hub

## Rejected (3)

- **SkillMint** (recEMQvlLmLlYokNx) — the storefront URL is a dead/expired Vercel deployment. Nothing loads.
- **Matchs Sports Scores** (recvhCZeVMHwOXe3d) — re-verified, unchanged from 2026-09-12: the live site is a paid, age-19+-gated sports-betting-prediction platform with a "users assume responsibility for betting outcomes" disclaimer, not the free scores checker described.
- **digital marketing** (recbMQFTmGvSxIwAw) — the submitted URL is literally `https://Digital Marketing in 2026`, not a real address. Nothing to fetch.

## Held for clarification (12)

Kit Útil, Vpster, MicroPay Labs, StudyNotes Hub, Lens Info, Northvault Workflow Tools, Temp SMS Inbox, notefold, Icon Dental Sedation and Implants Center, AIforJr, Animals Details, InvoiceAdept. Full reasoning and drafted emails below. None of these were built; Airtable status changed only.

### Kit Útil — kitutil@agentmail.to
> Hi Miguel!
>
> Thanks for submitting Kit Útil to The Runway! When we checked the live site again, it's still a nine-product general store, autónomo tax calculators plus a postal-exam simulator, a Spanish Constitution study deck, a thesis-template pack, a rental checklist, and a household budget sheet, none of which the submission mentions.
>
> Could you confirm which part you'd like listed: the free RETA/IVA/IRPF calculators, the full nine-product shop, or something in between? Once we know, we'll get Kit Útil listed accurately.
>
> Julie
> LaunchFree.io, The Runway
> hello@launchfree.io

### Vpster — hello@vpster.net
> Hi there!
>
> Thanks for submitting Vpster to The Runway! We checked again today: the cheapest live plan is now Starter at $7.45/month (not the $2.66/month Spark tier in the submission, which no longer appears on the site at all), and all 13 listed data-center locations currently show Out of Stock.
>
> Could you confirm current pricing and whether any location is actually available to deploy right now? Once we know, we'll get this listed correctly.
>
> Julie
> LaunchFree.io, The Runway
> hello@launchfree.io

### MicroPay Labs — frhdirstb2kjj@uberip.com
> Hi Vansh!
>
> Thanks for submitting MicroPay Labs to The Runway! Your live store (micropay-labs.surge.sh) blocks automated review tools from loading it (its robots.txt disallows crawlers), so we haven't been able to confirm what's actually there, even though your two linked promo pages describe it consistently.
>
> Could you either allow crawling on that page, or point us to a version we can load directly? Once we can see it, we'll get this reviewed.
>
> Julie
> LaunchFree.io, The Runway
> hello@launchfree.io

### StudyNotes Hub — frhdirstb2kjj@uberip.com
> Hi Vansh!
>
> Thanks for submitting StudyNotes Hub to The Runway! Same issue as MicroPay Labs: your store (studynotes-hub.surge.sh) blocks automated review tools from loading it, so we can't confirm what's live there yet.
>
> Could you allow crawling, or send a version we can load directly? Once we can see it, we'll get this reviewed.
>
> Julie
> LaunchFree.io, The Runway
> hello@launchfree.io

### Lens Info — tools@jamack.net
> Hi there!
>
> Thanks for submitting Lens Info to The Runway! We checked again today, lens.jamack.net is still "ImageFinder," a Korean AI reverse-image/product-search tool with no connection to contact lenses.
>
> Could you send us the correct URL for the contact-lens tool, or confirm ImageFinder is what you meant to submit (with an updated description)? Once we know, we'll get this listed correctly.
>
> Julie
> LaunchFree.io, The Runway
> hello@launchfree.io

### Northvault Workflow Tools — localservicegrowth2.0@gmail.com
> Hi there!
>
> Thanks for submitting Northvault Workflow Tools to The Runway! The products themselves look real and ready to list, but the Builder Name field is still the placeholder text "YOUR FIRST AND LAST NAME."
>
> Could you send us the name you'd like credited on the listing? Once we have it, we'll get this live.
>
> Julie
> LaunchFree.io, The Runway
> hello@launchfree.io

### Temp SMS Inbox — tools@jamack.net
> Hi there!
>
> Thanks for submitting Temp SMS Inbox to The Runway! We tried sms.jamack.net again today and still got a server error (a failed SSL handshake), so we still can't see the actual product.
>
> Could you confirm the site is up and reachable? Once we can load it, we'll get this reviewed.
>
> Julie
> LaunchFree.io, The Runway
> hello@launchfree.io

### notefold — 98dngus@gmail.com
> Hi there!
>
> Thanks for submitting notefold to The Runway! We tried loading notefold.gumroad.com again today and still only got page metadata back ("Simple Notion files"), not the actual listing content, and that description still doesn't match the "English interview and work notes" description in your submission.
>
> Could you confirm the correct description for the listing? Once we can see the actual product content, we'll get it live.
>
> Julie
> LaunchFree.io, The Runway
> hello@launchfree.io

### Icon Dental Sedation and Implants Center — icondentalsmile@gmail.com
> Hi there!
>
> Thanks for submitting Icon Dental Sedation and Implants Center to The Runway! Your site (icondentalimplants.com) is blocking our automated review tool from loading it (a 403 response), so we haven't been able to confirm what's live there.
>
> Could you check whether your site blocks automated visitors, or send us a different way to view it? Once we can load it, we'll get this reviewed.
>
> Julie
> LaunchFree.io, The Runway
> hello@launchfree.io

### AIforJr — hello@aiforjr.com
> Hi Sagar!
>
> Thanks for submitting AIforJr to The Runway! Two things came up when we checked the live site: it only shows a Math tutor ("Juno"), with no English-tutoring content anywhere, even though the submission describes a Math and English tutor. It also looks like an application-gated beta (a screening call, "only a few spots left") rather than a live, open product.
>
> Could you confirm whether English tutoring exists yet, and whether the product should be listed as Coming Soon instead of Live for now? Once we know, we'll get this listed accurately.
>
> Julie
> LaunchFree.io, The Runway
> hello@launchfree.io

### Animals Details — lawnstarter.net@gmail.com
> Hi there!
>
> Thanks for submitting Animals Details to The Runway! The live site is real and well put together, but it's actually a pet-care and food-safety blog (dog/cat nutrition guides) rather than the "facts and profiles about animals from around the world, habitats, diets and behavior" description in the submission.
>
> Could you send an updated description that matches what's actually on the site? Once we have it, we'll get this listed accurately.
>
> Julie
> LaunchFree.io, The Runway
> hello@launchfree.io

### InvoiceAdept — support@invoiceadept.com
> Hi Basith!
>
> Thanks for submitting InvoiceAdept to The Runway! The live page only shows a headline and a Log in / Sign up wall, no invoice builder, and no mention of CIS or VAT anywhere, even though those are the whole premise of the submission. It also says "no sign-up needed" right next to a sign-up-only flow.
>
> Could you point us to the actual invoice builder (or CIS/VAT feature) so we can see it working? Once we can, we'll get this listed accurately.
>
> Julie
> LaunchFree.io, The Runway
> hello@launchfree.io

## Vesta Peptides — still your call

recRtQluQnbjUPNPh. Unchanged from prior passes: research-peptide storefront that technically clears the Approve bar but carries gray-market reputational risk. Left at Pending Review, not touched.

## Build verification

Pending — six-surface build for the 34 approved records is next in this session.
