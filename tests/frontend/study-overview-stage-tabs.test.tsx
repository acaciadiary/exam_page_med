import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";
import {
  StudyOverviewPage,
  type ExamProgressStat,
  type StudyOverviewSummary,
} from "../../src/features/progress/StudyOverviewPage";
import { storageKeys } from "../../src/lib/storageKeys";
import type { ExamManifestItem } from "../../src/types/exam";

function exam(subject: string, questionCount: number): ExamManifestItem {
  return {
    id: `114-1_${subject}`,
    year: "114-1",
    title: `114-1 ${subject}`,
    subject,
    path: `data/exams/114-1/${subject}.json`,
    question_count: questionCount,
  };
}

function stat(subject: string, total: number, answered: number): ExamProgressStat {
  return {
    exam: exam(subject, total),
    total,
    answered,
    correct: Math.floor(answered / 2),
    wrong: answered - Math.floor(answered / 2),
    accuracy: answered === 0 ? 0 : 50,
    completion: total === 0 ? 0 : Math.round((answered / total) * 100),
  };
}

const summary: StudyOverviewSummary = {
  totalAnswered: 80,
  totalQuestions: 360,
  totalCorrect: 40,
  totalWrong: 40,
  accuracy: 50,
  completion: 22,
  completedExamCount: 0,
  wrongQuestionCount: 2,
  activeWrongQuestionCount: 2,
  favoriteCount: 1,
  masteredMistakeCount: 0,
};

function renderPage() {
  return render(
    <StudyOverviewPage
      summary={summary}
      examStats={[
        stat("medicine-1", 100, 20),
        stat("medicine-2", 100, 0),
        stat("medicine-3", 80, 30),
        stat("medicine-4", 80, 30),
      ]}
      categoryStats={[]}
      continueTitle="從第 1 題繼續"
      continueDescription="繼續上一題"
      canContinue
      onContinuePractice={vi.fn()}
      onOpenExam={vi.fn()}
      onGoMistakes={vi.fn()}
      onGoFavorites={vi.fn()}
    />,
  );
}

describe("StudyOverviewPage stage tabs", () => {
  beforeEach(() => {
    window.localStorage.clear();
  });

  it("separates first-stage and second-stage progress into tabs", () => {
    renderPage();

    expect(screen.getByText("一階作答")).toBeInTheDocument();
    expect(screen.getByText("20")).toBeInTheDocument();
    expect(screen.queryByText("二階作答")).not.toBeInTheDocument();

    fireEvent.click(screen.getByRole("button", { name: /二階/ }));

    expect(screen.getByText("二階作答")).toBeInTheDocument();
    expect(screen.getByText("60")).toBeInTheDocument();

    fireEvent.click(screen.getByRole("button", { name: /一階/ }));

    expect(screen.getByText("一階作答")).toBeInTheDocument();
  });

  it("remembers the selected stage after returning to the progress overview", async () => {
    const firstRender = renderPage();

    fireEvent.click(screen.getByRole("button", { name: /二階/ }));

    await waitFor(() => {
      expect(window.localStorage.getItem(storageKeys.progressStage)).toBe(
        JSON.stringify("stage-2"),
      );
    });

    firstRender.unmount();
    renderPage();

    expect(screen.getByText("二階作答")).toBeInTheDocument();
    expect(screen.getByText("60")).toBeInTheDocument();
  });

  it("keeps compact status filters available inside the selected stage", () => {
    renderPage();

    expect(screen.getByRole("button", { name: "全部狀態" })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "有未寫" })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "寫到一半" })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "已完成" })).toBeInTheDocument();
  });
});
