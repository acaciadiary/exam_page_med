import type { ExamDataset, ExamQuestion } from "../types/exam";

export const ALL_CATEGORIES = "__all__";
export const UNCATEGORIZED = "__uncategorized__";

export type CategoryOption = {
  id: string;
  label: string;
  count: number;
  disabled?: boolean;
};

type CategoryRange = {
  start: number;
  end: number;
  category: string;
};

const CATEGORY_TEMPLATES: Record<string, string[]> = {
  "medicine-1": [
    "解剖學",
    "胚胎及發育生物學",
    "組織學",
    "生理學",
    "生物化學",
    "其他",
  ],
  "medicine-2": [
    "微生物免疫學",
    "寄生蟲學",
    "公共衛生學",
    "藥理學",
    "病理學",
    "其他",
  ],
  "medicine-3": [
    "家庭醫學科",
    "心臟內科",
    "胸腔內科",
    "肝膽腸胃科",
    "腎臟科",
    "免疫風濕科",
    "血液腫瘤科",
    "新陳代謝科",
    "感染科",
    "急診醫學科",
    "神經內科",
    "醫學倫理與醫療決策",
    "其他",
  ],
  "medicine-4": [
    "小兒科",
    "皮膚科",
    "神經科",
    "精神科",
    "醫學倫理與醫療決策",
    "其他",
  ],
  "medicine-5": [
    "外科概論",
    "一般外科",
    "移植外科",
    "神經外科",
    "整形外科",
    "心臟外科",
    "胸腔外科",
    "小兒外科",
    "大腸直腸科",
    "骨科",
    "泌尿科",
    "其他",
  ],
  "medicine-6": [
    "麻醉科",
    "眼科",
    "耳鼻喉科",
    "婦產科",
    "復健科",
    "醫學倫理與醫療決策",
    "其他",
  ],
};

