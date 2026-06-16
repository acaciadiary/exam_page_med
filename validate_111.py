# -*- coding: utf-8 -*-
from validate_all import validate_file
import sys

batches = [
    "111-1_medicine-4_batch-001",
    "111-1_medicine-4_batch-002",
    "111-1_medicine-4_batch-003",
    "111-1_medicine-4_batch-004",
    "111-1_medicine-4_batch-005"
]

all_ok = True
for b in batches:
    p_path = f"reports/gemini_prompts/{b}.md"
    o_path = f"reports/gemini_outputs/{b}.json"
    
    res = validate_file(p_path, o_path)
    print(f"{b}: {res}")
    if res != "OK":
        all_ok = False

if not all_ok:
    print("Validation failed!")
    sys.exit(1)
else:
    print("All 5 batches validated successfully against official prompt constraints!")
    sys.exit(0)
