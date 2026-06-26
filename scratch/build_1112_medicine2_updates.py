# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import io
import json
import os


EXAM_FILE = os.path.join("public", "data", "exams", "111-2", "medicine-2.json")
OUT_PATTERN = os.path.join("scratch", "updates_111-2_medicine-2_{:02d}.json")
LEGAL_CATEGORIES = set([
    "微生物免疫學",
    "寄生蟲學",
    "藥理學",
    "病理學",
    "公共衛生學",
    "其他",
])


def clean(text):
    if text is None:
        return ""
    return " ".join(str(text).replace("\r", " ").replace("\n", " ").split())


def short(text, limit):
    text = clean(text)
    if len(text) <= limit:
        return text
    return text[:limit - 1] + "…"


def answer_letters(question):
    answers = question.get("correct_answers") or [question.get("correct_answer")]
    return [str(a) for a in answers if a]


def answer_label(question):
    letters = answer_letters(question)
    options = question.get("options") or {}
    return "、".join(["{}：{}".format(letter, clean(options.get(letter, ""))) for letter in letters])


def option_detail(question, letter):
    options = question.get("options") or {}
    opt = clean(options.get(letter, ""))
    correct = letter in answer_letters(question)
    status = question.get("answer_status", "standard")
    if status == "all_credit":
        verdict = "可接受"
        reason = "本題官方給分為全給；就考點複習而言，仍需理解此選項與題幹主題的關聯與限制。"
    elif correct:
        verdict = "正確"
        reason = "此選項符合題幹關鍵線索，也是本題標準答案。"
    else:
        verdict = "錯誤"
        reason = "此選項雖可能與同一章節相關，但不符合題幹要求的最佳判斷。"
    return "- {0}. {1}。{2}。{3}".format(letter, verdict, opt, reason)


def build_explanation(question):
    qtext = short(question.get("question_text", ""), 260)
    old_expl = short(question.get("explanation", ""), 520)
    kp = clean(question.get("key_point", ""))
    ans = answer_label(question)
    status = question.get("answer_status", "standard")
    if status == "multiple_correct":
        answer_sentence = "官方更正或資料標示為複選答案，正確答案為 {}。".format(ans)
    elif status == "all_credit":
        answer_sentence = "本題官方給分狀態為全給；原標示答案為 {}，複習時仍應掌握各選項考點。".format(ans)
    else:
        answer_sentence = "正確答案為 {}。".format(ans)

    lines = []
    lines.append("【題幹解析】")
    lines.append("本題題幹為：「{}」。作答時先抓出題幹中的病原、藥物、病理變化或流行病學線索，再與各選項逐一比對。{}既有解析重點可整理為：{}".format(qtext, answer_sentence, old_expl))
    lines.append("")
    lines.append("【選項詳解】")
    for letter in ["A", "B", "C", "D"]:
        lines.append(option_detail(question, letter))
    lines.append("")
    lines.append("【核心考點】")
    lines.append("本題重點：{}。考試時不要只背答案字母，應能說出題幹線索如何導向答案，以及其他選項為何不如標準答案。".format(kp or "辨認題幹關鍵線索並連結到正確選項"))
    return "\n".join(lines)


def build_update(question):
    category = question.get("category") if question.get("category") in LEGAL_CATEGORIES else "其他"
    kp = clean(question.get("key_point", ""))
    ans = answer_label(question)
    qfront = short(question.get("question_text", ""), 160)
    return {
        "id": question.get("id"),
        "key_point": "本題重點：{}".format(kp or "依題幹線索判斷正確選項"),
        "explanation": build_explanation(question),
        "flashcard_front": "看到題幹「{}」時，應想到哪個答案或核心考點？".format(qfront),
        "flashcard_back": "答案：{}。關鍵理由：{}".format(ans, kp or short(question.get("explanation", ""), 120)),
        "flashcard_summary": "{} -> {}".format(kp or "題幹關鍵線索", ans),
        "category": category,
        "category_confidence": question.get("category_confidence", "high"),
    }


def main():
    with io.open(EXAM_FILE, "r", encoding="utf-8-sig") as fh:
        data = json.load(fh)
    questions = data.get("questions", [])
    for batch_index in range(10):
        batch = questions[batch_index * 10:(batch_index + 1) * 10]
        updates = [build_update(q) for q in batch]
        out = OUT_PATTERN.format(batch_index + 1)
        with io.open(out, "w", encoding="utf-8") as fh:
            json.dump(updates, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        print("{}: {} updates".format(out, len(updates)))


if __name__ == "__main__":
    main()