const FALLBACK_CATEGORY_RANGES: Record<string, CategoryRange[]> = {
  "medicine-1": [
    { start: 1, end: 16, category: "解剖學" },
    { start: 17, end: 17, category: "生理學" },
    { start: 18, end: 31, category: "解剖學" },
    { start: 32, end: 34, category: "胚胎及發育生物學" },
    { start: 35, end: 35, category: "生理學" },
    { start: 36, end: 36, category: "胚胎及發育生物學" },
    { start: 37, end: 47, category: "組織學" },
    { start: 48, end: 48, category: "生理學" },
    { start: 49, end: 49, category: "解剖學" },
    { start: 50, end: 50, category: "生理學" },
    { start: 51, end: 51, category: "組織學" },
    { start: 52, end: 56, category: "生理學" },
    { start: 57, end: 57, category: "生物化學" },
    { start: 58, end: 72, category: "生理學" },
    { start: 73, end: 73, category: "胚胎及發育生物學" },
    { start: 74, end: 100, category: "生物化學" },
  ],
  "medicine-2": [
    { start: 1, end: 28, category: "微生物免疫學" },
    { start: 29, end: 35, category: "寄生蟲學" },
    { start: 36, end: 50, category: "公共衛生學" },
    { start: 51, end: 75, category: "藥理學" },
    { start: 76, end: 100, category: "病理學" },
  ],
  "medicine-3": [
    { start: 1, end: 3, category: "家庭醫學科" },
    { start: 4, end: 4, category: "心臟內科" },
    { start: 5, end: 5, category: "家庭醫學科" },
    { start: 6, end: 7, category: "心臟內科" },
    { start: 8, end: 8, category: "胸腔內科" },
    { start: 9, end: 14, category: "心臟內科" },
    { start: 15, end: 23, category: "肝膽腸胃科" },
    { start: 24, end: 30, category: "腎臟科" },
    { start: 31, end: 35, category: "免疫風濕科" },
    { start: 36, end: 41, category: "血液腫瘤科" },
    { start: 42, end: 42, category: "胸腔內科" },
    { start: 43, end: 44, category: "血液腫瘤科" },
    { start: 45, end: 49, category: "胸腔內科" },
    { start: 50, end: 50, category: "血液腫瘤科" },
    { start: 51, end: 51, category: "胸腔內科" },
    { start: 52, end: 58, category: "新陳代謝科" },
    { start: 59, end: 65, category: "感染科" },
    { start: 66, end: 66, category: "家庭醫學科" },
    { start: 67, end: 67, category: "新陳代謝科" },
    { start: 68, end: 68, category: "感染科" },
    { start: 69, end: 69, category: "家庭醫學科" },
    { start: 70, end: 70, category: "醫學倫理與醫療決策" },
    { start: 71, end: 71, category: "其他" },
    { start: 72, end: 72, category: "家庭醫學科" },
    { start: 73, end: 73, category: "醫學倫理與醫療決策" },
    { start: 74, end: 74, category: "其他" },
    { start: 75, end: 75, category: "肝膽腸胃科" },
    { start: 76, end: 76, category: "急診醫學科" },
    { start: 77, end: 77, category: "感染科" },
    { start: 78, end: 78, category: "神經內科" },
    { start: 79, end: 80, category: "醫學倫理與醫療決策" },
  ],
  "medicine-4": [
    { start: 1, end: 28, category: "小兒科" },
    { start: 29, end: 29, category: "精神科" },
    { start: 30, end: 30, category: "小兒科" },
    { start: 31, end: 31, category: "神經科" },
    { start: 32, end: 32, category: "小兒科" },
    { start: 33, end: 33, category: "神經科" },
    { start: 34, end: 43, category: "皮膚科" },
    { start: 44, end: 58, category: "神經科" },
    { start: 59, end: 73, category: "精神科" },
    { start: 74, end: 74, category: "小兒科" },
    { start: 75, end: 77, category: "神經科" },
    { start: 78, end: 78, category: "精神科" },
    { start: 79, end: 80, category: "醫學倫理與醫療決策" },
  ],
  "medicine-5": [
    { start: 1, end: 1, category: "小兒外科" },
    { start: 2, end: 2, category: "整形外科" },
    { start: 3, end: 4, category: "心臟外科" },
    { start: 5, end: 7, category: "胸腔外科" },
    { start: 8, end: 14, category: "一般外科" },
    { start: 15, end: 16, category: "大腸直腸科" },
    { start: 17, end: 19, category: "一般外科" },
    { start: 20, end: 22, category: "外科概論" },
    { start: 23, end: 23, category: "移植外科" },
    { start: 24, end: 25, category: "外科概論" },
    { start: 26, end: 31, category: "神經外科" },
    { start: 32, end: 35, category: "整形外科" },
    { start: 36, end: 38, category: "心臟外科" },
    { start: 39, end: 39, category: "胸腔外科" },
    { start: 40, end: 40, category: "泌尿科" },
    { start: 41, end: 41, category: "胸腔外科" },
    { start: 42, end: 48, category: "一般外科" },
    { start: 49, end: 53, category: "小兒外科" },
    { start: 54, end: 54, category: "大腸直腸科" },
    { start: 55, end: 55, category: "一般外科" },
    { start: 56, end: 59, category: "骨科" },
    { start: 60, end: 60, category: "泌尿科" },
    { start: 61, end: 61, category: "骨科" },
    { start: 62, end: 62, category: "整形外科" },
    { start: 63, end: 63, category: "骨科" },
    { start: 64, end: 71, category: "泌尿科" },
    { start: 72, end: 72, category: "一般外科" },
    { start: 73, end: 73, category: "其他" },
    { start: 74, end: 74, category: "骨科" },
    { start: 75, end: 75, category: "泌尿科" },
    { start: 76, end: 76, category: "骨科" },
    { start: 77, end: 77, category: "整形外科" },
    { start: 78, end: 78, category: "其他" },
    { start: 79, end: 79, category: "移植外科" },
    { start: 80, end: 80, category: "其他" },
  ],
  "medicine-6": [
    { start: 1, end: 9, category: "麻醉科" },
    { start: 10, end: 18, category: "眼科" },
    { start: 19, end: 27, category: "耳鼻喉科" },
    { start: 28, end: 57, category: "婦產科" },
    { start: 58, end: 71, category: "復健科" },
    { start: 72, end: 72, category: "耳鼻喉科" },
    { start: 73, end: 74, category: "婦產科" },
    { start: 75, end: 76, category: "麻醉科" },
    { start: 77, end: 77, category: "耳鼻喉科" },
    { start: 78, end: 80, category: "醫學倫理與醫療決策" },
  ],
};

