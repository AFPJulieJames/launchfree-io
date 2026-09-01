import React, {useEffect, useState} from 'react';
import {
  AbsoluteFill,
  Sequence,
  Img,
  Audio,
  staticFile,
  useCurrentFrame,
  interpolate,
  delayRender,
  continueRender,
  Easing,
} from 'remotion';

import '@fontsource/playfair-display/latin-500.css';
import '@fontsource/playfair-display/latin-700.css';
import '@fontsource/playfair-display/latin-900.css';
import '@fontsource/playfair-display/latin-500-italic.css';
import '@fontsource/space-grotesk/latin-400.css';
import '@fontsource/space-grotesk/latin-500.css';
import '@fontsource/space-grotesk/latin-700.css';

const INK = '#0A0F1A';
const CREAM = '#F6F3EC';
const DIM = '#C0BCB2';
const MUTED = '#6C7686';
const LIME = '#E8FF47';
const SERIF = "'Playfair Display', Georgia, serif";
const SANS = "'Space Grotesk', system-ui, sans-serif";

const GRAIN =
  "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E\")";

const ease = Easing.bezier(0.2, 0.7, 0.2, 1);

const Grain: React.FC = () => (
  <AbsoluteFill
    style={{backgroundImage: GRAIN, opacity: 0.05, mixBlendMode: 'overlay'}}
  />
);

const Glow: React.FC<{y?: number}> = ({y = 32}) => (
  <AbsoluteFill
    style={{
      background: `radial-gradient(120% 52% at 50% ${y}%, rgba(232,255,71,0.10), transparent 60%)`,
    }}
  />
);

const Vignette: React.FC = () => (
  <AbsoluteFill
    style={{
      background:
        'radial-gradient(130% 100% at 50% 50%, transparent 55%, rgba(0,0,0,0.55) 100%)',
    }}
  />
);

// fade in over first `inF`, out over last `outF`
const useBeat = (dur: number, inF = 18, outF = 16) => {
  const f = useCurrentFrame();
  const opacity = interpolate(
    f,
    [0, inF, dur - outF, dur],
    [0, 1, 1, 0],
    {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: ease}
  );
  const rise = interpolate(f, [0, inF], [16, 0], {
    extrapolateRight: 'clamp',
    easing: ease,
  });
  return {f, opacity, rise};
};

const Stage: React.FC<{children: React.ReactNode}> = ({children}) => (
  <AbsoluteFill style={{backgroundColor: INK}}>
    {children}
    <Grain />
    <Vignette />
  </AbsoluteFill>
);

// ---------- Beat 1 : cold open ----------
const B1: React.FC<{dur: number}> = ({dur}) => {
  const {opacity, rise} = useBeat(dur);
  return (
    <Stage>
      <Glow />
      <AbsoluteFill
        style={{
          alignItems: 'center',
          justifyContent: 'center',
          padding: 120,
          textAlign: 'center',
        }}
      >
        <div
          style={{
            fontFamily: SERIF,
            fontWeight: 700,
            color: CREAM,
            fontSize: 116,
            lineHeight: 1.02,
            letterSpacing: '-0.01em',
            opacity,
            transform: `translateY(${rise}px)`,
          }}
        >
          I tried to launch
          <br />
          for free.
        </div>
      </AbsoluteFill>
    </Stage>
  );
};

// ---------- Beat 2 : the wall ($300) ----------
const B2: React.FC<{dur: number}> = ({dur}) => {
  const {f, opacity} = useBeat(dur);
  const numRise = interpolate(f, [0, 22], [26, 0], {
    extrapolateRight: 'clamp',
    easing: ease,
  });
  const subOp = interpolate(f, [16, 34], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: ease,
  });
  return (
    <Stage>
      <AbsoluteFill
        style={{
          alignItems: 'center',
          justifyContent: 'center',
          flexDirection: 'column',
          padding: 120,
          textAlign: 'center',
          opacity,
        }}
      >
        <div
          style={{
            fontFamily: SERIF,
            fontWeight: 900,
            color: CREAM,
            fontSize: 400,
            lineHeight: 0.9,
            letterSpacing: '-0.02em',
            transform: `translateY(${numRise}px)`,
          }}
        >
          $300
        </div>
        <div
          style={{
            fontFamily: SANS,
            fontWeight: 400,
            color: DIM,
            fontSize: 46,
            marginTop: 34,
            letterSpacing: '0.01em',
            opacity: subOp,
          }}
        >
          or a ninety&#8209;week wait. just to get listed.
        </div>
      </AbsoluteFill>
    </Stage>
  );
};

// ---------- Beat 3 : the turn ----------
const B3: React.FC<{dur: number}> = ({dur}) => {
  const {opacity, rise} = useBeat(dur);
  return (
    <Stage>
      <Glow y={38} />
      <AbsoluteFill
        style={{
          alignItems: 'center',
          justifyContent: 'center',
          padding: 120,
          textAlign: 'center',
        }}
      >
        <div
          style={{
            fontFamily: SERIF,
            fontWeight: 700,
            color: CREAM,
            fontSize: 118,
            lineHeight: 1.02,
            letterSpacing: '-0.01em',
            opacity,
            transform: `translateY(${rise}px)`,
          }}
        >
          So I built
          <br />
          the <span style={{color: LIME, fontStyle: 'italic'}}>free</span> one.
        </div>
      </AbsoluteFill>
    </Stage>
  );
};

