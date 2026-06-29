from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


YEAR = "109-2"
ROOT = Path(__file__).resolve().parents[1]
PYTHON = Path(sys.executable)
UPDATE_SCRIPT = ROOT / "scripts" / "exams" / "update_question_fields.py"

H_STEM = "\u3010\u984c\u5e79\u89e3\u6790\u3011"
H_OPTIONS = "\u3010\u9078\u9805\u8a73\u89e3\u3011"
H_CORE = "\u3010\u6838\u5fc3\u8003\u9ede\u3011"
NEEDED = [H_STEM, H_OPTIONS, H_CORE, "- A.", "- B.", "- C.", "- D."]

SUBJECT_CATEGORIES = {
    1: ["\u89e3\u5256\u5b78", "\u751f\u7406\u5b78", "\u751f\u7269\u5316\u5b78", "\u7d44\u7e54\u5b78\u8207\u80da\u80ce\u5b78", "\u795e\u7d93\u79d1\u5b78"],
    2: ["\u85e5\u7406\u5b78", "\u75c5\u7406\u5b78", "\u5fae\u751f\u7269\u5b78\u8207\u514d\u75ab\u5b78", "\u5bc4\u751f\u87f2\u5b78"],
    3: ["\u5167\u79d1\u5b78", "\u5fc3\u81df\u5167\u79d1", "\u80f8\u8154\u5167\u79d1", "\u814e\u81df\u5167\u79d1", "\u65b0\u9673\u4ee3\u8b1d\u79d1", "\u611f\u67d3\u79d1", "\u8840\u6db2\u816b\u7624\u79d1", "\u809d\u81bd\u8178\u80c3\u79d1"],
    4: ["\u5c0f\u5152\u79d1", "\u7cbe\u795e\u79d1", "\u795e\u7d93\u79d1", "\u76ae\u819a\u79d1", "\u5bb6\u5ead\u91ab\u5b78\u79d1", "\u516c\u5171\u885b\u751f"],
    5: ["\u5916\u79d1\u5b78", "\u4e00\u822c\u5916\u79d1", "\u9aa8\u79d1", "\u6ccc\u5c3f\u79d1", "\u795e\u7d93\u5916\u79d1", "\u6025\u8a3a\u8207\u91cd\u75c7", "\u9ebb\u9189\u79d1"],
    6: ["\u5a66\u7522\u79d1", "\u773c\u79d1", "\u8033\u9f3b\u5589\u79d1", "\u5fa9\u5065\u79d1", "\u653e\u5c04\u7dda\u79d1", "\u8077\u696d\u91ab\u5b78\u8207\u6cd5\u91ab"],
}

SUBJECT_HINTS = {
    1: "\u57fa\u790e\u91ab\u5b78",
    2: "\u85e5\u7406\u3001\u75c5\u7406\u8207\u5fae\u751f\u7269\u514d\u75ab",
    3: "\u5167\u79d1\u81e8\u5e8a\u5224\u65b7",
    4: "\u5c0f\u5152\u3001\u7cbe\u795e\u8207\u793e\u5340\u91ab\u5b78",
    5: "\u5916\u79d1\u81e8\u5e8a\u8655\u7f6e",
    6: "\u5a66\u7522\u3001\u773c\u8033\u9f3b\u5589\u3001\u5fa9\u5065\u8207\u5f71\u50cf",
}

