# LaunchFree.io — brand assets (v1)

Logo: **Centerline** mark + **LaunchFree.io** wordmark ("Free" in runway lime),
with **The Runway** as the endorsement line. Master brand = LaunchFree.io.
Brand world = The Runway.

Palette: ink #0A0F1A · runway lime #E8FF47 · cream #F8F5EE · muted #6B7585.
Wordmark type is outlined to vector paths (Space Grotesk 700, the reliable
open-source match to the site's Cabinet Grotesk), so every SVG renders
identically with no font dependency.

## Files

Vector (SVG, scalable, use these first)
- launchfree-horizontal.svg        primary logo (LaunchFree.io(TM)), dark backgrounds
- launchfree-horizontal-light.svg  primary logo (with TM), light backgrounds
- launchfree-stacked.svg           stacked lockup (with TM), dark backgrounds
- launchfree-stacked-light.svg     stacked lockup (with TM), light backgrounds
- launchfree-horizontal-plain.svg  no-TM version, for small / repeated use
- launchfree-horizontal-light-plain.svg
- launchfree-stacked-plain.svg / launchfree-stacked-light-plain.svg   no-TM versions

The (TM) primary lockups carry a small trademark mark, correct for the logo as
your primary brand use. Use the -plain versions where the logo repeats or runs
small. TM signals a common-law claim and needs no registration (never use the
R symbol until you hold a federal registration). Also flag "The Runway(TM)" on
its prominent standalone uses (the site, the "Listed on The Runway" badge): it
is your stronger, more protectable mark. See the naming/trademark project note.
- mark-lime.svg                    mark only (lime), transparent
- mark-cream.svg                   mark only (cream), transparent
- mark-mono.svg                    single-ink mark, fill=currentColor (recolors to any one ink) — use for the "Listed on The Runway" badge and one-color print

Raster (PNG/ICO)
- png/favicon-16.png, favicon-32.png      browser tab
- png/favicon.ico                          legacy .ico (16/32/48)
- png/apple-touch-icon-180.png             iOS home screen (opaque)
- png/icon-192.png, icon-512.png           PWA / Android (opaque, maskable-safe)
- png/og-image.png (1200x630)              social share card
- png/avatar-512.png                       square social avatar (X, LinkedIn, etc.)

## Where each file goes in the repo (suggested)

Logos:            assets/brand/   (all .svg lockups + marks)
Favicons/icons:   web root, next to index/listing pages, so paths are /favicon.ico etc.
OG image:         assets/brand/og-image.png  (or web root)
Avatar:           not deployed to the site; upload directly to X / LinkedIn / etc.

## Wiring it into the site  (SEPARATE BUILD STEP — needs your approval)

These links live in the shared <head> of docs/LISTING_TEMPLATE_SSR.html, so any
change here rebuilds across all 400+ pages. Do NOT let me do this silently.
When you are ready, add to the template <head> and run the normal build +
python3 docs/validate_build.py (must report 0 errors), then commit in GitHub
Desktop:

    <link rel="icon" href="/favicon.ico" sizes="any">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon-180.png">
    <link rel="icon" type="image/png" sizes="192x192" href="/icon-192.png">
    <link rel="icon" type="image/png" sizes="512x512" href="/icon-512.png">
    <meta property="og:image" content="https://launchfree.io/assets/brand/og-image.png">
    <meta name="twitter:card" content="summary_large_image">

Notes
- I did not edit any page, template, or favicon link, and I did not run git.
- The ".io" in the wordmark is optional. Say the word and I'll ship a clean
  "LaunchFree" set without it.
