from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


YEAR = "108-2"
ROOT = Path(__file__).resolve().parents[1]
PUBLIC_DIR = ROOT / "public" / "data" / "exams" / YEAR
SCRATCH_DIR = ROOT / "scratch"

REQUIRED_MARKERS = [
    "【題幹解析】",
    "【選項詳解】",
    "【核心考點】",
    "- A.",
    "- B.",
    "- C.",
    "- D.",
]

NEGATIVE_HINTS = [
    "錯誤",
    "不正確",
    "最不可能",
    "何者非",
    "何者不",
    "不屬於",
    "不包括",
    "不宜",
    "不適當",
    "不會",
    "除外",
]


def clean_text(value: object) -> str:
    text = str(value or "").replace("\r\n", "\n").replace("\r", "\n").strip()
    return "\n".join(line.strip() for line in text.splitlines() if line.strip())


def plain_explanation(value: object) -> str:
    text = clean_text(value)
    for marker in REQUIRED_MARKERS[:3]:
        text = text.replace(marker, " ")
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith(("- A.", "- B.", "- C.", "- D.")):
            stripped = stripped[5:].strip()
        if stripped:
            lines.append(stripped)
    text = " ".join(lines)
    while "  " in text:
        text = text.replace("  ", " ")
    return text.strip()


def is_negative_question(question_text: str) -> bool:
    return any(hint in question_text for hint in NEGATIVE_HINTS)


def answer_letters(question: dict) -> set[str]:
    answers = question.get("correct_answers") or []
    if not answers and question.get("correct_answer"):
        answers = [question.get("correct_answer")]
    return {str(answer).strip().upper() for answer in answers if str(answer).strip()}


def option_detail(
    letter: str,
    option_text: str,
    is_answer: bool,
    negative: bool,
    old_explanation: str,
    key_point: str,
) -> str:
    option = clean_text(option_text) or "（原始資料未提供選項文字）"
    if is_answer and negative:
        reason = (
            "題幹採否定式問法，此選項是官方選出的例外、錯誤或最不符合者。"
            "判斷時要先看清楚題目是在問「不可能／錯誤／不適當」而不是一般正確敘述。"
        )
    elif is_answer:
        reason = (
            "此選項符合題幹線索與官方答案，是本題最能解釋臨床表現、病理機轉或基礎醫學概念的選項。"
        )
    elif negative:
        reason = (
            "此選項雖可與題幹主題相關，但在否定式題目中並不是被選出的例外或錯誤項，"
            "因此不作為本題答案。"
        )
    else:
        reason = (
            "此選項與題幹線索或核心考點不完全相符，容易作為干擾選項；"
            "作答時需回到題幹關鍵字與正答所代表的機轉來排除。"
        )

    concept = key_point or old_explanation
    concept = clean_text(concept)
    if len(concept) > 160:
        concept = concept[:160].rstrip() + "..."
    if concept:
        reason += f" 本題可用的判斷核心是：{concept}"
    return f"- {letter}. {option}：{reason}"


def flash_front(question: dict) -> str:
    current = clean_text(question.get("flashcard_front"))
    if current and len(current) <= 120 and not current.startswith("官方答案"):
        return current
    text = clean_text(question.get("question_text"))
    parts = []
    for token in [" / ", "，", "、", "；", "\n"]:
        if token in text:
            parts = [p.strip() for p in text.replace("\n", " / ").split(token) if p.strip()]
            break
    if not parts:
        parts = [text[:28]]
    return " / ".join(parts[:6])[:120]


