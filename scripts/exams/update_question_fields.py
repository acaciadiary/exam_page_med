import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Update question explanation fields in exam JSON.")
    parser.add_argument("--exam-file", required=True, help="Path to the exam JSON file")
    parser.add_argument("--updates-file", required=True, help="Path to the JSON file containing updates")
    args = parser.parse_args()

    exam_path = Path(args.exam_file)
    updates_path = Path(args.updates_file)

    if not exam_path.exists():
        print(f"Error: Exam file {exam_path} does not exist.")
        return

    if not updates_path.exists():
        print(f"Error: Updates file {updates_path} does not exist.")
        return

    try:
        exam_data = json.loads(exam_path.read_text(encoding="utf-8-sig"))
    except Exception as e:
        print(f"Error reading exam file: {e}")
        return

    try:
        updates_data = json.loads(updates_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Error reading updates file: {e}")
        return

    # Create a mapping of question ID to update dict
    # Supports both list of dicts with 'id' / 'question_id' or a dict mapping id -> update
    updates_map = {}
    if isinstance(updates_data, list):
        for item in updates_data:
            qid = item.get("question_id") or item.get("id")
            if qid:
                updates_map[str(qid)] = item
    elif isinstance(updates_data, dict):
        updates_map = {str(k): v for k, v in updates_data.items()}
    else:
        print("Error: Updates data must be a list of objects or a dictionary.")
        return

    questions = exam_data.get("questions", [])
    updated_count = 0
    now = datetime.now(timezone.utc).isoformat()

    for question in questions:
        qid = str(question.get("id"))
        if qid in updates_map:
            upd = updates_map[qid]
            
            # Update fields if present in update dict
            for field in ["key_point", "explanation", "flashcard_front", "flashcard_back", "flashcard_summary", "category", "category_confidence"]:
                if field in upd:
                    question[field] = upd[field]
            
            # Set metadata
            question["review_status"] = "ai_generated"
            question["explanation_model"] = "antigravity-direct"
            question["explanation_generated_at"] = now
            question["category_source"] = "auto"
            updated_count += 1

    if updated_count > 0:
        exam_data["updated_at"] = now
        exam_path.write_text(json.dumps(exam_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Successfully updated {updated_count} questions in {exam_path}")
    else:
        print("No matching questions found to update.")

if __name__ == "__main__":
    main()
