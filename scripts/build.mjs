import { spawnSync } from "node:child_process";
import { resolve } from "node:path";

function run(scriptPath, args) {
  const result = spawnSync(process.execPath, [resolve(scriptPath), ...args], {
    stdio: "inherit",
  });

  if (result.status !== 0) {
    process.exit(result.status ?? 1);
  }
}

run("node_modules/typescript/bin/tsc", ["-b"]);
run("node_modules/vite/bin/vite.js", ["build"]);
