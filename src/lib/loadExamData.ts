import type { ExamDataset, ExamManifest } from "../types/exam";

function publicPath(path: string) {
  const base = import.meta.env.BASE_URL || "/";
  const cleanBase = base.endsWith("/") ? base : `${base}/`;
  const cleanPath = path.replace(/^\//, "");
  return `${cleanBase}${cleanPath}`;
}

async function loadJson<T>(path: string): Promise<T> {
  const response = await fetch(publicPath(path));
  if (!response.ok) {
    throw new Error(`Unable to load ${path}: ${response.status}`);
  }
  return response.json() as Promise<T>;
}

export async function loadManifest() {
  return loadJson<ExamManifest>("data/manifest.json");
}

const examDataCache: Record<string, ExamDataset> = {};

export async function loadExamData(path: string) {
  if (examDataCache[path]) {
    return examDataCache[path];
  }
  const data = await loadJson<ExamDataset>(path);
  examDataCache[path] = data;
  return data;
}

