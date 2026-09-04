# LaunchFree.io: Operations Manual

**Version 1.0. Written 2026-08-16 from the live repo and the live site.**

This is the "someone else has to run this" document. If Julie is unavailable for a week, a month,
or permanently, everything needed to keep The Runway alive is in this file or is pointed at from it.

Read this first. Then read `docs/BUILD_SPEC.md`, which is the step by step for publishing new
launches. Those two files together are the whole operation.

House style: no em dashes in body copy, anywhere, ever.

---

## 1. What this is

**LaunchFree.io**, brand name **The Runway**, is a free product launch directory. Founders, indie
builders and side hustlers submit a product and get a permanent listing page, a free dofollow
backlink, a "Listed on The Runway" badge, and a spot in the weekly newsletter. Every submission is
reviewed by a person, usually within about 24 hours.

**The promise, which is the entire brand: free to list, forever.** No listing fee, no approval fee,
no paywall, no skip-the-queue upsell. The idea came from hitting paywalls on TAAFT, Futurepedia,
Toolify, MicroLaunch and a 90 week free queue on OpenHunts. The frustration is the product. If a
future decision would put the core listing behind money, that decision kills the reason this exists.

Tagline: "Every launch needs a runway. Yours is free."

| | |
|---|---|
| Live site | https://launchfree.io |
| Contact | hello@launchfree.io |
| Owner | Julie James |
| Legal entity | Automated Income Tools LLC |
| X handle | @JulieBuilds |
| Newsletter | The Runway Radar, weekly on Fridays, on Beehiiv |
| Scale as of 2026-08-16 | 235 live launches across 17 categories |

**Money.** The core directory is free and stays free. Revenue is meant to come from sponsored
featured placements, newsletter advertising, and an optional paid verification badge. As of this
writing none of those are switched on. The `featured` flag exists in the data model and one record
uses it. There is no billing system, no Stripe, nothing to reconcile. Whoever picks this up is not
inheriting a payments problem.

---

## 2. The stack in one picture

```
Builder fills submit.html
        |
        v
  POST to the Make.com webhook  ->  Airtable "Submissions" table (Status: Pending Review)
        |
        v
  Human review: open every URL, decide Approve / Review / Reject
        |
        v
  Build pages in the local repo folder, following docs/BUILD_SPEC.md
        |
        v
  Commit + Fetch + Pull + Push in GitHub Desktop
        |
        v
  GitHub Pages redeploys (1 to 3 minutes) -> live at launchfree.io
```

Everything on the public side is static HTML, CSS and JavaScript. There is no server, no database
behind the site, no build step, no framework, no npm install. A `.html` file in the repo is a page
on the internet a couple of minutes after it is pushed. That is the whole deployment story, and it
is deliberately boring so that it keeps working.

Two live services sit alongside it:

- **Supabase** holds the upvote counts, read and written directly from the browser.
- **Beehiiv** holds the newsletter list and sends the weekly issue.

---

## 3. Repository map

Repo: `AFPJulieJames/launchfree-io`, hosted on GitHub Pages, custom domain via the `CNAME` file.
Local working copy: `/Users/jules/Documents/Claude/LaunchFree Hub/launchfree-io/`

