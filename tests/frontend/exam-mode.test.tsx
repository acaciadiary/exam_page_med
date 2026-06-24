import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it, vi } from "vitest";
import { QuestionCard } from "../../src/features/exam/QuestionCard";
import type { ExamQuestion } from "../../src/types/exam";

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
