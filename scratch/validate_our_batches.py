# -*- coding: utf-8 -*-
import sys
import os

sys.path.insert(0, os.path.abspath('.'))
from validate_all import validate_file

our_batches = [
    "110-1_medicine-4_batch-002",
    "110-1_medicine-4_batch-003",
    "110-1_medicine-4_batch-004",
    "110-1_medicine-4_batch-005",
    "110-1_medicine-4_batch-006",
    "110-1_medicine-5_batch-001"
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
    print("\nSome of our batches failed validation!")
    sys.exit(1)
else:
    print("\nAll 6 of our batches validated successfully!")
    sys.exit(0)
