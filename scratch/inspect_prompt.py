import os
import json

batches = [
    "109-2_medicine-5_batch-005",
    "109-2_medicine-5_batch-006",
    "109-2_medicine-6_batch-001",
    "109-2_medicine-6_batch-002",
    "109-2_medicine-6_batch-003",
    "109-2_medicine-6_batch-004",
    "109-2_medicine-6_batch-005",
    "109-2_medicine-6_batch-006"
]

def extract_json(prompt_path):
    with open(prompt_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find JSON content
    start_idx = content.find('{')
    if start_idx == -1:
        return None
        
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
                
    if end_idx == -1:
        return None
        
    json_str = content[start_idx:end_idx]
    try:
        return json.loads(json_str)
    except Exception as e:
        print(f"Error parsing JSON from {prompt_path}: {e}")
        return None

out_path = "scratch/parsed_questions.txt"
with open(out_path, 'w', encoding='utf-8') as out_f:
    for batch_id in batches:
        p_path = f"reports/gemini_prompts/{batch_id}.md"
        data = extract_json(p_path)
        if data:
            out_f.write(f"=== {batch_id} ===\n")
            out_f.write(f"Category Group: {data.get('category_group')}\n")
            out_f.write(f"Allowed Categories: {data.get('allowed_categories')}\n")
            for q in data.get('questions', []):
                out_f.write(f"Q{q.get('question_number')} ({q.get('question_id')}): Correct: {q.get('correct_answer')}\n")
                out_f.write(f"  Text: {q.get('question_text').strip()}\n")
                for opt_key, opt_val in q.get('options', {}).items():
                    out_f.write(f"    {opt_key}: {opt_val}\n")
            out_f.write("\n")
        else:
            out_f.write(f"Failed to extract JSON from {batch_id}\n\n")

print("Successfully written to scratch/parsed_questions.txt")