| Path | What it does | Changes when |
|---|---|---|
| `index.html` | Homepage. Fetches `listings.json` on load, reads live vote counts from Supabase, has search and category filters and the newsletter signup | Only for design or copy changes. **Never for a new launch** |
| `browse.html` | The full filterable grid. Same live fetch, plus sorting | Same |
| `submit.html` | The 4 step submission form. POSTs JSON to the Make webhook | Only to change the form |
| `listings/<slug>.html` | One permanent page per launch, 235 of them | One new file per approved launch |
| `listings.json` | **The catalog.** The homepage and browse page read this live. A launch that is not in here does not appear on the site | Every build |
| `directory.html` | Every launch as plain crawlable links grouped by category. This is the page that guarantees crawlers can reach deep listings without JavaScript | Every build, regenerate from `listings.json` |
| `categories/*.html` | 17 static category landing pages, one per category | Every build. **This is the surface that keeps getting missed** |
| `sitemap.xml` | 282 URLs. Every listing, category, article and root page | Every build |
| `llms.txt` | A plain language site summary written for AI answer engines, with links and a live launch count | Every build |
| `robots.txt` | Explicitly welcomes GPTBot, ClaudeBot, PerplexityBot, CCBot, Google-Extended, Bingbot and the social unfurl bots | Rarely |
| `radar.html` + `radar/*.html` | The Runway Radar content hub, 17 SEO articles about launching for free. Hand-authored, no template, see section 9 rule 8 for the required favicon block | When new articles are written |
| `research/*.html` | Original research, currently "State of Indie Launches 2026" | Rarely |
| `faq.html`, `privacy.html`, `terms.html`, `disclaimer.html` | Static legal and info pages | Rarely |
| `add-badge.html`, `badge-dark.svg`, `badge-light.svg` | The "Listed on The Runway" badge builders embed on their own sites. This is what generates the reciprocal links | Rarely |
| `free-product-launch-directory.html`, `indie-maker-directory.html`, `launch-saas-free.html`, `bootstrap-founder-tools.html`, `submit-startup-free.html`, `product-hunt-alternative.html` | Keyword landing pages | Rarely |
| `404.html`, `og-image.png`, `CNAME` | Error page, default social image, custom domain | Rarely |
| `ai-undetectable-logo.png`, `direction-reset-review-logo.png`, `late-payment-recovery-pack-logo.png` | Builder logos hosted here instead of on the builder's own domain. Referenced from `listings.json` and their listing pages | Occasionally, when a builder has no stable logo URL |
| `LaunchFree_Project_Instructions.md` (root) | Standing project context, pasted into the Claude project knowledge. Rewritten 2026-08-16 to point at `BUILD_SPEC.md` and this file | When the standing rules change |
| `README.md`, `.gitignore` | Repo housekeeping | Rarely |
| `template.html` (root) | Retired stub as of 2026-08-16. It was the JavaScript-rendered listing skeleton that produced pages crawlers saw as blank. Safe to delete in GitHub Desktop | Never |
| `docs/BUILD_SPEC.md` | How to publish a launch. The current process. **New file, commit it** | When the process changes |
| `docs/LISTING_TEMPLATE_SSR.html` | The one template all new listing pages come from. **New file, commit it** | Rarely, carefully |
| `docs/validate_build.py` | Pre-commit checker. Run it before every push. **New file, commit it** | Rarely |
| `docs/rebuild_listings.py` | Re-renders every listing page from the template. Idempotent. **New file, commit it** | Rarely |
| `docs/regen_indexes.py` | Rebuilds the category pages, `directory.html` and `llms.txt` from `listings.json`. Run it on every batch. **New file, commit it** | Rarely |
| `docs/fix_house_style.py` | Strips em dashes from the hand-written pages. **New file, commit it** | Rarely |
| `docs/apply_cleanup.py` | The one-time 2026-08-16 cleanup, kept for the record. **New file, commit it** | Never again |
| `docs/OPERATIONS_MANUAL.md` | This file. **New file, commit it** | When the operation changes |
| `docs/RUNBOOK.md` | Retired stub pointing at `BUILD_SPEC.md`. Safe to delete | Never |
| `docs/HANDOFF-*.md`, `docs/SEO_GEO_Audit_*.md` | Dated session history. The newest is the most recent state | Each session |
| `The_Runway_New_Listings_Runbook.md` (root) | Retired stub. Safe to delete | Never |
| `listing-generator.html` | Local admin tool. **Kept off the repo on purpose. Do not upload it.** Note that `.gitignore` does not exclude it, so this is enforced by discipline only | Never |

---

## 4. The data model

### `listings.json` is the catalog

A single JSON array. One object per launch, 14 fields, documented field by field in
`BUILD_SPEC.md` section 9. The homepage and browse page fetch it on every page load and build the
grid from it. Nothing else on the site is a database.

Two fields exist but are not live truth:

- `votes` is always `0` in the file. Real counts come from Supabase.
- `featured` is the hook for future sponsored placements. Currently `true` on one record.

`mrr` is intake-only and stays empty in the published file. Builders share revenue numbers in
confidence on the form and they do not get published.

### Supabase holds the votes

