import {bundle} from '@remotion/bundler';
import {selectComposition, renderMedia} from '@remotion/renderer';
import path from 'path';

const CHROME = '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell';
const OUT = process.argv[2] || '/mnt/user-data/outputs/runway-origin-story.mp4';

console.log('Bundling...');
const serveUrl = await bundle({
  entryPoint: path.resolve('src/index.ts'),
  onProgress: (p) => { if (p % 25 === 0) console.log('  bundle', p + '%'); },
});

console.log('Selecting composition...');
const composition = await selectComposition({
  serveUrl,
  id: 'OriginStory',
  browserExecutable: CHROME,
  chromiumOptions: {gl: 'swiftshader'},
});
console.log('  duration frames:', composition.durationInFrames, 'fps', composition.fps);

console.log('Rendering ->', OUT);
await renderMedia({
  composition,
  serveUrl,
  codec: 'h264',
  outputLocation: OUT,
  browserExecutable: CHROME,
  chromiumOptions: {gl: 'swiftshader'},
  concurrency: 2,
  crf: 18,
  x264Preset: 'slow',
  pixelFormat: 'yuv420p',
  onProgress: ({progress}) => {
    const pct = Math.round(progress * 100);
    if (pct % 10 === 0) console.log('  render', pct + '%');
  },
});
console.log('DONE ->', OUT);
