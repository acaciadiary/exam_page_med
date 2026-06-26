import json
import sys

# Reconfigure stdout to use utf-8 encoding
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


def print_questions(start, end):
    with open('public/data/exams/114-2/medicine-3.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    questions = data['questions'][start:end]
    for q in questions:
        print(f"ID: {q['id']}")
        print(f"Number: {q['question_number']}")
        print(f"Text: {q['question_text']}")
        print("Options:")
        for k, v in q['options'].items():
            print(f"  {k}: {v}")
        print(f"Correct Answer: {q.get('correct_answer')} or {q.get('correct_answers')}")
        print("="*60)

if __name__ == '__main__':
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    print_questions(start, end)
