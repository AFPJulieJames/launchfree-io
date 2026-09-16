# LaunchFree.io Submission Review — 2026-09-16

## Summary

Pulled the full Pending Review queue: 136 records. 14 were carryover already held in the 09-15 PM pass (LUMYRA, Atopu, iChartCool AI, IntelAfri IMT, NoFilterGPT, WebThrone, PasteFast, Pikkai, Aria Icons, HN Top10, WebElan, UK Freelance Starter Pack, VOWBOOK, MEDICAB 3-Pack Organizer Boxes) — untouched here, still your call.

Of the remaining 122, 27 were duplicate resubmissions (same product, same builder, submitted minutes to hours apart) and have been deleted from Airtable, leaving 95 unique new submissions. All 95 were reviewed live from the sandbox (WebFetch only), 5 at a time across 20 parallel review passes, each judged against BUILD_SPEC section 5's exact standard.

**Result: 58 Approve, 25 Review, 12 Reject.**

Of the 58 Approves, 3 turned out to be duplicate submissions of products already live under an existing slug (collision-checked against `listings.json`) — those are flip-only, not rebuilt. **55 are genuinely new builds.**

## Two things worth your attention before anything else

**A single builder flooded the queue overnight.** Between 1:18am and 4:17am UTC today, one person (email typo'd between `deuscrusader@gmail.com` and `deuscruader@gmail.com`, going by "Hustle Ledger") submitted 35 records for 16 distinct gig-worker/freelancer Excel templates ($5–$29 each on Payhip/Gumroad), most submitted twice across two storefront mirrors. Every individual product that resolved live is a real, working, distinctly-named template — nothing here is fraudulent — so I approved the ones that check out. But 16 near-identical finance-tracker templates going live from one builder in a single overnight window is unusual volume, and I held 3 of them (Schedule C Log, Freelance Client CRM Lite, Mileage Log Pro) in Review specifically so you can decide whether you want all 16 live at once or want to space them out. The other 13 are in the Approve list below, flagged individually.

**A "Claude Resets" listing needs a trademark call.** The product itself is real and functional (tracks Anthropic's Claude usage-limit resets), but it uses "Claude" in both the product name and domain with no Anthropic affiliation, and was submitted 5 times under 3 different throwaway-looking email addresses for the exact same URL — itself a spam signal on top of the trademark question. Held in Review, not built.

Also rejected as a pair: **ASTROC2M Smart Contribution** and **ASTROC2M Mission Passport**, both crypto wallet-connect / token-reward schemes from the same builder — textbook crypto-scheme reject, and structured close enough to a wallet-drainer pattern that I'd treat any future ASTROC2M submission the same way.

## Duplicate submissions collapsed (later records deleted from Airtable)

27 duplicate records removed, covering: Digital Dignity Transformation Kit, ToolSphare, Swarm Hosts, Side Hustle Money Command Center 2026, 1099 Quarterly Tax Set-Aside Calculator 2026, Etsy & Small Shop Seller P&L 2026, Schedule C Expense & Receipt Log 2026, Freelance Client CRM Lite 2026 (x3 extra), Mileage Log Pro 2026 (x3 extra), Gig Tip Tracker 2026 (x3 extra), Uber Lyft Rideshare Weekly P&L 2026, Side Hustle Savings Goal Tracker 2026, Freelance Rate Profit Calculator 2026, Claude Resets (x4 extra), Agentes Inteligentes, Freelancer Invoice Late-Pay Tracker $9, DoorDash Uber Weekly P&L $11, Content Creator Income Tracker $12.

## Approve (58) — 55 new builds + 3 already-live (flip-only)

**Already live, flip-only (not rebuilt):** Digital Dignity Transformation Kit, ToolSphare, Rapid Indexer — all three collided with an existing slug in `listings.json` on the collision check. Same product, already shipped in an earlier pass; the new submission just gets its Airtable record flipped to Approved with the existing Listing URL.

**New builds (55):** SimpleSaaS Analytics, ProQR, KKIKA.ai, Petro, Top Proxy, RestReserve, LoreJam, Timothy Kane Dev Micro Kits, Best Launch Platforms, Steady Ground, Swarm Hosts, Side Hustle Money Command Center 2026 [deuscrusader], Client Ledger Mini, 1099 Quarterly Tax Set-Aside Calculator 2026 [deuscrusader], DoorDash Uber Weekly P&L $11 [deuscrusader], Freelancer Invoice Late-Pay Tracker $9 [deuscrusader], Content Creator Income Tracker $12 [deuscrusader], Cupid, Etsy & Small Shop Seller P&L 2026 [deuscrusader], My Celebrity Parents, Gig Tip Tracker 2026 [deuscrusader], Konversa, Uber Lyft Rideshare Weekly P&L 2026 [deuscrusader], Side Hustle Savings Goal Tracker 2026 [deuscrusader], Freelance Rate Profit Calculator 2026 [deuscrusader], Baojiji Tools, MailVeri, Gig & Freelance AI Prompt Pack [deuscrusader], Hustle Ledger Starter Pack [deuscrusader], Skirr AI, Find Accountant UAE, Agentes Inteligentes, Budy, PinoyFreelance.PH, Deepli Clean™, Nest — Free Pregnancy & Baby Notion Tracker, Statsnet, HTML4SEO, FISCUS AI, AI SEO Rainmakers, High Signal, Paper Route, NamingCube, Story of Us, Derelict Properties Leads, Astrology Geeks, LetsBeta, Lahjty, SizeCompare, KwaFlux, Peon, CVwerk, BillFast, Panda Largo, Subscription & Tool Cost Audit 2026.

Two need a note on build:
- **Nest** — free product ($0), Notion + offline HTML tracker; build as normal, just don't apply a price tag.
- **Panda Largo** — leans commerce/buying-guide-heavy in its editorial mix; real multi-article site, clears the bar, but keep an eye on it if it ever starts reading as a bare affiliate page.

## Review (25) — held, not built

- **Vesta Peptides** — live catalog shows ~158 products, not the claimed ~2,700. Needs the real number confirmed.
- **Shopfolio** — main URL blocked by robots.txt in the sandbox; linked asset host shows placeholder text only.
- **SMB Owner Cash Control Pack** — submitted checkout URL 404s.
- **LaunchRepo** — site is real, but its own pricing page says "Checkout opens soon" despite Stage = Live.
- **Outreach OS, PostReady, PawPrint** — same builder (Jordan Lee), same day, all three blocked by robots.txt/proxy policy in the sandbox; couldn't verify any of the three live. Worth a manual check before deciding, and worth deciding as a batch given it's 3 near-identical listings from one builder in one window.
- **Meeting OS** — Gumroad page loads but is client-rendered; couldn't confirm the listed products are actually there.
- **Cash Pulse Pack** — surge.sh blocks WebFetch site-wide; unverifiable from the sandbox.
- **PropostaJá** — submitter's own Stage says Beta, not Live; also an unusual manual (non-automated) payment flow worth confirming.
- **Football Intelligence HQ** — submitted URL redirects to a different domain than the one in the builder's own email; needs a canonical-URL confirmation.
- **Role & Opportunity Kit** — couldn't verify live (robots.txt/proxy blocked); unusual burner-looking builder email.
- **Nevergrad, Harem Mate** — both ArcherLab sub-apps, both show only "Loading…" with no rendered content.
- **ArcherLab News** — same URL (news.archerlab.dev) as yesterday's "HN Top10" hold, just resubmitted under a new name. Root is a placeholder, `/hn/` still only shows a loading spinner. Treat as the same held item, still not verifiably live.
- **Schedule C Expense & Receipt Log 2026, Freelance Client CRM Lite 2026, Mileage Log Pro 2026** — all live and real, held specifically as part of the "Hustle Ledger" mass-submission cluster described above.
- **Claude Resets** — trademark + spam-signal issue described above.
- **Geom + Grain Seamless Pattern Pack, Homeowner Bill and Utility Tracker** — both bare, non-indexed Whop checkout pages with no verifiable product content, and both share the same builder email under two different builder names (sockpuppet pattern) — hold both for a builder-identity clarification.
- **Monibeen From Germany** — live and functional, but the domain/branding says "Munibeen" not "Monibeen," and Stage says Coming Soon while the site is demonstrably already live and taking bookings.
- **Paysavo Payments** — cites specific FINTRAC/Bank of Canada/FinCEN registration numbers that need independent verification before a money-transmission product goes live on the directory.
- **ViralRefer Ultra** — works as claimed, but the submission URL carries a directory-tracking parameter and the builder identity looks like a template account built for mass cross-directory submission.
- **30 Instagram Captions for UK Local Businesses (Swipe File)** — live and purchasable, but the live listing advertises 120 captions while the submission says 30.

## Reject (12)

- **Liquid Spread Desk, Local PDF Privacy Kit** (same builder, MaxwellAI) — bare Stripe Payment Links, no product page behind either.
- **AI Money Ops Pack, Freelance Close Kit** — bare PayPal.me links, no product page.
- **LeadGuard AI** — URL is a bare checkout form showing "tickets sold out," not a product page.
- **ShipPage** — domain doesn't resolve at all.
- **KeyBack** — crypto wallet-recovery service on a disposable subdomain with a success-fee structure matching the advance-fee crypto-recovery scam pattern.
- **50+ Excel useful shortcuts** — content-farm Blogspot page gated behind a countdown and CPM ad redirects; delivers 3 shortcuts against a claimed 50+.
- **Soccer Impostor: Party Game** — the submitted Google Play URL loads a completely different, unrelated app.
- **ASTROC2M Smart Contribution, ASTROC2M Mission Passport** — crypto token/NFT schemes, described above.
- **Purgebg** — submission claims no-account, 100%-browser processing; the live site gates every actual output behind a sign-in wall.

## Next step

Moving straight to the build: the collision check is done (3 flip-only, 55 clean), and I'm building all 55 from `docs/LISTING_TEMPLATE_SSR.html` now, regenerating the indexes, validating, and flipping Airtable — same pass, no need to ask again. The build summary will follow this doc.
