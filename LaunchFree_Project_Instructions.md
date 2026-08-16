# LaunchFree.io: Project Instructions

Standing context for every session. This lives in the Claude project knowledge so it loads every
time. Keep it short and current.

- **Build process:** `docs/BUILD_SPEC.md`. The only build process.
- **How the site works:** `docs/OPERATIONS_MANUAL.md`. Architecture, accounts, cadence, recovery.
- **What happened last:** the newest `docs/HANDOFF-YYYY-MM-DD*.md`.

House style: no em dashes in body copy, anywhere, ever.

---

## What this is

LaunchFree.io, brand name The Runway, is a free product launch directory for founders, indie
builders and side hustlers. Tagline: "Every launch needs a runway. Yours is free." Run by Julie
James under Automated Income Tools LLC. The core listing is free forever. Money comes later from
optional sponsored placements and newsletter advertising, never from gating the directory.

- Live site: https://launchfree.io
- Contact: hello@launchfree.io
- X: @JulieBuilds
- Newsletter: The Runway Radar (Beehiiv), weekly on Fridays
- Scale: 235 live launches across 17 categories as of 2026-08-16

---

## Architecture in five lines

- Static HTML, CSS and JavaScript on GitHub Pages. Repo `AFPJulieJames/launchfree-io`, local path
  `/Users/jules/Documents/Claude/LaunchFree Hub/launchfree-io/`. No server, no build step.
- **`listings.json` is the catalog.** The homepage and browse page fetch it live. A launch that is
  not in it does not exist on the site.
- **Votes live in Supabase**, project `launchfree-votes`, ref `klsfvbmqlmmsdnfvoiqw`, table
  `public.launch_votes`, single write path `increment_vote(p_slug)`. The publishable key is
  client-safe and sits in the pages. New records are always `votes: 0`.
- Submissions POST from `submit.html` to a Make webhook, Make writes them into the Airtable
  `Submissions` table, and a notification email goes to Julie. Verified by live test on 2026-08-16.
  Publishing is manual from the repo. If any doc says Make and Airtable are gone, that doc is wrong.
- Everything else is generated: see the scripts in `docs/`.

---

## The golden rules

1. **The assistant never runs git.** Not `git status`, not anything. Claude edits files. Julie
   commits, fetches, pulls and pushes in GitHub Desktop. Two git processes on one repo leave a
   `.git/index.lock` that blocks every future commit.
2. **Every listing page is built from `docs/LISTING_TEMPLATE_SSR.html`.** Never from
   `template.html`, never by copying another page, never by hand. All 235 pages share one shape as
   of 2026-08-16 and it stays that way.
3. **Pages are server-rendered.** Turn JavaScript off and the content must still be there. A page
   that renders its content in JavaScript is invisible to Google and to AI answer engines.
4. **One slug, decided once, never renamed.** It is the filename, the vote key and the dofollow
   backlink at the same time.
5. **Every new listing touches six surfaces:** the page, `listings.json`, `sitemap.xml`, `llms.txt`,
   `directory.html`, and its category page. Skip one and the launch is half published.
6. **Live-review every submission** before approving. Real, working, honest products only.
7. **Run `python3 docs/validate_build.py` before every commit.** It must report 0 errors.
8. **Nothing is done until it is verified live**, including View Source showing the real content.

---

## Deploy

GitHub Desktop only. Commit, then Fetch, then Pull, then Push. If a commit is blocked by a lock
file: quit GitHub Desktop, run
`rm -f "/Users/jules/Documents/Claude/LaunchFree Hub/launchfree-io/.git/index.lock"`, reopen, retry.

---

## Newsletter

Pick the weekly Runway Radar winner from the Supabase `launch_votes` table (approved that week,
sorted by votes), never from `listings.json`, where every vote value is 0.

---

At the start of a session: read this file, the newest handoff, and `docs/BUILD_SPEC.md`. Then work.
