import { useState, useEffect, useMemo } from "react";
import { GitCompare, Lightbulb, PenLine, Plus, Trash2, CheckCircle2, XCircle } from "lucide-react";
import { loadDiseaseComparisons } from "../../lib/loadExamData";
import { DiseaseComparison } from "./DiseaseComparison";
import type { DiseaseComparisonGroup } from "../../types/disease";
import type { StickyNoteItem } from "../../types/stickyNote";

interface DiseaseComparePageProps {
  stickyNotes: StickyNoteItem[];
  onAddNote: (text: string) => void;
  onRemoveNote: (id: string) => void;
  theme: string;
}

interface QuizQuestion {
  featureKey: string;
  text: string;
  options: string[];
  correctIndex: number;
}

export function DiseaseComparePage({
  stickyNotes,
  onAddNote,
  onRemoveNote,
  theme,
}: DiseaseComparePageProps) {
  const [groups, setGroups] = useState<DiseaseComparisonGroup[]>([]);
  const [selectedGroupId, setSelectedGroupId] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string>("");

  // Quiz State
  const [quizList, setQuizList] = useState<QuizQuestion[]>([]);
  const [currentQuizIndex, setCurrentQuizIndex] = useState<number>(0);
  const [selectedAnswer, setSelectedAnswer] = useState<number | null>(null);
  const [showExplanation, setShowExplanation] = useState<boolean>(false);

  // Note Input State
  const [noteInput, setNoteInput] = useState<string>("");

  // Load comparison groups
  useEffect(() => {
    loadDiseaseComparisons()
      .then((data) => {
        setGroups(data.comparison_groups);
        if (data.comparison_groups.length > 0) {
          setSelectedGroupId(data.comparison_groups[0].id);
        }
        setLoading(false);
      })
      .catch((err) => {
        console.error("Failed to load disease comparisons", err);
        setError("無法載入疾病對照資料庫，請稍後再試。");
        setLoading(false);
      });
  }, []);

  const selectedGroup = useMemo(() => {
    return groups.find((g) => g.id === selectedGroupId) || null;
  }, [groups, selectedGroupId]);

  // Generate quizzes when selected group changes
  useEffect(() => {
    if (!selectedGroup) return;

    const disA = selectedGroup.diseases[0];
    const disB = selectedGroup.diseases[1];
    const generated: QuizQuestion[] = [];

    const keys = Object.keys(disA.features || {});
    for (const key of keys) {
      const valA = disA.features[key];
      const valB = disB.features[key];

      if (valA && valA !== "—" && valA !== "無" && valA.length > 3) {
        generated.push({
          featureKey: key,
          text: `大腸、腦部或關節等檢查出現臨床特徵【${key}】為：\n「${valA}」\n\n請問這最符合下列哪一種疾病的診斷？`,
          options: [disA.name, disB.name],
          correctIndex: 0,
        });
      }

      if (valB && valB !== "—" && valB !== "無" && valB.length > 3) {
        generated.push({
          featureKey: key,
          text: `大腸、腦部或關節等檢查出現臨床特徵【${key}】為：\n「${valB}」\n\n請問這最符合下列哪一種疾病的診斷？`,
          options: [disA.name, disB.name],
          correctIndex: 1,
        });
      }
    }

    // Shuffle quizzes
    const shuffled = generated.sort(() => Math.random() - 0.5);
    setQuizList(shuffled);
    setCurrentQuizIndex(0);
    setSelectedAnswer(null);
    setShowExplanation(false);
  }, [selectedGroup]);

  // Get sticky notes linked to the selected comparison group
  const linkedNotes = useMemo(() => {
    if (!selectedGroup) return [];
    const prefix = `[對照:${selectedGroup.title}]`;
    return stickyNotes.filter((note) => note.text.startsWith(prefix));
  }, [stickyNotes, selectedGroup]);

  const handleAddLinkedNote = (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedGroup || !noteInput.trim()) return;

    const prefix = `[對照:${selectedGroup.title}]`;
    onAddNote(`${prefix} ${noteInput.trim()}`);
    setNoteInput("");
  };

  const handleQuizAnswer = (index: number) => {
    if (selectedAnswer !== null) return; // Already answered
    setSelectedAnswer(index);
    setShowExplanation(true);
  };

  const handleNextQuiz = () => {
    setSelectedAnswer(null);
    setShowExplanation(false);
    setCurrentQuizIndex((prev) => (prev + 1) % quizList.length);
  };

  // Grouped menu sidebar items by category
  const categorizedGroups = useMemo(() => {
    const categories: Record<string, DiseaseComparisonGroup[]> = {};
    for (const g of groups) {
      const cat = g.category.split(" / ")[0] || "其他學科";
      if (!categories[cat]) {
        categories[cat] = [];
      }
      categories[cat].push(g);
    }
    return categories;
  }, [groups]);

  if (loading) {
    return (
      <div className="flex h-64 items-center justify-center">
        <div className="text-center">
          <div className="h-8 w-8 animate-spin rounded-full border-4 border-[#b8527a] border-t-transparent mx-auto"></div>
          <p className="mt-3 text-sm text-[#8a7066] font-hand">正在載入鑑別對照資料庫...</p>
        </div>
      </div>
    );
  }

  if (error || !selectedGroup) {
    return (
      <div className="rounded-[1.2rem] border border-red-200 bg-red-50 p-6 text-center text-red-800">
        <p>{error || "尚未建立疾病對照資料。"}</p>
      </div>
    );
  }

  const currentQuiz = quizList[currentQuizIndex] || null;

  return (
    <div className="grid gap-6 lg:grid-cols-[280px_1fr] items-start">
      {/* Sidebar List */}
      <aside className="rounded-[1.4rem] border border-white/90 bg-white/80 p-4 shadow-[0_12px_40px_rgba(181,133,117,0.08)] backdrop-blur-xl lg:sticky lg:top-24 max-h-[80vh] overflow-y-auto">
        <div className="flex items-center gap-2 border-b border-[#efd9d0] pb-3 mb-3">
          <GitCompare size={18} className="text-[#b8527a]" />
          <span className="font-hand font-bold text-base text-[#4b3b35]">魔王對照目錄</span>
        </div>
        
        <div className="space-y-4">
          {Object.entries(categorizedGroups).map(([category, items]) => (
            <div key={category}>
              <h4 className="text-[11px] font-bold tracking-wider text-[#9c7b70] uppercase px-2 mb-1.5">
                {category}
              </h4>
              <ul className="space-y-1">
                {items.map((item) => (
                  <li key={item.id}>
                    <button
                      type="button"
                      onClick={() => setSelectedGroupId(item.id)}
                      className={`w-full text-left rounded-lg px-2.5 py-2 text-xs font-semibold transition cursor-pointer ${
                        item.id === selectedGroupId
                          ? "bg-[#fdf0f4] text-[#b8527a] font-bold"
                          : "text-[#6f5b50] hover:bg-white"
                      }`}
                    >
                      {item.title.split(" (")[0]}
                    </button>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </aside>

      {/* Main Content View */}
      <div className="space-y-6">
        {/* Intro */}
        <div className="rounded-[1.4rem] border border-white/90 bg-white/82 p-5 shadow-[0_12px_40px_rgba(181,133,117,0.08)] backdrop-blur-xl">
          <h2 className="font-hand text-2xl font-bold text-[#4b3b35] flex items-center gap-2.5">
            <GitCompare size={24} className="text-[#b8527a]" />
            疾病鑑別與對照專區
          </h2>
          <p className="mt-2 text-sm text-[#725b52] leading-6 font-reading">
            本專區精選 10 組國考經典魔王對照組，透過雙向比對核心相異處（高亮顯示），並整合歷屆考題與自訂對照筆記（同步至便利貼），幫助您直擊考點、秒殺陷阱。
          </p>
        </div>

        {/* Dynamic Comparison Card */}
        <DiseaseComparison group={selectedGroup} />

        <div className="grid gap-6 md:grid-cols-2">
          {/* Interactive Quiz (Decision Tree alternative) */}
          <section className="rounded-[1.3rem] border border-[#e6d6c9] bg-white/90 p-5 shadow-sm">
            <div className="flex items-center gap-2 border-b border-[#efd9d0] pb-3 mb-4">
              <Lightbulb size={17} className="text-[#d89e1b]" />
              <h3 className="text-sm font-bold text-[#4b3b35]">臨床決策 PK 診斷測驗</h3>
            </div>

            {currentQuiz ? (
              <div className="space-y-4">
                <p className="text-xs text-[#a68e98] font-semibold">
                  診斷練習 第 {currentQuizIndex + 1} 題 / 共 {quizList.length} 題
                </p>
                <div className="rounded-xl bg-[#fffcf2] border border-[#fceeac]/60 p-4 min-h-24 flex items-center">
                  <p className="text-xs font-semibold leading-6 text-[#725e3c] whitespace-pre-wrap">
                    {currentQuiz.text}
                  </p>
                </div>

                <div className="grid gap-2">
                  {currentQuiz.options.map((opt, idx) => {
                    const isSelected = selectedAnswer === idx;
                    const isCorrect = currentQuiz.correctIndex === idx;
                    let btnStyle = "border-[#efd9d0] hover:bg-[#fffbf9] text-[#6f5b50]";

                    if (selectedAnswer !== null) {
                      if (isCorrect) {
                        btnStyle = "border-[#4c806e] bg-[#e9f6f1] text-[#4c806e] font-bold";
                      } else if (isSelected) {
                        btnStyle = "border-[#9a496b] bg-[#fff0f3] text-[#9a496b] font-bold";
                      } else {
                        btnStyle = "opacity-50 border-[#efd9d0] text-[#a68e98]";
                      }
                    }

                    return (
                      <button
                        key={idx}
                        type="button"
                        onClick={() => handleQuizAnswer(idx)}
                        disabled={selectedAnswer !== null}
                        className={`w-full text-left rounded-xl border p-3 text-xs font-semibold transition flex items-center justify-between cursor-pointer ${btnStyle}`}
                      >
                        <span>{opt}</span>
                        {selectedAnswer !== null && isCorrect && <CheckCircle2 size={16} className="text-[#4c806e]" />}
                        {selectedAnswer !== null && isSelected && !isCorrect && <XCircle size={16} className="text-[#9a496b]" />}
                      </button>
                    );
                  })}
                </div>

                {showExplanation && (
                  <div className="rounded-xl bg-[#effaf5] border border-[#d8eadf] p-4 text-xs">
                    <p className="font-bold text-[#4c806e]">
                      {selectedAnswer === currentQuiz.correctIndex ? "🎉 答對了！診斷正確。" : "💡 需要再加強記憶。"}
                    </p>
                    <p className="mt-2 leading-5 text-[#604b43]">
                      考點解析：這項特徵屬於「{currentQuiz.options[currentQuiz.correctIndex]}」的經典國考特徵，常用於與「{currentQuiz.options[1 - currentQuiz.correctIndex]}」做鑑別診斷。
                    </p>
                    <button
                      type="button"
                      onClick={handleNextQuiz}
                      className="mt-3 inline-flex h-8 items-center justify-center rounded-lg bg-[#4c806e] px-4 text-xs font-bold text-white transition hover:bg-[#3d695a] cursor-pointer"
                    >
                      下一題
                    </button>
                  </div>
                )}
              </div>
            ) : (
              <p className="text-xs text-[#8a7066] font-hand py-8 text-center">本組對照尚未設定足夠的特徵測驗。</p>
            )}
          </section>

          {/* Linked Sticky Notes */}
          <section className="rounded-[1.3rem] border border-[#e6d6c9] bg-white/90 p-5 shadow-sm">
            <div className="flex items-center gap-2 border-b border-[#efd9d0] pb-3 mb-4">
              <PenLine size={17} className="text-[#b8527a]" />
              <h3 className="text-sm font-bold text-[#4b3b35]">自訂對照筆記</h3>
              <span className="text-[10px] bg-[#fdf0f4] text-[#b8527a] px-2 py-0.5 rounded-full font-bold ml-auto border border-[#f1aac8]/40">
                連動便利貼
              </span>
            </div>

            {/* List Linked Notes */}
            <div className="space-y-3 max-h-56 overflow-y-auto mb-4 pr-1">
              {linkedNotes.length > 0 ? (
                linkedNotes.map((note) => {
                  // Strip the prefix for display
                  const prefix = `[對照:${selectedGroup.title}]`;
                  const displayText = note.text.substring(prefix.length).trim();

                  return (
                    <div
                      key={note.id}
                      className="flex items-start justify-between gap-3 rounded-xl bg-[#fffcf0] border border-[#fceeac] p-3 text-xs shadow-[0_2px_8px_rgba(240,220,130,0.06)]"
                    >
                      <div className="space-y-1">
                        <p className="leading-5 text-[#7a6040] font-hand whitespace-pre-wrap">{displayText}</p>
                        <p className="text-[9px] text-[#b2a18d]">
                          {new Date(note.createdAt).toLocaleDateString()}
                        </p>
                      </div>
                      <button
                        type="button"
                        onClick={() => onRemoveNote(note.id)}
                        className="text-[#b2a18d] hover:text-[#9a496b] p-0.5 transition cursor-pointer"
                        title="刪除筆記"
                      >
                        <Trash2 size={13} />
                      </button>
                    </div>
                  );
                })
              ) : (
                <div className="py-8 text-center text-xs text-[#b2a18d] border border-dashed border-[#efd9d0] rounded-xl font-hand">
                  尚未針對本組建立個人筆記。您可以在下方新增！
                </div>
              )}
            </div>

            {/* Add Linked Note Form */}
            <form onSubmit={handleAddLinkedNote} className="space-y-2">
              <textarea
                value={noteInput}
                onChange={(e) => setNoteInput(e.target.value)}
                placeholder="寫下您對這兩個疾病的學習筆記或口訣（將自動同步至「便利貼」頁面）..."
                className="w-full rounded-xl border border-[#efd9d0] bg-white p-3 text-xs leading-5 text-[#6f5b50] focus:border-[#c5a6b4] focus:outline-none placeholder-[#b2a18d]"
                rows={3}
                required
              />
              <button
                type="submit"
                className="inline-flex h-9 w-full items-center justify-center gap-1.5 rounded-xl bg-[#b8527a] text-xs font-bold text-white transition hover:bg-[#9c3e5e] cursor-pointer shadow-sm"
              >
                <Plus size={14} />
                儲存筆記
              </button>
            </form>
          </section>
        </div>
      </div>
    </div>
  );
}
