import json
import re
from pathlib import Path

def extract_questions(batch_id):
    md_path = Path(f"reports/gemini_prompts/{batch_id}.md")
    if not md_path.exists():
        print(f"File {md_path} does not exist")
        return None
    content = md_path.read_text(encoding="utf-8")
    
    # Try finding the JSON block
    match = re.search(r"請處理以下 JSON 輸入：\s*\n(\{.*?\})\n\s*\n請完全依照以下", content, re.DOTALL)
    if not match:
        match = re.search(r"(\{.*\})", content, re.DOTALL)
    
    if match:
        try:
            return json.loads(match.group(1))
        except Exception as e:
            try:
                return json.loads(match.group(0))
            except Exception as e2:
                print(f"JSON load failed for {batch_id}: {e2}")
                return None
    else:
        print(f"No JSON block found in {batch_id}")
        return None

batches = [
    "108-2_medicine-5_batch-002",
    "108-2_medicine-5_batch-003",
    "108-2_medicine-5_batch-004",
    "108-2_medicine-5_batch-005",
    "108-2_medicine-5_batch-006",
    "108-2_medicine-6_batch-001"
]

for bid in batches:
    data = extract_questions(bid)
    if data:
        print("="*60)
        print(f"Batch: {bid}")
        print(f"Allowed categories: {data.get('allowed_categories')}")
        print("="*60)
        for q in data.get("questions", []):
            print(f"Q{q['question_number']} (ID: {q['question_id']}) -> Ans: {q['correct_answer']}")
            print(q['question_text'].strip())
            for opt, val in q.get('options', {}).items():
                print(f"  {opt}: {val.strip()}")
            print("-" * 40)
