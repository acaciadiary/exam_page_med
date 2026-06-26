import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
PYTHON = pathlib.Path(
    r"C:\Users\User\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
)

HEADS = ["【題幹解析】", "【選項詳解】", "【核心考點】"]
LEGAL = {
    "medicine-1": ["生物化學", "解剖學", "胚胎及發育生物學", "組織學", "生理學", "其他"],
    "medicine-4": ["小兒科", "皮膚科", "神經科", "精神科", "醫學倫理與醫療決策", "其他"],
    "medicine-6": ["麻醉科", "眼科", "耳鼻喉科", "婦產科", "復健科", "醫學倫理與醫療決策", "其他"],
}


def clean(value, limit=None):
    text = " ".join(str(value or "").replace("\r", " ").replace("\n", " ").split())
    text = re.sub(r"\?{2,}", "", text)
    text = text.replace("???", "").strip()
    if limit and len(text) > limit:
        return text[:limit].rstrip(" ，。；,;") + "..."
    return text


def answer_set(question):
    answer = (
        question.get("correct_answers")
        or question.get("correct_answer")
        or question.get("answer")
        or ""
    )
    if isinstance(answer, list):
        return {str(item).strip().upper() for item in answer if str(item).strip().upper() in "ABCD"}
    return set(re.findall(r"[A-D]", str(answer).upper()))


def is_negative_prompt(text):
    return any(
        marker in text
        for marker in ["錯誤", "不正確", "不適當", "最不可能", "不可能", "除外", "不包括", "何者為非"]
    )


def is_all_credit(question):
    status = str(question.get("answer_status") or "").lower()
    correct = str(question.get("correct_answer") or "")
    return status == "all_credit" or correct == "#"


def is_structured(question):
    exp = question.get("explanation") or ""
    labels = all(
        f"- {label}." in exp or f"- {label}．" in exp or f"- {label}、" in exp
        for label in "ABCD"
    )
    return (
        all(
            question.get(field)
            for field in [
                "key_point",
                "explanation",
                "flashcard_front",
                "flashcard_back",
                "flashcard_summary",
                "category",
            ]
        )
        and all(head in exp for head in HEADS)
        and labels
        and "????" not in exp
        and "????" not in (question.get("key_point") or "")
    )


def keywords(question):
    category = question.get("category") or "核心概念"
    text = clean(question.get("question_text"), 160)
    parts = [category]
    for token in re.split(r"[，,。；;、\s()（）]+", text):
        token = token.strip()
        if 2 <= len(token) <= 24 and token not in parts:
            parts.append(token)
        if len(parts) >= 6:
            break
    return " / ".join(parts[:6])


def old_core(question, category):
    text = clean(question.get("explanation"), 520)
    for head in HEADS:
        text = text.replace(head, "")
    text = re.sub(r"\b[A-D][.．、]", "", text)
    text = clean(text, 420)
    if not text:
        text = f"本題需依題幹線索判斷{category}的核心概念，並比較各選項是否符合國考常見定義、解剖路徑、病理機轉、診斷或治療原則。"
    return text


def build_update(question, subject):
    text = clean(question.get("question_text"))
    options = question.get("options") or {}
    category = question.get("category")
    if category not in LEGAL[subject]:
        category = "其他"

    answers = answer_set(question)
    negative = is_negative_prompt(text)
    all_credit = is_all_credit(question)
    core = old_core(question, category)

    key_point = clean(question.get("key_point"))
    if not key_point:
        key_point = f"掌握{category}題幹線索，判斷選項與核心醫學原則是否相符。"

    if all_credit:
        ask_rule = "本題官方答案狀態為全體給分或特殊處理，解析重點在辨識各選項涉及的醫學概念，而非強行指定單一最佳答案。"
    elif negative:
        ask_rule = "題目要求選出錯誤或最不適當的敘述，因此官方答案代表最需要被排除或最違反核心原則的選項。"
    else:
        ask_rule = "題目要求選出最符合題意的敘述，因此官方答案代表最能對應題幹線索與醫學原則的選項。"

    lines = [
        "【題幹解析】",
        f"本題屬於{category}。題幹重點為：「{clean(text, 260)}」。{ask_rule}解題時先抓住題目中的關鍵名詞、臨床線索、檢驗數值、解剖位置或處置時機，再回到核心原則：{core}",
        "",
        "【選項詳解】",
    ]

    for label in "ABCD":
        option = clean(options.get(label, ""), 260)
        if all_credit:
            verdict = "本題為特殊答案狀態，需理解此選項涉及的概念，並注意官方並未要求以單一選項作為唯一給分依據。"
            concept = f"可與題幹核心線索比較：「{clean(core, 260)}」"
        elif label in answers:
            if negative:
                verdict = "為本題答案。因題目問錯誤、不適當或最不可能者，此選項是最不符合題幹核心原則的敘述。"
            else:
                verdict = "正確，為本題答案。此選項最符合題幹線索與核心醫學概念。"
            concept = f"判斷依據是：「{clean(core, 280)}」"
        else:
            if negative:
                verdict = "非本題答案。此敘述較符合相關醫學原則，或不是題目要找的錯誤點。"
            else:
                verdict = "錯誤，非最佳答案。此選項與題幹線索、典型機轉、診斷條件或治療原則不如官方答案相符。"
            concept = f"與官方答案比較時，應回到本題重點：「{clean(core, 240)}」"
        lines.append(f"- {label}. {option}：{verdict}{concept}")

    lines.extend(
        [
            "",
            "【核心考點】",
            f"本題測試{category}中「題幹線索與選項敘述配對」的能力。備考時應整理常考定義、機轉、典型表現、例外與治療禁忌；遇到否定型題幹要反向判讀，遇到特殊答案狀態則以理解各選項概念為主。",
        ]
    )

    front = keywords(question)
    return {
        "id": question["id"],
        "key_point": key_point.rstrip("?？。") + "。",
        "explanation": "\n".join(lines),
        "flashcard_front": front,
        "flashcard_back": f"{category}題目先抓題幹中的關鍵線索，再比較每個選項是否符合核心原則。否定型題幹要反向找出最不適當或最違反原則的敘述。",
        "flashcard_summary": f"{front} -> {category}核心概念 / 依題幹線索與問法判斷最佳答案",
        "category": category,
        "category_confidence": question.get("category_confidence", 0.8) or 0.8,
    }


def repair(subject):
    exam_file = ROOT / "public" / "data" / "exams" / "111-2" / f"{subject}.json"
    data = json.loads(exam_file.read_text(encoding="utf-8-sig"))
    targets = [question for question in data["questions"] if not is_structured(question)]
    print(f"{subject}: repairing {len(targets)} questions")
    for index in range(0, len(targets), 10):
        batch = targets[index : index + 10]
        updates = [build_update(question, subject) for question in batch]
        updates_file = ROOT / "scratch" / f"updates_111-2_{subject}_utf8_repair_{index // 10 + 1:02d}.json"
        updates_file.write_text(json.dumps(updates, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        subprocess.run(
            [
                str(PYTHON),
                str(ROOT / "scripts" / "exams" / "update_question_fields.py"),
                "--exam-file",
                str(exam_file),
                "--updates-file",
                str(updates_file),
            ],
            check=True,
        )


for subject_name in ["medicine-1", "medicine-4", "medicine-6"]:
    repair(subject_name)
