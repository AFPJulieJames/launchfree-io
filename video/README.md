# The Runway - video pipeline (Remotion)

Sleek 9:16 short-video generator for LaunchFree.io / The Runway. Visuals are
code (no Fliki). Fliki is only used to make the voiceover MP3.

## What's here
- src/OriginStory.tsx  the composition (the sleek look + 7 beats). Edit text,
  colors, and the D[] beat durations here.
- src/Root.tsx, src/index.ts  Remotion registration (1080x1920, 30fps).
- render.mjs  bundles + renders to an MP4 (uses the headless-shell Chrome).
- public/  scene assets: hero-shot.png, directory-shot.png, listing-shot.png,
  and vo.mp3 (the voiceover; swap per video).

## Build (in a Cowork cloud session)
1. cd into this folder.
2. npm install   (restores remotion + react + @fontsource, ~30s)
3. Put the voiceover at public/vo.mp3 and any product screenshots in public/.
4. node render.mjs /mnt/user-data/outputs/my-video.mp4
   (render uses /opt/pw-browsers/chromium_headless_shell-*/chrome-linux/headless_shell;
    render.mjs already points at it. The full 'chromium' binary will NOT work.)

## Make a NEW video (e.g. Launch of the Week)
- Copy OriginStory.tsx to a new component, or reuse it: change the beat text
  (B1/B2/B3/B7), swap the Hero screenshots + captions, and retime D[] to the new
  voiceover length. D[] are frame counts at 30fps; total must equal the sum.
- Timing rule of thumb: measure the VO duration (ffprobe), multiply by 30 for
  frames, split across beats by line length, add ~45 frames tail on the end card.
- Fonts load from @fontsource locally (Google Fonts is blocked in the cloud).

## The look (locked)
Ink #0A0F1A + film grain, Playfair Display serif headlines, Space Grotesk labels,
ONE lime #E8FF47 accent per frame, real-site screenshots as hero shots with one
quiet lower-third caption, confident holds, no karaoke captions. See the style
system: claude/runway-video-look.html and claude/tiktok-origin-story-build-2026-08-31.md.