// ---------- Product-hero beats ----------
const Hero: React.FC<{
  dur: number;
  src: string;
  caption: string;
  alt: string;
}> = ({dur, src, caption, alt}) => {
  const {f, opacity} = useBeat(dur, 16, 16);
  const scale = interpolate(f, [0, dur], [1.06, 1.0], {
    extrapolateRight: 'clamp',
    easing: Easing.inOut(Easing.quad),
  });
  const capOp = interpolate(f, [14, 32], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: ease,
  });
  return (
    <AbsoluteFill style={{backgroundColor: INK, opacity}}>
      <AbsoluteFill style={{transform: `scale(${scale})`}}>
        <Img src={staticFile(src)} alt={alt} style={{width: '100%', height: '100%', objectFit: 'cover'}} />
      </AbsoluteFill>
      <AbsoluteFill
        style={{
          background:
            'linear-gradient(to top, rgba(6,9,15,0.94) 7%, rgba(6,9,15,0.20) 40%, transparent 62%)',
        }}
      />
      <Grain />
      <AbsoluteFill
        style={{
          justifyContent: 'flex-end',
          padding: '0 88px 150px',
        }}
      >
        <div style={{display: 'flex', alignItems: 'center', gap: 20, opacity: capOp}}>
          <div
            style={{
              width: 18,
              height: 18,
              borderRadius: '50%',
              background: LIME,
              boxShadow: '0 0 26px 3px rgba(232,255,71,0.55)',
              flex: 'none',
            }}
          />
          <div style={{fontFamily: SANS, fontWeight: 500, color: CREAM, fontSize: 44, letterSpacing: '0.005em'}}>
            {caption}
          </div>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// ---------- Beat 7 : end card ----------
const B7: React.FC<{dur: number}> = ({dur}) => {
  const {f, opacity} = useBeat(dur, 20, 18);
  const rise = interpolate(f, [0, 22], [18, 0], {extrapolateRight: 'clamp', easing: ease});
  const tagOp = interpolate(f, [16, 36], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: ease});
  const pillOp = interpolate(f, [30, 50], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: ease});
  return (
    <Stage>
      <Glow y={40} />
      <AbsoluteFill style={{alignItems: 'center', justifyContent: 'center', flexDirection: 'column', textAlign: 'center', padding: 120, opacity}}>
        <div style={{fontFamily: SANS, fontWeight: 700, fontSize: 96, letterSpacing: '-0.01em', transform: `translateY(${rise}px)`}}>
          <span style={{color: CREAM}}>Launch</span>
          <span style={{color: LIME}}>Free</span>
          <span style={{color: '#6C7686', fontWeight: 400, fontSize: 60}}>.io</span>
        </div>
        <div style={{fontFamily: SERIF, fontStyle: 'italic', color: CREAM, fontSize: 62, marginTop: 30, opacity: tagOp}}>
          put yours on the runway.
        </div>
        <div style={{fontFamily: SANS, fontWeight: 500, color: '#7C8698', fontSize: 40, marginTop: 54, letterSpacing: '0.05em', opacity: pillOp}}>
          search LaunchFree
        </div>
      </AbsoluteFill>
    </Stage>
  );
};

const FontGate: React.FC = () => {
  const [h] = useState(() => delayRender('fonts'));
  useEffect(() => {
    let done = false;
    // @ts-ignore
    document.fonts.ready.then(() => {
      if (!done) {
        done = true;
        continueRender(h);
      }
    });
    const t = setTimeout(() => {
      if (!done) {
        done = true;
        continueRender(h);
      }
    }, 3000);
    return () => clearTimeout(t);
  }, [h]);
  return null;
};

// Beat durations (frames @30fps), timed to the voiceover lines (24.6s VO
// distributed by line length) plus a hold on the end card after the VO ends.
const D = [98, 123, 135, 49, 159, 159, 144];

export const OriginStory: React.FC = () => {
  let at = 0;
  const seq = (dur: number, node: React.ReactNode) => {
    const el = (
      <Sequence key={at} from={at} durationInFrames={dur}>
        {node}
      </Sequence>
    );
    at += dur;
    return el;
  };
  return (
    <AbsoluteFill style={{backgroundColor: INK}}>
      <FontGate />
      <Audio src={staticFile('vo.mp3')} />
      {seq(D[0], <B1 dur={D[0]} />)}
      {seq(D[1], <B2 dur={D[1]} />)}
      {seq(D[2], <B3 dur={D[2]} />)}
      {seq(D[3], <Hero dur={D[3]} src="hero-shot.png" caption="launchfree.io" alt="LaunchFree homepage" />)}
      {seq(D[4], <Hero dur={D[4]} src="directory-shot.png" caption="520 launches. $0 to list." alt="The Runway directory" />)}
      {seq(D[5], <Hero dur={D[5]} src="listing-shot.png" caption="a permanent page + a real backlink" alt="A live listing page" />)}
      {seq(D[6], <B7 dur={D[6]} />)}
    </AbsoluteFill>
  );
};

export const ORIGIN_DURATION = 98 + 123 + 135 + 49 + 159 + 159 + 144;
