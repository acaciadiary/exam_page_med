from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

EXPECTED_OPTIONS = {"A", "B", "C", "D"}


def validate_dataset(path: str | Path) -> dict[str, Any]:
    dataset_path = Path(path)
    dataset = json.loads(dataset_path.read_text(encoding="utf-8-sig"))
    questions = dataset.get("questions", [])

    issues: list[dict[str, Any]] = []
    answer_counter: Counter[str] = Counter()
    seen_ids: set[str] = set()
    seen_numbers: set[int] = set()

    for index, question in enumerate(questions, start=1):
        qid = question.get("id")
        number = question.get("question_number")
        options = question.get("options", {})
        answer = question.get("correct_answer")
        text = str(question.get("question_text", "")).strip()

        if not qid:
            issues.append(issue(index, number, "missing_id", "題目缺少 id"))
        elif qid in seen_ids:
            issues.append(issue(index, number, "duplicate_id", f"重複 id: {qid}"))
        else:
            seen_ids.add(qid)

        if not isinstance(number, int):
            issues.append(issue(index, number, "invalid_number", "question_number 不是整數"))
        elif number in seen_numbers:
            issues.append(issue(index, number, "duplicate_number", f"重複題號: {number}"))
        else:
            seen_numbers.add(number)

        if not text:
            issues.append(issue(index, number, "empty_question", "題幹為空"))

        option_keys = set(options.keys())
        if option_keys != EXPECTED_OPTIONS:
            issues.append(
                issue(
                    index,
                    number,
                    "invalid_options",
                    f"選項不是 A-D 完整集合: {sorted(option_keys)}",
                )
            )

        for key in sorted(EXPECTED_OPTIONS & option_keys):
            option_text = str(options.get(key, "")).strip()
            if not option_text:
                issues.append(issue(index, number, "empty_option", f"{key} 選項為空"))
            if looks_like_next_question(option_text):
                issues.append(
                    issue(index, number, "option_contains_next_question", f"{key} 選項疑似含下一題題號")
                )

        if answer:
            answer_counter[str(answer)] += 1
            if str(answer) not in EXPECTED_OPTIONS and "#" not in str(answer):
                issues.append(issue(index, number, "invalid_answer", f"答案格式異常: {answer}"))
        else:
            issues.append(issue(index, number, "missing_answer", "缺少標準答案"))

    expected_numbers = set(range(1, len(questions) + 1))
    missing_numbers = sorted(expected_numbers - seen_numbers)
    if missing_numbers:
        issues.append(
            {
                "index": None,
                "question_number": None,
                "code": "missing_sequence_numbers",
                "message": f"題號序列缺漏: {missing_numbers[:20]}",
            }
        )

    return {
        "path": str(dataset_path),
        "id": dataset.get("id"),
        "title": dataset.get("title"),
        "question_count": len(questions),
        "answers": dict(sorted(answer_counter.items())),
        "issue_count": len(issues),
        "issues": issues,
    }


def issue(index: int, number: Any, code: str, message: str) -> dict[str, Any]:
    return {
        "index": index,
        "question_number": number,
        "code": code,
        "message": message,
    }


def looks_like_next_question(text: str) -> bool:
    return re.search(r"\s\d{1,3}\.(?!\d)\s*\S", text) is not None


def validate_many(paths: list[str]) -> dict[str, Any]:
    reports = [validate_dataset(path) for path in paths]
    return {
        "dataset_count": len(reports),
        "total_questions": sum(report["question_count"] for report in reports),
        "total_issues": sum(report["issue_count"] for report in reports),
        "reports": reports,
    }


def issue_signature(dataset_path: str, issue: dict[str, Any]) -> str:
    return json.dumps(
        {
            "path": dataset_path.replace("\\", "/"),
            "index": issue.get("index"),
            "question_number": issue.get("question_number"),
            "code": issue.get("code"),
            "message": issue.get("message"),
        },
        ensure_ascii=False,
        sort_keys=True,
    )


def collect_issue_signatures(report: dict[str, Any]) -> set[str]:
    signatures: set[str] = set()
    for dataset_report in report.get("reports", []):
        dataset_path = str(dataset_report.get("path", ""))
        for current_issue in dataset_report.get("issues", []):
            signatures.add(issue_signature(dataset_path, current_issue))
    return signatures


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate generated frontend exam datasets.")
    parser.add_argument("paths", nargs="+", help="Dataset JSON paths or glob patterns")
    parser.add_argument("--out", default=None, help="Optional report JSON path")
    parser.add_argument(
        "--baseline",
        default=None,
        help="Optional baseline report JSON. Existing known issues in the baseline will not fail validation.",
    )
    args = parser.parse_args()

    expanded: list[str] = []
    for pattern in args.paths:
        matches = sorted(str(path) for path in Path().glob(pattern))
        expanded.extend(matches or [pattern])

    report = validate_many(expanded)
    output = json.dumps(report, ensure_ascii=False, indent=2)

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output, encoding="utf-8")
    print(output)

    if args.baseline:
        baseline_path = Path(args.baseline)
        baseline_report = json.loads(baseline_path.read_text(encoding="utf-8"))
        baseline_signatures = collect_issue_signatures(baseline_report)
        current_signatures = collect_issue_signatures(report)
        new_signatures = sorted(current_signatures - baseline_signatures)

        summary = {
            "baseline_issue_count": len(baseline_signatures),
            "current_issue_count": len(current_signatures),
            "new_issue_count": len(new_signatures),
        }
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        if new_signatures:
            raise SystemExit(1)
        raise SystemExit(0)

    if report["total_issues"] > 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
