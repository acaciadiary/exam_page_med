from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class CategoryRange:
    start: int
    end: int
    category: str
    category_group: str | None = None

    def contains(self, question_number: int) -> bool:
        return self.start <= question_number <= self.end


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Apply manual question-number category ranges to MOEX datasets."
    )
    parser.add_argument(
        "--map",
        default="scripts/exams/category_ranges.json",
        help="Path to a JSON category range map.",
    )
    parser.add_argument(
        "--data-dir",
        default="public/data/exams",
        help="Root folder that contains exam dataset JSON files.",
    )
    parser.add_argument(
        "--clear-unmatched",
        action="store_true",
        help="Clear category fields for questions not covered by a range.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the planned changes without writing files.",
    )
    return parser.parse_args()


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def write_json(path: Path, payload: Any) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as file:
        json.dump(payload, file, ensure_ascii=False, indent=2)
        file.write("\n")


def load_ranges(config: dict[str, Any], dataset_id: str) -> list[CategoryRange]:
    raw_dataset = config.get("datasets", {}).get(dataset_id)
    if raw_dataset is None:
        return []

    raw_ranges = raw_dataset if isinstance(raw_dataset, list) else raw_dataset.get("ranges", [])
    ranges = [
        CategoryRange(
            start=int(item["start"]),
            end=int(item["end"]),
            category=str(item["category"]).strip(),
            category_group=(
                str(item["category_group"]).strip()
                if item.get("category_group")
                else None
            ),
        )
        for item in raw_ranges
    ]
    validate_ranges(dataset_id, ranges)
    return ranges


def validate_ranges(dataset_id: str, ranges: list[CategoryRange]) -> None:
    seen: dict[int, str] = {}
    for item in ranges:
        if item.start <= 0 or item.end < item.start:
            raise ValueError(
                f"{dataset_id}: invalid range {item.start}-{item.end} for {item.category}"
            )
        for question_number in range(item.start, item.end + 1):
            if question_number in seen:
                raise ValueError(
                    f"{dataset_id}: question {question_number} is mapped to both "
                    f"{seen[question_number]} and {item.category}"
                )
            seen[question_number] = item.category


def find_dataset_path(data_dir: Path, dataset_id: str) -> Path:
    year, subject = dataset_id.split("_", 1)
    candidate = data_dir / year / f"{subject}.json"
    if candidate.exists():
        return candidate

    matches = list(data_dir.glob(f"**/{subject}.json"))
    if matches:
        return matches[0]
    raise FileNotFoundError(f"Cannot find dataset JSON for {dataset_id}")


def apply_ranges(
    dataset: dict[str, Any],
    ranges: list[CategoryRange],
    clear_unmatched: bool,
) -> dict[str, int]:
    assigned = 0
    cleared = 0
    unassigned = 0

    for question in dataset.get("questions", []):
        question_number = int(question["question_number"])
        match = next((item for item in ranges if item.contains(question_number)), None)

        if match:
            question["category"] = match.category
            if match.category_group:
                question["category_group"] = match.category_group
            else:
                question.pop("category_group", None)
            question["category_source"] = "manual_range"
            assigned += 1
            continue

        unassigned += 1
        if clear_unmatched:
            for key in ("category", "category_group"):
                question.pop(key, None)
            question["category_source"] = "unassigned"
            cleared += 1

    return {
        "assigned": assigned,
        "cleared": cleared,
        "unassigned": unassigned,
    }


def main() -> None:
    args = parse_args()
    map_path = Path(args.map)
    data_dir = Path(args.data_dir)
    config = load_json(map_path)

    for dataset_id in sorted(config.get("datasets", {}).keys()):
        ranges = load_ranges(config, dataset_id)
        if not ranges:
            print(f"{dataset_id}: no ranges, skipped")
            continue

        dataset_path = find_dataset_path(data_dir, dataset_id)
        dataset = load_json(dataset_path)
        stats = apply_ranges(dataset, ranges, clear_unmatched=args.clear_unmatched)
        print(
            f"{dataset_id}: assigned={stats['assigned']} "
            f"unassigned={stats['unassigned']} cleared={stats['cleared']}"
        )

        if not args.dry_run:
            write_json(dataset_path, dataset)


if __name__ == "__main__":
    main()
