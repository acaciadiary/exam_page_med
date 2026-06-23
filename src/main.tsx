import React from "react";
import ReactDOM from "react-dom/client";
import App from "./app/App";
import "./styles/index.css";

type BeforeInstallPromptEvent = Event & {
  prompt: () => Promise<void>;
  userChoice: Promise<{ outcome: "accepted" | "dismissed"; platform: string }>;
};

if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register(`${import.meta.env.BASE_URL}sw.js`).catch(() => {
      // The app still works normally if the browser blocks service workers.
    });
  });
}

function setupInstallPrompt() {
  const dismissedKey = "exam-page-med-install-dismissed";
  const standaloneNavigator = navigator as Navigator & { standalone?: boolean };
  const isStandalone =
    window.matchMedia("(display-mode: standalone)").matches ||
    Boolean(standaloneNavigator.standalone);

  if (isStandalone || window.localStorage.getItem(dismissedKey) === "true") {
    return;
  }

  let installEvent: BeforeInstallPromptEvent | null = null;
  let banner: HTMLDivElement | null = null;

  const removeBanner = () => {
    banner?.remove();
    banner = null;
  };

  const dismissBanner = () => {
    window.localStorage.setItem(dismissedKey, "true");
    removeBanner();
  };

  const showBanner = (variant: "prompt" | "ios") => {
    if (banner) return;

    banner = document.createElement("div");
    banner.className = "install-prompt";
    banner.innerHTML = `
      <div class="install-prompt__text">
        <strong>安裝到手機桌面</strong>
        <span>${
          variant === "prompt"
            ? "下次可以像 App 一樣直接打開。"
            : "在 Safari 點分享按鈕，再選「加入主畫面」。"
        }</span>
      </div>
      <div class="install-prompt__actions">
        ${
          variant === "prompt"
            ? '<button type="button" class="install-prompt__primary">安裝</button>'
            : ""
        }
        <button type="button" class="install-prompt__dismiss" aria-label="關閉">×</button>
      </div>
    `;

    banner
      .querySelector(".install-prompt__primary")
      ?.addEventListener("click", async () => {
        if (!installEvent) return;
        await installEvent.prompt();
        await installEvent.userChoice.catch(() => undefined);
        dismissBanner();
      });

    banner
      .querySelector(".install-prompt__dismiss")
      ?.addEventListener("click", dismissBanner);

    document.body.appendChild(banner);
  };

  window.addEventListener("beforeinstallprompt", (event) => {
    event.preventDefault();
    installEvent = event as BeforeInstallPromptEvent;
    showBanner("prompt");
  });

  const isIos =
    /iPad|iPhone|iPod/.test(navigator.userAgent) ||
    (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1);

  if (isIos) {
    window.setTimeout(() => showBanner("ios"), 1200);
  }
}

setupInstallPrompt();

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);
