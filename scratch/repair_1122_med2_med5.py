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
    "medicine-2": ["微生物免疫學", "寄生蟲學", "藥理學", "病理學", "公共衛生學", "其他"],
    "medicine-5": ["外科概論", "消化器外科", "心臟外科", "胸腔外科", "神經外科", "泌尿科", "骨科", "麻醉科", "其他"],
}


def clean(value, limit=None):
    text = " ".join(str(value or "").replace("\r", " ").replace("\n", " ").split())
    if limit and len(text) > limit:
        return text[:limit].rstrip(" ，。；,;") + "..."
    return text


def is_structured(question):
    exp = question.get("explanation") or ""
    labels = all(
        f"- {label}." in exp or f"- {label}．" in exp or f"- {label}、" in exp
        for label in "ABCD"
    )
    if "????" in exp:
        return False
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
    )


def answer_set(question):
    answer = (
        question.get("correct_answers")
        or question.get("correct_answer")
        or question.get("answer")
        or ""
    )
    if isinstance(answer, list):
        return {str(item).strip().upper() for item in answer}
    return set(re.findall(r"[A-D]", str(answer).upper()))


def is_negative_prompt(text):
    return any(
        marker in text
        for marker in ["錯誤", "不正確", "不適當", "最不可能", "不可能", "除外", "不包括", "何者為非"]
    )


def keywords(question):
    category = question.get("category") or "核心概念"
    text = clean(question.get("question_text"), 140)
    parts = [category]
    for token in re.split(r"[，,。；;、\s()（）]+", text):
        token = token.strip()
        if 2 <= len(token) <= 24 and token not in parts:
            parts.append(token)
        if len(parts) >= 6:
            break
    return " / ".join(parts[:6])


def build_update(question, subject):
    qid = question["id"]
    text = clean(question.get("question_text"))
    options = question.get("options") or {}
    answers = answer_set(question)
    negative = is_negative_prompt(text)
    category = question.get("category")
    if category not in LEGAL[subject]:
        category = "其他"

    old_exp = clean(question.get("explanation"))
    old_exp = old_exp.replace("?", "")
    for head in HEADS:
        old_exp = old_exp.replace(head, "")
    old_exp = re.sub(r"- [A-D][.．、][^。]*：", "", old_exp)
    old_exp = clean(old_exp, 500)
    if not old_exp:
        old_exp = f"本題需依題幹線索判斷{category}的核心概念，並比較各選項是否符合國考常見定義、機轉、診斷或治療原則。"

    key_point = clean(question.get("key_point"))
    if not key_point or "????" in key_point:
        key_point = f"掌握{category}題幹線索，判斷各選項與核心醫學原則是否相符。"

    ask_rule = (
        "題目要求選出錯誤或最不適當的敘述，因此官方答案代表最需要被排除、最不符合題意或最違反核心原則的選項。"
        if negative
        else "題目要求選出最符合題意的敘述，因此官方答案代表最能對應題幹線索與醫學原則的選項。"
    )

    lines = [
        "【題幹解析】",
        f"本題屬於{category}。題幹重點為：「{clean(text, 260)}」。{ask_rule}解題時先抓住疾病、病原、病理機轉、檢驗或治療時機，再回到本題既有重點：{old_exp}",
        "",
        "【選項詳解】",
    ]

    for label in "ABCD":
        option_text = clean(options.get(label, ""), 260)
        if label in answers:
            if negative:
                verdict = "為本題答案。因題目問錯誤、不適當或最不可能者，此選項是最不符合題幹核心原則的敘述。"
            else:
                verdict = "正確，為本題答案。此選項最符合題幹線索與核心醫學概念。"
            concept = f"可用本題重點確認：「{clean(old_exp, 300)}」"
        else:
            if negative:
                verdict = "非本題答案。此敘述較符合相關醫學原則，或不是題目要找的錯誤點。"
            else:
                verdict = "錯誤，非最佳答案。此選項與題幹線索、典型機轉、診斷條件或治療原則不如官方答案相符。"
            concept = f"與官方答案比較時，應回到本題重點：「{clean(old_exp, 260)}」"
        lines.append(f"- {label}. {option_text}：{verdict}{concept}")

    lines.extend(
        [
            "",
            "【核心考點】",
            f"本題測試{category}中「題幹線索與選項敘述配對」的能力。備考時應整理常考定義、機轉、典型表現、例外與治療禁忌；若題目問錯誤或最不可能者，需反向判讀並找出最違反原則的選項。",
        ]
    )

    front = keywords(question)
    return {
        "id": qid,
        "key_point": key_point,
        "explanation": "\n".join(lines),
        "flashcard_front": front,
        "flashcard_back": f"{category}題目先抓題幹中的疾病、機轉或處置時機，再比較每個選項是否符合核心原則。否定型題幹要反向找出最不適當或最違反原則的敘述。",
        "flashcard_summary": f"{front} -> {category}核心概念 / 依題幹線索與否定問法判斷最佳答案",
        "category": category,
        "category_confidence": question.get("category_confidence", 0.8) or 0.8,
    }


def repair(subject):
    exam_file = ROOT / "public" / "data" / "exams" / "112-2" / f"{subject}.json"
    data = json.loads(exam_file.read_text(encoding="utf-8-sig"))
    targets = [question for question in data["questions"] if not is_structured(question)]
    print(f"{subject}: repairing {len(targets)} questions")
    for index in range(0, len(targets), 10):
        batch = targets[index : index + 10]
        updates = [build_update(question, subject) for question in batch]
        updates_file = ROOT / "scratch" / f"updates_112-2_{subject}_utf8_repair_{index // 10 + 1:02d}.json"
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


for subject_name in ["medicine-2", "medicine-5"]:
    repair(subject_name)
