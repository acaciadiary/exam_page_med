const fs = require("node:fs");
const path = require("node:path");

const root = process.cwd();
function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf8").replace(/^\uFEFF/, ""));
}

const manifest = readJson(path.join(root, "public/data/manifest.json"));
const glossary = readJson(path.join(root, "public/data/medical_glossary.json"));

const existingGlossaryText = JSON.stringify(glossary).toLowerCase();

const keywordGroups = [
  {
    id: "aminoglycosides",
    type: "glossary",
    priority: 1,
    name: "胺基醣苷類抗生素",
    keywords: ["aminoglycoside", "aminoglycosides", "胺基醣苷", "gentamicin", "amikacin"],
  },
  {
    id: "sulfonamides",
    type: "glossary",
    priority: 1,
    name: "磺胺類藥物",
    keywords: ["sulfonamide", "sulfonamides", "磺胺", "PABA", "dihydropteroate"],
  },
  {
    id: "clostridioides_difficile_colitis",
    type: "glossary",
    priority: 1,
    name: "偽膜性腸炎 / C. difficile",
    keywords: ["C. difficile", "Clostridioides", "Clostridium difficile", "偽膜", "pseudomembranous"],
  },
  {
    id: "serotonin_syndrome",
    type: "glossary",
    priority: 1,
    name: "血清素症候群",
    keywords: ["serotonin syndrome", "血清素症候群", "serotonin", "SSRI", "MAOI"],
  },
  {
    id: "neuroleptic_malignant_syndrome",
    type: "glossary",
    priority: 1,
    name: "抗精神病藥惡性症候群",
    keywords: ["neuroleptic malignant", "NMS", "惡性症候群", "dantrolene", "抗精神病"],
  },
  {
    id: "tumor_lisis_syndrome",
    type: "glossary",
    priority: 1,
    name: "腫瘤溶解症候群",
    keywords: ["tumor lysis", "腫瘤溶解", "rasburicase", "allopurinol", "高尿酸"],
  },
  {
    id: "siadh",
    type: "glossary",
    priority: 1,
    name: "抗利尿激素分泌不當症候群",
    keywords: ["SIADH", "抗利尿激素", "hyponatremia", "低血鈉", "urine osmolality"],
  },
  {
    id: "diabetes_insipidus",
    type: "glossary",
    priority: 2,
    name: "尿崩症",
    keywords: ["diabetes insipidus", "尿崩", "desmopressin", "water deprivation"],
  },
  {
    id: "acute_stroke_window",
    type: "instant_kill",
    priority: 1,
    name: "急性缺血性中風 rt-PA 時窗與血壓",
    keywords: ["rt-PA", "tPA", "alteplase", "4.5", "185/110", "ischemic stroke", "缺血性中風"],
  },
  {
    id: "status_epilepticus_5min",
    type: "instant_kill",
    priority: 1,
    name: "癲癇重積 5 分鐘與第一線 BZD",
    keywords: ["status epilepticus", "5 分鐘", "5分鐘", "lorazepam", "diazepam", "midazolam"],
  },
  {
    id: "anaphylaxis_epinephrine",
    type: "instant_kill",
    priority: 1,
    name: "過敏性休克 epinephrine IM 劑量",
    keywords: ["anaphylaxis", "anaphylactic", "epinephrine", "0.3", "0.5", "過敏性休克"],
  },
  {
    id: "thyroid_cancer_age_cutoff",
    type: "instant_kill",
    priority: 1,
    name: "分化型甲狀腺癌 TNM 年齡切點",
    keywords: ["thyroid cancer", "甲狀腺癌", "TNM", "45", "55"],
  },
  {
    id: "insulinoma_90_percent",
    type: "instant_kill",
    priority: 2,
    name: "Insulinoma 90% rule",
    keywords: ["insulinoma", "Whipple", "90%", "胰島素瘤"],
  },
  {
    id: "er_positive_breast_ai",
    type: "guideline",
    priority: 2,
    name: "停經後 ER/PR+ 乳癌第一線內分泌治療",
    keywords: ["aromatase inhibitor", "tamoxifen", "ER", "PR", "乳癌", "HER-2"],
  },
  {
    id: "cbd_stone_ercp",
    type: "guideline",
    priority: 2,
    name: "總膽管結石處置：ERCP",
    keywords: ["CBD stone", "common bile duct", "ERCP", "總膽管結石", "膽管炎"],
  },
  {
    id: "ra_vs_oa",
    type: "comparison",
    priority: 3,
    name: "RA vs OA",
    keywords: ["rheumatoid arthritis", "osteoarthritis", "Heberden", "Bouchard", "morning stiffness"],
  },
  {
    id: "serotonin_vs_nms",
    type: "comparison",
    priority: 3,
    name: "血清素症候群 vs NMS",
    keywords: ["serotonin syndrome", "neuroleptic malignant", "clonus", "lead-pipe"],
  },
];

function haystack(question) {
  return [
    question.question_text,
    question.explanation,
    question.key_point,
    question.flashcard_summary,
    question.flashcard_front,
    question.flashcard_back,
    ...Object.values(question.options || {}),
  ]
    .filter(Boolean)
    .join("\n");
}

const questionIds = new Set();
const hits = new Map(keywordGroups.map((group) => [group.id, []]));

for (const exam of manifest.exams) {
  const dataset = readJson(path.join(root, "public", exam.path));
  for (const question of dataset.questions) {
    questionIds.add(question.id);
    const text = haystack(question);
    const lower = text.toLowerCase();
    for (const group of keywordGroups) {
      const matchedKeywords = group.keywords.filter((keyword) => lower.includes(keyword.toLowerCase()));
      if (matchedKeywords.length > 0) {
        hits.get(group.id).push({
          question_id: question.id,
          category: question.category || question.category_group || exam.subject,
          matched_keywords: [...new Set(matchedKeywords)],
          question_text: (question.question_text || "").replace(/\s+/g, " ").slice(0, 120),
          key_point: (question.key_point || question.flashcard_summary || "").replace(/\s+/g, " ").slice(0, 160),
        });
      }
    }
  }
}

const candidates = keywordGroups
  .map((group) => {
    const groupHits = hits.get(group.id);
    const inGlossary = group.type === "glossary" && group.keywords.some((keyword) => existingGlossaryText.includes(keyword.toLowerCase()));
    const uniqueHits = [];
    const seen = new Set();
    for (const hit of groupHits) {
      if (!seen.has(hit.question_id)) {
        uniqueHits.push(hit);
        seen.add(hit.question_id);
      }
    }
    return {
      ...group,
      hit_count: uniqueHits.length,
      already_in_glossary: inGlossary,
      selected_related_questions: uniqueHits.slice(0, 8),
    };
  })
  .sort((a, b) => a.priority - b.priority || b.hit_count - a.hit_count || a.name.localeCompare(b.name, "zh-Hant"));

const report = {
  generated_at: new Date().toISOString(),
  question_count: questionIds.size,
  candidate_count: candidates.length,
  candidates,
};

fs.writeFileSync(path.join(root, "reports/must_know_candidate_priorities.json"), `${JSON.stringify(report, null, 2)}\n`, "utf8");

for (const c of candidates) {
  console.log(`${c.priority}. [${c.type}] ${c.name} hits=${c.hit_count} existingGlossary=${c.already_in_glossary}`);
  for (const hit of c.selected_related_questions.slice(0, 3)) {
    console.log(`   - ${hit.question_id}: ${hit.question_text}`);
  }
}
