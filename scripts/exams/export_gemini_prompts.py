from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


CATEGORY_PROFILES: dict[str, dict[str, Any]] = {
    "medicine-1": {
        "year": "115",
        "category_group": "醫學（一）",
        "categories": ["生物化學", "解剖學", "胚胎及發育生物學", "組織學", "生理學", "其他"],
    },
    "medicine-2": {
        "year": "115",
        "category_group": "醫學（二）",
        "categories": ["微生物免疫學", "寄生蟲學", "藥理學", "病理學", "公共衛生學", "其他"],
    },
    "medicine-3": {
        "year": "115",
        "category_group": "醫學（三）",
        "categories": [
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
    },
    "medicine-4": {
        "year": "115",
        "category_group": "醫學（四）",
        "categories": ["小兒科", "皮膚科", "神經科", "精神科", "醫學倫理與醫療決策", "其他"],
    },
    "medicine-5": {
        "year": "115",
        "category_group": "醫學（五）",
        "categories": [
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
    },
    "medicine-6": {
        "year": "115",
        "category_group": "醫學（六）",
        "categories": ["麻醉科", "眼科", "耳鼻喉科", "婦產科", "復健科", "醫學倫理與醫療決策", "其他"],
    },
}


def category_profile(dataset: dict[str, Any]) -> dict[str, Any]:
    subject = str(dataset.get("subject", ""))
    return CATEGORY_PROFILES.get(
        subject,
        {
            "year": str(dataset.get("year", "")),
            "category_group": dataset.get("title") or subject or "未指定",
            "categories": ["其他"],
        },
    )


def needs_explanation(question: dict[str, Any], force: bool) -> bool:
    if force:
        return True
    return not all(
        str(question.get(field, "")).strip()
        for field in [
            "key_point",
            "explanation",
            "flashcard_front",
            "flashcard_back",
            "flashcard_summary",
        ]
    )


def expand_paths(patterns: list[str]) -> list[Path]:
    paths: list[Path] = []
    for pattern in patterns:
        matches = sorted(Path().glob(pattern))
        paths.extend(matches or [Path(pattern)])
    return paths


def safe_name(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "-", value).strip("-") or "dataset"


def chunked(items: list[dict[str, Any]], size: int) -> list[list[dict[str, Any]]]:
    return [items[index : index + size] for index in range(0, len(items), size)]


def answer_for_prompt(question: dict[str, Any]) -> str:
    answer = question.get("correct_answer")
    if answer:
        return str(answer)
    answers = question.get("correct_answers") or []
    return ",".join(str(item) for item in answers)


def question_payload(question: dict[str, Any]) -> dict[str, Any]:
    return {
        "question_id": question.get("id"),
        "question_number": question.get("question_number"),
        "question_text": question.get("question_text"),
        "options": question.get("options", {}),
        "correct_answer": answer_for_prompt(question),
        "answer_note": question.get("answer_note", ""),
    }


def build_prompt(dataset: dict[str, Any], batch_id: str, questions: list[dict[str, Any]]) -> str:
    profile = category_profile(dataset)
    payload = {
        "dataset_id": dataset.get("id"),
        "dataset_year": profile["year"],
        "dataset_title": dataset.get("title"),
        "batch_id": batch_id,
        "category_group": profile["category_group"],
        "allowed_categories": profile["categories"],
        "questions": [question_payload(question) for question in questions],
    }
    expected = {
        "dataset_id": dataset.get("id"),
        "batch_id": batch_id,
        "items": [
            {
                "question_id": question.get("id"),
                "question_number": question.get("question_number"),
                "correct_answer": answer_for_prompt(question),
                "category_group": profile["category_group"],
                "category": profile["categories"][0],
                "category_confidence": "high",
                "key_point": "一句話整理本題核心考點。",
                "explanation": "結構化繁體中文詳解，格式如下：\n【題幹解析】\n（解析題幹中的重要關鍵字與臨床線索）\n\n【選項詳解】\n- A. （說明此選項正確或錯誤的原因，以及對應的醫學概念）\n- B. （說明此選項正確或錯誤的原因，以及對應的醫學概念）\n- C. （說明此選項正確或錯誤的原因，以及對應的醫學概念）\n- D. （說明此選項正確或錯誤的原因，以及對應的醫學概念）\n\n【核心考點】\n（總結此題測試的核心醫學概念）",
                "flashcard_front": "3 到 6 個關鍵字或線索，不要放完整題目或選項。",
                "flashcard_back": "知識點與判斷規則，用 1 到 2 句說明看到線索時該如何判斷。",
                "flashcard_summary": "關鍵字 / 線索 -> 知識點 / 判斷規則",
            }
            for question in questions
        ],
    }
    return f"""你是醫師國考備考助教。請根據題目、選項與官方答案，重新分析每一題，產生詳解、細分科目、年份資訊與可用於複習的閃卡欄位。

重要規則：
1. 只回傳純 JSON，不要 Markdown，不要 ```json。
2. 不可更改 dataset_id、batch_id、question_id、question_number、correct_answer。
3. 每題都必須回傳 category_group、category、category_confidence、key_point、explanation、flashcard_front、flashcard_back、flashcard_summary。
4. category 只能從 allowed_categories 選一個；如果無法明確判斷，請選「其他」，不要自行發明新科目。
5. category_confidence 只能填 high、medium、low。
6. key_point 用一句話整理本題核心考點。
7. explanation 必須是結構化繁體中文詳解，包含【題幹解析】、【選項詳解】（A/B/C/D 逐項說明）與【核心考點】三部分。在【選項詳解】中，必須逐一針對 A、B、C、D 選項進行深入分析，說明正確答案成立的理由，以及其他選項錯誤/不適當的原因或所代表的醫學概念。請使用換行符號（\\n）將這三個部分隔開，使其在畫面上呈現清晰的段落。避免寫成臨床醫囑。
8. flashcard_front 是閃卡正面，只放「關鍵字 / 線索」，讓考生看到線索時練習回想考點。請不要複製完整題目，不要列 A/B/C/D 選項，不要直接暴露答案。建議 3 到 6 個關鍵線索，或一句很短的臨床/基礎醫學提示。
9. flashcard_back 是閃卡背面，只放「知識點 / 判斷規則」。請用 1 到 2 句繁體中文說明：看到正面線索時，應該想到哪個考點、如何判斷、容易跟什麼混淆。可以包含正確答案方向，但重點不是背選項，而是背判斷規則。
10. flashcard_summary 保留為相容舊資料的短句，格式用「關鍵字 / 線索 -> 知識點 / 判斷規則」。
11. 這是備考教材，不是醫療建議；遇到題意不足或爭議時要保守表述。
12. dataset_year 是 {profile["year"]}，請保留並理解這批題目屬於該年份。

輸出前自我檢查：
在輸出 JSON 前，請先自行完成一次嚴格檢查，但不要把檢查過程輸出給我。請確認：
1. items 題數必須與輸入 questions 題數完全一致。
2. 每題都必須包含 question_id、question_number、correct_answer、category_group、category、category_confidence、key_point、explanation、flashcard_front、flashcard_back、flashcard_summary。
3. dataset_id 與 batch_id 只放在最外層，不要放在單題內。
4. question_id 必須符合輸入資料，question_number 必須連續且正確。
5. correct_answer 必須與題目提供的正解一致，不可自行更改。
6. category_group 必須等於輸入的 category_group。
7. category 只能從 allowed_categories 選擇；若無法確定，請選「其他」，不可自創分類名稱。
8. category_confidence 只能是 high、medium、low。
9. explanation 必須支持 correct_answer，不可與正解矛盾。
10. flashcard_front 不可複製完整題目、不可列選項、不可直接暴露答案。
11. flashcard_back 必須是知識點或判斷規則，不要只寫選項代號。
12. flashcard_summary 必須使用「關鍵字 / 線索 -> 知識點 / 判斷規則」格式。
如果你發現自己原本的分類、詳解或閃卡欄位不符合以上規則，請在輸出前自行修正，最後只輸出修正後的合法 JSON。

請處理以下 JSON 輸入：
{json.dumps(payload, ensure_ascii=False, indent=2)}

請完全依照以下 JSON Schema 與欄位名稱輸出：
{json.dumps(expected, ensure_ascii=False, indent=2)}
"""


def export_prompts(
    paths: list[Path],
    out_dir: Path,
    batch_size: int,
    force: bool,
) -> dict[str, Any]:
    out_dir.mkdir(parents=True, exist_ok=True)
    batches: list[dict[str, Any]] = []

    for path in paths:
        dataset = json.loads(path.read_text(encoding="utf-8"))
        questions = [
            question
            for question in dataset.get("questions", [])
            if needs_explanation(question, force)
        ]

        for index, batch_questions in enumerate(chunked(questions, batch_size), start=1):
            batch_id = f"{dataset.get('id')}_batch-{index:03d}"
            prompt_path = out_dir / f"{safe_name(batch_id)}.md"
            prompt_path.write_text(
                build_prompt(dataset, batch_id, batch_questions),
                encoding="utf-8",
            )
            batches.append(
                {
                    "dataset_id": dataset.get("id"),
                    "dataset_path": str(path),
                    "batch_id": batch_id,
                    "prompt_path": str(prompt_path),
                    "suggested_output_path": str(
                        Path("reports/gemini_outputs") / f"{safe_name(batch_id)}.json"
                    ),
                    "question_count": len(batch_questions),
                }
            )

    manifest = {
        "batch_count": len(batches),
        "question_count": sum(batch["question_count"] for batch in batches),
        "batches": batches,
    }
    (out_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description="Export Gemini copy-paste prompts.")
    parser.add_argument("paths", nargs="+", help="Dataset JSON paths or glob patterns")
    parser.add_argument("--out-dir", default="reports/gemini_prompts")
    parser.add_argument("--batch-size", type=int, default=15)
    parser.add_argument("--force", action="store_true", help="Include questions that already have explanations")
    args = parser.parse_args()

    manifest = export_prompts(
        paths=expand_paths(args.paths),
        out_dir=Path(args.out_dir),
        batch_size=args.batch_size,
        force=args.force,
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
