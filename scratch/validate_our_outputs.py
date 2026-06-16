# -*- coding: utf-8 -*-
import sys
import os

# Add root directory to python path if needed
sys.path.insert(0, os.path.abspath('.'))

from validate_all import validate_file

our_batches = [
    "109-1_medicine-6_batch-005",
    "109-1_medicine-6_batch-006",
    "109-2_medicine-1_batch-001",
    "109-2_medicine-1_batch-002",
    "109-2_medicine-1_batch-003",
    "109-2_medicine-1_batch-004",
    "109-2_medicine-1_batch-005",
    "109-2_medicine-1_batch-006"
]

all_ok = True
for b in our_batches:
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
    print("\nSome batches failed validation!")
    sys.exit(1)
else:
    print("\nAll 8 batches validated successfully!")
    sys.exit(0)