| | |
|---|---|
| Project | `launchfree-votes` |
| Project ref | `klsfvbmqlmmsdnfvoiqw` |
| Table | `public.launch_votes` (slug, votes, updated_at) |
| Write path | the `increment_vote(p_slug)` function, and nothing else |
| Client key | the publishable key, which is client-safe by design and is in the page source |
| Secret key | never in the repo, never in a page. It lives in the Supabase dashboard |

How it works: each listing page reads its own count on load and writes one vote on click, guarded
per browser by a `localStorage` key `lf_vote_<slug>`. The homepage and browse grid batch-read all
counts at once and their upvote buttons write through the same function.

**The table is sparse.** A slug only appears after its first real vote. A brand new launch showing
0 is correct, not a bug.

The publishable key being visible in page source is intentional and is how Supabase is designed to
work from a browser. Row level security and the single write function are what protect the table.
If the key is ever rotated, it has to be updated in every listing page plus `index.html` and
`browse.html`, which is a find and replace across the repo.

---

## 5. From submission to live

### Step 1: intake

`submit.html` collects the fields listed in `BUILD_SPEC.md` section 2 and POSTs them as JSON to a
Make.com webhook, with `Status: "Pending Review"` attached. Make routes it into the Airtable
`Submissions` table.

**Verified working on 2026-08-16** by sending a test submission through the live form: it reached
Airtable and the notification email arrived. An older project instructions file claimed Make and
Airtable were out of the stack. That was wrong, and it has been corrected. Make and Airtable are
live parts of this operation.

If intake ever needs to point somewhere else, it is one constant, `WEBHOOK_URL`, at the top of the
script block in `submit.html`. The way to test any change is the same: submit through the live form
and confirm the record appears in Airtable and the email arrives.

Builders are told to expect a decision in about 24 hours. That promise is on the form and in
`llms.txt`, so it is a real commitment.

### Step 2: review

Open every submitted URL live and decide Approve, Review or Reject with a one line reason. Full
standard in `BUILD_SPEC.md` section 5. Short version: it has to be a real, working, honest product,
and it cannot be fraud, a crypto token, or anything involving minors unsafely.

### Step 3: build

Follow `BUILD_SPEC.md`. Every approved launch gets a page built from
`docs/LISTING_TEMPLATE_SSR.html`, plus updates to five other files. All six in one commit.

### Step 4: deploy

GitHub Desktop only. Commit, Fetch, Pull, Push. Full detail in `BUILD_SPEC.md` section 11.

**The one absolute rule: an assistant never runs git against this repo.** Not `git status`, not
anything. Two git processes on the same folder leave a stale `.git/index.lock` that blocks every
future commit until it is deleted by hand. The assistant edits files. GitHub Desktop does git.

### Step 5: email the builder

Approvals, rejections and review requests all get an email. Rejections say why, plainly and
kindly. Review emails say exactly what is needed to move forward, usually a live URL.

---

## 6. Hosting, domain and email

| Thing | Where | Notes |
|---|---|---|
| Hosting | GitHub Pages, from the `main` branch of `AFPJulieJames/launchfree-io` | Free. No build step. Deploys on push |
| Custom domain | The `CNAME` file in the repo contains `launchfree.io` | If this file is ever deleted in a commit, the custom domain unbinds and the site falls back to the github.io URL. Do not delete it |
| Domain registrar | Namecheap | Renewal date and auto-renew status need to be confirmed and calendared. **A lapsed domain takes the whole site down and is the single highest impact failure in this stack** |
| DNS | At the registrar, pointing at GitHub Pages | Confirm the A records and the `www` CNAME are documented in the password manager |
| Email | `hello@launchfree.io` | Confirm which provider forwards or hosts it |

---

## 7. Newsletter: The Runway Radar

Weekly, on Fridays, sent from Beehiiv. The signup form is embedded on the homepage.

Content shape: the week's new launches, plus the top voted launch of the week.

**Pick the weekly winner from the Supabase `launch_votes` table**, filtered to launches approved
that week and sorted by votes. Never from `listings.json`, where every value is 0.

Builders who ticked the newsletter opt-in on the submission form go on the list.

---

## 8. Analytics

Google Analytics 4, property `G-7CKQDBEDBB`, on every page including every listing page. Custom
events currently fired: `upvote` (with the launch slug) and `submission_complete`.

There is no other tracking, no ad pixel, and no third party script beyond Google Fonts, the GA4
tag, Beehiiv's embed on the homepage, and the Supabase calls.

