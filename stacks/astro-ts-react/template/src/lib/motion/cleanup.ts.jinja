export type DisposeFn = () => void;

export function createDisposer() {
  const disposers: DisposeFn[] = [];

  return {
    add(disposer: DisposeFn): void {
      disposers.push(disposer);
    },
    flush(): void {
      while (disposers.length > 0) {
        const disposer = disposers.pop();
        if (!disposer) {
          continue;
        }

        disposer();
      }
    },
  };
}

export interface TimelineLike {
  kill: () => void;
}

export function killTimeline(timeline: TimelineLike | null | undefined): void {
  if (!timeline) {
    return;
  }

  timeline.kill();
}