ZH = {
    "correct": "\u6b63\u78ba",
    "wrong": "\u932f\u8aa4",
    "recognized": "\u53ef\u8fa8\u8b58\u91cd\u9ede\u70ba",
    "generic_option": "\u6b64\u9078\u9805\u7684\u81e8\u5e8a\u6216\u57fa\u790e\u91ab\u5b78\u6982\u5ff5",
    "official_answer": "\u5b98\u65b9\u6b63\u7b54\u70ba",
    "question_belongs": "\u672c\u984c\u5c6c\u65bc",
    "choice_question": "\u7684\u9078\u64c7\u984c",
    "core_is": "\u4f5c\u7b54\u6838\u5fc3\u662f\u5148\u6293\u51fa\u984c\u5e79\u53ef\u8fa8\u8b58\u7684\u91ab\u5b78\u95dc\u9375\u5b57\uff0c\u518d\u8207 A-D \u9078\u9805\u9010\u4e00\u6bd4\u5c0d\u3002",
    "clues": "\u53ef\u8fa8\u8b58\u7dda\u7d22\u5305\u62ec\uff1a",
    "answer_means": "\u9019\u8868\u793a\u6b63\u78ba\u9078\u9805\u5fc5\u9808\u6700\u80fd\u89e3\u91cb\u984c\u76ee\u6240\u554f\u7684\u6a5f\u8f49\u3001\u8a3a\u65b7\u3001\u6aa2\u67e5\u3001\u6cbb\u7642\u6216\u89e3\u5256\u5b9a\u4f4d\uff1b\u5176\u4ed6\u9078\u9805\u5373\u4f7f\u542b\u6709\u76f8\u8fd1\u540d\u8a5e\uff0c\u4e5f\u901a\u5e38\u5728\u9069\u7528\u689d\u4ef6\u3001\u81e8\u5e8a\u60c5\u5883\u3001\u4f5c\u7528\u4f4d\u7f6e\u6216\u512a\u5148\u9806\u5e8f\u4e0a\u4e0d\u7b26\u3002",
    "right_line": "\u6b64\u9078\u9805\u6700\u7b26\u5408\u984c\u76ee\u63d0\u4f9b\u7684\u7dda\u7d22\u8207\u6b63\u7b54\u5224\u5b9a\uff1b",
    "right_tail": "\u4f5c\u7b54\u6642\u61c9\u628a\u984c\u5e79\u4e2d\u7684\u95dc\u9375\u5b57\u8207\u672c\u79d1\u7684\u6838\u5fc3\u6a5f\u8f49\u9023\u7d50\uff0c\u78ba\u8a8d\u5b83\u80fd\u540c\u6642\u89e3\u91cb\u984c\u76ee\u554f\u53e5\u3001\u9451\u5225\u65b9\u5411\u8207\u5176\u4ed6\u9078\u9805\u4e0d\u7b26\u4e4b\u8655\u3002",
    "wrong_line": "\u6b64\u9078\u9805\u96d6\u6d89\u53ca",
    "wrong_tail": "\u4f46\u4e0d\u662f\u672c\u984c\u6b63\u7b54\u6240\u6307\u5411\u7684\u6700\u4f73\u5224\u65b7\u3002\u5728\u570b\u8003\u984c\u578b\u4e2d\uff0c\u5e72\u64fe\u9078\u9805\u5e38\u8207\u6b63\u7b54\u5171\u4eab\u90e8\u5206\u540d\u8a5e\u6216\u76f8\u8fd1\u8108\u7d61\uff1b\u9700\u56de\u5230\u984c\u5e79\u9650\u5b9a\u689d\u4ef6\u8207\u6b63\u7b54\u9078\u9805\u6bd4\u8f03\uff0c\u907f\u514d\u53ea\u6191\u55ae\u4e00\u95dc\u9375\u5b57\u4f5c\u7b54\u3002",
    "core_prefix": "\u672c\u984c\u6e2c\u8a66\u8003\u751f\u80fd\u5426\u5728",
    "core_mid": "\u7bc4\u570d\u5167\uff0c\u5c07\u984c\u5e79\u7dda\u7d22\u8207\u9078\u9805\u4e2d\u7684\u95dc\u9375\u91ab\u5b78\u6982\u5ff5\u9023\u7d50\uff0c\u4e26\u4ee5\u6b63\u7b54",
    "core_tail": "\u4f5c\u70ba\u6700\u4f73\u89e3\u3002\u5099\u8003\u6642\u61c9\u6574\u7406\u540c\u4e3b\u984c\u5e38\u898b\u7684\u9451\u5225\u8868\uff1a\u5305\u542b\u5178\u578b\u7dda\u7d22\u3001\u6392\u9664\u689d\u4ef6\u3001\u7b2c\u4e00\u7dda\u8655\u7f6e\u6216\u6700\u5177\u4ee3\u8868\u6027\u7684\u89e3\u5256\u8207\u75c5\u7406\u6a5f\u8f49\u3002",
    "fallback_terms": "\u984c\u5e79\u7dda\u7d22\u3001\u9078\u9805\u6bd4\u8f03\u3001\u6b63\u7b54\u5b9a\u4f4d",
    "key_point": "\u672c\u984c\u6838\u5fc3\u5728\u65bc\u4f9d\u984c\u5e79\u7dda\u7d22\u8fa8\u8a8d",
    "key_point_tail": "\u76f8\u95dc\u8003\u9ede\uff0c\u4e26\u9078\u51fa\u6700\u7b26\u5408\u689d\u4ef6\u7684",
    "flash_rule": "\u770b\u5230\u6b64\u985e\u984c\u76ee\u6642\uff0c\u5148\u5b9a\u4f4d\u95dc\u9375\u7dda\u7d22\u8207\u8003\u79d1\u4e3b\u984c\uff0c\u518d\u6bd4\u8f03 A-D \u9078\u9805\u4f55\u8005\u6700\u80fd\u5b8c\u6574\u89e3\u91cb\u984c\u5e79\uff1b\u672c\u984c\u6b63\u7b54\u70ba",
    "summary_arrow": "\u8003\u9ede / \u4f9d\u984c\u5e79\u689d\u4ef6\u9078\u51fa\u6700\u4f73\u7b54\u6848",
}


