import sys
import json
from pathlib import Path
from coordinator import get_status

def main():
    if len(sys.argv) < 3:
        print("Usage: python assign_batches.py <num_subagents> <batches_per_subagent>")
        sys.exit(1)
        
    num_subagents = int(sys.argv[1])
    batches_per_subagent = int(sys.argv[2])
    
    total, completed, pending = get_status()
    
    limit = num_subagents * batches_per_subagent
    to_assign = pending[:limit]
    
    assignments = []
    for i in range(num_subagents):
        start = i * batches_per_subagent
        end = start + batches_per_subagent
        chunk = to_assign[start:end]
        if chunk:
            assignments.append(chunk)
            
    print(json.dumps({
        "num_assigned": len(to_assign),
        "assignments": [
            [b["batch_id"] for b in chunk]
            for chunk in assignments
        ]
    }, indent=2))

if __name__ == "__main__":
    main()
