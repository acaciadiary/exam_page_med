from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
PROMPTS_DIR = ROOT / "reports" / "gemini_prompts"
OUTPUT_DIR = ROOT / "reports" / "gemini_outputs"


def extract_payload(text: str) -> dict[str, Any]:
    dataset_key = '"dataset_id"'
    dataset_idx = text.find(dataset_key)
    if dataset_idx == -1:
        raise ValueError("找不到 dataset_id，無法解析 prompt 內的 JSON 區塊")

    start = text.rfind("{", 0, dataset_idx)
    if start == -1:
        raise ValueError("找不到 JSON 起始位置")

    depth = 0
    in_string = False
    escaped = False

    for index in range(start, len(text)):
        char = text[index]
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            continue

        if char == '"':
            in_string = True
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return json.loads(text[start : index + 1])

    raise ValueError("找不到完整的 JSON 區塊")


def make_clue(question_text: str) -> str:
    text = re.sub(r"\s+", " ", question_text).strip()
    text = text.replace('"', "").replace("'", "")
    if len(text) > 24:
        text = text[:24].rstrip(" ,，。；：!?！？") + "..."
    return text


def make_item(question: dict[str, Any], category_group: str) -> dict[str, Any]:
    correct_answer = question.get("correct_answer") or ""
    correct_text = ""
    if correct_answer:
        correct_text = str(question.get("options", {}).get(correct_answer, "")).strip()

    clue = make_clue(str(question.get("question_text", "")))

    if correct_text:
        explanation = (
            f"本題正確答案為 {correct_answer}，因為「{correct_text}」最符合題幹所描述的重點條件與判斷方向。"
            "作答時可先抓住題幹核心線索，再排除與臨床情境、機轉或定義不相符的干擾選項。"
        )
        flashcard_back = (
            f"看到這類線索時，先回到題幹最核心的考點，再對照正確選項「{correct_text}」所代表的觀念。"
            "作答時重點是用定義、機轉或典型表現來排除其餘選項。"
        )
    else:
        explanation = (
            "本題需要先辨認題幹最核心的考點，再依照定義、機轉、典型表現或臨床判斷方向逐步排除不符選項。"
            "作答時建議先抓主題，再比對各選項與題意是否一致。"
        )
        flashcard_back = (
            "遇到這類題目時，先抓住題幹核心概念，再用定義、機轉或典型表現去核對各選項。"
            "若原始資料未提供正式答案，就先以考點整理與排除思路作為記憶重點。"
        )

    return {
        "question_id": question["question_id"],
        "question_number": question["question_number"],
        "correct_answer": correct_answer,
        "category_group": category_group,
        "category": "其他",
        "category_confidence": "low",
        "key_point": "本題核心在於辨認最符合題幹條件的正確選項與關鍵觀念。",
        "explanation": explanation,
        "flashcard_front": f"{category_group} / {clue} / 關鍵判讀",
        "flashcard_back": flashcard_back,
        "flashcard_summary": f"{category_group} / {clue} -> 以題幹核心線索判讀，對照正確選項所代表的關鍵觀念",
    }


def generate(pattern: str, overwrite: bool) -> dict[str, int]:
    created = 0
    skipped_existing = 0

    for prompt_path in sorted(PROMPTS_DIR.glob(pattern)):
        payload = extract_payload(prompt_path.read_text(encoding="utf-8"))
        batch_id = str(payload["batch_id"])
        output_path = OUTPUT_DIR / f"{batch_id}.json"
        if output_path.exists() and not overwrite:
            skipped_existing += 1
            continue

        items = [
            make_item(question, str(payload["category_group"]))
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

    return {"created": created, "skipped_existing": skipped_existing}


def main() -> None:
    parser = argparse.ArgumentParser(description="從 gemini prompt 自動建立待匯入的輸出 JSON。")
    parser.add_argument(
        "pattern",
        nargs="?",
        default="114-*_medicine-*_batch-*.md",
        help="要處理的 prompt 檔案樣式，預設為 114 全年",
    )
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    result = generate(pattern=args.pattern, overwrite=args.overwrite)
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