---

## 9. SEO and GEO: the rules that keep this site visible

The whole product is discoverability. A listing that search engines and AI assistants cannot read
is worth nothing to the builder who submitted it, which means the free backlink promise quietly
stops being true. These rules are the product working.

**1. Every page is server-rendered.** The real content lives in the static HTML. JavaScript is only
for interaction. Turn JavaScript off and the page must still show the name, tagline, description
and story. On 2026-08-16, 56 pages were found rendering their content in JavaScript: crawlers and
AI bots saw a "Loading" title, an empty description, an empty H1, empty schema and a canonical
pointing at the homepage. They were rebuilt. It must not recur, which is why there is now exactly
one template.

**2. Canonicals always point at the page's own URL.** A canonical pointing at the homepage tells
Google the listing is a duplicate of the homepage and should not be indexed on its own.

**3. Every listing carries `SoftwareApplication` and `BreadcrumbList` JSON-LD.** This is how answer
engines extract what a product is, who built it, and where it sits.

**4. Crawl paths without JavaScript.** `directory.html` and the 17 category pages are plain static
links to listings. They exist so a crawler that runs no JavaScript can still reach every page. Both
must be regenerated on every build or launches become unreachable except through the sitemap.
Both were brought current on 2026-08-16 and `docs/regen_indexes.py` keeps them that way. All 235
launches are reachable from `directory.html` and from their category page.

**5. `llms.txt` is maintained deliberately.** It is a plain language description of the site written
for AI assistants, with a link and a one line summary per recent launch, and a live launch count.

**6. `robots.txt` explicitly welcomes AI crawlers.** GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot,
Claude-Web, anthropic-ai, PerplexityBot, Perplexity-User, Google-Extended, Applebot-Extended,
Amazonbot, Bytespider, CCBot, cohere-ai, Meta-ExternalAgent, Bingbot, plus the social unfurl bots. This is a strategic
choice: being cited by AI assistants is a distribution channel, not a threat.

**7. Internal links matter.** Every listing links to three related launches in the same category.
That is what pulls crawl depth through the catalog.

**8. Every page ships the full favicon and touch-icon set, no exceptions.** Six link tags, right
after the viewport meta tag:

```html
<link rel="icon" href="https://launchfree.io/favicon.ico" sizes="any" />
<link rel="icon" type="image/png" sizes="16x16" href="https://launchfree.io/favicon-16.png" />
<link rel="icon" type="image/png" sizes="32x32" href="https://launchfree.io/favicon-32.png" />
<link rel="apple-touch-icon" sizes="180x180" href="https://launchfree.io/apple-touch-icon-180.png" />
<link rel="icon" type="image/png" sizes="192x192" href="https://launchfree.io/icon-192.png" />
<link rel="icon" type="image/png" sizes="512x512" href="https://launchfree.io/icon-512.png" />
```

Listings, category pages, the homepage and directory all get this automatically because they are
generated from `docs/LISTING_TEMPLATE_SSR.html`, which carries the block. **The radar articles
(`radar/*.html`) do not have a generator or shared template, they are hand-authored one file at a
time, so this block does not propagate to them automatically.** This is exactly how all 17 of them
shipped with no favicon markup until the 2026-09-04 audit caught it. When writing a new radar
article: copy the full `<head>` block from the most recently published article in `radar/` (they
are all identical in structure, only title/description/canonical/OG differ per article) rather than
writing the head from scratch, and confirm the six icon lines above are present before publishing.

Latest full audit: `docs/SEO_GEO_Audit_2026-08-16.md`.

---

## 10. Accounts, and where the keys live

**No secret values are written in this file, or in any file in the repo.** Every account below
should have its credentials in Julie's password manager, with the LLC listed as owner, and with a
recovery contact set. If you are taking this over, the password manager is the thing you need
access to first. Everything else follows from it.

