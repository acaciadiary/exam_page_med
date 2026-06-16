import json
import os
from pathlib import Path

OUTPUT_DIR = Path("reports/gemini_outputs")
EXAMS_DIR = Path("public/data/exams")

def verify_and_filter():
    if not OUTPUT_DIR.exists():
        print(f"Output directory {OUTPUT_DIR} does not exist.")
        return

    output_files = list(OUTPUT_DIR.glob("*.json"))
    print(f"Found {len(output_files)} files in {OUTPUT_DIR}.")

    deleted_count = 0
    kept_count = 0

    # Cache for loaded original exams to avoid reloading them repeatedly
    original_exams_cache = {}

    for output_path in output_files:
        try:
            with open(output_path, "r", encoding="utf-8") as f:
                output_data = json.load(f)
        except Exception as e:
            print(f"[ERROR] Failed to read/parse {output_path.name}: {e}")
            print(f"Deleting corrupted file {output_path.name}...")
            output_path.unlink()
            deleted_count += 1
            continue

        dataset_id = output_data.get("dataset_id")
        if not dataset_id:
            print(f"[ERROR] Missing dataset_id in {output_path.name}. Deleting...")
            output_path.unlink()
            deleted_count += 1
            continue

        # Split dataset_id to find the original exam path
        parts = dataset_id.split("_")
        if len(parts) != 2:
            print(f"[ERROR] Invalid dataset_id format '{dataset_id}' in {output_path.name}. Deleting...")
            output_path.unlink()
            deleted_count += 1
            continue

        year, subject = parts
        original_exam_path = EXAMS_DIR / year / f"{subject}.json"

        if not original_exam_path.exists():
            print(f"[ERROR] Original exam file {original_exam_path} not found for {output_path.name}. Deleting...")
            output_path.unlink()
            deleted_count += 1
            continue

        # Load or retrieve cached original exam
        if str(original_exam_path) not in original_exams_cache:
            try:
                with open(original_exam_path, "r", encoding="utf-8") as f:
                    original_exam_data = json.load(f)
                    # Map question_id to correct_answer
                    q_map = {q["id"]: q.get("correct_answer", "") for q in original_exam_data.get("questions", [])}
                    original_exams_cache[str(original_exam_path)] = q_map
            except Exception as e:
                print(f"[ERROR] Failed to read original exam {original_exam_path}: {e}")
                continue

        original_q_map = original_exams_cache[str(original_exam_path)]
        items = output_data.get("items", [])
        mismatch_found = False
        mismatch_details = []

        for item in items:
            q_id = item.get("question_id")
            out_ans = item.get("correct_answer")

            if not q_id:
                mismatch_found = True
                mismatch_details.append("Item missing question_id")
                break

            if q_id not in original_q_map:
                mismatch_found = True
                mismatch_details.append(f"Question ID {q_id} not found in original exam {year}_{subject}")
                break

            orig_ans = original_q_map[q_id]
            # Strip spaces/newlines to prevent false positives due to formatting
            out_ans_clean = str(out_ans).strip() if out_ans is not None else ""
            orig_ans_clean = str(orig_ans).strip() if orig_ans is not None else ""

            if out_ans_clean != orig_ans_clean:
                mismatch_found = True
                mismatch_details.append(
                    f"Answer mismatch for {q_id}: Output has '{out_ans_clean}', Original has '{orig_ans_clean}'"
                )

        if mismatch_found:
            print(f"[MISMATCH] {output_path.name} is mismatched! Details:")
            for detail in mismatch_details:
                print(f"  - {detail}")
            print(f"Deleting {output_path.name}...")
            output_path.unlink()
            deleted_count += 1
        else:
            # print(f"[OK] {output_path.name} is valid.")
            kept_count += 1

    print("\nVerification Summary:")
    print(f"  Total analyzed: {len(output_files)}")
    print(f"  Valid (Kept)  : {kept_count}")
    print(f"  Mismatched (Deleted): {deleted_count}")

if __name__ == "__main__":
    verify_and_filter()
