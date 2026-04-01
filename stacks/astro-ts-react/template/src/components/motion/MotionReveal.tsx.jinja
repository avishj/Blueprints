import React, { type ReactNode, useEffect, useRef } from "react";
import gsap from "gsap";
import { ensureFocusableVisibility } from "@lib/motion/a11y";
import { createDisposer, killTimeline } from "@lib/motion/cleanup";
import { createInViewObserver } from "@lib/motion/in-view";
import { motionPresets, type MotionPresetName } from "@lib/motion/presets";
import { shouldAnimate } from "@lib/motion/reduced-motion";
import { createMotionTimeline } from "@lib/motion/timeline";

interface MotionRevealProps {
  children: ReactNode;
  className?: string;
  once?: boolean;
  preset?: MotionPresetName;
}

export default function MotionReveal({
  children,
  className,
  once = true,
  preset = "slideUp",
}: MotionRevealProps) {
  const ref = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    const element = ref.current;

    if (!element) {
      return;
    }

    const disposer = createDisposer();
    const activePreset = motionPresets[preset];
    const { duration, ease, ...toTarget } = activePreset.to;

    if (!shouldAnimate()) {
      gsap.set(element, toTarget);
      ensureFocusableVisibility(element);
      return;
    }

    gsap.set(element, activePreset.from);

    const observer = createInViewObserver(
      (target) => {
        const timeline = createMotionTimeline({
          paused: false,
          defaults: { duration, ease },
        });

        timeline.to(target, {
          ...toTarget,
          duration,
          ease,
        });
        timeline.eventCallback("onComplete", () => {
          ensureFocusableVisibility(element);
        });

        disposer.add(() => {
          killTimeline(timeline);
        });
      },
      { once },
    );

    observer.observe(element);
    disposer.add(() => observer.disconnect());

    return () => {
      disposer.flush();
    };
  }, [once, preset]);

  return (
    <div ref={ref} className={className}>
      {children}
    </div>
  );
}
