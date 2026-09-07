# LaunchFree submission review, 2026-09-07

Pulled the current `Status = Pending Review` queue: 76 records. 24 are carryover already dispositioned (untouched, tracked in prior review docs). The remaining 52 were new since the last pass: 43 unique products plus 9 duplicate resubmissions, which collapsed down to the 43 via the collision/duplicate rule. All 43 were checked live from the sandbox (WebFetch only, parallelized across six review agents plus one direct check, following BUILD_SPEC section 5 exactly).

## Duplicates collapsed to the earliest record (9 records deleted)

- **Kade Studio ZZP rekentools 2026** - submitted 4 times across 2 throwaway hosts (3x tiiny.site, 1x here.now). Collapsed to the single earliest record; the 3 later duplicates deleted.
- **GetBrazilVisa** - submitted twice, same URL. Collapsed to the earliest; 1 duplicate deleted.
- **Your I Ching** - submitted 3 times, same URL. Collapsed to the earliest; 2 duplicates deleted.
- **PepLedger** - submitted twice (bare domain, then www subdomain of the same site). Collapsed to the earliest; 1 duplicate deleted.
- **Songtell** - submitted twice, same URL. Collapsed to the earliest; 1 duplicate deleted.
- **Lynqra** - already built and live (slug `lynqra`) from the 2026-09-06 afternoon batch. This was a resubmission of the same product; deleted rather than rebuilt.

## Approved and built (29)

- **SignSlip** (signslip.jqgrowllc.com) - live $1.99 one-page-agreement tool with named e-signature and timestamped PDF; matches submission, explicit not-a-law-firm disclaimer.
- **Consultant Pharmacist AIChat** (jqgrowconsultlive.vercel.app) - live $9.99/mo educational medication Q&A with strong not-medical-advice disclaimers; matches submission.
- **Solicitor Digital** (solicitordigital.ie) - live digital marketing agency site for solicitors/law firms with real business details.
- **VibeHacker** (vibehacker.com) - live community/directory for AI builders with real listings, reviews, and human-reviewed submissions.
- **Cash Tracker Template** (Payhip) - live £8 cash-flow spreadsheet template for freelancers, instant download.
- **HourlyRateCalc** (hourlyratecalc.com) - live, working suite of pay/salary/overtime calculators, no signup.
- **Remind** (remind.ing) - live macOS app with real App Store listing, AI meeting briefings, $19.99/yr with trial.
- **Stash** (yourstash.ai) - live public-beta Mac screenshot/recording tool built for AI coding agents.
- **Dance Party** (danceparty.ai) - live dashboard-on-Apple-TV product with a real App Store listing and 70+ data integrations.
- **Matrix Desktop** (matrix.watch) - live Mac Matrix-rain wallpaper/screensaver app, Apple Silicon, free.
- **AI Ebook Generator** (aiebookgenerator.ai) - live idea-to-book AI workflow with working app, export formats confirmed.
- **NextFeed** (nx-feed.com) - live ecommerce product-feed management SaaS with a 14-day trial; matches submission (page names ~10 explicit channels, not literally "100+", minor tagline puffery only).
- **After-Hours Web Capture Kit** (Gumroad) - live $49 lead-capture file kit for local-service sites, explicitly not a phone bot.
- **AYZO** (ayzo.io) - live evidence-first on-chain analysis tool; discloses a future token with no mint/trading pair yet, which is disclosure of a roadmap item rather than active promotion of an investment scheme.
- **Start This Task** (startthistask.com) - live AI task-breakdown tool with Focus Mode, matches submission exactly.
- **NovaTik** (novatik.app) - live browser-based TikTok downloader, ordinary personal-use utility, no abuse angle found.
- **Deposit Back: Apartment Move-Out Kit** (Gumroad) - live $14 printable renter move-out kit with "not legal advice" disclaimer.
- **Your I Ching** (youriching.com) - live free I Ching oracle, hand-cast lines plus AI interpretation, no account required.
- **CosmoDex** (cosmodex.in) - live public beta gamified coding-battle platform with a working course and real-time 1v1 arena.
- **NeutrixFlow** (neutrixflow.com) - live AI tools discovery/comparison site with real listings and reviews.
- **jobfinder-ai** (jobfinder-ai.com) - live job-outreach agent that explicitly sends from the user's own inbox with capped follow-ups, not impersonation.
- **Same-day README / setup polish (Pack A)** (Gumroad) - live $40 same-day documentation service, matches submission.
- **FreyaVideo** (freyavideo.com) - live AI flyer-to-video tool, credits-based pricing confirmed.
- **Freelance AI Launch Kit** (Netlify) - live $9-$47 prompt/template/sprint bundle for freelancers.
- **Base2026** (base2026.dev) - live source-backed video research engine with working search and citation links.
- **Appliance Repair Triage Eval Pack** (Gumroad) - live $79 eval dataset/harness for appliance-repair triage agents, matches submission.
- **Stokvel OS** (Gumroad) - live R199 treasurer pack for South African savings clubs, with clear not-a-bank/not-insurance disclaimers.
- **Face Swap AI** (faceswapai.com) - live AI face-swap tool with real consent safeguards for uploaded media.
- **Privro AI** (privro.com) - live free local-transcription/caption/AI-voice browser suite, genuinely distinct product from its builder's other submission below.

