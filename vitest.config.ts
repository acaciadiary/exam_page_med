import { defineConfig } from "vitest/config";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [react(), tailwindcss()],
  test: {
    include: ["tests/frontend/**/*.test.tsx"],
    environment: "jsdom",
    setupFiles: ["./tests/frontend/setup.ts"],
    css: true,
    exclude: [
      "**/node_modules/**",
      "**/dist/**",
      "**/.pytest_cache/**",
      "**/.chrome-cdp-profile*/**",
      "**/.npm-cache/**",
      "**/.tools/**",
      "**/.python-packages/**",
    ],
  },
});
