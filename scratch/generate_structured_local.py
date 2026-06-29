import json
import pathlib
import re


BASE = pathlib.Path("public/data/exams/110-2")
OUT = pathlib.Path("scratch")
REPORTS = pathlib.Path("reports/gemini_outputs")


def clean(value):
    text = "" if value is None else str(value)
    text = text.replace("\r\n", "\n").replace("\r", "\n").strip()
    text = re.sub(r"\?{3,}", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def load_report_items(dataset_id):
    items = {}
    for path in sorted(REPORTS.glob(f"{dataset_id}_batch-*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        for item in data.get("items", []):
            qid = item.get("question_id") or item.get("id")
            if qid:
                items[qid] = item
    return items


def infer_front(question, key_point):
    parts = []
    stem = clean(question.get("question_text", ""))
    if stem:
        parts.append(stem[:24])
    correct = question.get("correct_answer") or (question.get("correct_answers") or [""])[0]
    option = clean((question.get("options") or {}).get(correct, ""))
    if option:
        parts.append(option[:24])
    if key_point:
        parts.append(key_point[:28])
    return " / ".join([part for part in parts if part][:6])


def build_explanation(question, key_point, base_explanation, correct_answer):
    stem = clean(question.get("question_text", ""))
    options = question.get("options") or {}
    is_negative = any(token in stem for token in ["不是", "不包括", "錯誤", "何者為非", "不正確"])
    stem_note = (
        "題幹採否定式問法，作答時要找出不符合常規、不是適當處置或不是正確敘述的選項。"
        if is_negative
        else "題幹採一般單選問法，作答時要找出最符合核心概念與臨床線索的選項。"
    )

    lines = [
        "【題幹解析】",
        f"{stem_note}本題題幹為：「{stem}」。核心判斷重點是：{key_point}。既有解析指出：{base_explanation}",
        "",
        "【選項詳解】",
    ]

    for letter in ["A", "B", "C", "D"]:
        option_text = clean(options.get(letter, ""))
        if letter == correct_answer:
            verdict = "本題應選答案" if is_negative else "正確答案"
            reason = (
                f"{verdict}。選項內容為「{option_text}」。此選項最符合題幹要求；"
                f"若題幹為否定式，代表它正是題目要找的例外、不適當處置或錯誤敘述。"
                f"判斷依據可回扣核心考點：{key_point}。"
            )
        else:
            reason = (
                f"非本題答案。選項內容為「{option_text}」。此選項雖可能涉及相關醫學概念，"
                f"但不是本題官方答案；判斷時應與正解 {correct_answer} 比較，"
                f"回到題幹關鍵字與核心考點：{key_point}。"
            )
        lines.append(f"- {letter}. {reason}")

    lines.extend(
        [
            "",
            "【核心考點】",
            f"{key_point}備考時不要只背答案，應同時熟悉題幹線索、正確選項的判斷理由，以及其他選項為何不是最佳答案。",
        ]
    )
    return "\n".join(lines)


def main():
    OUT.mkdir(exist_ok=True)
    for exam_path in sorted(BASE.glob("medicine-*.json")):
        data = json.loads(exam_path.read_text(encoding="utf-8"))
        report_items = load_report_items(data["id"])
        updates = []

        for question in data["questions"]:
            qid = question["id"]
            source = report_items.get(qid, {})
            key_point = clean(
                source.get("key_point")
                or question.get("key_point")
                or "本題核心在於辨認題幹線索、正確答案與各選項間的鑑別重點。"
            )
            base_explanation = clean(source.get("explanation") or question.get("explanation") or key_point)
            correct_answer = clean(
                question.get("correct_answer")
                or source.get("correct_answer")
                or (question.get("correct_answers") or [""])[0]
            )
            explanation = build_explanation(question, key_point, base_explanation, correct_answer)

            flashcard_front = clean(
                source.get("flashcard_front") or question.get("flashcard_front") or infer_front(question, key_point)
            )
            flashcard_back = clean(
                source.get("flashcard_back")
                or question.get("flashcard_back")
                or f"看到相關線索時，先判斷題幹問的是正確敘述或例外選項，再用核心考點定位答案 {correct_answer}。"
            )
            flashcard_summary = clean(
                source.get("flashcard_summary") or question.get("flashcard_summary") or f"{flashcard_front} -> {key_point}"
            )
            category = clean(source.get("category") or question.get("category") or "")

            updates.append(
                {
                    "question_id": qid,
                    "key_point": key_point,
                    "explanation": explanation,
                    "flashcard_front": flashcard_front,
                    "flashcard_back": flashcard_back,
                    "flashcard_summary": flashcard_summary,
                    "category": category,
                }
            )

        for index in range(0, len(updates), 10):
            output_path = OUT / f"updates_110-2_{exam_path.stem}_structured_local_{index // 10 + 1:02d}.json"
            output_path.write_text(
                json.dumps(updates[index : index + 10], ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            print(output_path)


if __name__ == "__main__":
    main()