All six surfaces will be touched per listing: the page, `listings.json`, `sitemap.xml`, `llms.txt`, `directory.html`, and each item's category page, regenerated via `docs/regen_indexes.py --write`.

## Held for review (13) - Airtable left in Pending Review, your call

- **PepLedger - Peptide Tracker** (pepledgerapp.com) - sandbox fetch only returned page metadata (title/description/App Store id), not the rendered product page; a direct curl was blocked by sandbox egress policy. Metadata matches the submission, but the live content itself is unverified - worth a manual check given it's a health-adjacent dosing tracker.
- **Kade Studio ZZP rekentools 2026** - the surviving record (after collapsing 3 duplicates) is a real Dutch freelancer rate/VAT calculator, but it's hosted on tiiny.site, a throwaway static-site host with no permanent domain. Needs a real domain before a never-renamed slug commits to it.
- **HVAC Intake Eval Pack** (Gumroad) - real, live $79 product, but the live page describes 200 total cases while the submission's tagline claims "50 labeled HVAC intake cases." Needs a one-line clarification on the actual count before this goes live as advertised.
- **AI Agent Business Operator Kit (Grok Bot Edition) / GBO-001** - real $67 digital ops kit with honest no-income-guarantee disclaimers, but hosted on here.now, the same throwaway prototype-builder pattern flagged before. Needs a permanent domain.
- **Servicekosten Afrekening** - matches the submission (Dutch service-charge settlement tool), but it's a waitlist-only page ("we bouwen alleen bij echte vraag" - nothing built yet) on a throwaway workers.dev subdomain. Not live as a usable product yet.
- **First-Client Paperwork Pack** (ko-fi) - the live page shows the item as **Free** and marked **Sold Out**, while the submission's tagline claims a **$12** price. Needs clarification before building at either price or availability.
- **Deep Swap AI** (deepswapai.com) - live and functional like its sibling Face Swap AI, but its consent/usage-rights language for uploaded faces reads weaker and less enforced on the live page. Holding for a closer look rather than approving alongside Face Swap AI.
- **Songtell** (songtell.art) - live and legitimate AI custom-song product on its own merits, but its live page footer cross-promotes onecustomsong.art (already built and live on The Runway) and both list the same builder, Xinpeng Yu. Flagging the apparent same-operator relationship between two directory listings rather than deciding unilaterally whether that matters to you.
- **Dianwu.AI Flow** - the submission has no URL field filled in at all. The description mentions working URLs (dianwu.ai, flow.dianwu.ai) but the required field itself is blank - a data-quality issue, not a live-page judgment call.
- **WSUP AI: Free AI Character Chat** (wsupai.app) - a free, no-signup AI character chat/roleplay product. The character roster and homepage hero didn't fully render via sandbox fetch (JS-heavy), so no age-gate could be confirmed one way or the other. This is the same sensitive category as the standing EIMI hold - flagging for the same reason rather than approving on incomplete evidence.
- **GetBrazilVisa** (getbrazilvisa.com) - real immigration-visa service with an OAB-licensed-lawyer claim, but the contact email name (hassanyassine@... in one duplicate, camilamota@... in the surviving record) doesn't consistently match the named builder, and the meta description carries an unsubstantiated "95% approval" figure. Worth a clarification given this is a paid legal/immigration service.
- **FLASHLAB Pack Offre 24h** (surge.sh) - completely unfetchable; the sandbox got an org-level policy denial on the surge.sh host on every attempt. Can't verify live content either way - hold until it's reachable or the builder provides a working link.
- **Close the Books: 45-Minute Month-End for Freelancers** (Gumroad, builder M Grinblat) - real, live $19 product matching its submission, but its exact product name and slug are already used by a different, unrelated listing built 2026-09-02 (different builder, different URL, phenomenal-gingersnap-32daa7.netlify.app). Slugs are never renamed once built, so this needs your call on whether it's a coincidence, a rebrand, or a copycat name before it gets a disambiguated slug.

## Rejected (1) - Airtable left in Pending Review, your call

- **Avinash Singh - Portfolio** (avinashs.com) - live, well-built site, but it's fundamentally a personal developer portfolio/resume (Work / Writing / About / Contact, blog posts) with two small incidental utilities tucked under a Tools tab. The submission itself frames it as "a portfolio," matching BUILD_SPEC's "not a product: personal blog" reject criterion. Note: the same builder's second submission, **Privro AI**, is a genuinely distinct standalone product and was approved above.

## Collision check (BUILD_SPEC section 4)

All 30 initially-approved slugs and hosts checked against the pre-batch listings.json (739 records). One collision found and moved to Held above (Close the Books slug/name collision). Shared checkout/hosting platforms (Payhip, Gumroad, Netlify) hosting other unrelated products are not collisions. No other slug or host collisions among the 29 that remain approved.

## Next: see `claude/launchfree-build-2026-09-07.md` for what got shipped.
