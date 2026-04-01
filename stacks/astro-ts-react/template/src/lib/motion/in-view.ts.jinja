import { MOTION_SCROLL_REVEAL_ENABLED } from "@lib/motion/tokens";

export interface InViewOptions {
  threshold?: number;
  rootMargin?: string;
  once?: boolean;
}

export interface InViewHandle {
  observe: (element: Element) => void;
  disconnect: () => void;
}

export function createInViewObserver(
  callback: (element: Element) => void,
  options: InViewOptions = {},
): InViewHandle {
  if (!MOTION_SCROLL_REVEAL_ENABLED || typeof window === "undefined") {
    return {
      observe(element: Element): void {
        callback(element);
      },
      disconnect(): void {},
    };
  }

  const once = options.once ?? true;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) {
          return;
        }

        callback(entry.target);

        if (once) {
          observer.unobserve(entry.target);
        }
      });
    },
    {
      threshold: options.threshold ?? 0.2,
      rootMargin: options.rootMargin ?? "0px 0px -10% 0px",
    },
  );

  return {
    observe(element: Element): void {
      observer.observe(element);
    },
    disconnect(): void {
      observer.disconnect();
    },
  };
}
