from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from scripts.exams.export_gemini_prompts import category_profile


def expand_paths(patterns: list[str]) -> list[Path]:
    paths: list[Path] = []
    for pattern in patterns:
        matches = sorted(Path().glob(pattern))
        paths.extend(matches or [Path(pattern)])
    return paths


def parse_json_file(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8").strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, flags=re.S)
        if not match:
            raise
        return json.loads(match.group(0))


def index_datasets(data_dir: Path) -> dict[str, Path]:
    index: dict[str, Path] = {}
    for path in sorted(data_dir.glob("**/*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        dataset_id = data.get("id")
        if dataset_id:
            index[str(dataset_id)] = path
    return index


def clean(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def clean_preserve_newlines(value: Any) -> str:
    text = str(value or "").replace("\r\n", "\n").strip()
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n", "\n\n", text)
    return text


def validate_category(dataset: dict[str, Any], item: dict[str, Any], question_id: str) -> tuple[str | None, str | None, str | None]:
    category = clean(item.get("category"))
    if not category:
        return None, None, None

    # Normalize category name for robustness against Simplified Chinese and variations
    replacements = {
        "医学": "醫學", "妇产": "婦產", "急诊": "急診", "神经": "神經",
        "风湿": "風濕", "儿科": "兒科", "免疫风湿": "免疫風濕",
        "心脏": "心臟", "肾脏": "腎臟", "新陈代谢": "新陳代謝",
        "血液肿瘤": "血液腫瘤", "耳鼻喉": "耳鼻喉科",
        "生物化学": "生物化學", "解剖": "解剖學",
        "组织学": "組織學", "生理": "生理學", "微生物免疫": "微生物免疫學",
        "寄生虫": "寄生蟲學", "药理": "藥理學", "病理": "病理學",
        "公共卫生": "公共衛生學", "外科概论": "外科概論",
        "大肠直肠": "大腸直腸科", "移植": "移植外科", "小儿外科": "小兒外科",
        "整形": "整形外科", "泌尿": "泌尿科",
    }
    for k, v in replacements.items():
        category = category.replace(k, v)

    # Specific exact matches
    if category == "麻醉":
        category = "麻醉科"
    elif category == "復健":
        category = "復健科"

    profile = category_profile(dataset)
    allowed = set(profile["categories"])
    
    # Attempt fuzzy matching if not exactly in allowed
    if category not in allowed:
        for a in allowed:
            if category in a or a in category:
                category = a
                break

    if category not in allowed:
        raise ValueError(
            f"Invalid category for {question_id}: {category}. "
            f"Allowed: {', '.join(profile['categories'])}"
        )

    confidence = clean(item.get("category_confidence") or "medium")
    if confidence not in {"high", "medium", "low"}:
        raise ValueError(
            f"Invalid category_confidence for {question_id}: {confidence}"
        )

    returned_group = clean(item.get("category_group") or profile["category_group"])
    
    def normalize_g(s: str) -> str:
        s = s.replace("'", "").replace('"', "").replace(" ", "")
        s = s.replace("(", "").replace(")", "").replace("（", "").replace("）", "")
        return s
        
    expected_normalized = normalize_g(str(profile["category_group"]))
    returned_normalized = normalize_g(returned_group)
    
    if not (expected_normalized == returned_normalized or returned_normalized.startswith(expected_normalized)):
        print(f"Warning: category_group mismatch for {question_id}: expected "
              f"{profile['category_group']}, got {returned_group}. Using expected.")

    return str(profile["category_group"]), category, confidence


def import_outputs(
    output_paths: list[Path],
    data_dir: Path,
    dry_run: bool,
    model_label: str,
) -> dict[str, Any]:
    dataset_index = index_datasets(data_dir)
    changed: dict[Path, dict[str, Any]] = {}
    reports: list[dict[str, Any]] = []
    now = datetime.now(timezone.utc).isoformat()

    for output_path in output_paths:
        output = parse_json_file(output_path)
        dataset_id = str(output.get("dataset_id", ""))
        dataset_path = dataset_index.get(dataset_id)
        if not dataset_path:
            raise ValueError(f"Unknown dataset_id in {output_path}: {dataset_id}")

        dataset = changed.get(dataset_path)
        if dataset is None:
            dataset = json.loads(dataset_path.read_text(encoding="utf-8"))
            changed[dataset_path] = dataset

        questions = {question.get("id"): question for question in dataset.get("questions", [])}
        imported = 0
        skipped = 0

        for item in output.get("items", []):
            question_id = item.get("question_id")
            question = questions.get(question_id)
            if not question:
                raise ValueError(f"Unknown question_id in {output_path}: {question_id}")
            if item.get("question_number") != question.get("question_number"):
                raise ValueError(f"Question number mismatch for {question_id}")

            expected_answer = str(question.get("correct_answer") or ",".join(question.get("correct_answers", [])))
            returned_answer = str(item.get("correct_answer", expected_answer))
            if returned_answer != expected_answer:
                raise ValueError(
                    f"Correct answer mismatch for {question_id}: expected {expected_answer}, got {returned_answer}"
                )

            key_point = clean(item.get("key_point"))
            explanation = clean_preserve_newlines(item.get("explanation"))
            flashcard_front = clean(item.get("flashcard_front"))
            flashcard_back = clean(item.get("flashcard_back"))
            flashcard_summary = clean(item.get("flashcard_summary"))
            if not (key_point and explanation and flashcard_summary):
                skipped += 1
                continue
            if not flashcard_front or not flashcard_back:
                front, separator, back = flashcard_summary.partition("->")
                flashcard_front = flashcard_front or clean(front)
                flashcard_back = flashcard_back or clean(back if separator else flashcard_summary)

            category_group, category, confidence = validate_category(dataset, item, str(question_id))

            question["key_point"] = key_point
            question["explanation"] = explanation
            question["flashcard_front"] = flashcard_front
            question["flashcard_back"] = flashcard_back
            question["flashcard_summary"] = flashcard_summary
            if category:
                question["category_group"] = category_group
                question["category"] = category
                question["category_confidence"] = confidence
                question["category_source"] = "auto"
            question["review_status"] = "ai_generated"
            question["explanation_model"] = model_label
            question["explanation_generated_at"] = now
            imported += 1

        reports.append(
            {
                "output_path": str(output_path),
                "dataset_id": dataset_id,
                "batch_id": output.get("batch_id"),
                "imported": imported,
                "skipped": skipped,
            }
        )

    if not dry_run:
        for path, dataset in changed.items():
            dataset["updated_at"] = now
            path.write_text(
                json.dumps(dataset, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )

    return {
        "dry_run": dry_run,
        "dataset_count": len(changed),
        "imported": sum(report["imported"] for report in reports),
        "skipped": sum(report["skipped"] for report in reports),
        "reports": reports,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Import Gemini JSON explanations into datasets.")
    parser.add_argument("outputs", nargs="+", help="Gemini output JSON files or glob patterns")
    parser.add_argument("--data-dir", default="public/data/exams")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--model-label", default="gemini-pro-manual")
    parser.add_argument("--report", default="reports/gemini-import-report.json")
    args = parser.parse_args()

    report = import_outputs(
        output_paths=expand_paths(args.outputs),
        data_dir=Path(args.data_dir),
        dry_run=args.dry_run,
        model_label=args.model_label,
    )
    output = json.dumps(report, ensure_ascii=False, indent=2)
    if args.report:
        report_path = Path(args.report)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(output + "\n", encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
