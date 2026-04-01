import React, { type ReactNode, useEffect, useRef } from "react";
import gsap from "gsap";
import { createDisposer, killTimeline } from "@lib/motion/cleanup";
import { motionPresets } from "@lib/motion/presets";
import { shouldAnimate } from "@lib/motion/reduced-motion";
import { createMotionTimeline } from "@lib/motion/timeline";

interface MotionStaggerProps {
  children: ReactNode;
  className?: string;
  itemSelector?: string;
}

export default function MotionStagger({
  children,
  className,
  itemSelector = "[data-motion-item]",
}: MotionStaggerProps) {
  const ref = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    const container = ref.current;

    if (!container) {
      return;
    }

    const items = Array.from(container.querySelectorAll(itemSelector));
    if (items.length === 0) {
      return;
    }

    const preset = motionPresets.listStagger;
    const { duration, ease, stagger, ...toTarget } = preset.to;

    if (!shouldAnimate()) {
      gsap.set(items, toTarget);
      return;
    }

    gsap.set(items, preset.from);

    const disposer = createDisposer();
    const timeline = createMotionTimeline({
      paused: false,
      defaults: { duration, ease },
    });

    timeline.to(items, {
      ...toTarget,
      duration,
      ease,
      stagger,
    });

    disposer.add(() => killTimeline(timeline));

    return () => {
      disposer.flush();
    };
  }, [itemSelector]);

  return (
    <div ref={ref} className={className}>
      {children}
    </div>
  );
}
