import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it, vi } from "vitest";
import { Flashcard } from "../../src/features/flashcards/Flashcard";
import type { ExamQuestion } from "../../src/types/exam";

const question: ExamQuestion = {
  id: "card1",
  question_number: 1,
  question_text: "Barking cough 與 stridor 最可能診斷？",
  options: {
    A: "Croup",
    B: "Asthma",
    C: "Pneumonia",
    D: "Tuberculosis",
  },
  correct_answer: "A",
  key_point: "Barking cough 與 stridor 要想到 croup。",
  explanation: "典型 croup 表現。",
  flashcard_front: "Barking cough + stridor",
  flashcard_back: "上呼吸道阻塞線索指向 croup。",
  flashcard_summary: "Barking cough + stridor -> Croup",
};

describe("Flashcard", () => {
  it("toggles marked flashcards independently", async () => {
    const user = userEvent.setup();
    const onToggleMarked = vi.fn();

    render(
      <Flashcard
        question={question}
        marked={false}
        onToggleMarked={onToggleMarked}
      />,
    );

    await user.click(screen.getByRole("button", { name: "收藏閃卡" }));

    expect(onToggleMarked).toHaveBeenCalledTimes(1);
  });

  it("renders front and back study content", () => {
    render(
      <Flashcard
        question={question}
        marked={false}
        onToggleMarked={() => undefined}
      />,
    );

    expect(screen.getByText("關鍵字 / 線索")).toBeInTheDocument();
    expect(screen.getByText(question.flashcard_front!)).toBeInTheDocument();
    expect(screen.getByText("知識點 / 判斷規則")).toBeInTheDocument();
    expect(screen.getByText(question.flashcard_back!)).toBeInTheDocument();
    expect(screen.queryByText(question.question_text)).not.toBeInTheDocument();
  });
});
