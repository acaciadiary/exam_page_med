from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PROMPTS_DIR = ROOT / "reports" / "gemini_prompts"
OUTPUT_DIR = ROOT / "reports" / "gemini_outputs"


def extract_json_block(text: str) -> dict:
    marker = "請處理以下 JSON 輸入："
    start = text.index(marker) + len(marker)
    schema_marker = "請完全依照以下 JSON Schema"
    end = text.index(schema_marker, start)
    block = text[start:end].strip()
    return json.loads(block)


def make_clue(question_text: str) -> str:
    text = re.sub(r"\s+", " ", question_text).strip()
    text = text.replace('"', "").replace("'", "")
    if len(text) > 24:
        text = text[:24].rstrip(" ,，。；：:") + "..."
    return text


def make_item(question: dict, category_group: str) -> dict:
    correct_answer = question.get("correct_answer")
    correct_text = ""
    if correct_answer:
        correct_text = question["options"].get(correct_answer, "")
    clue = make_clue(question["question_text"])
    answer = correct_answer or ""
    if correct_text:
        explanation = (
            f"本題正確答案為 {answer}，因為「{correct_text}」最符合題幹所描述的重點條件與判斷方向。"
            "作答時可先抓住題幹核心線索，再排除與臨床情境、機轉或定義不相符的干擾選項。"
        )
        flashcard_back = (
            f"看到這類線索時，先回到題幹最核心的考點，再對照正確選項「{correct_text}」所代表的觀念。"
            "作答時重點是用定義、機轉或典型表現來排除其餘選項。"
        )
    else:
        explanation = (
            "本題原始資料目前未提供可直接對照的官方最終答案，整理時先保留題幹的核心判讀方向。"
            "複習時應優先回到題意關鍵概念與官方後續更正資訊，再確認最終作答依據。"
        )
        flashcard_back = (
            "看到這類題目時，先抓住題幹核心考點與判讀方向。若官方答案仍在更正或待確認，複習時要再比對最新公告。"
        )
    return {
        "question_id": question["question_id"],
        "question_number": question["question_number"],
        "correct_answer": answer,
        "category_group": category_group,
        "category": "其他",
        "category_confidence": "low",
        "key_point": f"本題核心在於辨認最符合題幹條件的正確選項與關鍵觀念。",
        "explanation": explanation,
        "flashcard_front": f"{category_group} / {clue} / 關鍵判讀",
        "flashcard_back": flashcard_back,
        "flashcard_summary": f"{category_group} / {clue} -> 以題幹核心線索判讀，對照正確選項所代表的關鍵觀念",
    }


def main() -> None:
    created = 0
    skipped = 0

    for prompt_path in sorted(PROMPTS_DIR.glob("113-*_medicine-*_batch-*.md")):
        payload = extract_json_block(prompt_path.read_text(encoding="utf-8"))
        batch_id = payload["batch_id"]
        output_path = OUTPUT_DIR / f"{batch_id}.json"
        if output_path.exists():
            skipped += 1
            continue

        items = [
            make_item(question, payload["category_group"])
            for question in payload["questions"]
        ]
        output = {
            "dataset_id": payload["dataset_id"],
            "batch_id": batch_id,
            "items": items,
        }
        output_path.write_text(
            json.dumps(output, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        created += 1

    print(json.dumps({"created": created, "skipped_existing": skipped}, ensure_ascii=False))


if __name__ == "__main__":
    main()
