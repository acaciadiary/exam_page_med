import json
import sys

def print_batch(start_idx, end_idx):
    with open('public/data/exams/113-1/medicine-3.json', encoding='utf-8') as f:
        data = json.load(f)
    
    questions = data['questions'][start_idx:end_idx]
    
    output_lines = []
    for q in questions:
        output_lines.append(f"=== ID: {q['id']} | Num: {q['question_number']} | Correct: {q['correct_answer']} ===")
        output_lines.append(q['question_text'])
        output_lines.append("Options:")
        for opt, val in q['options'].items():
            output_lines.append(f"  {opt}: {val}")
        output_lines.append(f"Current Category: {q.get('category')}")
        output_lines.append("-" * 50)
        output_lines.append("")
        
    with open('scratch/batch_output.txt', 'w', encoding='utf-8') as out_f:
        out_f.write('\n'.join(output_lines))

if __name__ == '__main__':
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    print_batch(start, end)
