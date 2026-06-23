import { describe, expect, it } from "vitest";
import {
  ALL_CATEGORIES,
  UNCATEGORIZED,
  buildCategoryOptions,
  filterQuestionsByCategory,
  getCategoryTemplates,
} from "../../src/lib/categoryFilters";
import type { ExamDataset, ExamQuestion } from "../../src/types/exam";

function makeQuestion(
  questionNumber: number,
  category?: string,
): ExamQuestion {
  return {
    id: `q${questionNumber}`,
    question_number: questionNumber,
    question_text: `題目 ${questionNumber}`,
    options: { A: "A", B: "B", C: "C", D: "D" },
    correct_answer: "A",
    explanation: "",
    flashcard_summary: "",
    category,
  };
}

const dataset: ExamDataset = {
  id: "115_medicine-3",
  year: "115",
  title: "醫學（三）",
  subject: "medicine-3",
  source: "fixture",
  updated_at: "2026-06-10T00:00:00Z",
  questions: [makeQuestion(1, "心臟內科"), makeQuestion(2)],
};

describe("category filters", () => {
  it("keeps the official subject button templates", () => {
    expect(getCategoryTemplates("medicine-1")).toEqual([
      "解剖學",
      "胚胎及發育生物學",
      "組織學",
      "生理學",
      "生物化學",
      "其他",
    ]);
    expect(getCategoryTemplates("medicine-4")).toEqual([
      "小兒科",
      "皮膚科",
      "神經科",
      "精神科",
      "醫學倫理與醫療決策",
      "其他",
    ]);
  });

  it("builds template options with counts and uncategorized questions", () => {
    const options = buildCategoryOptions(dataset);

    expect(options[0]).toMatchObject({
      id: ALL_CATEGORIES,
      label: "全部",
      count: 2,
    });
    expect(options.find((option) => option.id === "心臟內科")).toMatchObject({
      count: 1,
      disabled: false,
    });
    expect(options.find((option) => option.id === "家庭醫學科")).toMatchObject({
      count: 0,
      disabled: false,
    });
    expect(options.find((option) => option.id === UNCATEGORIZED)).toMatchObject({
      label: "未分類",
      count: 1,
    });
  });

  it("filters questions by assigned category", () => {
    expect(filterQuestionsByCategory(dataset, "心臟內科")).toHaveLength(1);
    expect(filterQuestionsByCategory(dataset, UNCATEGORIZED)).toHaveLength(1);
    expect(filterQuestionsByCategory(dataset, ALL_CATEGORIES)).toHaveLength(2);
  });

  it("uses fallback categories when a dataset is mostly marked as other", () => {
    const brokenDataset: ExamDataset = {
      ...dataset,
      id: "114-1_medicine-4",
      year: "114-1",
      subject: "medicine-4",
      questions: Array.from({ length: 80 }, (_, index) =>
        makeQuestion(index + 1, "其他"),
      ),
    };

    const options = buildCategoryOptions(brokenDataset);

    expect(options.find((option) => option.id === "小兒科")).toMatchObject({
      count: 31,
    });
    expect(options.find((option) => option.id === "皮膚科")).toMatchObject({
      count: 10,
    });
    expect(filterQuestionsByCategory(brokenDataset, "小兒科")).toHaveLength(31);
  });

  it("replaces wrong subject categories with fallback ranges", () => {
    const brokenDataset: ExamDataset = {
      ...dataset,
      id: "113-1_medicine-4",
      year: "113-1",
      subject: "medicine-4",
      questions: Array.from({ length: 80 }, (_, index) => {
        const questionNumber = index + 1;
        const badCategory = questionNumber <= 27 ? "內科" : "其他";
        return makeQuestion(questionNumber, badCategory);
      }),
    };

    const options = buildCategoryOptions(brokenDataset);

    expect(options.find((option) => option.id === "內科")).toBeUndefined();
    expect(options.find((option) => option.id === "小兒科")).toMatchObject({
      count: 31,
    });
    expect(options.find((option) => option.id === "醫學倫理與醫療決策")).toMatchObject({
      count: 2,
    });
  });
});
