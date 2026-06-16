import json
import os

batches = [
    "110-1_medicine-6_batch-002",
    "110-1_medicine-6_batch-003",
    "110-1_medicine-6_batch-004",
    "110-1_medicine-6_batch-005",
    "110-1_medicine-6_batch-006",
    "110-2_medicine-1_batch-001"
]

prompt_dir = "reports/gemini_prompts"
out_file = "scratch/extracted_questions_all.txt"

os.makedirs("scratch", exist_ok=True)

with open(out_file, "w", encoding="utf-8") as out:
    for b in batches:
        p_path = os.path.join(prompt_dir, f"{b}.md")
        if not os.path.exists(p_path):
            out.write(f"Batch {b} NOT FOUND\n\n")
            continue
        
        with open(p_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Extract JSON from prompt
        input_mark = "請處理以下 JSON 輸入："
        input_pos = content.find(input_mark)
        if input_pos != -1:
            start_idx = content.find('{', input_pos)
        else:
            start_idx = content.find('{')
            
        brace_count = 0
        end_idx = -1
        for i in range(start_idx, len(content)):
            if content[i] == '{':
                brace_count += 1
            elif content[i] == '}':
                brace_count -= 1
                if brace_count == 0:
                    end_idx = i + 1
                    break
        
        json_str = content[start_idx:end_idx]
        try:
            data = json.loads(json_str)
            out.write(f"=== BATCH: {b} ===\n")
            out.write(f"Category Group: {data.get('category_group')}\n")
            out.write(f"Allowed Categories: {data.get('allowed_categories')}\n")
            out.write(f"Questions:\n")
            for q in data.get("questions", []):
                out.write(f"Q{q.get('question_number')} ({q.get('question_id')}): {q.get('question_text')}\n")
                for opt, val in q.get("options", {}).items():
                    out.write(f"  {opt}: {val}\n")
                out.write(f"Correct Answer: {q.get('correct_answer')}\n\n")
            out.write("\n" + "="*50 + "\n\n")
        except Exception as e:
            out.write(f"Error parsing {b}: {e}\n\n")

print("Done! Extracted questions written to", out_file)
