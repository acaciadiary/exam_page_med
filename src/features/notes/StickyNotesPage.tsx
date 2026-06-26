import { ArrowRight, Check, Copy, Trash2 } from "lucide-react";
import { useMemo, useState } from "react";
import { EmptyState } from "../../components/EmptyState";
import type { StickyNoteItem } from "../../types/stickyNote";

type StickyNotesPageProps = {
  notes: StickyNoteItem[];
  onAddNote: (text: string) => void;
  onRemoveNote: (id: string) => void;
  onClearNotes: () => void;
  onOpenQuestion: (examId: string, questionId: string) => void;
};

export function StickyNotesPage({
  notes,
  onAddNote,
  onRemoveNote,
  onClearNotes,
  onOpenQuestion,
}: StickyNotesPageProps) {
  const [draft, setDraft] = useState("");
  const [query, setQuery] = useState("");
  const [copied, setCopied] = useState(false);
  const sortedNotes = useMemo(
    () =>
      [...notes].sort(
        (left, right) =>
          new Date(right.createdAt).getTime() - new Date(left.createdAt).getTime(),
      ),
    [notes],
  );
  const visibleNotes = useMemo(() => {
    const keyword = query.trim().toLocaleLowerCase();
    if (!keyword) return sortedNotes;

    return sortedNotes.filter((note) =>
      note.text.toLocaleLowerCase().includes(keyword),
    );
  }, [query, sortedNotes]);

  const handleAddNote = () => {
    const text = draft.trim();
    if (!text) return;

    onAddNote(text);
    setDraft("");
  };

  const handleCopyNotes = async () => {
    if (sortedNotes.length === 0) return;

    const text = sortedNotes
      .map((note, index) => `${index + 1}. ${formatNoteTime(note.createdAt)}\n${note.text}`)
      .join("\n\n");

    try {
      await navigator.clipboard.writeText(text);
      setCopied(true);
      window.setTimeout(() => setCopied(false), 1600);
    } catch {
      setCopied(false);
    }
  };

  return (
    <section className="space-y-6">
      <div className="rounded-[1.5rem] border border-white/80 bg-white/80 p-6 shadow-[0_18px_60px_rgba(181,133,117,0.16)] backdrop-blur-2xl">
        <div className="flex flex-col gap-4 lg:flex-row lg:items-start lg:justify-between">
          <div>
            <p className="text-sm font-semibold tracking-[0.12em] text-[#b36a84]">
              我的便利貼
            </p>
            <h2 className="mt-3 text-3xl font-semibold text-[#3f342d]">
              所有學習筆記都集中在這裡
            </h2>
            <p className="mt-3 text-sm leading-7 text-[#725b52]">
              你可以在這裡新增、查看、刪除便利貼，之後複習時會更方便。
            </p>
          </div>

          <div className="flex flex-wrap gap-2 lg:justify-end">
            <button
              type="button"
              onClick={handleCopyNotes}
              disabled={sortedNotes.length === 0}
              className="inline-flex h-11 items-center justify-center gap-2 rounded-full border border-[#efd9d0] bg-white px-4 text-sm font-semibold text-[#6f5b50] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b] disabled:cursor-not-allowed disabled:opacity-50"
            >
              {copied ? <Check size={16} /> : <Copy size={16} />}
              {copied ? "已複製" : "複製全部便利貼"}
            </button>

            <button
              type="button"
              onClick={onClearNotes}
              disabled={notes.length === 0}
              className="inline-flex h-11 items-center justify-center rounded-full border border-[#efd9d0] bg-white px-4 text-sm font-semibold text-[#6f5b50] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b] disabled:cursor-not-allowed disabled:opacity-50"
            >
              清空全部便利貼
            </button>
          </div>
        </div>

        <div className="mt-6 rounded-[1.25rem] bg-[#fff8f4] p-4">
          <label className="block text-sm font-semibold text-[#5b4841]">
            新增便利貼
          </label>
          <textarea
            value={draft}
            onChange={(event) => setDraft(event.target.value)}
            rows={5}
            placeholder="例如：腎臟、心臟、感染科這幾題要再重看一次。"
            className="mt-3 w-full resize-none rounded-[1rem] border border-[#efd9d0] bg-white px-4 py-3 text-sm leading-7 text-[#4b3b35] outline-none transition placeholder:text-[#aa8a7d] focus:border-[#f1aac8] focus:ring-4 focus:ring-[#ffd9e8]/55"
          />
          <div className="mt-3 flex justify-end">
            <button
              type="button"
              onClick={handleAddNote}
              className="inline-flex h-11 items-center justify-center rounded-full bg-[#b8e2d4] px-5 text-sm font-semibold text-[#355249] shadow-[0_8px_22px_rgba(123,190,168,0.24)] transition hover:-translate-y-0.5"
            >
              新增便利貼
            </button>
          </div>
        </div>
      </div>

      {sortedNotes.length > 0 && (
        <div className="rounded-[1.2rem] border border-white/80 bg-white/78 p-4 shadow-[0_14px_42px_rgba(181,133,117,0.12)] backdrop-blur-2xl">
          <label className="block text-sm font-semibold text-[#5b4841]">
            搜尋便利貼
          </label>
          <input
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            placeholder="輸入關鍵字，例如：腎臟、抗生素、兒科"
            className="mt-3 h-11 w-full rounded-full border border-[#efd9d0] bg-white px-4 text-sm text-[#4b3b35] outline-none transition placeholder:text-[#aa8a7d] focus:border-[#f1aac8] focus:ring-4 focus:ring-[#ffd9e8]/55"
          />
        </div>
      )}

      {sortedNotes.length === 0 ? (
        <EmptyState
          title="目前還沒有便利貼"
          description="先寫下你的重點、提醒或容易忘記的觀念，之後就能集中整理。"
        />
      ) : visibleNotes.length === 0 ? (
        <EmptyState
          title="找不到符合的便利貼"
          description="換個關鍵字試試看，或先清空搜尋內容。"
        />
      ) : (
        <div className="grid gap-4 md:grid-cols-2">
          {visibleNotes.map((note) => (
            <article
              key={note.id}
              className="rounded-[1.2rem] border border-[#f2d7a9] bg-[#fff9e8] p-5 shadow-[0_12px_32px_rgba(181,133,117,0.12)]"
            >
              <div className="flex items-start justify-between gap-3">
                <div className="min-w-0">
                  <p className="text-xs font-semibold tracking-[0.08em] text-[#9d7b58]">
                    {formatNoteTime(note.createdAt)}
                  </p>
                  {note.examId && note.questionId ? (
                    <button
                      type="button"
                      onClick={() => onOpenQuestion(note.examId!, note.questionId!)}
                      className="mt-2 inline-flex max-w-full items-center gap-1.5 rounded-full bg-white/72 px-3 py-1 text-xs font-bold text-[#9a496b] transition hover:bg-[#fff0f6]"
                      title={note.examTitle}
                    >
                      <span className="truncate">
                        {note.examTitle ?? "題目筆記"}
                        {note.questionNumber ? ` 第 ${note.questionNumber} 題` : ""}
                      </span>
                      <ArrowRight size={13} className="shrink-0" />
                    </button>
                  ) : null}
                </div>
                <button
                  type="button"
                  onClick={() => onRemoveNote(note.id)}
                  className="inline-flex h-9 w-9 items-center justify-center rounded-full text-[#9d7b58] transition hover:bg-white/70 hover:text-[#9a496b]"
                  aria-label="刪除便利貼"
                  title="刪除便利貼"
                >
                  <Trash2 size={16} />
                </button>
              </div>
              <p className="mt-3 whitespace-pre-wrap text-sm leading-7 text-[#604b43]">
                {note.text}
              </p>
              {note.questionText ? (
                <p className="mt-3 line-clamp-2 rounded-[0.85rem] bg-white/58 px-3 py-2 text-xs leading-5 text-[#8a7066]">
                  來源題目：{note.questionText}
                </p>
              ) : null}
            </article>
          ))}
        </div>
      )}
    </section>
  );
}

function formatNoteTime(value: string) {
  const date = new Date(value);

  if (Number.isNaN(date.getTime())) {
    return "剛剛建立";
  }

  return date.toLocaleString("zh-TW", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
  });
}
