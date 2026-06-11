import { describe, expect, it } from "vitest";
import {
  ALL_CATEGORIES,
  UNCATEGORIZED,
  buildCategoryOptions,
  filterQuestionsByCategory,
  getCategoryTemplates,
} from "../../src/lib/categoryFilters";
import type { ExamDataset } from "../../src/types/exam";

const dataset: ExamDataset = {
  id: "115_medicine-3",
  year: "115",
  title: "醫學（三）",
  subject: "medicine-3",
  source: "fixture",
  updated_at: "2026-06-10T00:00:00Z",
  questions: [
    {
      id: "q1",
      question_number: 1,
      question_text: "心臟內科題目",
      options: { A: "A", B: "B", C: "C", D: "D" },
      correct_answer: "A",
      explanation: "",
      flashcard_summary: "",
      category: "心臟內科",
    },
    {
      id: "q2",
      question_number: 2,
      question_text: "尚未分類題目",
      options: { A: "A", B: "B", C: "C", D: "D" },
      correct_answer: "B",
      explanation: "",
      flashcard_summary: "",
    },
  ],
};

describe("category filters", () => {
  it("keeps the official subject button templates", () => {
    expect(getCategoryTemplates("medicine-1")).toEqual([
      "生物化學",
      "解剖學",
      "胚胎及發育生物學",
      "組織學",
      "生理學",
      "其他",
    ]);
    expect(getCategoryTemplates("medicine-2")).toEqual([
      "微生物免疫學",
      "寄生蟲學",
      "藥理學",
      "病理學",
      "公共衛生學",
      "其他",
    ]);
    expect(getCategoryTemplates("medicine-3")).toEqual([
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
    ]);
    expect(getCategoryTemplates("medicine-4")).toEqual([
      "小兒科",
      "皮膚科",
      "神經科",
      "精神科",
      "醫學倫理與醫療決策",
      "其他",
    ]);
    expect(getCategoryTemplates("medicine-5")).toEqual([
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
    ]);
    expect(getCategoryTemplates("medicine-6")).toEqual([
      "麻醉科",
      "眼科",
      "耳鼻喉科",
      "婦產科",
      "復健科",
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
    expect(options.find((option) => option.id === "胸腔內科")).toMatchObject({
      count: 0,
      disabled: false,
    });
    expect(options.find((option) => option.id === UNCATEGORIZED)).toMatchObject({
      label: "未分類",
      count: 1,
    });
  });

  it("filters questions by assigned category", () => {
    expect(filterQuestionsByCategory(dataset.questions, "心臟內科")).toHaveLength(1);
    expect(filterQuestionsByCategory(dataset.questions, UNCATEGORIZED)).toHaveLength(1);
    expect(filterQuestionsByCategory(dataset.questions, ALL_CATEGORIES)).toHaveLength(2);
  });
});