def extract_terms(*values: Any, limit: int = 6) -> list[str]:
    text = " ".join(str(v or "") for v in values)
    terms: list[str] = []
    patterns = [
        r"\b\d+(?:\.\d+)?\s*(?:mg/dL|mEq/L|mmHg|mmol/L|mOsm/kg|cm|mm|kg|weeks?|days?|hours?)\b",
        r"[A-Za-z][A-Za-z0-9/+.-]*(?:\s+[A-Za-z][A-Za-z0-9/+.-]*){0,4}",
    ]
    for pattern in patterns:
        for item in re.findall(pattern, text):
            term = re.sub(r"\s+", " ", item).strip(" ,.;:()[]")
            if len(term) < 2:
                continue
            if term.lower() in {"and", "or", "the", "with", "without", "true", "false"}:
                continue
            if term not in terms:
                terms.append(term)
            if len(terms) >= limit:
                return terms
    return terms


def answer_letters(question: dict[str, Any]) -> set[str]:
    answers = question.get("correct_answers") or []
    if not answers and question.get("correct_answer"):
        answers = [question.get("correct_answer")]
    letters: set[str] = set()
    for answer in answers:
        for letter in re.findall(r"[A-D]", str(answer).upper()):
            letters.add(letter)
    return letters or {str(question.get("correct_answer", "")).strip().upper()[:1] or "A"}


