import { ArrowRight, BookmarkCheck, Trash2 } from "lucide-react";
import clsx from "clsx";
import { useMemo, useState, type ReactNode } from "react";
import { EmptyState } from "../../components/EmptyState";
import { getExamDisplayTitle } from "../../lib/examMetadata";
import { compactText } from "../../lib/text";
import type { ExamManifestItem, ExamQuestion } from "../../types/exam";

export type FavoriteTag = "高頻" | "易混淆" | "考前必看" | "秒殺數字";

export type FavoriteEntry = {
  exam: ExamManifestItem;
  question: ExamQuestion;
  source: "question" | "flashcard" | "both";
  tags: FavoriteTag[];
};

type FavoritesPageProps = {
  favorites: FavoriteEntry[];
  loading: boolean;
  onOpenQuestion: (examId: string, questionId: string) => void;
  onClearFavorites: () => void;
  onRemoveFavorite: (examId: string, questionId: string) => void;
  onToggleTag: (examId: string, questionId: string, tag: FavoriteTag) => void;
};

const allTag = "全部";
const favoriteTagOptions: FavoriteTag[] = ["高頻", "易混淆", "考前必看", "秒殺數字"];

export function FavoritesPage({
  favorites,
  loading,
  onOpenQuestion,
  onClearFavorites,
  onRemoveFavorite,
  onToggleTag,
}: FavoritesPageProps) {
  const [activeTag, setActiveTag] = useState<FavoriteTag | typeof allTag>(allTag);
  const filteredFavorites = useMemo(
    () =>
      activeTag === allTag
        ? favorites
        : favorites.filter((favorite) => favorite.tags.includes(activeTag)),
    [activeTag, favorites],
  );

  return (
    <section className="space-y-6">
      <div className="rounded-[1.5rem] border border-white/80 bg-white/80 p-6 shadow-[0_18px_60px_rgba(181,133,117,0.16)] backdrop-blur-2xl">
        <div className="flex flex-col gap-4 lg:flex-row lg:items-start lg:justify-between">
          <div>
            <p className="text-sm font-semibold tracking-[0.12em] text-[#b36a84]">收藏</p>
            <h2 className="mt-3 text-3xl font-semibold text-[#3f342d]">收藏國考題</h2>
            <div className="mt-4 inline-flex rounded-full bg-[#fff1f6] px-4 py-2 text-sm font-semibold text-[#9a496b]">
              目前 {favorites.length} 題
            </div>
            <div className="mt-4 flex flex-wrap gap-2">
              <FavoriteTagFilterButton active={activeTag === allTag} onClick={() => setActiveTag(allTag)}>
                全部
              </FavoriteTagFilterButton>
              {favoriteTagOptions.map((tag) => (
                <FavoriteTagFilterButton key={tag} active={activeTag === tag} onClick={() => setActiveTag(tag)}>
                  {tag}
                </FavoriteTagFilterButton>
              ))}
            </div>
          </div>

          <button
            type="button"
            onClick={onClearFavorites}
            disabled={loading || favorites.length === 0}
            className="inline-flex h-11 items-center justify-center gap-2 rounded-full border border-[#efd9d0] bg-white px-4 text-sm font-semibold text-[#6f5b50] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b] disabled:cursor-not-allowed disabled:opacity-50"
          >
            <Trash2 size={16} />
            清空收藏
          </button>
        </div>
      </div>

      {loading ? (
        <div className="rounded-[1.1rem] border border-dashed border-[#eacfc4] bg-white/52 px-6 py-10 text-center text-sm font-semibold text-[#8a7066]">
          正在整理收藏...
        </div>
      ) : favorites.length === 0 ? (
        <EmptyState title="目前沒有收藏" description="在題目或卡片中按下收藏，會出現在這裡。" />
      ) : filteredFavorites.length === 0 ? (
        <EmptyState title={`沒有「${activeTag}」收藏`} description="可以替收藏題加上不同標籤。" />
      ) : (
        <div className="grid gap-4">
          {filteredFavorites.map(({ exam, question, source, tags }) => (
            <article
              key={`${exam.id}-${question.id}`}
              className="rounded-[1.2rem] border border-white/80 bg-white/82 p-5 shadow-[0_14px_44px_rgba(181,133,117,0.13)] backdrop-blur-2xl"
            >
              <div className="flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between">
                <div className="min-w-0">
                  <p className="flex flex-wrap items-center gap-2 text-sm font-semibold text-[#c4869b]">
                    <BookmarkCheck size={16} />
                    <span>{getExamDisplayTitle(exam)} · 第 {question.question_number} 題</span>
                    <span className="rounded-full bg-[#f8eee8] px-2 py-0.5 text-xs text-[#7d6259]">
                      {getSourceLabel(source)}
                    </span>
                  </p>
                  <h3 className="mt-2 text-base font-semibold leading-8 text-[#3f342d]">
                    {compactText(question.question_text, 150)}
                  </h3>
                </div>

                <div className="flex shrink-0 flex-wrap gap-2 sm:justify-end">
                  <button
                    type="button"
                    onClick={() => onRemoveFavorite(exam.id, question.id)}
                    className="inline-flex items-center gap-2 rounded-full border border-[#efd9d0] bg-white px-4 py-2 text-sm font-semibold text-[#6f5b50] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b]"
                  >
                    <Trash2 size={16} />
                    取消收藏
                  </button>

                  <button
                    type="button"
                    onClick={() => onOpenQuestion(exam.id, question.id)}
                    className="inline-flex items-center gap-2 rounded-full border border-[#efd9d0] bg-white px-4 py-2 text-sm font-semibold text-[#6f5b50] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b]"
                  >
                    回到題目
                    <ArrowRight size={16} />
                  </button>
                </div>
              </div>

              <div className="mt-4 flex flex-wrap gap-2 border-t border-[#f0ded6] pt-4">
                {favoriteTagOptions.map((tag) => {
                  const active = tags.includes(tag);

                  return (
                    <button
                      key={tag}
                      type="button"
                      onClick={() => onToggleTag(exam.id, question.id, tag)}
                      className={clsx(
                        "rounded-full border px-3 py-1.5 text-xs font-semibold transition",
                        active
                          ? "border-[#f1aac8] bg-[#ffddea] text-[#9a496b]"
                          : "border-[#efd9d0] bg-white/70 text-[#806b60] hover:border-[#f1aac8] hover:bg-[#fff0f6]",
                      )}
                    >
                      {tag}
                    </button>
                  );
                })}
              </div>
            </article>
          ))}
        </div>
      )}
    </section>
  );
}

function FavoriteTagFilterButton({
  active,
  onClick,
  children,
}: {
  active: boolean;
  onClick: () => void;
  children: ReactNode;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      className={clsx(
        "inline-flex h-10 items-center justify-center rounded-full border px-4 text-sm font-semibold transition",
        active
          ? "border-[#f1aac8] bg-[#ffddea] text-[#9a496b] shadow-[0_8px_24px_rgba(238,148,185,0.18)]"
          : "border-[#efd9d0] bg-white/80 text-[#6f5b50] hover:border-[#f1aac8] hover:bg-[#fff0f6]",
      )}
    >
      {children}
    </button>
  );
}

function getSourceLabel(source: FavoriteEntry["source"]) {
  if (source === "both") return "題目與卡片";
  return source === "question" ? "題目" : "卡片";
}
