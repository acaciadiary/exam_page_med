import json
import os

batches = [
    "109-1_medicine-5_batch-003",
    "109-1_medicine-5_batch-004",
    "109-1_medicine-5_batch-005",
    "109-1_medicine-5_batch-006",
    "109-1_medicine-6_batch-001",
    "109-1_medicine-6_batch-002",
    "109-1_medicine-6_batch-003",
    "109-1_medicine-6_batch-004"
]

with open("scratch/all_questions.md", "w", encoding="utf-8") as out_f:
    for batch in batches:
        in_path = f"scratch/{batch}_input.json"
        if not os.path.exists(in_path):
            continue
        with open(in_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        out_f.write(f"# Batch: {batch}\n")
        out_f.write(f"Category Group: {data.get('category_group')}\n")
        out_f.write(f"Allowed Categories: {', '.join(data.get('allowed_categories', []))}\n\n")
        
        for q in data.get("questions", []):
            out_f.write(f"## Q{q.get('question_number')}: {q.get('question_id')}\n")
            out_f.write(f"Question: {q.get('question_text')}\n\n")
            for opt, val in q.get("options", {}).items():
                out_f.write(f"- {opt}: {val}\n")
            out_f.write(f"\nCorrect Answer: **{q.get('correct_answer')}**\n\n")
            out_f.write("---\n\n")
        print(f"Dumped {batch}")