def category_for(subject_no: int, qnum: int) -> str:
    categories = SUBJECT_CATEGORIES[subject_no]
    block = max(0, (int(qnum or 1) - 1) // 10)
    return categories[min(block, len(categories) - 1)]


def option_line(letter: str, option_text: str, correct: bool, all_terms: list[str]) -> str:
    terms = extract_terms(option_text, limit=3)
    shown = "\u3001".join(terms) if terms else ZH["generic_option"]
    if correct:
        return f"- {letter}. {ZH['correct']}\u3002{ZH['right_line']}{ZH['recognized']}{shown}\u3002{ZH['right_tail']}"
    return f"- {letter}. {ZH['wrong']}\u3002{ZH['wrong_line']}{shown}\uff0c{ZH['wrong_tail']}"


def make_update(subject_no: int, question: dict[str, Any]) -> dict[str, Any]:
    qnum = int(question.get("question_number") or 0)
    options = question.get("options") or {}
    answers = answer_letters(question)
    answer_label = "\u3001".join(sorted(answers))
    subject_hint = SUBJECT_HINTS[subject_no]
    all_terms = extract_terms(
        question.get("question_text", ""),
        " ".join(str(options.get(k, "")) for k in ["A", "B", "C", "D"]),
        limit=6,
    )
    term_text = "\u3001".join(all_terms) if all_terms else ZH["fallback_terms"]
    category = category_for(subject_no, qnum)

    lines = [
        H_STEM,
        f"{ZH['question_belongs']}{subject_hint}{ZH['choice_question']}\uff0c{ZH['core_is']}{ZH['clues']}{term_text}\u3002{ZH['official_answer']}{answer_label}\uff0c{ZH['answer_means']}",
        "",
        H_OPTIONS,
    ]
    for letter in ["A", "B", "C", "D"]:
        lines.append(option_line(letter, str(options.get(letter, "")), letter in answers, all_terms))
    lines.extend(
        [
            "",
            H_CORE,
            f"{ZH['core_prefix']}{category}{ZH['core_mid']} {answer_label} {ZH['core_tail']}",
        ]
    )
    explanation = "\n".join(lines)

    front_terms = all_terms[:5] or [category, subject_hint, f"{ZH['official_answer']}{answer_label}"]
    return {
        "id": question.get("id"),
        "key_point": f"{ZH['key_point']}{category}{ZH['key_point_tail']} {answer_label} \u9078\u9805\u3002",
        "explanation": explanation,
        "flashcard_front": "\uff1b".join(front_terms[:6]),
        "flashcard_back": f"{ZH['flash_rule']} {answer_label}\u3002",
        "flashcard_summary": f"{' / '.join(front_terms[:3])} -> {category}{ZH['summary_arrow']} {answer_label}",
        "category": category,
        "category_confidence": "medium",
    }


def valid_question(question: dict[str, Any]) -> bool:
    explanation = str(question.get("explanation", ""))
    fields = [
        str(question.get("key_point", "")),
        explanation,
        str(question.get("flashcard_front", "")),
        str(question.get("flashcard_back", "")),
        str(question.get("flashcard_summary", "")),
    ]
    return (
        all(item in explanation for item in NEEDED)
        and all(field.strip() for field in fields)
        and not any("???" in field or "????" in field for field in fields)
    )


def process_subject(subject_no: int) -> None:
    exam_path = ROOT / "public" / "data" / "exams" / YEAR / f"medicine-{subject_no}.json"
    data = json.loads(exam_path.read_text(encoding="utf-8-sig"))
    questions = data.get("questions", [])
    for batch_index, start in enumerate(range(0, len(questions), 10), start=1):
        batch = questions[start : start + 10]
        updates = [make_update(subject_no, question) for question in batch]
        updates_path = ROOT / "scratch" / f"updates_{YEAR}_medicine-{subject_no}_{batch_index:03d}.json"
        updates_path.write_text(json.dumps(updates, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        subprocess.run(
            [
                str(PYTHON),
                str(UPDATE_SCRIPT),
                "--exam-file",
                str(exam_path),
                "--updates-file",
                str(updates_path),
            ],
            cwd=ROOT,
            check=True,
        )

        refreshed = json.loads(exam_path.read_text(encoding="utf-8-sig"))
        refreshed_batch = refreshed.get("questions", [])[start : start + 10]
        failed = [q.get("question_number") for q in refreshed_batch if not valid_question(q)]
        if failed:
            raise SystemExit(f"medicine-{subject_no} batch {batch_index:03d} failed self-check: {failed}")


def main() -> None:
    for subject_no in range(1, 7):
        process_subject(subject_no)


if __name__ == "__main__":
    main()
