from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

VALID_STATUSES = {"empty", "ai_generated", "reviewed"}
EXPLANATION_HEADINGS = ("【題幹解析】", "【選項詳解】", "【核心考點】")


def expand_paths(patterns: list[str]) -> list[Path]:
    paths: list[Path] = []
    for pattern in patterns:
        matches = sorted(Path().glob(pattern))
        paths.extend(matches or [Path(pattern)])
    return paths


def validate_dataset(path: Path) -> dict[str, Any]:
    dataset = json.loads(path.read_text(encoding="utf-8-sig"))
    issues: list[dict[str, Any]] = []
    complete = 0
    reviewed = 0
    ai_generated = 0

    for question in dataset.get("questions", []):
        qid = question.get("id")
        number = question.get("question_number")
        fields = {
            "key_point": str(question.get("key_point", "")).strip(),
            "explanation": str(question.get("explanation", "")).strip(),
            "flashcard_front": str(question.get("flashcard_front", "")).strip(),
            "flashcard_back": str(question.get("flashcard_back", "")).strip(),
            "flashcard_summary": str(question.get("flashcard_summary", "")).strip(),
        }
        status = question.get("review_status", "empty")

        if status not in VALID_STATUSES:
            issues.append(issue(qid, number, "invalid_review_status", str(status)))
        if all(fields.values()):
            complete += 1
        elif any(fields.values()):
            issues.append(issue(qid, number, "partial_explanation", "詳解欄位不完整"))

        if status == "reviewed":
            reviewed += 1
        if status == "ai_generated":
            ai_generated += 1
        if fields["explanation"] and len(fields["explanation"]) < 24:
            issues.append(issue(qid, number, "short_explanation", "詳解過短，建議人工檢查"))
        if fields["explanation"]:
            duplicate_headings = [
                heading for heading in EXPLANATION_HEADINGS if fields["explanation"].count(heading) > 1
            ]
            if duplicate_headings:
                issues.append(
                    issue(
                        qid,
                        number,
                        "nested_repeated_explanation",
                        f"詳解章節重複，疑似把既有詳解再次包入新詳解: {', '.join(duplicate_headings)}",
                    )
                )

    total = len(dataset.get("questions", []))
    return {
        "path": str(path),
        "dataset_id": dataset.get("id"),
        "question_count": total,
        "complete": complete,
        "missing": total - complete,
        "ai_generated": ai_generated,
        "reviewed": reviewed,
        "issue_count": len(issues),
        "issues": issues,
    }


def issue(question_id: Any, number: Any, code: str, message: str) -> dict[str, Any]:
    return {
        "question_id": question_id,
        "question_number": number,
        "code": code,
        "message": message,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate generated explanation fields.")
    parser.add_argument("paths", nargs="+", help="Dataset JSON paths or glob patterns")
    parser.add_argument("--out", default="reports/explanation-quality.json")
    parser.add_argument("--strict", action="store_true", help="Fail when any explanation is missing")
    args = parser.parse_args()

    reports = [validate_dataset(path) for path in expand_paths(args.paths)]
    report = {
        "dataset_count": len(reports),
        "question_count": sum(item["question_count"] for item in reports),
        "complete": sum(item["complete"] for item in reports),
        "missing": sum(item["missing"] for item in reports),
        "issue_count": sum(item["issue_count"] for item in reports),
        "reports": reports,
    }
    output = json.dumps(report, ensure_ascii=False, indent=2)
    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output + "\n", encoding="utf-8")
    print(output)

    if report["issue_count"] > 0 or (args.strict and report["missing"] > 0):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
