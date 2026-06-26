# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import argparse
import io
import json
from datetime import datetime


FIELDS = [
    "key_point",
    "explanation",
    "flashcard_front",
    "flashcard_back",
    "flashcard_summary",
    "category",
    "category_confidence",
]


def load_json(path, encoding):
    with io.open(path, "r", encoding=encoding) as fh:
        return json.load(fh)


def write_json(path, data):
    with io.open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--exam-file", required=True)
    parser.add_argument("--updates-file", required=True)
    args = parser.parse_args()

    exam_data = load_json(args.exam_file, "utf-8-sig")
    updates_data = load_json(args.updates_file, "utf-8")

    if isinstance(updates_data, list):
        updates_map = {}
        for item in updates_data:
            qid = item.get("question_id") or item.get("id")
            if qid:
                updates_map[str(qid)] = item
    else:
        updates_map = dict((str(k), v) for k, v in updates_data.items())

    now = datetime.utcnow().isoformat() + "+00:00"
    count = 0
    for question in exam_data.get("questions", []):
        qid = str(question.get("id"))
        if qid not in updates_map:
            continue
        update = updates_map[qid]
        for field in FIELDS:
            if field in update:
                question[field] = update[field]
        question["review_status"] = "ai_generated"
        question["explanation_model"] = "antigravity-direct"
        question["explanation_generated_at"] = now
        question["category_source"] = "auto"
        count += 1

    if count:
        exam_data["updated_at"] = now
        write_json(args.exam_file, exam_data)
    print("Successfully updated {} questions in {}".format(count, args.exam_file))


if __name__ == "__main__":
    main()
