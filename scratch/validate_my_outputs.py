import os
import sys

# Append root directory to sys.path so we can import validate_all
sys.path.append(os.getcwd())
from validate_all import validate_file

batches = [
    "111-2_medicine-5_batch-001",
    "111-2_medicine-5_batch-002",
    "111-2_medicine-5_batch-003",
    "111-2_medicine-5_batch-004",
    "111-2_medicine-5_batch-005"
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
    print("Validation failed!")
    sys.exit(1)
else:
    print("All generated files validated successfully!")
    sys.exit(0)
