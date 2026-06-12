import json
import os

files_to_check = [
    ('reports/gemini_prompts/109-1_medicine-4_batch-002.md', '109-1_medicine-4_028'),
    ('reports/gemini_prompts/109-1_medicine-4_batch-005.md', '109-1_medicine-4_069'),
    ('reports/gemini_prompts/109-1_medicine-5_batch-001.md', '109-1_medicine-5_013')
]

out = []
for filepath, qid in files_to_check:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse the JSON from markdown
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
            for q in data['questions']:
                if q['question_id'] == qid:
                    out.append(f"File: {os.path.basename(filepath)}")
                    out.append(f"ID: {q['question_id']}")
                    out.append(f"Text: {q['question_text']}")
                    out.append("Options:")
                    for k, v in q['options'].items():
                        out.append(f"  {k}: {v}")
                    out.append(f"Correct Answer: '{q['correct_answer']}'")
                    out.append(f"Answer Note: {q['answer_note']}")
                    out.append("-" * 50)
        except Exception as e:
            out.append(f"Error parsing {filepath}: {e}")

with open('empty_answers_debug.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
print("Done writing to empty_answers_debug.txt")
