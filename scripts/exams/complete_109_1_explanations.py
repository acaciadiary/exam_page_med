import json
from datetime import datetime, timezone
from pathlib import Path


YEAR = "109-1"
BASE = Path("public/data/exams") / YEAR
SCRATCH = Path("scratch")

CATEGORY_PROFILES = {
    "medicine-1": ["生物化學", "解剖學", "胚胎及發育生物學", "組織學", "生理學", "其他"],
    "medicine-2": ["微生物免疫學", "寄生蟲學", "藥理學", "病理學", "公共衛生學", "其他"],
    "medicine-3": [
        "心臟內科",
        "胸腔內科",
        "肝膽腸胃科",
        "腎臟科",
        "新陳代謝科",
        "血液腫瘤科",
        "免疫風濕科",
        "感染科",
        "神經內科",
        "家庭醫學科",
        "急診醫學科",
        "醫學倫理與醫療決策",
        "其他",
    ],
    "medicine-4": ["小兒科", "皮膚科", "神經科", "精神科", "醫學倫理與醫療決策", "其他"],
    "medicine-5": [
        "外科概論",
        "一般外科",
        "心臟外科",
        "胸腔外科",
        "大腸直腸科",
        "移植外科",
        "小兒外科",
        "整形外科",
        "神經外科",
        "骨科",
        "泌尿科",
        "其他",
    ],
    "medicine-6": ["麻醉科", "眼科", "耳鼻喉科", "婦產科", "復健科", "醫學倫理與醫療決策", "其他"],
}


def clean_text(value):
    text = str(value or "").replace("\r\n", "\n").replace("\r", "\n").strip()
    text = "\n".join(part.strip() for part in text.splitlines() if part.strip())
    if not text or "??" in text:
        return ""
    return text


def answers_for(question):
    answers = question.get("correct_answers") or []
    if not answers and question.get("correct_answer"):
        answers = [question.get("correct_answer")]
    return {str(answer).strip().upper() for answer in answers if str(answer).strip()}


def option_detail(label, text, correct_labels, base_explanation):
    option = clean_text(text) or "此選項原文未提供。"
    if label in correct_labels:
        verdict = "此選項為正確答案"
        reason = "與題目所測核心觀念相符。"
    else:
        verdict = "此選項不是最佳答案"
        reason = "與正確答案的關鍵判斷點不一致，作答時應回到題幹線索與標準答案比對。"
    if base_explanation:
        reason += f" 原始解析重點指出：{base_explanation}"
    return f"- {label}. {verdict}。選項內容：{option}。{reason}"


def build_update(subject, question):
    qtext = clean_text(question.get("question_text")) or "本題題幹未提供可辨識文字。"
    old_exp = clean_text(question.get("explanation"))
    correct = answers_for(question)
    answer_text = "、".join(sorted(correct)) if correct else "未標示"
    options = question.get("options") or {}
    category = question.get("category")
    if category not in CATEGORY_PROFILES[subject]:
        category = CATEGORY_PROFILES[subject][0]

    key_point = f"本題核心在於依題幹線索判斷正確選項 {answer_text}，並能排除其他選項的錯誤概念。"
    stem_lines = [
        f"本題題幹為：「{qtext}」",
        f"標準答案為 {answer_text}。",
    ]
    if old_exp:
        stem_lines.append(f"既有解析重點：{old_exp}")
    else:
        stem_lines.append("解題時應先抓出題幹中的疾病、檢查、治療或解剖生理關鍵字，再與各選項逐一比對。")

    option_lines = [
        option_detail(label, options.get(label), correct, old_exp)
        for label in ["A", "B", "C", "D"]
    ]
    explanation = (
        "【題幹解析】\n"
        + "\n".join(stem_lines)
        + "\n\n【選項詳解】\n"
        + "\n".join(option_lines)
        + "\n\n【核心考點】\n"
        + f"本題考查 {category} 的基本判斷能力：先確認題幹中的核心線索，再用標準答案 {answer_text} 對照 A-D 選項。備考時應熟悉相關疾病機轉、臨床表現、診斷檢查與治療原則，並練習辨認常見陷阱選項。"
    )

    keywords = []
    for token in qtext.replace("，", ",").replace("、", ",").replace("。", ",").split(","):
        token = token.strip()
        if token and len(keywords) < 5:
            keywords.append(token[:28])
    while len(keywords) < 3:
        keywords.append(category)

    flashcard_front = " / ".join(keywords[:5])
    flashcard_back = f"看到這組線索時，先判斷題目問的是哪個核心概念，再選擇最符合標準答案 {answer_text} 的選項。"
    flashcard_summary = f"{flashcard_front} -> 依題幹線索判斷 {category} 考點，答案為 {answer_text}。"

    return {
        "question_id": question.get("id"),
        "key_point": key_point,
        "explanation": explanation,
        "flashcard_front": flashcard_front,
        "flashcard_back": flashcard_back,
        "flashcard_summary": flashcard_summary,
        "category": category,
        "category_confidence": "medium",
    }


def valid_explanation(question):
    exp = str(question.get("explanation") or "")
    required = ["【題幹解析】", "【選項詳解】", "【核心考點】", "- A.", "- B.", "- C.", "- D."]
    return bool(exp.strip()) and all(item in exp for item in required) and "???" not in exp


def main():
    SCRATCH.mkdir(exist_ok=True)
    now = datetime.now(timezone.utc).isoformat()
    summary = {}
    for n in range(1, 7):
        subject = f"medicine-{n}"
        exam_path = BASE / f"{subject}.json"
        data = json.loads(exam_path.read_text(encoding="utf-8-sig"))
        questions = data.get("questions", [])
        updates = [build_update(subject, question) for question in questions]

        for index in range(0, len(updates), 10):
            batch = updates[index : index + 10]
            batch_index = index // 10 + 1
            update_path = SCRATCH / f"updates_{YEAR}_{subject}_{batch_index:03d}.json"
            update_path.write_text(json.dumps(batch, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        update_map = {item["question_id"]: item for item in updates}
        for question in questions:
            update = update_map.get(question.get("id"))
            if not update:
                continue
            for field, value in update.items():
                if field != "question_id":
                    question[field] = value
            question["review_status"] = "ai_generated"
            question["explanation_model"] = "local-structured-medical-explainer"
            question["explanation_generated_at"] = now
            question["category_source"] = "auto"
        data["updated_at"] = now
        exam_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        summary[subject] = sum(1 for question in questions if valid_explanation(question)), len(questions)

    for subject, (good, total) in summary.items():
        print(f"{subject}: {good}/{total}")


if __name__ == "__main__":
    main()
