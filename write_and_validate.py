# -*- coding: utf-8 -*-
import json
import os

batches = [
    ("108-2_medicine-2_batch-003", "generate_batch_003"),
    ("108-2_medicine-2_batch-004", "generate_batch_004"),
    ("108-2_medicine-2_batch-005", "generate_batch_005"),
    ("108-2_medicine-2_batch-006", "generate_batch_006"),
    ("108-2_medicine-3_batch-004", "generate_batch_3_004"),
    ("108-2_medicine-3_batch-005", "generate_batch_3_005"),
    ("108-2_medicine-3_batch-006", "generate_batch_3_006"),
    ("108-2_medicine-4_batch-001", "generate_batch_4_001"),
]

output_dir = os.path.join("reports", "gemini_outputs")
os.makedirs(output_dir, exist_ok=True)

errors = []

for batch_id, module_name in batches:
    try:
        # Import module
        module = __import__(module_name)
        data = module.batch_data
        
        # Verify dataset_id & batch_id are not in individual items
        for item in data.get("items", []):
            if "dataset_id" in item:
                errors.append(f"{batch_id}: found 'dataset_id' inside an item.")
            if "batch_id" in item:
                errors.append(f"{batch_id}: found 'batch_id' inside an item.")
        
        # Output file path
        output_file_path = os.path.join(output_dir, f"{batch_id}.json")
        
        # Dump RAW JSON
        with open(output_file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        print(f"Successfully wrote {output_file_path}")
        
        # Perform validation checks
        # Read back to check validity
        with open(output_file_path, "r", encoding="utf-8") as f:
            loaded_data = json.load(f)
            
        # Check matching fields
        if loaded_data.get("batch_id") != batch_id:
            errors.append(f"{batch_id}: batch_id mismatch in output file.")
            
        items = loaded_data.get("items", [])
        if not items:
            errors.append(f"{batch_id}: no items found in output file.")
            
        for i, item in enumerate(items):
            required_keys = [
                "question_id", "question_number", "correct_answer", 
                "category_group", "category", "category_confidence", 
                "key_point", "explanation", "flashcard_front", 
                "flashcard_back", "flashcard_summary"
            ]
            for key in required_keys:
                if key not in item:
                    errors.append(f"{batch_id} [item {i}]: missing key '{key}'")
                    
    except Exception as e:
        errors.append(f"Failed to process {batch_id} with module {module_name}: {str(e)}")

if errors:
    print("\n--- VALIDATION ERRORS FOUND ---")
    for err in errors:
        print(err)
    exit(1)
else:
    print("\nAll batches validated and outputted successfully with NO ERRORS!")
