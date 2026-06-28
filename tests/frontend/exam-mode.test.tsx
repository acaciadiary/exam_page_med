import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it, vi } from "vitest";
import { ExamMode } from "../../src/features/exam/ExamMode";
import { QuestionCard } from "../../src/features/exam/QuestionCard";
import type { ExamDataset, ExamQuestion } from "../../src/types/exam";

vi.mock("../../src/lib/loadExamData", () => ({
  loadDiseaseComparisons: vi.fn().mockResolvedValue({ comparison_groups: [] }),
}));

const question: ExamQuestion = {
  id: "q1",
  question_number: 1,
  question_text: "高鈉血症處理，下列何者最適當？",
  options: {
    A: "估算全身水體積",
    B: "計算 free water deficit",
    C: "不易感知水分流失",
    D: "血鈉矯正速度",
  },
  correct_answer: "B",
  explanation: "此題重點為 free water deficit 的計算。",
  flashcard_summary: "高鈉血症 -> free water deficit",
};

describe("QuestionCard", () => {
  it("shows answer feedback and explanation after choosing an option", async () => {
    const user = userEvent.setup();
    const onAnswer = vi.fn();

    render(
      <QuestionCard
        question={question}
        marked={false}
        selected={undefined}
        onAnswer={onAnswer}
        onToggleMarked={() => undefined}
      />,
    );

    await user.click(screen.getByRole("button", { name: /free water/i }));

    expect(onAnswer).toHaveBeenCalledWith("B");
  });

  it("renders explanation when selected", () => {
    render(
      <QuestionCard
        question={question}
        marked={false}
        selected="B"
        onAnswer={() => undefined}
        onToggleMarked={() => undefined}
      />,
    );

    expect(screen.getByText("答對了")).toBeInTheDocument();
    expect(screen.getByText("此題重點為 free water deficit 的計算。")).toBeInTheDocument();
  });
});

describe("ExamMode", () => {
  it("loads and focuses a target question beyond the first page", async () => {
    const scrollTo = vi.fn();
    Object.defineProperty(window, "scrollTo", {
      configurable: true,
      value: scrollTo,
    });

    const questions: ExamQuestion[] = Array.from({ length: 20 }, (_, index) => ({
      id: `q${index + 1}`,
      question_number: index + 1,
      question_text: `第 ${index + 1} 題測試題目`,
      options: {
        A: "選項 A",
        B: "選項 B",
        C: "選項 C",
        D: "選項 D",
      },
      correct_answer: "A",
      explanation: "解析",
      flashcard_summary: "摘要",
    }));

    const dataset: ExamDataset = {
      id: "exam-a",
      year: "115-1",
      title: "測試考卷",
      subject: "medicine-6",
      source: "test",
      updated_at: "2026-06-24",
      questions,
    };
    const onFocusComplete = vi.fn();

    render(
      <ExamMode
        dataset={dataset}
        answers={{}}
        markedQuestions={{
          marked: [],
          markedSet: new Set<string>(),
          toggleMarked: vi.fn(),
          clearMarked: vi.fn(),
          removeMarked: vi.fn(),
        }}
        onAnswer={vi.fn()}
        mode="exam"
        onModeChange={vi.fn()}
        theme="light"
        focusQuestionId="q17"
        onFocusComplete={onFocusComplete}
      />,
    );

    await waitFor(() => {
      expect(screen.getByText("第 17 題測試題目")).toBeInTheDocument();
    });
    await waitFor(() => {
      expect(scrollTo).toHaveBeenCalled();
      expect(onFocusComplete).toHaveBeenCalledWith("q17");
    });
  });
});