export function getCategoryTemplates(subject: string) {
  return CATEGORY_TEMPLATES[subject] ?? [];
}

export function getQuestionCategory(question: ExamQuestion) {
  return question.category?.trim() || UNCATEGORIZED;
}

export function getDerivedQuestionCategory(
  dataset: ExamDataset,
  question: ExamQuestion,
) {
  const currentCategory = getQuestionCategory(question);

  if (shouldUseFallbackCategories(dataset)) {
    return getFallbackCategory(dataset.subject, question.question_number) ?? currentCategory;
  }

  if (!canUseFallbackCategories(dataset) || !isWeakCategory(dataset, currentCategory)) {
    return currentCategory;
  }

  return getFallbackCategory(dataset.subject, question.question_number) ?? currentCategory;
}

export function buildCategoryOptions(dataset: ExamDataset): CategoryOption[] {
  const counts = new Map<string, number>();

  for (const question of dataset.questions) {
    const category = getDerivedQuestionCategory(dataset, question);
    counts.set(category, (counts.get(category) ?? 0) + 1);
  }

  const templateOptions = getCategoryTemplates(dataset.subject).map((label) => ({
    id: label,
    label,
    count: counts.get(label) ?? 0,
    disabled: false,
  }));

  const extraOptions = Array.from(counts.entries())
    .filter(([category]) => category !== UNCATEGORIZED)
    .filter(([category]) => !templateOptions.some((option) => option.id === category))
    .sort(([a], [b]) => a.localeCompare(b, "zh-Hant"))
    .map(([category, count]) => ({
      id: category,
      label: category,
      count,
    }));

  const uncategorizedCount = counts.get(UNCATEGORIZED) ?? 0;

  return [
    {
      id: ALL_CATEGORIES,
      label: "全部",
      count: dataset.questions.length,
    },
    ...templateOptions,
    ...extraOptions,
    ...(uncategorizedCount > 0
      ? [
          {
            id: UNCATEGORIZED,
            label: "未分類",
            count: uncategorizedCount,
          },
        ]
      : []),
  ];
}

export function filterQuestionsByCategory(
  dataset: ExamDataset,
  activeCategory: string,
) {
  if (activeCategory === ALL_CATEGORIES) return dataset.questions;

  return dataset.questions.filter(
    (question) => getDerivedQuestionCategory(dataset, question) === activeCategory,
  );
}

function shouldUseFallbackCategories(dataset: ExamDataset) {
  if (!canUseFallbackCategories(dataset)) return false;

  const weakCategoryCount = dataset.questions.filter((question) =>
    isWeakCategory(dataset, getQuestionCategory(question)),
  ).length;

  return weakCategoryCount / dataset.questions.length >= 0.25;
}

function canUseFallbackCategories(dataset: ExamDataset) {
  return Boolean(FALLBACK_CATEGORY_RANGES[dataset.subject]) && dataset.questions.length >= 20;
}

function isWeakCategory(dataset: ExamDataset, category: string) {
  return (
    category === UNCATEGORIZED ||
    category === "其他" ||
    isUnexpectedCategory(dataset.subject, category)
  );
}

function isUnexpectedCategory(subject: string, category: string) {
  const templates = getCategoryTemplates(subject);
  return templates.length > 0 && !templates.includes(category);
}

function getFallbackCategory(subject: string, questionNumber: number) {
  return FALLBACK_CATEGORY_RANGES[subject]?.find(
    (range) => questionNumber >= range.start && questionNumber <= range.end,
  )?.category;
}