| Service | Used for | What is public | What is secret |
|---|---|---|---|
| GitHub (`AFPJulieJames`) | Repo and hosting | Repo name, all site source | Account password, 2FA, any personal access tokens |
| Namecheap | Domain registration | Domain name | Account login, auth code for transfers |
| Supabase (`launchfree-votes`) | Vote counts | Project ref and publishable key, both in page source by design | Account login, service role key, database password |
| Beehiiv | Newsletter | Publication and embed form id | Account login, API key |
| Make.com | Submission webhook routing | Webhook URL, which is in `submit.html` and therefore public | Account login |
| Airtable | Submission inbox | Base id `appuyAibeokhZsDJ9`, which is still in the current `index.html` and `browse.html` source | Account login, API key |
| Google Analytics | Traffic | Measurement id `G-7CKQDBEDBB` | Google account |
| Google Search Console, Bing Webmaster | Index monitoring | none | Google and Microsoft accounts |
| Email for `hello@launchfree.io` | Builder correspondence | Address | Mailbox login |

### Two security items to action

1. **A GitHub personal access token is sitting in plain text in the May 9 project handoff doc.**
   Tokens in documents get copied into other documents. Revoke it at
   `github.com/settings/tokens`, and if anything still needs it, issue a fresh fine-grained token
   scoped to this one repo and store it in the password manager only.
2. **The Make webhook URL is public**, because it is in `submit.html` where any browser can read it.
   That is unavoidable for a client side form, but it means anyone can POST junk to it. If spam
   submissions ever become a problem, the fix is a filter in Make or a spam check on the form, not
   hiding the URL.

---

## 11. Operating cadence

**Per batch, which currently runs every day or two**

1. Check the submission inbox
2. Live-review every new URL
3. Build the approved ones per `BUILD_SPEC.md`
4. Run `python3 docs/validate_build.py`
5. Commit, fetch, pull, push in GitHub Desktop
6. Verify live, including View Source on one new page
7. Send approval, rejection and review emails

**Weekly**

- Send The Runway Radar on Friday, top launch picked from the Supabase vote counts
- Skim Search Console for coverage errors and new indexing

**Monthly**

- Resubmit the sitemap to Google Search Console and Bing Webmaster Tools
- Check that the total in `llms.txt`, `directory.html` and the category pages all match
  `listings.json`
- Confirm the domain renewal is still on auto-renew

**Never**

- Charge for a core listing

---

## 12. Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| GitHub Desktop says "a lock file already exists" | Stale `.git/index.lock`, almost always because something other than GitHub Desktop ran git | Quit GitHub Desktop, run `rm -f "/Users/jules/Documents/Claude/LaunchFree Hub/launchfree-io/.git/index.lock"`, reopen, retry |
| Push is blocked by "newer commits on remote" | The remote moved ahead | Fetch origin, then Pull origin, then Push |
| A new listing page 404s | Pages has not redeployed yet, or the filename does not match the slug | Wait 3 minutes, then check the filename against `listings.json` |
| A launch is live but not on the homepage | It is missing from `listings.json`, or the browser cached the old file | Check `listings.json`, then hard refresh |
| A launch is not on its category page or in the directory | Those two surfaces were not regenerated | Regenerate both, see `BUILD_SPEC.md` section 9 |
| Upvote button shows nothing or does not respond | The vote script slug does not match the filename, or the page has no `.upvote-btn` | Check both, per the pre-flight checklist |
| A page shows "Loading" in View Source | A client-rendered page shipped | Rebuild it from `docs/LISTING_TEMPLATE_SSR.html`. This is the regression that must not recur |
| The whole site is down | Almost always the domain or the `CNAME` file | Check the registrar first, then confirm `CNAME` still exists in the repo root, then check GitHub's status page |
| Submissions stop arriving | Make or Airtable lapsed, or a plan limit was hit | Submit a test entry through the live form and trace it |
| Newsletter signup errors on the homepage | Beehiiv embed or publication setting | Check Beehiiv first |

---

## 13. If Julie is not available

**Minimum viable operation, in priority order.** Doing only the first two keeps the promise to
everyone who has already listed. The rest is growth.

1. **Keep the domain and the GitHub account alive.** Everything else is recoverable. These two are
   not. If the domain lapses, 235 builders lose the backlink they were promised.
2. **Keep the site up.** It is static. It needs nothing to stay live. Do not "clean up" the repo.
3. **Answer `hello@launchfree.io`.** Even a holding reply. Builders who submitted are waiting.
4. **Keep publishing batches** using `BUILD_SPEC.md`. It is a mechanical process and it does not
   require knowing the history.
