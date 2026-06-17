import { Trash2 } from "lucide-react";
import { useMemo, useState } from "react";
import { EmptyState } from "../../components/EmptyState";
import type { StickyNoteItem } from "../../types/stickyNote";

type StickyNotesPageProps = {
  notes: StickyNoteItem[];
  onAddNote: (text: string) => void;
  onRemoveNote: (id: string) => void;
  onClearNotes: () => void;
};

export function StickyNotesPage({
  notes,
  onAddNote,
  onRemoveNote,
  onClearNotes,
}: StickyNotesPageProps) {
  const [draft, setDraft] = useState("");
  const sortedNotes = useMemo(
    () =>
      [...notes].sort(
        (left, right) =>
          new Date(right.createdAt).getTime() - new Date(left.createdAt).getTime(),
      ),
    [notes],
  );

  const handleAddNote = () => {
    const text = draft.trim();
    if (!text) return;

    onAddNote(text);
    setDraft("");
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

          <button
            type="button"
            onClick={onClearNotes}
            disabled={notes.length === 0}
            className="inline-flex h-11 items-center justify-center rounded-full border border-[#efd9d0] bg-white px-4 text-sm font-semibold text-[#6f5b50] transition hover:border-[#f1aac8] hover:bg-[#fff0f6] hover:text-[#9a496b] disabled:cursor-not-allowed disabled:opacity-50"
          >
            清空全部便利貼
          </button>
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

      {sortedNotes.length === 0 ? (
        <EmptyState
          title="目前還沒有便利貼"
          description="先寫下你的重點、提醒或容易忘記的觀念，之後就能集中整理。"
        />
      ) : (
        <div className="grid gap-4 md:grid-cols-2">
          {sortedNotes.map((note) => (
            <article
              key={note.id}
              className="rounded-[1.2rem] border border-[#f2d7a9] bg-[#fff9e8] p-5 shadow-[0_12px_32px_rgba(181,133,117,0.12)]"
            >
              <div className="flex items-start justify-between gap-3">
                <p className="text-xs font-semibold tracking-[0.08em] text-[#9d7b58]">
                  {formatNoteTime(note.createdAt)}
                </p>
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
