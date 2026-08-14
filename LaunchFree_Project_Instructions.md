# LaunchFree.io — Project Instructions

Standing context for every session. Paste this into the LaunchFree project knowledge so it loads
every time. Keep it short and current. For the step-by-step build process, see `docs/RUNBOOK.md`.
For what happened last, read the newest `docs/HANDOFF-YYYY-MM-DD.md`.

House style: no em dashes anywhere, ever.

---

## What this is

LaunchFree.io ("The Runway") is a free product launch directory for founders, indie builders, and
side-hustlers. Tagline: "Every launch needs a runway. Yours is free." Run by Julie James under
Automated Income Tools LLC. The core listing is free forever; money comes later from optional
sponsored placements and services, never from gating the core directory.

- Live site: https://launchfree.io
- Contact: hello@launchfree.io
- X: @JulieBuilds
- Newsletter: The Runway Radar (Beehiiv), weekly on Fridays

---

## How the site is built (current architecture)

- **Static HTML/CSS/JS on GitHub Pages.** Repo `AFPJulieJames/launchfree-io`, local path
  `/Users/jules/Documents/Claude/LaunchFree Hub/launchfree-io/`.
- **The connected repo is the only source of truth.** Not a scratchpad, not a zip, not Airtable.
  Connect the repo folder to the session and work inside it.
- **`listings.json` is the catalog.** The homepage and browse page read it live at page load.
  A launch that is not in `listings.json` does not appear on the site.
- **Voting runs on Supabase**, not in files. Project `launchfree-votes`, ref
  `klsfvbmqlmmsdnfvoiqw`, table `public.launch_votes`, single write path `increment_vote(p_slug)`.
  The publishable key is client-safe and lives in the pages; the secret key never goes in the repo.
  New records are always `votes: 0`. Never hardcode vote numbers.
- Airtable and Make are no longer part of the stack. Ignore any older doc that references them.

---

## The golden rules (do not break these)

1. **The assistant never runs git.** Claude edits files only. Julie stages, commits, fetches,
   pulls, and pushes in GitHub Desktop. Two git processes on one repo create a `.git/index.lock`
   that blocks commits. No `git status`, no `git commit`, nothing.
2. **Build in the repo. Never unzip a delivered folder into it.** That is what created the old
   `listings 2` mess. Write pages straight into `listings/`, one file at a time.
3. **One slug, decided once, never renamed.** The slug is the filename, the vote key, and the
   dofollow backlink. Renaming a live slug breaks all three. Kebab-case rule in the RUNBOOK.
4. **Every new listing touches four surfaces together:** the page in `listings/`, `listings.json`,
   `sitemap.xml`, and `llms.txt`. Skip one and the launch is half-published.
5. **Live-review every submission before approving.** Pull each URL live and check it is a real,
   working product within standards (no dead links, fraud, terms-of-service violations, crypto
   tokens, or non-products).
6. **Nothing is done until verified live** on the site and, for votes, against Supabase.

---

## Deploy flow (GitHub Desktop, by Julie)

Commit, then Fetch, then Pull, then Push. Always fetch and pull before pushing. If a commit is
blocked by a lock file: quit GitHub Desktop, run
`rm -f "/Users/jules/Documents/Claude/LaunchFree Hub/launchfree-io/.git/index.lock"`, reopen, retry.

---

## Working docs (where the truth lives)

- **Standing SOP:** `docs/RUNBOOK.md` (the full build process). This is the single canonical runbook.
- **Latest handoff:** the newest `docs/HANDOFF-YYYY-MM-DD.md`. The newest dated file is always the
  truth; older ones are history.
- **This file:** standing context, kept in project knowledge so every session starts aligned.

At the start of a session: read this file, the newest handoff, and the RUNBOOK. Then work.

---

## Newsletter

Pick the weekly Runway Radar winner from the Supabase `launch_votes` table (approved that week,
sorted by votes), never from `listings.json`.
