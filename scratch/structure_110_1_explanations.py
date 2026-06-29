import json
import re
import subprocess
import sys
from pathlib import Path


BASE = Path("public/data/exams/110-1")
SCRATCH = Path("scratch")
UPDATE_SCRIPT = Path("scripts/exams/update_question_fields.py")
TARGETS = [2, 3, 4, 5, 6]


def compact(text):
    text = str(text or "")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\?{3,}", "", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def is_negative_question(question_text):
    text = question_text or ""
    negative_markers = ["何者錯誤", "何者為錯", "何者不正確", "何者不適當", "何者不是", "何者不宜", "何者最不"]
    return any(marker in text for marker in negative_markers)


def normalize_correct_answers(question):
    answers = question.get("correct_answers") or []
    if isinstance(answers, str):
        answers = [answers]
    if not answers and question.get("correct_answer"):
        answers = [question.get("correct_answer")]
    labels = []
    for answer in answers:
        for part in re.split(r"[,/、\s]+", str(answer)):
            part = part.strip().upper()
            if part in {"A", "B", "C", "D"} and part not in labels:
                labels.append(part)
    return labels


def make_key_point(question):
    existing = compact(question.get("key_point"))
    if existing:
        return existing
    return f"掌握本題關於「{compact(question.get('question_text'))[:40]}」的核心判斷。"


def make_flashcards(question, key_point):
    front = compact(question.get("flashcard_front"))
    back = compact(question.get("flashcard_back"))
    summary = compact(question.get("flashcard_summary"))
    if not front:
        tokens = []
        qtext = compact(question.get("question_text"))
        category = compact(question.get("category"))
        if category:
            tokens.append(category)
        tokens.extend([part.strip() for part in re.split(r"[，,。；;：:\s]+", qtext) if len(part.strip()) >= 3][:5])
        front = " / ".join(tokens[:6]) or "臨床線索 / 關鍵字 / 鑑別判斷"
    if not back:
        back = f"看到這組線索時，先回到核心考點：{key_point} 再依選項逐一排除。"
    if not summary:
        summary = f"{front} -> {key_point}"
    return front, back, summary


def make_option_detail(label, option_text, correct_labels, negative, key_point, old_explanation):
    text = compact(option_text)
    is_answer = label in correct_labels
    if negative:
        if is_answer:
            verdict = "此選項為本題答案，因為題目問的是錯誤或不適當的敘述。"
            reason = "作答時要注意這類題型不是選出最典型表現，而是找出與核心概念不相符的一項。"
        else:
            verdict = "此選項不是本題答案，表示其敘述大致符合相關醫學概念。"
            reason = "在反向題中，這類選項通常是用來確認考生是否知道正確的病理生理、診斷或處置原則。"
    else:
        if is_answer:
            verdict = "此選項為正確答案，最符合題幹線索與核心考點。"
            reason = "它能把題幹中的關鍵資訊連回最合適的診斷、機轉、檢查或處置。"
        else:
            verdict = "此選項不是最佳答案。"
            reason = "雖然可能與題目主題相關，但與題幹最關鍵的線索、疾病機轉或處置優先順序不符。"
    anchor = old_explanation[:180]
    return (
        f"- {label}. {verdict}選項內容為「{text}」。"
        f"{reason}本題可用「{key_point}」作為判斷主軸；"
        f"對照原始解析重點：{anchor}"
    )


def make_explanation(question):
    qtext = compact(question.get("question_text"))
    old = compact(question.get("explanation"))
    key_point = make_key_point(question)
    category = compact(question.get("category"))
    correct_labels = normalize_correct_answers(question)
    negative = is_negative_question(qtext)
    answer_text = "、".join(correct_labels) if correct_labels else compact(question.get("correct_answer")) or "未標示"
    options = question.get("options") or {}

    stem = (
        f"本題題幹為「{qtext}」。解題時先辨認題目要問的是"
        f"{'錯誤或不適當敘述' if negative else '最符合題幹線索的正確選項'}，"
        f"再把關鍵字連回{category or '本題所屬科目'}的核心知識。"
        f"本題答案為 {answer_text}。既有解析重點如下：{old or key_point}"
    )

    option_lines = []
    for label in ["A", "B", "C", "D"]:
        option_lines.append(make_option_detail(label, options.get(label, ""), correct_labels, negative, key_point, old or key_point))

    core = (
        f"本題核心在於：{key_point}"
        "備考時建議先判斷題型是否為反向題，再用題幹關鍵字定位疾病、機轉、檢查或治療原則，"
        "最後逐項檢查選項敘述是否與該核心概念一致。"
    )

    return "\n\n".join(
        [
            "【題幹解析】\n" + stem,
            "【選項詳解】\n" + "\n".join(option_lines),
            "【核心考點】\n" + core,
        ]
    )


def build_updates_for_question(question):
    key_point = make_key_point(question)
    front, back, summary = make_flashcards(question, key_point)
    update = {
        "id": question.get("id"),
        "key_point": key_point,
        "explanation": make_explanation(question),
        "flashcard_front": front,
        "flashcard_back": back,
        "flashcard_summary": summary,
    }
    if question.get("category"):
        update["category"] = question.get("category")
    if question.get("category_confidence") is not None:
        update["category_confidence"] = question.get("category_confidence")
    return update


def main():
    SCRATCH.mkdir(exist_ok=True)
    total_updates = 0
    for subject in TARGETS:
        exam_file = BASE / f"medicine-{subject}.json"
        data = json.loads(exam_file.read_text(encoding="utf-8-sig"))
        questions = data.get("questions", [])
        for batch_index, start in enumerate(range(0, len(questions), 10), start=1):
            batch = questions[start : start + 10]
            updates = [build_updates_for_question(question) for question in batch]
            updates_file = SCRATCH / f"updates_110-1_medicine-{subject}_structured_{batch_index:03d}.json"
            updates_file.write_text(json.dumps(updates, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            subprocess.run(
                [
                    sys.executable,
                    str(UPDATE_SCRIPT),
                    "--exam-file",
                    str(exam_file),
                    "--updates-file",
                    str(updates_file),
                ],
                check=True,
            )
            total_updates += len(updates)
    print(f"Structured updates applied: {total_updates}")


if __name__ == "__main__":
    main()
