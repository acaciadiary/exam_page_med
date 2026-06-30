import { useState, useEffect, useMemo } from "react";
import { Sparkles, RotateCcw, Check, HelpCircle, Shuffle, ChevronRight, Bookmark, BookOpen, AlertTriangle } from "lucide-react";
import type { DiseaseComparisonGroup } from "../../types/disease";

interface BuzzwordFlashcardsProps {
  groups: DiseaseComparisonGroup[];
  theme: string;
}

interface CardItem {
  id: string;
  diseaseName: string;
  groupTitle: string;
  category: string;
  stage: string;
  importance: string;
  features: Record<string, string>;
  focusTips: string;
  commonTraps: string;
  highlightKeywords: string[];
}

type StageFilter = "all" | "一階" | "二階";
type StageOnly = Exclude<StageFilter, "all">;

const STAGE_FILTERS: Array<[StageFilter, string]> = [
  ["all", "全部"],
  ["一階", "一階"],
  ["二階", "二階"],
];

const STAGE_CATEGORY_LABELS: Record<StageOnly, string> = {
  "一階": "一階科目",
  "二階": "二階科目",
};

function extractCategoryNames(category: string) {
  return category
    .split("/")
    .map((part) => part.trim().split(" ")[0].split("(")[0])
    .filter(Boolean);
}

