import type { ExamDataset, ExamManifest } from "../types/exam";
import type { DiseaseComparisonsData } from "../types/disease";

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

import type { InstantKillFactsData } from "../types/disease";

let diseaseComparisonsCache: DiseaseComparisonsData | null = null;
let instantKillFactsCache: InstantKillFactsData | null = null;

export async function loadDiseaseComparisons() {
  if (diseaseComparisonsCache) {
    return diseaseComparisonsCache;
  }
  const data = await loadJson<DiseaseComparisonsData>("data/disease_comparisons.json");
  diseaseComparisonsCache = data;
  return data;
}

export async function loadInstantKillFacts() {
  if (instantKillFactsCache) {
    return instantKillFactsCache;
  }
  const data = await loadJson<InstantKillFactsData>("data/instant_kill_facts.json");
  instantKillFactsCache = data;
  return data;
}


