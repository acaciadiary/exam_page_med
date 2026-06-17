import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";

function resolveBasePath() {
  if (process.env.VITE_BASE_PATH) {
    return process.env.VITE_BASE_PATH;
  }

  const repositoryName = process.env.GITHUB_REPOSITORY?.split("/")[1];
  if (repositoryName) {
    return `/${repositoryName}/`;
  }

  return "/";
}

export default defineConfig({
  base: resolveBasePath(),
  plugins: [react(), tailwindcss()],
});
