const fs = require("node:fs");
const path = require("node:path");

const root = process.cwd();

function readJson(relativePath) {
  return JSON.parse(fs.readFileSync(path.join(root, relativePath), "utf8").replace(/^\uFEFF/, ""));
}

const manifest = readJson("public/data/manifest.json");
const questionIds = new Set();

for (const exam of manifest.exams) {
  const dataset = readJson(path.join("public", exam.path));
  for (const question of dataset.questions) {
    questionIds.add(question.id);
  }
}

const files = [
  "public/data/instant_kill_facts.json",
  "public/data/medical_glossary.json",
  "public/data/clinical_guidelines.json",
  "public/data/disease_comparisons.json",
  "reports/must_know_candidate_priorities.json",
];

for (const file of files) {
  readJson(file);
}

function validateRelated(items, label) {
  const missing = [];
  for (const item of items) {
    for (const related of item.related_questions || []) {
      if (!questionIds.has(related.question_id)) {
        missing.push(`${label}:${item.id}->${related.question_id}`);
      }
    }
  }
  return missing;
}

const instantKill = readJson("public/data/instant_kill_facts.json");
const glossary = readJson("public/data/medical_glossary.json");
const guidelines = readJson("public/data/clinical_guidelines.json");
const comparisons = readJson("public/data/disease_comparisons.json");

const missingFactIds = instantKill.facts.filter((fact) => !questionIds.has(fact.id)).map((fact) => fact.id);
const missingRelated = [
  ...validateRelated(glossary.terms, "glossary"),
  ...validateRelated(guidelines.guidelines, "guideline"),
  ...validateRelated(comparisons.comparison_groups, "comparison"),
];

if (missingFactIds.length > 0 || missingRelated.length > 0) {
  console.error(JSON.stringify({ missingFactIds, missingRelated }, null, 2));
  process.exit(1);
}

console.log(JSON.stringify({
  ok: true,
  question_count: questionIds.size,
  instant_kill_facts: instantKill.facts.length,
  glossary_terms: glossary.terms.length,
  guidelines: guidelines.guidelines.length,
  comparison_groups: comparisons.comparison_groups.length,
}, null, 2));
