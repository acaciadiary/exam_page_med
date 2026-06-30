import fs from "node:fs";
import path from "node:path";

const DATA_DIR = path.join("public", "data");
const MANIFEST_PATH = path.join(DATA_DIR, "manifest.json");
const GLOSSARY_PATH = path.join(DATA_DIR, "medical_glossary.json");
const MAX_RELATED_QUESTIONS = 10;
const MIN_RELATED_QUESTIONS = 3;

const extraAliasesByTermId = {
  serotonin_syndrome: ["serotonin", "5-HT", "SSRI", "SNRI", "MAOI"],
  neuroleptic_malignant_syndrome: [
    "抗精神病藥惡性症候群",
    "惡性症候群",
  ],
  compartment_syndrome: [
    "compartment syndrome",
    "急性肌腔室症候群",
    "腔室症候群",
    "腹部腔室症候群",
    "腹腔腔室症候群",
    "abdominal compartment syndrome",
    "fasciotomy",
    "筋膜切開術",
    "被動伸展疼痛",
    "壓砸傷",
  ],
};

const requiredQuestionIdsByTermId = {
  neuroleptic_malignant_syndrome: [
    "115-1_medicine-4_064",
    "110-1_medicine-4_060",
    "108-2_medicine-4_059",
    "110-2_medicine-4_078",
    "110-1_medicine-2_072",
    "109-1_medicine-2_072",
    "111-2_medicine-2_072",
    "112-1_medicine-4_061",
  ],
  compartment_syndrome: [
    "115-1_medicine-5_076",
    "113-2_medicine-5_077",
    "113-1_medicine-5_003",
    "110-2_medicine-5_057",
    "110-2_medicine-5_075",
    "110-1_medicine-5_059",
    "109-1_medicine-5_005",
    "108-1_medicine-5_056",
  ],
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
  return /^[A-Za-z0-9][A-Za-z0-9+\-/_.'() ]*$/.test(alias);
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
  const cleaned = normalizeText(source)
    .replace(/^【[^】]+】/, "")
    .trim();
  const truncated = cleaned.length > 180 ? `${cleaned.slice(0, 180)}...` : cleaned;
  const aliasHint = matchedAliases.length > 0 ? `命中：${matchedAliases.join("、")}。` : "";
  return `${aliasHint}${truncated}`;
}

function scoreMatch(question, matchedAliases, searchText, isRequired) {
  let score = isRequired ? 100 : matchedAliases.length * 10;
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

function relatedQuestionsForTerm(term, indexedQuestions, questionById) {
  const aliases = [...(term.aliases ?? []), ...(extraAliasesByTermId[term.id] ?? [])];
  const seenAliases = [...new Set(aliases.map(normalizeText).filter((alias) => alias.length >= 3))];
  const requiredIds = new Set(requiredQuestionIdsByTermId[term.id] ?? []);

  const matchesById = new Map();
  for (const indexedQuestion of indexedQuestions) {
    const matchedAliases = seenAliases.filter((alias) => aliasMatches(indexedQuestion.searchText, alias));
    const isRequired = requiredIds.has(indexedQuestion.question.id);
    if (matchedAliases.length === 0 && !isRequired) continue;

    matchesById.set(indexedQuestion.question.id, {
      ...indexedQuestion,
      matchedAliases,
      score: scoreMatch(indexedQuestion.question, matchedAliases, indexedQuestion.searchText, isRequired),
    });
  }

  for (const questionId of requiredIds) {
    if (matchesById.has(questionId)) continue;
    const indexedQuestion = questionById.get(questionId);
    if (!indexedQuestion) continue;
    matchesById.set(questionId, {
      ...indexedQuestion,
      matchedAliases: [],
      score: scoreMatch(indexedQuestion.question, [], indexedQuestion.searchText, true),
    });
  }

  return [...matchesById.values()]
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
const questionById = new Map(indexedQuestions.map((item) => [item.question.id, item]));

const report = [];
for (const term of glossary.terms) {
  const existingCount = term.related_questions?.length ?? 0;
  const shouldRefresh =
    existingCount < MIN_RELATED_QUESTIONS ||
    Object.hasOwn(requiredQuestionIdsByTermId, term.id) ||
    Object.hasOwn(extraAliasesByTermId, term.id);

  if (!shouldRefresh) {
    report.push({ id: term.id, action: "kept", count: existingCount });
    continue;
  }

  const relatedQuestions = relatedQuestionsForTerm(term, indexedQuestions, questionById);
  term.related_questions = relatedQuestions;
  report.push({
    id: term.id,
    action: existingCount === 0 ? "filled" : "refreshed",
    before: existingCount,
    count: relatedQuestions.length,
  });
}

fs.writeFileSync(GLOSSARY_PATH, `${JSON.stringify(glossary, null, 2)}\n`, "utf8");

console.table(report);
