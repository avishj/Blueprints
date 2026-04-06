import { motionTokens } from "@lib/motion/tokens";

const REDUCED_MOTION_QUERY = "(prefers-reduced-motion: reduce)";

export function prefersReducedMotion(): boolean {
  if (typeof window === "undefined" || typeof window.matchMedia !== "function") {
    return false;
  }

  return window.matchMedia(REDUCED_MOTION_QUERY).matches;
}

export function getMotionDuration(duration: number): number {
  return prefersReducedMotion() ? motionTokens.durations.instant : duration;
}

export function shouldAnimate(): boolean {
  return !prefersReducedMotion();
}
