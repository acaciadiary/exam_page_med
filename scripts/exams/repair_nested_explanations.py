from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


EXPLANATION_FIELDS = [
    "key_point",
    "explanation",
    "flashcard_front",
    "flashcard_back",
    "flashcard_summary",
]

OPTION_LABELS = ["A", "B", "C", "D"]

CURATED_FALLBACKS: dict[str, dict[str, str]] = {
    "110-1_medicine-2_022": {
        "key_point": "癌症免疫檢查點治療的重點是 CTLA-4 與 PD-1 主要抑制 T 細胞反應，抗體治療可解除此抑制。",
        "explanation": (
            "【題幹解析】\n"
            "本題問免疫系統與腫瘤交互作用何者錯誤。CTLA-4 是 T 細胞上的免疫檢查點分子，會抑制 T 細胞活化；PD-1 也在 T 細胞上，與腫瘤或抗原呈現細胞上的 PD-L1 結合後會降低 T 細胞反應。因此錯誤敘述是把 CTLA-4 說成腫瘤細胞表面因突變而表現的分子。\n\n"
            "【選項詳解】\n"
            "- A. 腫瘤若表現腫瘤特定抗原，可被毒殺性 T 細胞辨識並清除，敘述正確。\n"
            "- B. CTLA-4 主要表現在 T 細胞上，不是腫瘤細胞累積突變後用來抑制 T 細胞反應的典型表面分子，因此本選項錯誤。\n"
            "- C. 自然殺手細胞也參與腫瘤監視與清除，尤其可攻擊 MHC I 表現下降的異常細胞，敘述正確。\n"
            "- D. 抗 CTLA-4 或抗 PD-1 抗體屬於免疫檢查點抑制劑，可解除抑制訊號並增強抗腫瘤 T 細胞反應，敘述正確。\n\n"
            "【核心考點】\n"
            "免疫檢查點抑制劑是解除 T 細胞煞車；CTLA-4 與 PD-1 的核心位置在 T 細胞，而不是腫瘤細胞表面 CTLA-4。"
        ),
        "flashcard_front": "癌症免疫療法 / CTLA-4 / PD-1 / T 細胞抑制",
        "flashcard_back": "CTLA-4 與 PD-1 是 T 細胞免疫檢查點；抗 CTLA-4 或抗 PD-1 抗體可解除 T 細胞抑制。腫瘤細胞表現 CTLA-4 來抑制 T 細胞不是正確敘述。",
        "flashcard_summary": "CTLA-4 / PD-1 / checkpoint inhibitor -> 解除 T 細胞抑制，錯在把 CTLA-4 當成腫瘤細胞表面分子",
    },
    "110-1_medicine-6_064": {
        "key_point": "門閾學說是刺激大直徑 A 型纖維，以抑制 C 型痛覺纖維傳遞。",
        "explanation": (
            "【題幹解析】\n"
            "Melzack 與 Wall 的門閾學說指出，刺激較大直徑、傳導較快的 A 型觸覺纖維，可在脊髓背角層級抑制較小直徑、傳導較慢的 C 型痛覺纖維訊號，減少疼痛傳入。因此 X 為 A 型神經纖維，Y 為 C 型神經纖維。\n\n"
            "【選項詳解】\n"
            "- A. B 型纖維主要與自主神經節前纖維相關，不是門閾學說中主要被抑制的痛覺 C 纖維，錯誤。\n"
            "- B. A 型纖維刺激可抑制 C 型痛覺纖維傳遞，符合門閾學說，正確。\n"
            "- C. 顛倒了刺激與被抑制纖維，也把 B 型纖維放入不適當位置，錯誤。\n"
            "- D. C 型纖維是慢痛傳入纖維，不是用來抑制 A 型纖維的刺激來源，錯誤。\n\n"
            "【核心考點】\n"
            "門閾學說可記成刺激快而大的 A 型纖維，關上慢而小的 C 型痛覺傳入。"
        ),
        "flashcard_front": "門閾學說 / gate control / A 型纖維 / C 型痛覺纖維",
        "flashcard_back": "刺激大直徑 A 型觸覺纖維可在脊髓背角抑制 C 型痛覺纖維傳遞，所以 X=A 型、Y=C 型。",
        "flashcard_summary": "Gate control theory -> 刺激 A 型纖維，抑制 C 型痛覺纖維",
    },
}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def clean(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def clean_preserve_newlines(value: Any) -> str:
    text = str(value or "").replace("\r\n", "\n").replace("\r", "\n").strip()
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n", "\n\n", text)
    return text


def has_nested_headings(text: str) -> bool:
    return any(text.count(heading) > 1 for heading in ("【題幹解析】", "【選項詳解】", "【核心考點】"))


def needs_from_report(report: dict[str, Any]) -> dict[str, dict[str, Any]]:
    needed: dict[str, dict[str, Any]] = {}
    for dataset_report in report.get("reports", []):
        for issue in dataset_report.get("issues", []):
            if issue.get("code") != "nested_repeated_explanation":
                continue
            needed[str(issue["question_id"])] = {
                "dataset_id": dataset_report.get("dataset_id"),
                "dataset_path": dataset_report.get("path"),
                "question_number": issue.get("question_number"),
            }
    return needed


def index_outputs(output_dir: Path, needed_ids: set[str]) -> dict[str, dict[str, Any]]:
    indexed: dict[str, dict[str, Any]] = {}
    for path in sorted(output_dir.glob("**/*.json")):
        try:
            output = read_json(path)
        except Exception:
            continue
        for item in output.get("items", []):
            question_id = str(item.get("question_id") or "")
            if question_id in needed_ids and question_id not in indexed:
                indexed[question_id] = item
    return indexed


def normalize_output_item(item: dict[str, Any]) -> dict[str, str]:
    normalized = {
        "key_point": clean(item.get("key_point")),
        "explanation": clean_preserve_newlines(item.get("explanation")),
        "flashcard_front": clean(item.get("flashcard_front")),
        "flashcard_back": clean(item.get("flashcard_back")),
        "flashcard_summary": clean(item.get("flashcard_summary")),
    }
    if not normalized["flashcard_front"] or not normalized["flashcard_back"]:
        front, separator, back = normalized["flashcard_summary"].partition("->")
        normalized["flashcard_front"] = normalized["flashcard_front"] or clean(front)
        normalized["flashcard_back"] = normalized["flashcard_back"] or clean(back if separator else normalized["flashcard_summary"])
    return normalized


def apply_repair(
    question: dict[str, Any],
    fields: dict[str, str],
    model_label: str,
    now: str,
) -> None:
    for field in EXPLANATION_FIELDS:
        question[field] = fields[field]
    question["review_status"] = "ai_generated"
    question["explanation_model"] = model_label
    question["explanation_generated_at"] = now


def main() -> None:
    parser = argparse.ArgumentParser(description="Repair nested repeated explanations using clean Gemini outputs.")
    parser.add_argument("--report", default="reports/explanation-quality.json")
    parser.add_argument("--data-dir", default="public/data/exams")
    parser.add_argument("--outputs-dir", default="reports/gemini_outputs")
    parser.add_argument("--out-report", default="reports/nested-explanation-repair.json")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    report = read_json(Path(args.report))
    needed = needs_from_report(report)
    output_index = index_outputs(Path(args.outputs_dir), set(needed))
    now = datetime.now(timezone.utc).isoformat()

    repaired_from_output = 0
    repaired_from_fallback = 0
    missing: list[str] = []
    datasets: dict[Path, dict[str, Any]] = {}
    per_dataset: dict[str, int] = {}

    by_dataset: dict[str, list[str]] = {}
    for question_id, info in needed.items():
        by_dataset.setdefault(str(info["dataset_path"]), []).append(question_id)

    for dataset_path_text, question_ids in by_dataset.items():
        dataset_path = Path(dataset_path_text)
        dataset = read_json(dataset_path)
        questions = {str(question.get("id")): question for question in dataset.get("questions", [])}
        changed = 0

        for question_id in question_ids:
            question = questions.get(question_id)
            if not question:
                missing.append(question_id)
                continue

            item = output_index.get(question_id)
            if item:
                fields = normalize_output_item(item)
                model_label = "gemini-pro-manual-restored"
                repaired_from_output += 1
            else:
                fields = CURATED_FALLBACKS.get(question_id)
                model_label = "manual-curated-repair"
                if fields:
                    repaired_from_fallback += 1
                else:
                    missing.append(question_id)
                    continue

            if any(not fields.get(field) for field in EXPLANATION_FIELDS):
                missing.append(question_id)
                continue
            if has_nested_headings(fields["explanation"]):
                missing.append(question_id)
                continue

            apply_repair(question, fields, model_label, now)
            changed += 1

        if changed:
            dataset["updated_at"] = now
            datasets[dataset_path] = dataset
            per_dataset[str(dataset_path)] = changed

    if not args.dry_run:
        for path, dataset in datasets.items():
            write_json(path, dataset)

    repair_report = {
        "dry_run": args.dry_run,
        "needed": len(needed),
        "repaired": repaired_from_output + repaired_from_fallback,
        "repaired_from_output": repaired_from_output,
        "repaired_from_fallback": repaired_from_fallback,
        "missing": missing,
        "datasets": per_dataset,
    }
    out_path = Path(args.out_report)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    write_json(out_path, repair_report)
    print(json.dumps(repair_report, ensure_ascii=False, indent=2))

    if missing:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
