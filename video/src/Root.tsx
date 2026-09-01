import React from 'react';
import {Composition} from 'remotion';
import {OriginStory, ORIGIN_DURATION} from './OriginStory';

export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="OriginStory"
      component={OriginStory}
      durationInFrames={ORIGIN_DURATION}
      fps={30}
      width={1080}
      height={1920}
    />
  );
};
