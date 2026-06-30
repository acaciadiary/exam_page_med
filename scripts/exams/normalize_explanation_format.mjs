import fs from "node:fs";
import path from "node:path";

const DATA_DIR = path.join("public", "data", "exams");
const HEADINGS = ["【題幹解析】", "【選項詳解】", "【核心考點】"];
const OPTION_LABELS = ["A", "B", "C", "D"];

function walkJsonFiles(dir) {
  const files = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      files.push(...walkJsonFiles(fullPath));
    } else if (entry.isFile() && entry.name.endsWith(".json")) {
      files.push(fullPath);
    }
  }
  return files.sort();
}

function readJson(filePath) {
  const text = fs.readFileSync(filePath, "utf8").replace(/^\uFEFF/, "");
  return JSON.parse(text);
}

function writeJson(filePath, data) {
  fs.writeFileSync(filePath, `${JSON.stringify(data, null, 2)}\n`, "utf8");
}

function cleanText(value) {
  return String(value ?? "")
    .replace(/\r\n?/g, "\n")
    .replace(/[ \t]+/g, " ")
    .replace(/\n{3,}/g, "\n\n")
    .trim();
}

function hasCompleteFormat(explanation) {
  return HEADINGS.every((heading) => explanation.includes(heading));
}

function correctAnswers(question) {
  const answers = Array.isArray(question.correct_answers) && question.correct_answers.length
    ? question.correct_answers
    : [question.correct_answer];
  return new Set(
    answers
      .map((answer) => String(answer ?? "").trim().toUpperCase())
      .filter(Boolean),
  );
}

function answerText(question) {
  const answers = [...correctAnswers(question)];
  return answers.length ? answers.join("、") : "未標示";
}

function optionLine(question, label) {
  const option = cleanText(question.options?.[label]) || "原始選項文字未提供。";
  const answers = correctAnswers(question);
  const isCorrect = answers.has(label);
  const verdict = isCorrect ? "正確答案" : "非本題答案";
  const reason = isCorrect
    ? "此選項最符合題幹線索與標準答案。"
    : `此選項不是本題標準答案；作答時應回到題幹關鍵線索，並與正解 ${answerText(question)} 比較。`;
  return `- ${label}. ${verdict}。選項內容：「${option}」${reason}`;
}

function buildStructuredExplanation(question) {
  const oldExplanation = cleanText(question.explanation);
  const questionText = cleanText(question.question_text) || "題幹文字未提供。";
  const keyPoint = cleanText(question.key_point) || "本題核心在於依題幹線索判斷正確選項。";
  const answer = answerText(question);
  const optionLines = OPTION_LABELS.map((label) => optionLine(question, label)).join("\n");
  const originalNote = oldExplanation
    ? `\n\n原本詳解重點：${oldExplanation}`
    : "";

  return [
    "【題幹解析】",
    `本題題幹為：「${questionText}」`,
    `標準答案為 ${answer}。解題時先抓住題幹中的臨床線索、檢查數值或關鍵概念，再判斷哪個選項最符合題意。${originalNote}`,
    "",
    "【選項詳解】",
    optionLines,
    "",
    "【核心考點】",
    `${keyPoint} 複習時不要只背答案，應同時確認正確選項成立的理由，以及其他選項為何不符合題幹條件。`,
  ].join("\n");
}

function main() {
  const now = new Date().toISOString();
  const report = [];
  let totalUpdated = 0;

  for (const filePath of walkJsonFiles(DATA_DIR)) {
    const dataset = readJson(filePath);
    let updated = 0;

    for (const question of dataset.questions ?? []) {
      const explanation = cleanText(question.explanation);
      if (!explanation || hasCompleteFormat(explanation)) {
        continue;
      }

      question.explanation = buildStructuredExplanation(question);
      question.review_status = question.review_status || "ai_generated";
      question.explanation_model = `${question.explanation_model || "existing-explanation"}+structured-v2`;
      question.explanation_generated_at = now;
      updated += 1;
    }

    if (updated > 0) {
      dataset.updated_at = now;
      writeJson(filePath, dataset);
      report.push({ path: filePath, dataset_id: dataset.id, updated });
      totalUpdated += updated;
    }
  }

  console.log(JSON.stringify({ updated: totalUpdated, datasets: report }, null, 2));
}

main();
