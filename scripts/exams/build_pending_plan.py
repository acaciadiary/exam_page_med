from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


MANIFEST_PATH = Path("reports/gemini_prompts/manifest.json")
OUTPUT_DIR = Path("reports/gemini_outputs")
DEFAULT_JSON_PATH = Path("reports/pending_generation_plan.json")
DEFAULT_MD_PATH = Path("reports/pending_generation_plan.md")


def load_manifest() -> list[dict[str, Any]]:
    data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return list(data.get("batches", []))


def current_completed_ids(output_dir: Path) -> set[str]:
    return {path.stem for path in output_dir.glob("*.json")}


def prompt_size_kb(path_str: str) -> float:
    path = Path(path_str)
    if not path.exists():
        return 0.0
    return round(path.stat().st_size / 1024, 1)


def dataset_sort_key(dataset_id: str) -> tuple[int, str]:
    subject = dataset_id.split("_", 1)[1]
    try:
        return int(subject.split("-")[1]), dataset_id
    except (IndexError, ValueError):
        return 999, dataset_id


def order_year_batches(batches: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for batch in batches:
        grouped.setdefault(batch["dataset_id"], []).append(batch)

    ordered: list[dict[str, Any]] = []
    datasets = sorted(grouped, key=dataset_sort_key)
    datasets.sort(key=lambda dataset_id: (len(grouped[dataset_id]) > 1, dataset_sort_key(dataset_id)))

    for dataset_id in datasets:
        items = sorted(grouped[dataset_id], key=lambda batch: batch["batch_id"])
        if len(items) > 1:
            min_question_count = min(item["question_count"] for item in items)
            items.sort(
                key=lambda batch: (
                    batch["question_count"] != min_question_count,
                    batch["batch_id"],
                )
            )
        ordered.extend(items)

    return ordered


def build_rounds(batches: list[dict[str, Any]], round_size: int) -> list[dict[str, Any]]:
    rounds: list[dict[str, Any]] = []
    for index in range(0, len(batches), round_size):
        chunk = batches[index : index + round_size]
        rounds.append(
            {
                "round": len(rounds) + 1,
                "batch_count": len(chunk),
                "question_count": sum(batch["question_count"] for batch in chunk),
                "prompt_kb": round(sum(batch["prompt_kb"] for batch in chunk), 1),
                "batch_ids": [batch["batch_id"] for batch in chunk],
            }
        )
    return rounds


def build_plan(focus_year: str | None, round_size: int) -> dict[str, Any]:
    manifest = load_manifest()
    completed_ids = current_completed_ids(OUTPUT_DIR)

    pending = []
    for batch in manifest:
        if batch["batch_id"] in completed_ids:
            continue
        if focus_year and not batch["dataset_id"].startswith(focus_year + "_"):
            continue
        pending.append(
            {
                "dataset_id": batch["dataset_id"],
                "batch_id": batch["batch_id"],
                "prompt_path": batch["prompt_path"],
                "suggested_output_path": batch["suggested_output_path"],
                "question_count": batch["question_count"],
                "prompt_kb": prompt_size_kb(batch["prompt_path"]),
            }
        )

    ordered = order_year_batches(pending)
    rounds = build_rounds(ordered, round_size)

    datasets: list[dict[str, Any]] = []
    by_dataset: dict[str, list[dict[str, Any]]] = {}
    for batch in ordered:
        by_dataset.setdefault(batch["dataset_id"], []).append(batch)
    for dataset_id in sorted(by_dataset, key=dataset_sort_key):
        items = by_dataset[dataset_id]
        datasets.append(
            {
                "dataset_id": dataset_id,
                "batch_count": len(items),
                "question_count": sum(batch["question_count"] for batch in items),
                "prompt_kb": round(sum(batch["prompt_kb"] for batch in items), 1),
                "batch_ids": [batch["batch_id"] for batch in items],
            }
        )

    return {
        "focus_year": focus_year or "ALL",
        "round_size": round_size,
        "pending_batch_count": len(ordered),
        "pending_question_count": sum(batch["question_count"] for batch in ordered),
        "pending_prompt_kb": round(sum(batch["prompt_kb"] for batch in ordered), 1),
        "datasets": datasets,
        "ordered_batches": ordered,
        "rounds": rounds,
    }


def render_markdown(plan: dict[str, Any]) -> str:
    lines = [
        f"# Pending Generation Plan: {plan['focus_year']}",
        "",
        f"- 待處理批次：{plan['pending_batch_count']}",
        f"- 待處理題數：{plan['pending_question_count']}",
        f"- Prompt 總量：約 {plan['pending_prompt_kb']} KB",
        f"- 建議每輪批次數：{plan['round_size']}",
        "",
        "## Dataset Summary",
        "",
    ]
    for dataset in plan["datasets"]:
        lines.append(
            f"- `{dataset['dataset_id']}`: {dataset['batch_count']} 批 / {dataset['question_count']} 題 / 約 {dataset['prompt_kb']} KB"
        )

    lines.extend(["", "## Recommended Rounds", ""])
    for round_info in plan["rounds"]:
        lines.append(
            f"### Round {round_info['round']} ({round_info['batch_count']} 批 / {round_info['question_count']} 題 / 約 {round_info['prompt_kb']} KB)"
        )
        lines.append("")
        for batch_id in round_info["batch_ids"]:
            lines.append(f"- `{batch_id}`")
        lines.append("")

    lines.extend(["## Ordered Batches", ""])
    for batch in plan["ordered_batches"]:
        lines.append(
            f"- `{batch['batch_id']}` | {batch['dataset_id']} | {batch['question_count']} 題 | 約 {batch['prompt_kb']} KB | `{batch['prompt_path']}`"
        )

    lines.append("")
    return "\n".join(lines)


def write_round_files(plan: dict[str, Any], round_dir: Path) -> None:
    round_dir.mkdir(parents=True, exist_ok=True)
    batch_lookup = {batch["batch_id"]: batch for batch in plan["ordered_batches"]}

    for round_info in plan["rounds"]:
        lines = [
            f"# {plan['focus_year']} Round {round_info['round']}",
            "",
            f"- 批次數：{round_info['batch_count']}",
            f"- 題數：{round_info['question_count']}",
            f"- Prompt 總量：約 {round_info['prompt_kb']} KB",
            "",
            "## Batches",
            "",
        ]
        for batch_id in round_info["batch_ids"]:
            batch = batch_lookup[batch_id]
            lines.append(f"- `{batch_id}`")
            lines.append(f"  prompt: `{batch['prompt_path']}`")
            lines.append(f"  output: `{batch['suggested_output_path']}`")
            lines.append(f"  questions: {batch['question_count']}")
            lines.append(f"  prompt_kb: {batch['prompt_kb']}")
            lines.append("")

        target = round_dir / f"round-{round_info['round']:02d}.md"
        target.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a low-risk, low-traffic pending generation plan.")
    parser.add_argument("--focus-year", default=None, help="例如 112-2")
    parser.add_argument("--round-size", type=int, default=8, help="每輪建議批次數")
    parser.add_argument("--json-out", default=str(DEFAULT_JSON_PATH))
    parser.add_argument("--md-out", default=str(DEFAULT_MD_PATH))
    parser.add_argument("--round-dir", default=None, help="若提供，另外輸出每輪一個 markdown 清單")
    args = parser.parse_args()

    plan = build_plan(focus_year=args.focus_year, round_size=args.round_size)

    json_out = Path(args.json_out)
    json_out.parent.mkdir(parents=True, exist_ok=True)
    json_out.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md_out = Path(args.md_out)
    md_out.parent.mkdir(parents=True, exist_ok=True)
    md_out.write_text(render_markdown(plan), encoding="utf-8")

    if args.round_dir:
        write_round_files(plan, Path(args.round_dir))

    print(json.dumps({
        "focus_year": plan["focus_year"],
        "pending_batch_count": plan["pending_batch_count"],
        "pending_question_count": plan["pending_question_count"],
        "json_out": str(json_out),
        "md_out": str(md_out),
        "round_dir": args.round_dir,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
