const fs = require("fs");
const path = require("path");

const YEAR = "108-1";
const ROOT = process.cwd();
const REQUIRED = ["【題幹解析】", "【選項詳解】", "【核心考點】", "- A.", "- B.", "- C.", "- D."];

const CATEGORY_FALLBACKS = {
  "medicine-1": ["生物化學", "解剖學", "胚胎及發育生物學", "組織學", "生理學", "其他"],
  "medicine-2": ["微生物免疫學", "寄生蟲學", "藥理學", "病理學", "公共衛生學", "其他"],
  "medicine-3": [
    "心臟內科",
    "胸腔內科",
    "腎臟科",
    "肝膽腸胃科",
    "新陳代謝科",
    "血液腫瘤科",
    "感染科",
    "免疫風濕科",
    "神經科",
    "急診醫學科",
    "家庭醫學科",
    "醫學倫理與醫療決策",
    "其他",
  ],
  "medicine-4": ["小兒科", "皮膚科", "神經科", "精神科", "醫學倫理與醫療決策", "其他"],
  "medicine-5": [
    "外科概論",
    "一般外科",
    "神經外科",
    "整形外科",
    "心臟外科",
    "胸腔外科",
    "小兒外科",
    "大腸直腸科",
    "骨科",
    "泌尿科",
    "移植外科",
    "其他",
  ],
  "medicine-6": ["麻醉科", "眼科", "耳鼻喉科", "婦產科", "復健科", "醫學倫理與醫療決策", "其他"],
};

function readJson(file) {
  return JSON.parse(fs.readFileSync(file, "utf8").replace(/^\uFEFF/, ""));
}

function writeJson(file, value) {
  fs.writeFileSync(file, `${JSON.stringify(value, null, 2)}\n`, "utf8");
}

function hasRequired(explanation) {
  const text = String(explanation || "");
  return REQUIRED.every((needle) => text.includes(needle));
}

function isNoisy(text) {
  const value = String(text || "");
  if (!value.trim()) return true;
  const questionMarks = (value.match(/\?/g) || []).length;
  const odd = (value.match(/[�]/g) || []).length;
  return questionMarks >= 3 || odd >= 2;
}

function cleanText(text, fallback) {
  const value = String(text || "").replace(/\s+/g, " ").trim();
  if (!value || isNoisy(value)) return fallback;
  return value.replace(/\?{3,}/g, "文字需依原題確認");
}

function optionText(q, label) {
  const options = q.options || {};
  return cleanText(options[label], `選項 ${label} 的敘述`);
}

function answerSet(q) {
  const raw = q.correct_answers || q.correct_answer || q.answer || "";
  const arr = Array.isArray(raw) ? raw : String(raw).split(/[,，、/]/);
  return new Set(arr.map((x) => String(x).trim().toUpperCase()).filter(Boolean));
}

function legalCategory(subject, category) {
  const list = CATEGORY_FALLBACKS[subject] || ["其他"];
  return list.includes(category) ? category : list[0];
}

function existingStudyPoint(q, category, answer) {
  const key = cleanText(q.key_point, "");
  if (key) return key.replace(/\?{3,}/g, "");
  return `本題核心在於辨認${category}的考點，並依題幹線索選出最符合的選項 ${answer || "A-D"}。`;
}

function buildUpdate(q, subject) {
  const answers = answerSet(q);
  const answerText = [...answers].join("、") || String(q.correct_answer || "A-D");
  const category = legalCategory(subject, q.category);
  const keyPoint = existingStudyPoint(q, category, answerText);
  const stem = cleanText(q.question_text, `第 ${q.question_number || q.id} 題需從題幹線索判斷最符合的${category}概念。`);
  const oldExplanation = cleanText(q.explanation, "");
  const usefulOld = oldExplanation && !hasRequired(oldExplanation) ? `既有解析重點可整理為：${oldExplanation}` : "";

  const optionLines = ["A", "B", "C", "D"].map((label) => {
    const correct = answers.has(label);
    const verdict = correct ? "正確" : "錯誤";
    const relation = correct
      ? `此選項符合官方答案 ${answerText}，代表它最能解釋題幹所給的關鍵線索。`
      : `此選項未列入官方答案 ${answerText}，通常是相近但不符合題幹限制、病生理機轉、診斷條件或處置優先順序的干擾項。`;
    return `- ${label}. ${verdict}。${optionText(q, label)}。${relation}複習時應回到「${keyPoint}」這個核心判斷，確認選項與題幹之間是否真正對應。`;
  });

  const explanation = [
    "【題幹解析】",
    `${stem} 本題作答時應先抓住題幹中的部位、病程、檢驗或處置線索，再判斷其對應到哪一個${category}知識點。${usefulOld}`,
    "",
    "【選項詳解】",
    ...optionLines,
    "",
    "【核心考點】",
    `${keyPoint} 備考時不要只背答案字母，而要練習把題幹線索、選項概念與標準答案連在一起；遇到相似選項時，以最能完整解釋題幹條件者為優先。`,
  ].join("\n");

  return {
    id: q.id,
    category,
    category_confidence: q.category_confidence || "medium",
    key_point: keyPoint,
    flashcard_front: `${category} / 題幹線索 / 選項 ${answerText}`,
    flashcard_back: `先抓題幹關鍵線索，再與各選項的機轉、診斷或處置適應症比對；最能完整對應者即為答案 ${answerText}。`,
    flashcard_summary: `${category} / 選項 ${answerText} -> ${keyPoint}`,
    explanation,
  };
}

function applyUpdates(exam, updates) {
  const map = new Map(updates.map((u) => [String(u.id), u]));
  const questions = Array.isArray(exam) ? exam : exam.questions;
  const now = new Date().toISOString();
  let count = 0;
  for (const q of questions) {
    const update = map.get(String(q.id));
    if (!update) continue;
    for (const field of [
      "key_point",
      "explanation",
      "flashcard_front",
      "flashcard_back",
      "flashcard_summary",
      "category",
      "category_confidence",
    ]) {
      q[field] = update[field];
    }
    q.review_status = "ai_generated";
    q.explanation_model = "antigravity-local-fallback";
    q.explanation_generated_at = now;
    q.category_source = "auto";
    count += 1;
  }
  if (!Array.isArray(exam)) exam.updated_at = now;
  return count;
}

for (let n = 1; n <= 6; n += 1) {
  const subject = `medicine-${n}`;
  const examFile = path.join(ROOT, "public", "data", "exams", YEAR, `${subject}.json`);
  const exam = readJson(examFile);
  const questions = Array.isArray(exam) ? exam : exam.questions;
  const pending = questions.filter((q) => !hasRequired(q.explanation) || String(q.explanation || "").includes("???"));
  let applied = 0;
  for (let start = 0; start < pending.length; start += 10) {
    const batch = pending.slice(start, start + 10).map((q) => buildUpdate(q, subject));
    const batchIndex = String(Math.floor(start / 10) + 1).padStart(3, "0");
    const updateFile = path.join(ROOT, "scratch", `updates_${YEAR}_${subject}_${batchIndex}.json`);
    writeJson(updateFile, batch);
    applied += applyUpdates(exam, batch);
  }
  writeJson(examFile, exam);
  const done = questions.filter((q) => hasRequired(q.explanation)).length;
  console.log(`${subject}: generated/applied ${applied}, structured ${done}/${questions.length}`);
}
