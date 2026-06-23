import { AlertTriangle, BookOpen, Lightbulb, Star } from "lucide-react";
import type { DiseaseComparisonGroup } from "../../types/disease";

interface DiseaseComparisonProps {
  group: DiseaseComparisonGroup;
  currentQuestionId?: string;
}

export function DiseaseComparison({ group, currentQuestionId }: DiseaseComparisonProps) {
  // Helper to escape regex special characters
  const escapeRegExp = (string: string) => {
    return string.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  };

  // Helper to highlight matching keywords inside a text
  const renderHighlightedText = (text: string, keywords: string[]) => {
    if (!text) return "";
    if (!keywords || keywords.length === 0) return text;

    // Sort keywords by length descending to match longer phrases first
    const sortedKeywords = [...keywords].sort((a, b) => b.length - a.length);
    const escapedKeywords = sortedKeywords.map(escapeRegExp);
    const regex = new RegExp(`(${escapedKeywords.join("|")})`, "gi");

    const parts = text.split(regex);

    return parts.map((part, i) => {
      const isMatch = sortedKeywords.some(
        (kw) => kw.toLowerCase() === part.toLowerCase()
      );
      return isMatch ? (
        <span key={i} className="highlight-text">
          {part}
        </span>
      ) : (
        part
      );
    });
  };

  // Helper to parse question ID into a readable display string
  // e.g. "111-1_medicine-2_093" -> "111-1 醫學（二） 第 93 題"
  const formatQuestionTitle = (id: string) => {
    const parts = id.split("_");
    if (parts.length < 3) return id;
    
    const year = parts[0];
    const subjectRaw = parts[1];
    const num = parseInt(parts[2], 10);

    let subjectDisplay = subjectRaw;
    if (subjectRaw.startsWith("medicine-")) {
      const subNum = subjectRaw.split("-")[1];
      const romanMap: Record<string, string> = {
        "1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六"
      };
      subjectDisplay = `醫學（${romanMap[subNum] || subNum}）`;
    }

    return `${year} ${subjectDisplay} 第 ${num} 題`;
  };

  const handleQuestionClick = (qId: string) => {
    const parts = qId.split("_");
    if (parts.length < 2) return;
    const examId = `${parts[0]}_${parts[1]}`;
    
    // Call the global openQuestion handler attached to window
    const openQuestionFn = (window as any).__openQuestion;
    if (typeof openQuestionFn === "function") {
      openQuestionFn(examId, qId);
    } else {
      // Fallback: if it's the current exam, just hash scroll
      const target = document.getElementById(qId);
      if (target) {
        target.scrollIntoView({ behavior: "smooth", block: "start" });
        window.location.hash = qId;
      }
    }
  };

  // Find all feature dimensions from the two diseases
  const featureKeys = Array.from(
    new Set([
      ...Object.keys(group.diseases[0].features || {}),
      ...Object.keys(group.diseases[1].features || {}),
    ])
  );

  return (
    <div className="mt-5 rounded-[1.3rem] border border-[#f1aac8]/70 bg-white/92 p-5 shadow-[0_12px_40px_rgba(241,170,200,0.12)] backdrop-blur-md">
      {/* Header */}
      <div className="flex flex-wrap items-start justify-between gap-3 border-b border-[#f1aac8]/30 pb-3">
        <div>
          <span className="inline-flex items-center gap-1 rounded-full bg-[#fdf0f4] px-2.5 py-0.5 text-xs font-bold text-[#b8527a]">
            🧠 經典比較表格統整
          </span>
          <h3 className="mt-2 text-base font-bold text-[#6f4054] sm:text-lg">
            {group.title}
          </h3>
          <p className="mt-1 text-xs text-[#a68e98]">{group.category}</p>
        </div>

        <div className="flex items-center gap-1 rounded-full bg-[#fffcf0] border border-[#fceeac] px-2.5 py-1 text-xs font-bold text-[#9e7a28]">
          <Star size={13} className="fill-[#fcd116] text-[#e0b016]" />
          <span>國考熱度 {group.exam_importance}</span>
        </div>
      </div>

      {/* Focus Tips & Traps */}
      <div className="mt-4 grid gap-3 sm:grid-cols-2">
        <div className="rounded-[0.95rem] border border-[#fceeac] bg-[#fffcf2]/80 p-3.5 shadow-sm">
          <div className="flex items-center gap-1.5 text-xs font-bold text-[#8c6b23]">
            <Lightbulb size={15} className="text-[#d89e1b]" />
            秒殺考點口訣
          </div>
          <p className="mt-2 text-xs leading-5 text-[#725e3c]">
            {group.exam_focus_tips}
          </p>
        </div>

        <div className="rounded-[0.95rem] border border-[#f9ccd6] bg-[#fdf3f5]/80 p-3.5 shadow-sm">
          <div className="flex items-center gap-1.5 text-xs font-bold text-[#9c3e5e]">
            <AlertTriangle size={15} className="text-[#c45378]" />
            常見考題陷阱
          </div>
          <p className="mt-2 text-xs leading-5 text-[#865466]">
            {group.common_traps}
          </p>
        </div>
      </div>

      {/* Comparison Table */}
      <div className="mt-4 overflow-hidden rounded-xl border border-[#ebdbe2] bg-white/70">
        <div className="overflow-x-auto">
          <table className="w-full border-collapse text-left text-xs">
            <thead>
              <tr className="border-b border-[#ebdbe2] bg-[#fbf7f9] text-[#705662] font-semibold">
                <th className="w-[18%] px-3 py-2.5 font-bold">比較維度</th>
                <th className="w-[41%] px-3 py-2.5 border-l border-[#ebdbe2]">
                  {group.diseases[0].name}
                </th>
                <th className="w-[41%] px-3 py-2.5 border-l border-[#ebdbe2]">
                  {group.diseases[1].name}
                </th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[#ebdbe2] text-[#604e57]">
              {featureKeys.map((key) => {
                const valA = group.diseases[0].features[key] || "—";
                const valB = group.diseases[1].features[key] || "—";
                return (
                  <tr key={key} className="hover:bg-[#fdfafb]/50 transition">
                    <td className="px-3 py-2.5 font-bold text-[#866e7b] bg-[#fcf9fa]/30">
                      {key}
                    </td>
                    <td className="px-3 py-2.5 border-l border-[#ebdbe2] leading-5">
                      {renderHighlightedText(valA, group.highlight_keywords)}
                    </td>
                    <td className="px-3 py-2.5 border-l border-[#ebdbe2] leading-5">
                      {renderHighlightedText(valB, group.highlight_keywords)}
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>

      {/* Related Questions */}
      {group.related_questions && group.related_questions.length > 0 && (
        <div className="mt-4 border-t border-[#ebdbe2]/40 pt-3">
          <div className="flex items-center gap-1.5 text-xs font-bold text-[#866e7b]">
            <BookOpen size={14} />
            延伸演練：相關歷屆國考題
          </div>
          <div className="mt-2 flex flex-wrap gap-2">
            {group.related_questions.map((rq) => {
              const isCurrent = rq.question_id === currentQuestionId;
              return (
                <button
                  key={rq.question_id}
                  type="button"
                  onClick={() => handleQuestionClick(rq.question_id)}
                  disabled={isCurrent}
                  className={`inline-flex items-center gap-1 rounded-lg border px-2.5 py-1 text-xs font-medium transition cursor-pointer ${
                    isCurrent
                      ? "border-[#b8527a] bg-[#fdf0f4] text-[#b8527a] cursor-default font-bold"
                      : "border-[#e0ccd5] bg-white text-[#6f4054] hover:bg-[#fdfafb] hover:border-[#c5a6b4]"
                  }`}
                  title={rq.note}
                >
                  {formatQuestionTitle(rq.question_id)}
                  {isCurrent && <span className="text-[10px] bg-[#b8527a] text-white px-1 rounded-sm ml-0.5">本題</span>}
                </button>
              );
            })}
          </div>
        </div>
      )}
    </div>
  );
}
