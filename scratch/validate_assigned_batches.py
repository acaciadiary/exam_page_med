import sys
import os

sys.path.append(os.getcwd())
from validate_all import validate_file

assigned_batches = [
    "109-2_medicine-1_batch-007",
    "109-2_medicine-2_batch-001",
    "109-2_medicine-2_batch-002",
    "109-2_medicine-2_batch-003",
    "109-2_medicine-2_batch-004",
    "109-2_medicine-2_batch-005",
    "109-2_medicine-2_batch-006",
    "109-2_medicine-2_batch-007"
]

all_ok = True
for b in assigned_batches:
    p_path = f"reports/gemini_prompts/{b}.md"
    o_path = f"reports/gemini_outputs/{b}.json"
    
    if os.path.exists(o_path):
        res = validate_file(p_path, o_path)
        print(f"{b}: {res}")
        if res != "OK":
            all_ok = False
    else:
        print(f"{b}: Output file does not exist!")
        all_ok = False
        
if not all_ok:
    print("\n--- Validation FAILED! ---")
    sys.exit(1)
else:
    print("\nAll 8 assigned batches validated successfully!")
    sys.exit(0)
