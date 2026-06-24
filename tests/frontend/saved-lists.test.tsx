import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it, vi } from "vitest";
import { FavoritesPage, type FavoriteEntry } from "../../src/features/favorites/FavoritesPage";
import {
  MistakeNotebookPage,
  type MistakeEntry,
} from "../../src/features/mistakes/MistakeNotebookPage";
import type { ExamManifestItem, ExamQuestion } from "../../src/types/exam";

const exam: ExamManifestItem = {
  id: "exam-a",
  year: "115-1",
  title: "醫學三",
  subject: "medicine-3",
  path: "/data/exam-a.json",
  question_count: 1,
};

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

describe("Saved list pages", () => {
  it("can remove a single mistake from the mistake notebook", async () => {
    const user = userEvent.setup();
    const onRemoveMistake = vi.fn();
    const mistakes: MistakeEntry[] = [
      {
        exam,
        question,
        selectedAnswer: "A",
        status: "first",
      },
    ];

    render(
      <MistakeNotebookPage
        mistakes={mistakes}
        loading={false}
        onOpenQuestion={vi.fn()}
        onClearMistakes={vi.fn()}
        onRemoveMistake={onRemoveMistake}
        onStartPractice={vi.fn()}
        onStatusChange={vi.fn()}
      />,
    );

    await user.click(screen.getByRole("button", { name: "從錯題本移除" }));

    expect(onRemoveMistake).toHaveBeenCalledWith("exam-a", "q1");
  });

  it("can remove a single favorite from the favorites page", async () => {
    const user = userEvent.setup();
    const onRemoveFavorite = vi.fn();
    const favorites: FavoriteEntry[] = [
      {
        exam,
        question,
        source: "both",
        tags: ["高頻"],
      },
    ];

    render(
      <FavoritesPage
        favorites={favorites}
        loading={false}
        onOpenQuestion={vi.fn()}
        onClearFavorites={vi.fn()}
        onRemoveFavorite={onRemoveFavorite}
        onToggleTag={vi.fn()}
      />,
    );

    await user.click(screen.getByRole("button", { name: "取消收藏" }));

    expect(onRemoveFavorite).toHaveBeenCalledWith("exam-a", "q1");
  });
});
