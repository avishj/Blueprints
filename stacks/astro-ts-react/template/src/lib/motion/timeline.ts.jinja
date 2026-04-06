import gsap from "gsap";
import { motionTokens } from "@lib/motion/tokens";
import { getMotionDuration } from "@lib/motion/reduced-motion";

export interface TimelineFactoryOptions {
  paused?: boolean;
  defaults?: {
    duration?: number;
    ease?: string;
  };
}

export function createMotionTimeline(options: TimelineFactoryOptions = {}): gsap.core.Timeline {
  const baseDuration = options.defaults?.duration ?? motionTokens.durations.base;
  const duration = getMotionDuration(baseDuration);
  const ease = options.defaults?.ease ?? motionTokens.easings.standard;

  return gsap.timeline({
    paused: options.paused ?? true,
    defaults: {
      duration,
      ease,
    },
  });
}
