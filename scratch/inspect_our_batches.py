import json
import os

batches = [
    "110-1_medicine-4_batch-002",
    "110-1_medicine-4_batch-003",
    "110-1_medicine-4_batch-004",
    "110-1_medicine-4_batch-005",
    "110-1_medicine-4_batch-006",
    "110-1_medicine-5_batch-001"
]

out_lines = []

for b in batches:
    path = f'reports/gemini_prompts/{b}.md'
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find JSON block by looking for "請處理以下 JSON 輸入："
        input_mark = "請處理以下 JSON 輸入："
        input_pos = content.find(input_mark)
        if input_pos != -1:
            start_idx = content.find('{', input_pos)
        else:
            start_idx = content.find('{\n  "dataset_id"')
            if start_idx == -1:
                start_idx = content.find('{"dataset_id"')
            if start_idx == -1:
                start_idx = content.find('{')
        
        # Find the matching closing bracket
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
            out_lines.append(f"=== {b} ===")
            out_lines.append(f"dataset_id: {data.get('dataset_id')}")
            out_lines.append(f"batch_id: {data.get('batch_id')}")
            out_lines.append(f"category_group: {data.get('category_group')}")
            out_lines.append(f"allowed_categories: {data.get('allowed_categories')}")
            out_lines.append(f"questions_count: {len(data['questions'])}")
            for q in data['questions']:
                out_lines.append(f"  Question {q['question_number']} ({q['question_id']}):")
                out_lines.append(f"    Text: {q['question_text'].strip()}")
                out_lines.append(f"    Options: {q['options']}")
                out_lines.append(f"    Correct Answer: {q['correct_answer']}")
                out_lines.append(f"    Answer Note: {q.get('answer_note', '')}")
            out_lines.append("")
        except Exception as e:
            out_lines.append(f"Error parsing {b}: {e}")
            out_lines.append(f"Extracted string preview: {json_str[:200]}")
    else:
        out_lines.append(f"{path} not found")

with open('scratch/our_batches_inspection.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out_lines))
print("Done writing to scratch/our_batches_inspection.txt")