5. **Keep the newsletter going** if you can. Skipping a week is fine. Silence for a month is not.

**What a successor must not do**

- Do not charge for core listings. It is the only thing that makes this different.
- Do not rename or delete live listing slugs. Every one is a permanent URL and a backlink someone
  was promised.
- Do not delete the `CNAME` file.
- Do not switch to a framework or a build step because the HTML looks old fashioned. The simplicity
  is why a non-engineer can run it.
- Do not remove the AI crawler allowances in `robots.txt`.

**Who to contact**

- Julie James, owner, Automated Income Tools LLC
- Moid Khan, developer who has worked on the related build
- The LLC's registered agent, for anything to do with the entity itself

Fill in current phone numbers and emails for the two people above in the password manager entry,
not in this file.

---

## 14. State of the repo, as of 2026-08-16

Everything the audit found was fixed the same day. `python3 docs/validate_build.py` reports 0 errors
and 0 warnings against the current repo. What that covers:

| Was | Now |
|---|---|
| Two page shapes in `listings/`, 62 tabbed and 173 stacked | All 235 generated from one template |
| Three related cards pointed at a `nanobanana.html` that does not exist | Every related card resolves |
| Category pages stale at 179 launches | All 17 match `listings.json` exactly |
| 6 seed pages had no `SoftwareApplication` or `BreadcrumbList` schema | Every page has both |
| 70 pages had no robots meta | Every page has one |
| 42 pages carried a dead `LF_SLUG` script | Removed |
| Em dashes in copy on listing pages, landing pages and radar articles | None outside the page title separator and the brand lockup |
| Submit form offered two categories that did not exist, and omitted two that did | Form and site agree on all 17 |
| Dead Airtable code and a stale seed array in `index.html` and `browse.html` | Removed. They read `listings.json` only |
| Four records with drifted stage values | Normalized |
| A dead `/css/content-shared.css` link on 32 pages | Removed |
| `template.html` and two conflicting runbooks | Stubs pointing at `BUILD_SPEC.md` |

Two files can be deleted in GitHub Desktop whenever convenient: `template.html` and
`The_Runway_New_Listings_Runbook.md`. They are stubs, so nothing depends on them either way.

The intake path was the one thing the repo could not confirm on its own. It was tested end to end
on 2026-08-16 and it works: the form posts to Make, the record lands in Airtable, and the
notification email arrives.

---

### A note on the front end, now that it is clean

`index.html` and `browse.html` used to carry an old Airtable code path and a hardcoded six record
seed list. In `index.html` the order was dangerous: it only read `listings.json` because the
Airtable key was still a placeholder string, so pasting a real key in there would have silently
switched the homepage to Airtable data. Both files were cleaned on 2026-08-16. They now fetch
`listings.json` and nothing else, and log an error if that fetch fails. Keep it that way: the
catalog has exactly one source.

---

## 15. Open questions to confirm and write down

These are things this manual could not verify from the repo alone. Answer them, then update this
file. Each one is a single point of failure until it is written down somewhere other than one
person's memory.

- [x] **Where do submissions land?** Confirmed 2026-08-16 by live test: `submit.html` posts to the
      Make webhook, Make writes the record to the Airtable `Submissions` table, and the
      notification email arrives. Make and Airtable are both active parts of the stack.
- [ ] What plan is the Make account on, and what is its monthly operation limit? A submission burst
      that exceeds it would drop entries silently
- [ ] Same question for Airtable: which plan, and what is the record limit on the base?
- [ ] Domain renewal date at Namecheap, and is auto-renew on?
- [ ] Who hosts or forwards `hello@launchfree.io`?
- [ ] Are all accounts in one password manager, and is there an emergency access contact on it?
- [ ] Is the Supabase project on the free tier, and what are its limits at current traffic?
- [ ] Is the GitHub personal access token from the May 9 doc revoked yet?
- [ ] Is there a backup of `listings.json` outside GitHub? Git history counts, as long as someone
      other than Julie can reach the account

---

*Companion documents: `docs/BUILD_SPEC.md` for publishing launches,
`docs/LISTING_TEMPLATE_SSR.html` for the page template, `docs/validate_build.py` for pre-commit
checks, and the newest `docs/HANDOFF-*.md` for what happened most recently.*
