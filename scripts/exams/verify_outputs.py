from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

OUTPUT_DIR = Path("reports/gemini_outputs")
EXAMS_DIR = Path("public/data/exams")
DEFAULT_REPORT = Path("reports/gemini_outputs_verification_report.json")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_answer(value: Any) -> str:
    return str(value or "").strip()


def index_exam_answers(exams_dir: Path) -> dict[str, dict[str, str]]:
    dataset_index: dict[str, dict[str, str]] = {}
    for exam_path in sorted(exams_dir.glob("**/*.json")):
        exam = load_json(exam_path)
        dataset_id = str(exam.get("id") or "").strip()
        if not dataset_id:
            continue
        answers: dict[str, str] = {}
        for question in exam.get("questions", []):
            question_id = str(question.get("id") or "").strip()
            if not question_id:
                continue
            answers[question_id] = normalize_answer(question.get("correct_answer"))
        dataset_index[dataset_id] = answers
    return dataset_index


def validate_output(
    output_path: Path,
    dataset_answers: dict[str, dict[str, str]],
) -> tuple[bool, list[str], str | None]:
    try:
        output = load_json(output_path)
    except Exception as exc:
        return False, [f"JSON 讀取失敗: {exc}"], None

    dataset_id = str(output.get("dataset_id") or "").strip()
    if not dataset_id:
        return False, ["缺少 dataset_id"], None

    if output.get("batch_id") and str(output.get("batch_id")).strip() != output_path.stem:
        return False, [f"batch_id 與檔名不一致: {output.get('batch_id')} != {output_path.stem}"], dataset_id

    questions = dataset_answers.get(dataset_id)
    if questions is None:
        return False, [f"找不到對應原始題庫 dataset_id: {dataset_id}"], dataset_id

    items = output.get("items")
    if not isinstance(items, list):
        return False, ["items 不是陣列"], dataset_id

    mismatches: list[str] = []
    for index, item in enumerate(items, start=1):
        question_id = str(item.get("question_id") or "").strip()
        if not question_id:
            mismatches.append(f"第 {index} 題缺少 question_id")
            break

        expected_answer = questions.get(question_id)
        if expected_answer is None:
            mismatches.append(f"{question_id} 不存在於原始題庫 {dataset_id}")
            break

        returned_answer = normalize_answer(item.get("correct_answer"))
        if returned_answer != expected_answer:
            mismatches.append(
                f"{question_id} correct_answer 不一致: output={returned_answer!r}, source={expected_answer!r}"
            )
            break

    return len(mismatches) == 0, mismatches, dataset_id


def verify_and_filter(
    output_dir: Path = OUTPUT_DIR,
    exams_dir: Path = EXAMS_DIR,
    report_path: Path = DEFAULT_REPORT,
) -> dict[str, Any]:
    if not output_dir.exists():
        raise FileNotFoundError(f"Output directory does not exist: {output_dir}")

    output_files = sorted(output_dir.glob("*.json"))
    print(f"Found {len(output_files)} files in {output_dir}.")

    dataset_answers = index_exam_answers(exams_dir)
    kept: list[str] = []
    deleted: list[dict[str, Any]] = []

    for output_path in output_files:
        is_valid, reasons, dataset_id = validate_output(output_path, dataset_answers)
        if is_valid:
            kept.append(output_path.name)
            continue

        print(f"[DELETE] {output_path.name}")
        for reason in reasons:
            print(f"  - {reason}")
        output_path.unlink()
        deleted.append(
            {
                "file": output_path.name,
                "dataset_id": dataset_id,
                "reasons": reasons,
            }
        )

    summary = {
        "total_analyzed": len(output_files),
        "kept_count": len(kept),
        "deleted_count": len(deleted),
        "deleted_files": deleted,
    }

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("\nVerification Summary:")
    print(f"  Total analyzed : {summary['total_analyzed']}")
    print(f"  Valid kept     : {summary['kept_count']}")
    print(f"  Mismatch delete: {summary['deleted_count']}")
    print(f"  Report saved   : {report_path}")

    return summary


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Verify Gemini output JSON files and delete any file whose correct_answer mismatches source data."
    )
    parser.add_argument("--output-dir", default=str(OUTPUT_DIR))
    parser.add_argument("--exams-dir", default=str(EXAMS_DIR))
    parser.add_argument("--report", default=str(DEFAULT_REPORT))
    args = parser.parse_args()

    verify_and_filter(
        output_dir=Path(args.output_dir),
        exams_dir=Path(args.exams_dir),
        report_path=Path(args.report),
    )


if __name__ == "__main__":
    main()