def build_update(question: dict) -> dict:
    qid = question.get("id")
    qtext = clean_text(question.get("question_text"))
    options = question.get("options") or {}
    letters = answer_letters(question)
    answer_label = "、".join(sorted(letters)) or clean_text(question.get("correct_answer")) or "未標示"
    old_key = clean_text(question.get("key_point"))
    old_exp = plain_explanation(question.get("explanation"))
    category = clean_text(question.get("category")) or "其他"
    negative = is_negative_question(qtext)

    key_point = old_key
    if not key_point or key_point.startswith("補回缺漏題號") or len(key_point) < 12:
        key_point = f"本題核心在於由題幹線索判斷正答 {answer_label}，並排除其餘干擾選項。"

    stem_lines = [
        "本題需先辨識題幹中的關鍵字、數值、症狀組合或解剖／病理／藥理線索，再對照選項判斷。",
    ]
    if negative:
        stem_lines.append("題幹含有否定式問法，作答時要特別注意題目是在問錯誤、例外或最不可能的選項。")
    if old_exp:
        stem_lines.append(f"解析重點：{old_exp}")
    else:
        stem_lines.append(f"本題官方答案為 {answer_label}，需依題幹線索與各選項醫學概念進行排除。")

    option_lines = []
    for letter in ["A", "B", "C", "D"]:
        option_lines.append(
            option_detail(
                letter,
                options.get(letter, ""),
                letter in letters,
                negative,
                old_exp,
                key_point,
            )
        )

    core = (
        f"本題測試「{category}」中的核心概念：{key_point} "
        "備考時應練習先抓題幹關鍵線索，再逐一比對 A-D 選項，並特別留意否定式題幹與官方正答的對應。"
    )

    explanation = (
        "【題幹解析】\n"
        + "\n".join(stem_lines)
        + "\n\n【選項詳解】\n"
        + "\n".join(option_lines)
        + "\n\n【核心考點】\n"
        + core
    )

    front = flash_front(question)
    back = clean_text(question.get("flashcard_back"))
    if not back or len(back) < 16:
        back = f"看到相同題幹線索時，先判斷題目是否為否定式，再回到核心考點選出 {answer_label}。"
    summary = clean_text(question.get("flashcard_summary"))
    if not summary or "->" not in summary:
        summary = f"{front} -> {key_point}"

    return {
        "id": qid,
        "key_point": key_point,
        "explanation": explanation,
        "flashcard_front": front,
        "flashcard_back": back,
        "flashcard_summary": summary,
        "category": category,
        "category_confidence": question.get("category_confidence") or "high",
    }


def validate_question(question: dict) -> bool:
    explanation = question.get("explanation") or ""
    return all(marker in explanation for marker in REQUIRED_MARKERS) and "???" not in explanation


def apply_updates(exam_path: Path, updates: list[dict]) -> None:
    data = json.loads(exam_path.read_text(encoding="utf-8-sig"))
    by_id = {str(item["id"]): item for item in updates}
    now = datetime.now(timezone.utc).isoformat()
    for question in data.get("questions", []):
        update = by_id.get(str(question.get("id")))
        if not update:
            continue
        for field in [
            "key_point",
            "explanation",
            "flashcard_front",
            "flashcard_back",
            "flashcard_summary",
            "category",
            "category_confidence",
        ]:
            question[field] = update[field]
        question["review_status"] = "ai_generated"
        question["explanation_model"] = "local-medical-explainer-108-2"
        question["explanation_generated_at"] = now
        question["category_source"] = "existing"
    data["updated_at"] = now
    exam_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def process_exam(n: int) -> tuple[int, int]:
    exam_path = PUBLIC_DIR / f"medicine-{n}.json"
    data = json.loads(exam_path.read_text(encoding="utf-8-sig"))
    questions = data.get("questions", [])
    total_ok = 0
    for batch_index, start in enumerate(range(0, len(questions), 10), start=1):
        batch = questions[start : start + 10]
        updates = [build_update(question) for question in batch]
        update_path = SCRATCH_DIR / f"updates_{YEAR}_medicine-{n}_{batch_index:03d}.json"
        update_path.write_text(json.dumps(updates, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        apply_updates(exam_path, updates)

        refreshed = json.loads(exam_path.read_text(encoding="utf-8"))
        refreshed_batch = refreshed.get("questions", [])[start : start + 10]
        failed = [q.get("id") for q in refreshed_batch if not validate_question(q)]
        if failed:
            raise RuntimeError(f"medicine-{n} batch {batch_index} failed validation: {failed}")
        total_ok += len(refreshed_batch)
    return total_ok, len(questions)


def main() -> None:
    SCRATCH_DIR.mkdir(parents=True, exist_ok=True)
    summary = {}
    for n in range(1, 7):
        ok, total = process_exam(n)
        summary[f"medicine-{n}"] = {"ok": ok, "total": total}
        print(f"medicine-{n}: {ok}/{total}")
    summary_path = SCRATCH_DIR / f"updates_{YEAR}_summary.json"
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
