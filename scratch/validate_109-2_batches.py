import os
import sys

# Add parent directory to sys.path so we can import validate_all
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from validate_all import validate_file

batches = [
    "109-2_medicine-5_batch-003",
    "109-2_medicine-5_batch-004",
    "109-2_medicine-5_batch-005",
    "109-2_medicine-5_batch-006",
    "109-2_medicine-6_batch-001",
    "109-2_medicine-6_batch-002"
]

all_ok = True
for b in batches:
    p_path = f"reports/gemini_prompts/{b}.md"
    o_path = f"reports/gemini_outputs/{b}.json"
    
    if os.path.exists(o_path):
        res = validate_file(p_path, o_path)
        print(f"{b}: {res}")
        if res != "OK":
            all_ok = False
    else:
        print(f"{b}: Output file not created yet")
        all_ok = False
        
if not all_ok:
    sys.exit(1)
else:
    print("All completed files are verified successfully!")
    sys.exit(0)
