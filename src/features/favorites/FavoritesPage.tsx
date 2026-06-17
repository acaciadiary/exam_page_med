import { ArrowRight, BookmarkCheck } from "lucide-react";
import { EmptyState } from "../../components/EmptyState";
import { getStageLabel, getSubjectLabel, getExamStage } from "../../lib/examMetadata";
import { compactText } from "../../lib/text";
import type { ExamManifestItem, ExamQuestion } from "../../types/exam";

export type FavoriteEntry = {
  exam: ExamManifestItem;
  question: ExamQuestion;
  source: "question" | "flashcard" | "both";
};

type FavoritesPageProps = {
  favorites: FavoriteEntry[];
  loading: boolean;
  onOpenQuestion: (examId: string, questionId: string) => void;
};

export function FavoritesPage({
  favorites,
  loading,
  onOpenQuestion,
}: FavoritesPageProps) {
  return (
    <section className="space-y-6">
      <div className="rounded-[1.5rem] border border-white/80 bg-white/80 p-6 shadow-[0_18px_60px_rgba(181,133,117,0.16)] backdrop-blur-2xl">
        <p className="text-sm font-semibold tracking-[0.12em] text-[#b36a84]">
          我的收藏
        </p>
        <h2 className="mt-3 text-3xl font-semibold text-[#3f342d]">
          全部收藏題目
        </h2>
        <div className="mt-4 inline-flex rounded-full bg-[#fff1f6] px-4 py-2 text-sm font-semibold text-[#9a496b]">
          目前共 {favorites.length} 題收藏
        </div>
      </div>

      {loading ? (
        <div className="rounded-[1.1rem] border border-dashed border-[#eacfc4] bg-white/52 px-6 py-10 text-center text-sm font-semibold text-[#8a7066]">
          正在整理收藏...
        </div>
      ) : favorites.length === 0 ? (
        <EmptyState
          title="目前還沒有收藏"
          description="在題目或背卡按下書籤後，收藏會集中顯示在這裡。"
        />
      ) : (
        <div className="grid gap-4">
          {favorites.map(({ exam, question, source }) => (
            <article
              key={`${exam.id}-${question.id}`}
              className="rounded-[1.2rem] border border-white/80 bg-white/82 p-5 shadow-[0_14px_44px_rgba(181,133,117,0.13)] backdrop-blur-2xl"
            >
              <div className="flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between">
                <div className="min-w-0">
                  <p className="flex flex-wrap items-center gap-2 text-sm font-semibold text-[#c4869b]">
                    <BookmarkCheck size={16} />
                    <span>
                      {exam.year}・{getStageLabel(getExamStage(exam))}・
                      {getSubjectLabel(exam)}・第 {question.question_number} 題
                    </span>
                    <span className="rounded-full bg-[#f8eee8] px-2 py-0.5 text-xs text-[#7d6259]">
                      {getSourceLabel(source)}
                    </span>
                  </p>
                  <h3 className="mt-2 text-base font-semibold leading-8 text-[#3f342d]">
                    {compactText(question.question_text, 150)}
                  </h3>
                </div>

                <button
                  type="button"
                  onClick={() => onOpenQuestion(exam.id, question.id)}
                  className="inline-flex shrink-0 items-center gap-2 rounded-full border border-[#efd9d0] bg-white px-4 py-2 text-sm font-semibold text-[#6f5b50] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b]"
                >
                  回到題目
                  <ArrowRight size={16} />
                </button>
              </div>
            </article>
          ))}
        </div>
      )}
    </section>
  );
}

function getSourceLabel(source: FavoriteEntry["source"]) {
  if (source === "both") return "題目與背卡";
  return source === "question" ? "題目" : "背卡";
}
