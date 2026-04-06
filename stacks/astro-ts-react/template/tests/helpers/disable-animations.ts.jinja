export function disableAnimations(): () => void {
  let style: HTMLStyleElement | null = null;

  if (typeof document !== "undefined") {
    style = document.createElement("style");
    style.setAttribute("data-test-disable-animations", "true");
    style.textContent = `
      *,
      *::before,
      *::after {
        animation: none !important;
        transition: none !important;
      }
      html {
        scroll-behavior: auto !important;
      }
    `;
    document.head.appendChild(style);
  }

  return () => {
    style?.remove();
  };
}
