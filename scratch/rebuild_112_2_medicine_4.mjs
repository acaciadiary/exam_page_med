import fs from "fs";
import path from "path";

const datasetId = "112-2_medicine-4";
const year = "112-2";
const subject = "medicine-4";
const title = "112-2 醫學（四）";
const source =
  "https://wwwq.moex.gov.tw/exam/wHandExamQandA_File.ashx?c=302&code=112080&q=1&s=22&t=Q";
const promptDir = "reports/gemini_prompts";
const outputDir = "reports/gemini_outputs";
const scratchDir = "scratch";
const examPath = "public/data/exams/112-2/medicine-4.json";

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

function extractFirstJsonObject(text) {
  const datasetIndex = text.indexOf('"dataset_id"');
  if (datasetIndex < 0) throw new Error("Cannot find dataset_id in prompt");
  const start = text.lastIndexOf("{", datasetIndex);
  if (start < 0) throw new Error("Cannot find JSON object start in prompt");
  let depth = 0;
  let inString = false;
  let escaped = false;
  for (let i = start; i < text.length; i += 1) {
    const ch = text[i];
    if (inString) {
      if (escaped) {
        escaped = false;
      } else if (ch === "\\") {
        escaped = true;
      } else if (ch === '"') {
        inString = false;
      }
      continue;
    }
    if (ch === '"') inString = true;
    if (ch === "{") depth += 1;
    if (ch === "}") {
      depth -= 1;
      if (depth === 0) return JSON.parse(text.slice(start, i + 1));
    }
  }
  throw new Error("Unclosed JSON object in prompt");
}

function cleanText(value) {
  return String(value ?? "")
    .replace(/\s+/g, " ")
    .trim();
}

function answerLabel(item) {
  const answer = String(item.correct_answer ?? "").trim();
  return answer || "官方答案";
}

function buildOptionDetail(letter, optionText, item) {
  const correctSet = new Set(String(item.correct_answer ?? "").split(",").map((x) => x.trim()));
  const isCorrect =
    correctSet.has(letter) ||
    (Array.isArray(item.correct_answers) && item.correct_answers.includes(letter));
  const option = cleanText(optionText) || "選項文字不完整";
  if (isCorrect) {
    return `- ${letter}. ${option}。此為官方答案；可由題幹關鍵線索與核心考點判定，需優先掌握其典型表現、診斷或處置原則。`;
  }
  return `- ${letter}. ${option}。此選項屬重要鑑別或常見干擾項，但與題幹最關鍵線索不完全相符；作答時應回到年齡、病程、檢查結果與典型臨床特徵判斷。`;
}

function buildExplanation(question, item) {
  const base = cleanText(item.explanation);
  const options = question.options || {};
  return [
    "【題幹解析】",
    base ||
      `本題核心在辨識題幹線索並選出最符合官方答案 ${answerLabel(item)} 的診斷、檢查或處置。`,
    "",
    "【選項詳解】",
    ["A", "B", "C", "D"].map((letter) => buildOptionDetail(letter, options[letter], item)).join("\n"),
    "",
    "【核心考點】",
    cleanText(item.key_point) ||
      `看到類似題幹時，先抓住關鍵臨床線索，再排除相近但不符合病程或檢查表現的選項。`,
  ].join("\n");
}

const questions = [];
for (let batch = 1; batch <= 6; batch += 1) {
  const promptPath = path.join(
    promptDir,
    `${datasetId}_batch-${String(batch).padStart(3, "0")}.md`,
  );
  const payload = extractFirstJsonObject(fs.readFileSync(promptPath, "utf8"));
  questions.push(...payload.questions);
}

const outputItems = [];
for (let batch = 1; batch <= 6; batch += 1) {
  const outputPath = path.join(
    outputDir,
    `${datasetId}_batch-${String(batch).padStart(3, "0")}.json`,
  );
  outputItems.push(...readJson(outputPath).items);
}

const outputById = new Map(outputItems.map((item) => [item.question_id, item]));

const allUpdates = questions.map((question) => {
  const item = outputById.get(question.question_id);
  if (!item) throw new Error(`Missing output for ${question.question_id}`);
  return {
    question_id: question.question_id,
    id: question.question_id,
    question_number: question.question_number,
    correct_answer: item.correct_answer,
    category: item.category || "其他",
    category_confidence: item.category_confidence || "medium",
    key_point: cleanText(item.key_point),
    explanation: buildExplanation(question, item),
    flashcard_front: cleanText(item.flashcard_front),
    flashcard_back: cleanText(item.flashcard_back),
    flashcard_summary: cleanText(item.flashcard_summary),
  };
});

for (let i = 0; i < allUpdates.length; i += 10) {
  const batchIndex = i / 10 + 1;
  const batchUpdates = allUpdates.slice(i, i + 10);
  fs.writeFileSync(
    path.join(scratchDir, `updates_112-2_medicine-4_${batchIndex}.json`),
    `${JSON.stringify(batchUpdates, null, 2)}\n`,
    "utf8",
  );
}

const updateById = new Map(allUpdates.map((item) => [item.question_id, item]));
const now = new Date().toISOString();
const rebuiltQuestions = questions.map((question) => {
  const update = updateById.get(question.question_id);
  const correctAnswers = String(question.correct_answer || update.correct_answer)
    .split(",")
    .map((part) => part.trim())
    .filter(Boolean);
  return {
    id: question.question_id,
    question_number: question.question_number,
    question_text: question.question_text,
    options: question.options || {},
    correct_answer: question.correct_answer,
    explanation: update.explanation,
    key_point: update.key_point,
    flashcard_summary: update.flashcard_summary,
    review_status: "ai_generated",
    correct_answers: correctAnswers,
    answer_status: correctAnswers.length > 1 ? "multiple_correct" : "standard",
    answer_source: "official_correction",
    flashcard_front: update.flashcard_front,
    flashcard_back: update.flashcard_back,
    category_group: "醫學（四）",
    category: update.category,
    category_confidence: update.category_confidence,
    category_source: "auto",
    explanation_model: "medical_explainer",
    explanation_generated_at: now,
  };
});

const exam = {
  id: datasetId,
  year,
  title,
  subject,
  source,
  updated_at: now,
  questions: rebuiltQuestions,
};

fs.writeFileSync(examPath, `${JSON.stringify(exam, null, 2)}\n`, "utf8");
console.log(
  JSON.stringify(
    {
      updates: allUpdates.length,
      batches: Math.ceil(allUpdates.length / 10),
      examPath,
      categories: [...new Set(allUpdates.map((item) => item.category))].sort(),
    },
    null,
    2,
  ),
);
