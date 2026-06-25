import { useState, useEffect } from "react";
import { Check, X, AlertTriangle, RefreshCcw, Sparkles, BookOpen, ChevronRight, HelpCircle } from "lucide-react";

interface TrapQuestion {
  id: string;
  category: string;
  source: string;
  source_id: string;
  source_type: "guideline" | "comparison";
  statement: string;
  is_trap: boolean;
  explanation: string;
}

interface TrapSpotterQuizProps {
  theme: string;
  onJumpToGuideline?: (sourceType: "guideline" | "comparison", sourceId: string) => void;
}

export function TrapSpotterQuiz({ theme, onJumpToGuideline }: TrapSpotterQuizProps) {
  const [allQuestions, setAllQuestions] = useState<TrapQuestion[]>([]);
  const [quizQuestions, setQuizQuestions] = useState<TrapQuestion[]>([]);
  const [currentIndex, setCurrentIndex] = useState<number>(0);
  const [selectedAnswer, setSelectedAnswer] = useState<boolean | null>(null); // true = Correct Concept, false = Trap
  const [showFeedback, setShowFeedback] = useState<boolean>(false);
  const [correctCount, setCorrectCount] = useState<number>(0);
  const [wrongQuestionIds, setWrongQuestionIds] = useState<string[]>([]);
  const [isFinished, setIsFinished] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(true);
  const [selectedReviewId, setSelectedReviewId] = useState<string | null>(null);

  // Fetch Questions from public JSON
  useEffect(() => {
    const fetchQuestions = async () => {
      try {
        const base = import.meta.env.BASE_URL || "/";
        const cleanBase = base.endsWith("/") ? base : `${base}/`;
        const res = await fetch(`${cleanBase}data/trap_questions.json`);
        if (!res.ok) throw new Error("Load failed");
        const data = await res.json();
        setAllQuestions(data.questions);
        
        // Shuffle and set current quiz questions
        const shuffled = [...data.questions].sort(() => Math.random() - 0.5);
        setQuizQuestions(shuffled);
        setLoading(false);
      } catch (err) {
        console.error("Failed to load trap questions", err);
        setLoading(false);
      }
    };

    fetchQuestions();
  }, []);

  // Get current question
  const currentQuestion = quizQuestions[currentIndex] || null;

  // Handle User Selection
  const handleAnswerSelect = (answer: boolean) => {
    if (showFeedback) return;
    setSelectedAnswer(answer);
    setShowFeedback(true);

    const isCorrect = answer === !currentQuestion.is_trap;
    if (isCorrect) {
      setCorrectCount((prev) => prev + 1);
    } else {
      setWrongQuestionIds((prev) => [...prev, currentQuestion.id]);
    }
  };

  // Move to next question
  const handleNext = () => {
    setSelectedAnswer(null);
    setShowFeedback(false);
    if (currentIndex + 1 < quizQuestions.length) {
      setCurrentIndex((prev) => prev + 1);
    } else {
      setIsFinished(true);
    }
  };

  // Reset/Restart Quiz
  const handleRestart = (onlyMistakes = false) => {
    setSelectedAnswer(null);
    setShowFeedback(false);
    setIsFinished(false);
    setSelectedReviewId(null);
    
    if (onlyMistakes) {
      const mistakes = allQuestions.filter((q) => wrongQuestionIds.includes(q.id));
      setQuizQuestions(mistakes.sort(() => Math.random() - 0.5));
    } else {
      setQuizQuestions([...allQuestions].sort(() => Math.random() - 0.5));
    }
    
    setCurrentIndex(0);
    setCorrectCount(0);
    setWrongQuestionIds([]);
  };

  if (loading) {
    return (
      <div className="flex flex-col items-center justify-center py-16 space-y-4">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-[#b8527a]" />
        <p className="text-xs text-[#8a7066] font-hand">正在載入避雷針試題資料庫...</p>
      </div>
    );
  }

  // Finished View
  if (isFinished) {
    const wrongQuestions = allQuestions.filter((q) => wrongQuestionIds.includes(q.id));
    const scorePercent = Math.round((correctCount / quizQuestions.length) * 100) || 0;
    
    // Performance assessment title
    let scoreTitle = "避雷菜鳥";
    let scoreDesc = "還需要加強喔！常考的誘答選項容易讓你混淆。";
    if (scorePercent >= 90) {
      scoreTitle = "完美避雷神探";
      scoreDesc = "太強了！你成功避開了所有國考雷區，完美掌握所有陷阱！";
    } else if (scorePercent >= 70) {
      scoreTitle = "避雷達人";
      scoreDesc = "表現優異！大部分的常見考點陷阱都難不倒你。";
    } else if (scorePercent >= 40) {
      scoreTitle = "避雷新手";
      scoreDesc = "有一些進步空間，多複習幾次就能輕鬆避開雷區。";
    }

    const activeReviewQuestion = wrongQuestions.find((q) => q.id === selectedReviewId) || wrongQuestions[0] || null;

    return (
      <div className="max-w-3xl mx-auto space-y-6">
        {/* Score Card */}
        <div className="bg-white/70 p-6 sm:p-8 rounded-3xl border border-white/90 shadow-sm backdrop-blur-xl text-center space-y-4">
          <div className="inline-flex items-center justify-center w-16 h-16 rounded-full bg-[#fdf0f4] text-[#b8527a]">
            <Sparkles size={32} />
          </div>
          
          <div className="space-y-1">
            <div className="text-[10px] font-extrabold text-[#b8527a] tracking-wider uppercase">特訓成果結算</div>
            <h2 className="text-xl sm:text-2xl font-extrabold text-[#4b3b35] font-hand">
              {scoreTitle} ({scorePercent}分)
            </h2>
            <p className="text-xs sm:text-sm text-[#8a7066] max-w-md mx-auto">{scoreDesc}</p>
          </div>

          <div className="flex justify-center gap-4 text-xs font-bold py-2 border-y border-[#efd9d0]/40 max-w-sm mx-auto">
            <span className="text-[#16a34a]">答對：{correctCount} 題</span>
            <span className="text-[#a7948a]">|</span>
            <span className="text-[#e53e3e]">答錯：{wrongQuestionIds.length} 題</span>
          </div>

          {/* Action Buttons */}
          <div className="flex justify-center gap-3 pt-2">
            <button
              type="button"
              onClick={() => handleRestart(false)}
              className="px-5 py-2.5 bg-[#b8527a] text-white font-bold rounded-xl hover:bg-[#9a3d60] transition cursor-pointer shadow-xs text-xs flex items-center gap-1.5"
            >
              <RefreshCcw size={13} />
              再挑戰一次
            </button>
            {wrongQuestionIds.length > 0 && (
              <button
                type="button"
                onClick={() => handleRestart(true)}
                className="px-5 py-2.5 bg-[#fff5f5] text-[#e53e3e] border border-[#fecaca] font-bold rounded-xl hover:bg-[#ffe3e3] transition cursor-pointer text-xs flex items-center gap-1.5"
              >
                <AlertTriangle size={13} />
                僅重練錯題
              </button>
            )}
          </div>
        </div>

        {/* Mistake Review Panel */}
        {wrongQuestions.length > 0 && (
          <div className="grid md:grid-cols-[240px_1fr] gap-6 items-start bg-white/50 p-4 rounded-3xl border border-white/80 shadow-xs backdrop-blur-md">
            {/* Sidebar list of wrong questions */}
            <aside className="space-y-3">
              <h3 className="text-xs font-extrabold text-[#e53e3e] border-b border-[#efd9d0]/50 pb-2 px-1 flex items-center gap-1">
                <AlertTriangle size={14} />
                錯題排查名單
              </h3>
              <ul className="space-y-1 max-h-[300px] overflow-y-auto pr-1">
                {wrongQuestions.map((q, idx) => (
                  <li key={q.id}>
                    <button
                      type="button"
                      onClick={() => setSelectedReviewId(q.id)}
                      className={`w-full text-left p-2 rounded-lg text-xs font-bold transition break-words whitespace-normal cursor-pointer ${
                        (selectedReviewId === q.id || (selectedReviewId === null && idx === 0))
                          ? "bg-[#fff5f5] text-[#e53e3e]"
                          : "text-[#6f5b50] hover:bg-white"
                      }`}
                    >
                      {idx + 1}. {q.source.split(" (")[0]}
                    </button>
                  </li>
                ))}
              </ul>
            </aside>

            {/* Wrong Question Detail Panel */}
            {activeReviewQuestion && (
              <div className="bg-white/80 p-5 rounded-2xl border border-white shadow-xs space-y-4">
                <div className="flex items-center justify-between border-b border-[#efd9d0]/30 pb-2.5">
                  <span className="text-[10px] font-extrabold text-[#e53e3e] tracking-wider bg-[#fff5f5] px-2 py-0.5 rounded-md">
                    {activeReviewQuestion.category.split(" / ")[0]}
                  </span>
                  <span className="text-xs text-[#a7948a] font-hand font-bold">
                    來自：{activeReviewQuestion.source}
                  </span>
                </div>

                <div className="space-y-1">
                  <h4 className="text-xs font-extrabold text-[#9c7b70]">【題目敘述】</h4>
                  <p className="text-sm font-semibold text-[#4b3b35] bg-[#fcf9f8] p-3 rounded-xl border border-[#efd9d0]/30 leading-relaxed">
                    {activeReviewQuestion.statement}
                  </p>
                </div>

                <div className="space-y-1.5">
                  <h4 className="text-xs font-extrabold text-[#e53e3e] flex items-center gap-1">
                    <AlertTriangle size={14} />
                    【避雷解析：為何錯誤？】
                  </h4>
                  <p className="text-xs sm:text-sm text-[#713f12] bg-[#fffbeb] p-3 sm:p-4 rounded-xl border border-[#fde68a] leading-relaxed">
                    {activeReviewQuestion.explanation}
                  </p>
                </div>

                {onJumpToGuideline && (
                  <button
                    type="button"
                    onClick={() => onJumpToGuideline(activeReviewQuestion.source_type, activeReviewQuestion.source_id)}
                    className="w-full py-2 bg-[#fdf0f4] hover:bg-[#fbdde8] text-[#b8527a] text-xs font-bold rounded-xl transition flex items-center justify-center gap-1.5 border border-[#fbdde8] cursor-pointer"
                  >
                    <BookOpen size={13} />
                    查看關聯首選指引 / 經典鑑別對照
                  </button>
                )}
              </div>
            )}
          </div>
        )}
      </div>
    );
  }

  // Active Quiz View
  const isTrapAnswer = !currentQuestion.is_trap; // true if Correct Concept, false if Trap
  const userGotItRight = selectedAnswer !== null && selectedAnswer === isTrapAnswer;

  return (
    <div className="max-w-2xl mx-auto space-y-6">
      {/* Quiz Progress */}
      <div className="space-y-2">
        <div className="flex justify-between text-xs font-bold text-[#8a7066]">
          <span>避雷挑戰中：第 {currentIndex + 1} / {quizQuestions.length} 題</span>
          <span>避雷成功率：{correctCount} / {currentIndex + (showFeedback ? 1 : 0)} 題</span>
        </div>
        <div className="w-full bg-[#efd9d0]/60 h-2 rounded-full overflow-hidden">
          <div
            className="bg-linear-to-r from-[#e49bb0] to-[#b8527a] h-full transition-all duration-300"
            style={{ width: `${((currentIndex + (showFeedback ? 1 : 0)) / quizQuestions.length) * 100}%` }}
          />
        </div>
      </div>

      {/* Main Question Card */}
      <div className="bg-white/80 rounded-3xl border border-white shadow-[0_12px_40px_rgba(181,133,117,0.06)] overflow-hidden">
        {/* Card Header */}
        <div className="p-4 sm:p-5 border-b border-[#efd9d0]/50 bg-linear-to-r from-[#fdfbfb] to-[#fdf9f8] flex items-center justify-between">
          <span className="text-[10px] sm:text-xs font-extrabold text-[#b8527a] tracking-wider bg-[#fdf0f4] px-2 py-0.5 rounded-md">
            {currentQuestion.category.split(" / ")[0]}
          </span>
          <span className="text-xs text-[#a7948a] font-hand font-bold">
            考點來源：{currentQuestion.source.split(" (")[0]}
          </span>
        </div>

        {/* Card Body - Statement */}
        <div className="p-6 sm:p-8 space-y-6">
          <div className="space-y-3 text-center">
            <HelpCircle size={24} className="mx-auto text-[#a7948a]/60" />
            <h3 className="text-xs sm:text-sm font-extrabold tracking-wider text-[#9c7b70] uppercase">
              請判定以下臨床敘述是「國考陷阱」或是「正確觀念」：
            </h3>
          </div>

          <div className="bg-[#fcf9f8] p-5 sm:p-6 rounded-2xl border border-[#efd9d0]/40 shadow-inner">
            <p className="text-sm sm:text-base font-extrabold text-[#4b3b35] leading-relaxed text-center font-hand">
              「 {currentQuestion.statement} 」
            </p>
          </div>

          {/* Option Buttons (Visible when not answered) */}
          {!showFeedback && (
            <div className="flex gap-4 pt-2">
              <button
                type="button"
                onClick={() => handleAnswerSelect(false)}
                className="flex-1 py-4 px-3 sm:px-4 rounded-2xl bg-[#fff5f5] hover:bg-[#ffe3e3] border border-[#fecaca] text-[#e53e3e] font-extrabold text-sm sm:text-base flex flex-col items-center justify-center gap-1.5 transition cursor-pointer shadow-xs active:scale-98"
              >
                <X size={20} className="stroke-[3]" />
                <span>這是國考陷阱！</span>
                <span className="text-[10px] font-normal opacity-70">（敘述含有誘答錯誤）</span>
              </button>
              <button
                type="button"
                onClick={() => handleAnswerSelect(true)}
                className="flex-1 py-4 px-3 sm:px-4 rounded-2xl bg-[#f0fdf4] hover:bg-[#dcfce7] border border-[#bbf7d0] text-[#16a34a] font-extrabold text-sm sm:text-base flex flex-col items-center justify-center gap-1.5 transition cursor-pointer shadow-xs active:scale-98"
              >
                <Check size={20} className="stroke-[3]" />
                <span>這是正確觀念！</span>
                <span className="text-[10px] font-normal opacity-70">（敘述正確無雷）</span>
              </button>
            </div>
          )}

          {/* Feedback & Explanation Panel (Visible after answered) */}
          {showFeedback && (
            <div
              className={`p-5 sm:p-6 rounded-2xl border transition-all duration-300 space-y-4 animate-fadeIn ${
                userGotItRight
                  ? "bg-[#f0fdf4] border-[#bbf7d0] text-[#16a34a]"
                  : "bg-[#fff5f5] border-[#fecaca] text-[#e53e3e]"
              }`}
            >
              <div className="flex items-center gap-2">
                {userGotItRight ? (
                  <>
                    <Check size={20} className="stroke-[3]" />
                    <span className="text-sm sm:text-base font-extrabold">🎉 恭喜答對！你成功避開了國考雷區！</span>
                  </>
                ) : (
                  <>
                    <AlertTriangle size={20} className="stroke-[3]" />
                    <span className="text-sm sm:text-base font-extrabold">⚠️ 踩中雷區！這是典型的國考誘答陷阱！</span>
                  </>
                )}
              </div>

              {/* Detail Explanation */}
              <div className="bg-white/80 p-4 rounded-xl border border-black/5 text-[#6f5b50] space-y-2">
                <h4 className="text-xs font-extrabold text-[#4b3b35] flex items-center gap-1">
                  <BookOpen size={14} className="text-[#b8527a]" />
                  避雷核心解析 (Explanation)
                </h4>
                <p className="text-xs sm:text-sm leading-relaxed font-semibold">
                  {currentQuestion.explanation}
                </p>
              </div>

              {/* Guideline Link & Next Button */}
              <div className="flex flex-wrap items-center justify-between gap-3 pt-2">
                {onJumpToGuideline ? (
                  <button
                    type="button"
                    onClick={() => onJumpToGuideline(currentQuestion.source_type, currentQuestion.source_id)}
                    className="py-2 px-4 bg-white hover:bg-white/90 text-[#b8527a] hover:text-[#9a3d60] border border-[#efd9d0] hover:border-[#b8527a]/30 text-xs font-bold rounded-xl transition flex items-center gap-1.5 cursor-pointer"
                  >
                    <BookOpen size={13} />
                    查看關聯首選指引
                  </button>
                ) : (
                  <div />
                )}
                <button
                  type="button"
                  onClick={handleNext}
                  className="py-2 px-5 bg-[#b8527a] hover:bg-[#9a3d60] text-white text-xs font-bold rounded-xl transition flex items-center gap-1 cursor-pointer shadow-xs active:scale-98"
                >
                  <span>下一題</span>
                  <ChevronRight size={13} />
                </button>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
