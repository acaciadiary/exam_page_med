from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from .build_dataset import build_dataset
    from .moex_sources import get_preset
except ImportError:
    from build_dataset import build_dataset
    from moex_sources import get_preset


def build_from_downloads(preset: str, downloads_dir: Path, data_dir: Path) -> list[dict]:
    manifest_items: list[dict] = []

    for source in get_preset(preset):
        subject_dir = downloads_dir / source.year / source.subject
        question_pdf = subject_dir / "questions.pdf"
        answer_pdf = subject_dir / "answers.pdf"
        correction_pdf = subject_dir / "corrections.pdf"

        if not question_pdf.exists() or not answer_pdf.exists():
            raise FileNotFoundError(
                f"Missing downloaded PDFs for {source.subject}: {question_pdf}, {answer_pdf}"
            )

        dataset = build_dataset(
            question_path=question_pdf,
            answer_path=answer_pdf,
            year=source.year,
            subject=source.subject,
            title=source.title,
            source=source.question_url,
            correction_path=correction_pdf if correction_pdf.exists() else None,
        )

        out_path = data_dir / "exams" / source.year / f"{source.subject}.json"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(dataset, ensure_ascii=False, indent=2), encoding="utf-8")

        manifest_items.append(
            {
                "id": dataset["id"],
                "year": source.year,
                "title": source.title,
                "subject": source.subject,
                "path": str(out_path.relative_to(data_dir.parent)).replace("\\", "/"),
                "question_count": len(dataset["questions"]),
            }
        )

    return manifest_items


def sort_manifest_item(item: dict[str, Any]) -> tuple[int, int, int]:
    year_value = str(item.get("year", "0-0"))
    year_part, _, stage_part = year_value.partition("-")
    subject_value = str(item.get("subject", "medicine-0")).rsplit("-", 1)[-1]

    try:
        year_number = int(year_part)
    except ValueError:
        year_number = 0
    try:
        stage_number = int(stage_part or "0")
    except ValueError:
        stage_number = 0
    try:
        subject_number = int(subject_value)
    except ValueError:
        subject_number = 0

    return (-year_number, -stage_number, -subject_number)


def write_merged_manifest(data_dir: Path, items: list[dict]) -> None:
    manifest_path = data_dir / "manifest.json"
    existing_items: list[dict[str, Any]] = []

    if manifest_path.exists():
        existing = json.loads(manifest_path.read_text(encoding="utf-8"))
        existing_items = list(existing.get("exams", []))

    merged_by_path = {
        str(item.get("path")): item
        for item in existing_items
        if item.get("path")
    }
    for item in items:
        merged_by_path[str(item["path"])] = item

    manifest = {
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "exams": sorted(merged_by_path.values(), key=sort_manifest_item),
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build frontend JSON for a downloaded MOEX preset.")
    parser.add_argument("--preset", default="physician-115-first")
    parser.add_argument("--downloads-dir", default="downloads/moex")
    parser.add_argument("--data-dir", default="public/data")
    parser.add_argument("--write-manifest", action="store_true")
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    items = build_from_downloads(args.preset, Path(args.downloads_dir), data_dir)

    if args.write_manifest:
        write_merged_manifest(data_dir, items)

    print(json.dumps(items, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