export function BuzzwordFlashcards({ groups, theme }: BuzzwordFlashcardsProps) {
  const [deck, setDeck] = useState<CardItem[]>([]);
  const [masteredCount, setMasteredCount] = useState<number>(0);
  const [totalInSession, setTotalInSession] = useState<number>(0);
  const [isFlipped, setIsFlipped] = useState<boolean>(false);
  const [selectedCategory, setSelectedCategory] = useState<string>("全部");
  const [selectedStage, setSelectedStage] = useState<StageFilter>("all");
  const [searchTerm, setSearchTerm] = useState<string>("");
  const [highYieldOnly, setHighYieldOnly] = useState<boolean>(false);
  const [missedCount, setMissedCount] = useState<number>(0);

  // Flatten the disease comparisons into individual disease cards
  const allCards = useMemo(() => {
    const cardsList: CardItem[] = [];
    groups.forEach((group) => {
      group.diseases.forEach((disease, idx) => {
        cardsList.push({
          id: `${group.id}_${idx}`,
          diseaseName: disease.name,
          groupTitle: group.title,
          category: group.category,
          stage: group.stage || "二階",
          importance: group.exam_importance || "★★★",
          features: disease.features,
          focusTips: group.exam_focus_tips,
          commonTraps: group.common_traps || "",
          highlightKeywords: group.highlight_keywords || [],
        });
      });
    });
    return cardsList;
  }, [groups]);

  const stageCategoryGroups = useMemo(() => {
    const groupsByStage: Record<StageOnly, string[]> = {
      "一階": ["全部"],
      "二階": ["全部"],
    };
    const seenByStage: Record<StageOnly, Set<string>> = {
      "一階": new Set(["全部"]),
      "二階": new Set(["全部"]),
    };

    allCards.forEach((card) => {
      const stage = card.stage === "一階" ? "一階" : "二階";
      extractCategoryNames(card.category).forEach((category) => {
        if (!seenByStage[stage].has(category)) {
          seenByStage[stage].add(category);
          groupsByStage[stage].push(category);
        }
      });
    });

    return groupsByStage;
  }, [allCards]);

  useEffect(() => {
    if (selectedStage === "all" && selectedCategory !== "全部") {
      setSelectedCategory("全部");
      return;
    }

    if (
      selectedStage !== "all" &&
      selectedCategory !== "全部" &&
      !stageCategoryGroups[selectedStage].includes(selectedCategory)
    ) {
      setSelectedCategory("全部");
    }
  }, [selectedCategory, selectedStage, stageCategoryGroups]);

  const handleStageFilterChange = (stage: StageFilter) => {
    setSelectedStage(stage);
    setSelectedCategory("全部");
  };

  const handleCategoryFilterChange = (stage: StageOnly, category: string) => {
    setSelectedStage(stage);
    setSelectedCategory(category);
  };

  const isHighYieldCard = (card: CardItem) => {
    return (
      card.importance.includes("★★★") ||
      /高頻|必考|常考|核心/.test(card.importance) ||
      card.highlightKeywords.length >= 3
    );
  };

  // Filter cards based on selected category, search and high-yield mode
  const filteredCards = useMemo(() => {
    const query = searchTerm.trim().toLowerCase();
    return allCards.filter((card) => {
      if (selectedStage !== "all" && card.stage !== selectedStage) return false;
      if (selectedCategory !== "全部" && !card.category.includes(selectedCategory)) return false;
      if (highYieldOnly && !isHighYieldCard(card)) return false;
      if (!query) return true;

      const searchableText = [
        card.diseaseName,
        card.groupTitle,
        card.category,
        card.importance,
        card.focusTips,
        card.commonTraps,
        ...card.highlightKeywords,
        ...Object.keys(card.features),
        ...Object.values(card.features),
      ]
        .join(" ")
        .toLowerCase();

      return searchableText.includes(query);
    });
  }, [allCards, selectedCategory, selectedStage, searchTerm, highYieldOnly]);

  // Initialize/Reset Deck
  const handleResetDeck = () => {
    setIsFlipped(false);
    const shuffled = [...filteredCards].sort(() => Math.random() - 0.5);
    setDeck(shuffled);
    setMasteredCount(0);
    setMissedCount(0);
    setTotalInSession(shuffled.length);
  };

  // Run on mount or when category changes
  useEffect(() => {
    handleResetDeck();
  }, [filteredCards]);

  const currentCard = deck[0] || null;

  // Handle Review Answer
  const handleMastered = () => {
    setIsFlipped(false);
    // Wait for card flip animation to reset before changing data
    setTimeout(() => {
      setDeck((prev) => prev.slice(1));
      setMasteredCount((prev) => prev + 1);
    }, 200);
  };

  const handleFailed = () => {
    setIsFlipped(false);
    setTimeout(() => {
      setMissedCount((prev) => prev + 1);
      setDeck((prev) => {
        if (prev.length <= 1) return prev;
        const [first, ...rest] = prev;
        return [...rest, first]; // Move current card to the end
      });
    }, 200);
  };

  // Helper to highlight keywords in texts
  const renderHighlightedText = (text: string, keywords: string[]) => {
    if (!keywords || keywords.length === 0) return text;
    // Sort keywords by length descending to avoid partial matches on shorter words first
    const sortedKeywords = [...keywords].sort((a, b) => b.length - a.length);
    const escapedKeywords = sortedKeywords.map(k => k.replace(/[-\/\\^$*+?.()|[\]{}]/g, "\\$&"));
    const regex = new RegExp(`(${escapedKeywords.join("|")})`, "gi");

    const parts = text.split(regex);
    const lowerKeywords = new Set(sortedKeywords.map((keyword) => keyword.toLowerCase()));
    return parts.map((part, index) =>
      lowerKeywords.has(part.toLowerCase()) ? (
        <mark key={index} className="bg-[#ffe4e6] px-0.5 font-bold text-[#b8527a] rounded dark:bg-[#573047] dark:text-[#ffc8da]">
          {part}
        </mark>
      ) : (
        part
      )
    );
  };

  return (
    <div className="space-y-6 max-w-4xl mx-auto min-w-0">
      <style>{`
        .flip-card {
          perspective: 1000px;
        }
        .flip-card-inner {
          transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
          transform-style: preserve-3d;
        }
        .flip-card-inner.flipped {
          transform: rotateY(180deg);
        }
        .flip-card-front, .flip-card-back {
          backface-visibility: hidden;
          -webkit-backface-visibility: hidden;
        }
        .flip-card-back {
          transform: rotateY(180deg);
        }
      `}</style>

      {/* Control Bar */}
      <div className="space-y-3 bg-white/70 p-4 rounded-2xl border border-white/90 shadow-sm backdrop-blur-md">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <div className="min-w-0 flex-[1_1_14rem]">
            <input
              type="text"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              placeholder="搜尋疾病、關鍵字或陷阱（例如：Murphy、Aspirin、低血糖）"
              className="w-full rounded-xl border border-[#efd9d0] bg-white px-3 py-2 text-xs leading-5 text-[#6f5b50] focus:border-[#c5a6b4] focus:outline-none placeholder-[#b2a18d]"
            />
          </div>

          <div className="flex flex-wrap items-center gap-2">
            <span className="rounded-lg border border-[#efd9d0]/70 bg-[#fff8fb]/80 px-3 py-1.5 text-[11px] font-bold text-[#8a7066]">
              目前牌組 {filteredCards.length} / {allCards.length} 張
            </span>
            <button
              type="button"
              onClick={handleResetDeck}
              className="px-3.5 py-1.5 text-xs font-bold text-[#b8527a] bg-[#fdf0f4] hover:bg-[#fbdde8] rounded-xl transition flex items-center gap-1.5 cursor-pointer border border-[#fbdde8]"
            >
              <Shuffle size={13} />
              重新洗牌
            </button>
          </div>
        </div>

        <div className="flex flex-wrap items-center gap-2">
          <span className="text-xs font-bold text-[#6f5b50]">考試階段：</span>
          <div className="flex flex-wrap gap-1">
            {STAGE_FILTERS.map(([value, label]) => (
              <button
                key={value}
                type="button"
                onClick={() => handleStageFilterChange(value)}
                className={`px-3 py-1 text-xs font-semibold rounded-lg transition cursor-pointer ${
                  selectedStage === value
                    ? "bg-[#b8527a] text-white shadow-xs"
                    : "bg-white/60 text-[#6f5b50] hover:bg-white border border-[#efd9d0]"
                }`}
              >
                {label}
              </button>
            ))}
          </div>
          {selectedStage !== "all" && (
            <>
              <span className="text-xs font-bold text-[#6f5b50]">篩選科目：</span>
              <div className="flex min-w-0 flex-1 flex-wrap items-center gap-1">
                <span className="mr-1 rounded-md bg-[#fcf9fa]/80 px-2 py-1 text-[10px] font-extrabold text-[#8a7066]">
                  {STAGE_CATEGORY_LABELS[selectedStage]}
                </span>
                {stageCategoryGroups[selectedStage].map((cat) => {
                  const isSelected = selectedCategory === cat;
                  return (
                    <button
                      key={`${selectedStage}-${cat}`}
                      type="button"
                      onClick={() => handleCategoryFilterChange(selectedStage, cat)}
                      className={`px-3 py-1 text-xs font-semibold rounded-lg transition cursor-pointer ${
                        isSelected
                          ? "bg-[#b8527a] text-white shadow-xs"
                          : "bg-white/60 text-[#6f5b50] hover:bg-white border border-[#efd9d0]"
                      }`}
                    >
                      {cat}
                    </button>
                  );
                })}
              </div>
            </>
          )}
          <button
            type="button"
            onClick={() => setHighYieldOnly((prev) => !prev)}
            className={`px-3 py-1 text-xs font-bold rounded-lg border transition cursor-pointer ${
              highYieldOnly
                ? "bg-[#b8527a] text-white border-[#b8527a]"
                : "bg-white/60 text-[#6f5b50] hover:bg-white border-[#efd9d0]"
            }`}
          >
            只練高頻
          </button>
        </div>
      </div>

      {/* Session Progress */}
      {currentCard && (
        <div className="space-y-2">
          <div className="flex justify-between text-xs font-bold text-[#8a7066]">
            <span>記憶特訓中：已掌握 {masteredCount} / {totalInSession} 張卡片</span>
            <span>答錯 {missedCount} 次，剩餘 {deck.length} 張</span>
          </div>
          <div className="w-full bg-[#efd9d0]/60 h-2 rounded-full overflow-hidden">
            <div
              className="bg-linear-to-r from-[#e49bb0] to-[#b8527a] h-full transition-all duration-300"
              style={{ width: `${(masteredCount / totalInSession) * 100}%` }}
            />
          </div>
        </div>
      )}

      {/* Main Flashcard View */}
      {currentCard ? (
        <div className="flex flex-col items-center gap-6">
          <div className="flip-card w-full h-[520px] max-w-2xl cursor-pointer">
            <div
              onClick={() => setIsFlipped(!isFlipped)}
              className={`flip-card-inner w-full h-full relative ${
                isFlipped ? "flipped" : ""
              }`}
            >
              {/* FRONT SIDE (Clues/Features) */}
              <div className="flip-card-front absolute inset-0 p-6 sm:p-8 flex flex-col justify-between overflow-y-auto bg-white border border-[#efd9d0] shadow-[0_16px_40px_rgba(181,133,117,0.08)] rounded-3xl">
                <div className="space-y-4">
                  {/* Card Header */}
                  <div className="flex items-center justify-between border-b border-[#efd9d0]/50 pb-3">
                    <div className="flex items-center gap-1.5">
                      <Sparkles size={15} className="text-[#b8527a]" />
                      <span className="text-[10px] sm:text-xs font-extrabold text-[#b8527a] tracking-wider uppercase bg-[#fdf0f4] px-2 py-0.5 rounded-md">
                        {currentCard.category.split(" / ")[0]}
                      </span>
                    </div>
                    <div className="flex items-center gap-2">
                      <span className="text-xs text-[#a7948a] font-hand">
                        重考星等：{currentCard.importance}
                      </span>
                    </div>
                  </div>

                  {/* Question */}
                  <div className="space-y-1">
                    <h3 className="text-base sm:text-lg font-bold text-[#4b3b35] font-hand">
                      根據以下臨床與病理特徵，這最可能是哪種疾病？
                    </h3>
                    <p className="text-xs text-[#9c7b70]">
                      （點擊卡片任何地方可翻面查看答案）
                    </p>
                  </div>

                  {/* Feature Clues List */}
                  <div className="space-y-3 pt-2">
                    {Object.entries(currentCard.features).map(([title, val]) => (
                      <div
                        key={title}
                        className="bg-white/50 p-3 rounded-xl border border-[#efd9d0]/30 hover:border-[#b8527a]/20 transition"
                      >
                        <div className="text-[10px] font-extrabold text-[#b8527a] tracking-wider uppercase mb-1">
                          【{title}】
                        </div>
                        <div className="text-xs sm:text-sm font-semibold text-[#6f5b50] leading-relaxed">
                          {renderHighlightedText(val, currentCard.highlightKeywords)}
                        </div>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Card Footer Clue */}
                <div className="text-center text-xs font-bold text-[#a7948a] pt-4 border-t border-[#efd9d0]/40 flex items-center justify-center gap-1">
                  <HelpCircle size={14} />
                  點擊卡片翻面揭曉答案
                </div>
              </div>

              {/* BACK SIDE (Answer & Traps) */}
              <div className="flip-card-back absolute inset-0 p-6 sm:p-8 flex flex-col justify-between overflow-y-auto bg-linear-to-b from-white to-[#fdf9f8] border border-[#efd9d0] shadow-[0_16px_40px_rgba(181,133,117,0.08)] rounded-3xl dark:from-[#241e2a] dark:to-[#17131d] dark:border-white/10 dark:shadow-[0_18px_48px_rgba(0,0,0,0.32)]">
                <div className="space-y-4">
                  {/* Card Header */}
                  <div className="flex items-center justify-between border-b border-[#efd9d0]/50 pb-3 dark:border-white/10">
                    <span className="text-xs font-bold text-[#9c7b70] dark:text-[#cbb8c2]">{currentCard.groupTitle}</span>
                    <span className="text-xs font-extrabold text-[#b8527a] bg-[#fdf0f4] px-2 py-0.5 rounded-md dark:bg-[#573047] dark:text-[#ffc8da]">
                      解答
                    </span>
                  </div>

                  {/* Disease Name (The Answer) */}
                  <div className="text-center py-4 bg-linear-to-r from-[#fdf0f4] to-[#fdf9f8] rounded-2xl border border-[#fbdde8] dark:from-[#3b2534] dark:to-[#211a26] dark:border-[#6b4056]">
                    <div className="text-[10px] font-bold text-[#b8527a] tracking-wider uppercase mb-1 dark:text-[#f3a6c4]">
                      最可能的疾病是
                    </div>
                    <h2 className="text-xl sm:text-2xl font-extrabold text-[#b8527a] font-hand dark:text-[#ffc8da]">
                      {currentCard.diseaseName}
                    </h2>
                  </div>

                  {/* Focus Tips */}
                  <div className="bg-[#fcf9f8] p-4 rounded-xl border border-[#efd9d0] space-y-1.5 dark:bg-white/5 dark:border-white/10">
                    <h4 className="text-xs font-bold text-[#4b3b35] flex items-center gap-1 dark:text-[#f8edf3]">
                      <BookOpen size={14} className="text-[#b8527a] dark:text-[#f3a6c4]" />
                      國考重點提煉 (Focus Tips)
                    </h4>
                    <p className="text-xs sm:text-sm text-[#6f5b50] leading-relaxed dark:text-[#dccbd3]">
                      {renderHighlightedText(currentCard.focusTips, currentCard.highlightKeywords)}
                    </p>
                  </div>

                  {/* Common Traps */}
                  {currentCard.commonTraps && (
                    <div className="bg-[#fffbeb] p-4 rounded-xl border border-[#fde68a] space-y-1.5 dark:bg-[#2d2417] dark:border-[#6f5424]">
                      <h4 className="text-xs font-bold text-[#854d0e] flex items-center gap-1 dark:text-[#f7db91]">
                        <AlertTriangle size={14} className="text-[#d97706] dark:text-[#f0b84b]" />
                        小心誘答陷阱 (Common Traps)
                      </h4>
                      <p className="text-xs sm:text-sm text-[#713f12] leading-relaxed dark:text-[#ead3a3]">
                        {renderHighlightedText(currentCard.commonTraps, currentCard.highlightKeywords)}
                      </p>
                    </div>
                  )}
                </div>

                <div className="text-center text-xs font-bold text-[#a7948a] pt-4 border-t border-[#efd9d0]/40 flex items-center justify-center gap-1 dark:border-white/10 dark:text-[#a2949e]">
                  點擊卡片可再次翻回正面
                </div>
              </div>
            </div>
          </div>

          {/* Action Buttons for Anki review style */}
          <div className="flex gap-4 w-full max-w-md">
            <button
              type="button"
              onClick={handleFailed}
              className="flex-1 py-3 px-4 rounded-2xl bg-[#fff5f5] hover:bg-[#ffe3e3] border border-[#fecaca] text-[#e53e3e] font-bold text-sm sm:text-base flex items-center justify-center gap-2 transition cursor-pointer shadow-xs active:scale-98"
            >
              <RotateCcw size={18} />
              忘記了 (重來)
            </button>
            <button
              type="button"
              onClick={handleMastered}
              className="flex-1 py-3 px-4 rounded-2xl bg-[#f0fdf4] hover:bg-[#dcfce7] border border-[#bbf7d0] text-[#16a34a] font-bold text-sm sm:text-base flex items-center justify-center gap-2 transition cursor-pointer shadow-xs active:scale-98"
            >
              <Check size={18} />
              記住了 (簡單)
            </button>
          </div>
        </div>
      ) : (
        /* Finished State */
        <div className="text-center py-16 bg-white/70 rounded-3xl border border-white/90 shadow-[0_12px_40px_rgba(181,133,117,0.08)] backdrop-blur-xl max-w-2xl mx-auto space-y-6">
          <div className="inline-flex items-center justify-center w-16 h-16 rounded-full bg-[#fdf0f4] text-[#b8527a]">
            <Sparkles size={32} />
          </div>
          <div className="space-y-2">
            <h2 className="text-xl sm:text-2xl font-extrabold text-[#4b3b35] font-hand">
              🎉 恭喜！你完成了所有記憶卡片！
            </h2>
            <p className="text-sm text-[#8a7066]">
              你已經成功複習並掌握了本區間的所有臨床秒殺 buzzwords。
            </p>
          </div>
          <button
            type="button"
            onClick={handleResetDeck}
            className="px-6 py-2.5 bg-[#b8527a] text-white font-bold rounded-xl hover:bg-[#9a3d60] transition cursor-pointer shadow-md flex items-center gap-2 mx-auto"
          >
            <RotateCcw size={16} />
            再挑戰一次
          </button>
        </div>
      )}
    </div>
  );
}
