import sys
import os

sys.path.append(os.getcwd())
from validate_all import validate_file

target_batches = [
    "109-2_medicine-6_batch-003",
    "109-2_medicine-6_batch-004",
    "109-2_medicine-6_batch-005",
    "109-2_medicine-6_batch-006",
    "110-1_medicine-1_batch-001",
    "110-1_medicine-1_batch-002"
]

all_ok = True
for b in target_batches:
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
    print("\nAll target batches validated successfully!")
    sys.exit(0)
