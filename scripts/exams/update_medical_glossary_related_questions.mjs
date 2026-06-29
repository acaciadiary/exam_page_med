import fs from "node:fs";
import path from "node:path";

const DATA_DIR = path.join("public", "data");
const MANIFEST_PATH = path.join(DATA_DIR, "manifest.json");
const GLOSSARY_PATH = path.join(DATA_DIR, "medical_glossary.json");
const MAX_RELATED_QUESTIONS = 10;

const extraAliasesByTermId = {
  serotonin_syndrome: ["serotonin", "血清素", "5-HT", "SSRI", "SNRI", "MAOI"],
};

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf8").replace(/^\uFEFF/, ""));
}

function normalizeText(value) {
  return String(value ?? "")
    .replace(/\s+/g, " ")
    .trim();
}

function questionSearchText(question) {
  const optionText = question.options ? Object.values(question.options) : [];
  return [
    question.question_text,
    question.key_point,
    question.explanation,
    question.flashcard_summary,
    question.flashcard_front,
    question.flashcard_back,
    ...optionText,
  ]
    .filter(Boolean)
    .join("\n");
}

function isAsciiKeyword(alias) {
  return /^[A-Za-z0-9][A-Za-z0-9+\-/_]*$/.test(alias);
}

function aliasMatches(text, alias) {
  const cleanAlias = normalizeText(alias);
  if (cleanAlias.length < 3) return false;

  if (isAsciiKeyword(cleanAlias)) {
    const escaped = cleanAlias.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    return new RegExp(`(?<![A-Za-z0-9])${escaped}(?![A-Za-z0-9])`, "i").test(text);
  }

  return text.toLowerCase().includes(cleanAlias.toLowerCase());
}

function buildNote(question, matchedAliases) {
  const source =
    question.key_point ||
    question.flashcard_summary ||
    question.explanation ||
    question.question_text ||
    "";
  const cleaned = normalizeText(source).replace(/^【[^】]+】/, "").trim();
  const truncated = cleaned.length > 180 ? `${cleaned.slice(0, 180)}...` : cleaned;
  const aliasHint = matchedAliases.length > 0 ? `命中：${matchedAliases.join("、")}。` : "";
  return `${aliasHint}${truncated}`;
}

function scoreMatch(question, matchedAliases, searchText) {
  let score = matchedAliases.length * 10;
  const primaryText = normalizeText([
    question.question_text,
    question.key_point,
    question.flashcard_summary,
    question.flashcard_front,
  ].join("\n")).toLowerCase();

  for (const alias of matchedAliases) {
    const cleanAlias = normalizeText(alias).toLowerCase();
    if (primaryText.includes(cleanAlias)) score += 6;
  }

  if (question.correct_answer) score += 1;
  if (searchText.length > 0) score += 1;
  return score;
}

function loadQuestions(manifest) {
  return manifest.exams.flatMap((exam, examIndex) => {
    const dataset = readJson(path.join("public", exam.path));
    return dataset.questions.map((question, questionIndex) => ({
      examIndex,
      questionIndex,
      question,
      searchText: questionSearchText(question),
    }));
  });
}

function relatedQuestionsForTerm(term, indexedQuestions) {
  const aliases = [...(term.aliases ?? []), ...(extraAliasesByTermId[term.id] ?? [])];
  const seenAliases = [...new Set(aliases.map(normalizeText).filter((alias) => alias.length >= 3))];

  const matches = [];
  for (const indexedQuestion of indexedQuestions) {
    const matchedAliases = seenAliases.filter((alias) => aliasMatches(indexedQuestion.searchText, alias));
    if (matchedAliases.length === 0) continue;

    matches.push({
      ...indexedQuestion,
      matchedAliases,
      score: scoreMatch(indexedQuestion.question, matchedAliases, indexedQuestion.searchText),
    });
  }

  return matches
    .sort((a, b) => {
      if (b.score !== a.score) return b.score - a.score;
      if (a.examIndex !== b.examIndex) return a.examIndex - b.examIndex;
      return a.questionIndex - b.questionIndex;
    })
    .slice(0, MAX_RELATED_QUESTIONS)
    .map((match) => ({
      question_id: match.question.id,
      note: buildNote(match.question, match.matchedAliases),
    }));
}

const manifest = readJson(MANIFEST_PATH);
const glossary = readJson(GLOSSARY_PATH);
const indexedQuestions = loadQuestions(manifest);

const report = [];
for (const term of glossary.terms) {
  const existingCount = term.related_questions?.length ?? 0;
  if (existingCount > 0) {
    report.push({ id: term.id, action: "kept", count: existingCount });
    continue;
  }

  const relatedQuestions = relatedQuestionsForTerm(term, indexedQuestions);
  term.related_questions = relatedQuestions;
  report.push({ id: term.id, action: "filled", count: relatedQuestions.length });
}

fs.writeFileSync(GLOSSARY_PATH, `${JSON.stringify(glossary, null, 2)}\n`, "utf8");

console.table(report);
