import type { ExamDataset, ExamQuestion } from "../types/exam";

export const ALL_CATEGORIES = "__all__";
export const UNCATEGORIZED = "__uncategorized__";

export type CategoryOption = {
  id: string;
  label: string;
  count: number;
  disabled?: boolean;
};

const CATEGORY_TEMPLATES: Record<string, string[]> = {
  "medicine-1": [
    "生物化學",
    "解剖學",
    "胚胎及發育生物學",
    "組織學",
    "生理學",
    "其他",
  ],
  "medicine-2": [
    "微生物免疫學",
    "寄生蟲學",
    "藥理學",
    "病理學",
    "公共衛生學",
    "其他",
  ],
  "medicine-3": [
    "心臟內科",
    "胸腔內科",
    "肝膽腸胃科",
    "腎臟科",
    "新陳代謝科",
    "血液腫瘤科",
    "免疫風濕科",
    "感染科",
    "神經內科",
    "家庭醫學科",
    "急診醫學科",
    "醫學倫理與醫療決策",
    "其他",
  ],
  "medicine-4": ["小兒科", "皮膚科", "神經科", "精神科", "醫學倫理與醫療決策", "其他"],
  "medicine-5": [
    "外科概論",
    "一般外科",
    "心臟外科",
    "胸腔外科",
    "大腸直腸科",
    "移植外科",
    "小兒外科",
    "整形外科",
    "神經外科",
    "骨科",
    "泌尿科",
    "其他",
  ],
  "medicine-6": ["麻醉科", "眼科", "耳鼻喉科", "婦產科", "復健科", "醫學倫理與醫療決策", "其他"],
};

export function getCategoryTemplates(subject: string) {
  return CATEGORY_TEMPLATES[subject] ?? [];
}

export function getQuestionCategory(question: ExamQuestion) {
  return question.category?.trim() || UNCATEGORIZED;
}

export function buildCategoryOptions(dataset: ExamDataset): CategoryOption[] {
  const counts = new Map<string, number>();

  for (const question of dataset.questions) {
    const category = getQuestionCategory(question);
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
  questions: ExamQuestion[],
  activeCategory: string,
) {
  if (activeCategory === ALL_CATEGORIES) return questions;
  return questions.filter((question) => getQuestionCategory(question) === activeCategory);
}
