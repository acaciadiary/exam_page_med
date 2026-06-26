# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import io
import json
import os
import sys


EXPECTED_OPTIONS = set(["A", "B", "C", "D"])
LEGAL_CATEGORIES = set(["微生物免疫學", "寄生蟲學", "藥理學", "病理學", "公共衛生學", "其他"])


def load_json(path):
    with io.open(path, "r", encoding="utf-8-sig") as fh:
        return json.load(fh)


def validate_file(path):
    issues = []
    data = load_json(path)
    questions = data.get("questions", [])
    ids = set()
    nums = set()
    for index, q in enumerate(questions, 1):
        qid = q.get("id")
        num = q.get("question_number")
        options = q.get("options", {})
        if not qid:
            issues.append([path, index, "missing_id"])
        elif qid in ids:
            issues.append([path, index, "duplicate_id"])
        ids.add(qid)
        if not isinstance(num, int):
            issues.append([path, index, "invalid_number"])
        elif num in nums:
            issues.append([path, index, "duplicate_number"])
        nums.add(num)
        if not str(q.get("question_text", "")).strip():
            issues.append([path, index, "empty_question"])
        if set(options.keys()) != EXPECTED_OPTIONS:
            issues.append([path, index, "invalid_options"])
        for key in EXPECTED_OPTIONS:
            if not str(options.get(key, "")).strip():
                issues.append([path, index, "empty_option_" + key])
        answer = q.get("correct_answer")
        if not answer:
            issues.append([path, index, "missing_answer"])
        elif str(answer) not in EXPECTED_OPTIONS and "#" not in str(answer):
            issues.append([path, index, "invalid_answer"])
    expected = set(range(1, len(questions) + 1))
    if nums != expected:
        issues.append([path, None, "missing_or_non_contiguous_numbers"])
    return issues


def iter_exam_jsons(root):
    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            if name.endswith(".json"):
                yield os.path.join(dirpath, name)


def validate_explanations(path):
    issues = []
    data = load_json(path)
    required = ["【題幹解析】", "【選項詳解】", "【核心考點】", "- A.", "- B.", "- C.", "- D."]
    for q in data.get("questions", []):
        exp = q.get("explanation", "")
        for token in required:
            if token not in exp:
                issues.append([q.get("id"), "missing_" + token])
        if q.get("category") not in LEGAL_CATEGORIES:
            issues.append([q.get("id"), "bad_category_" + str(q.get("category"))])
    return issues


def main():
    root = os.path.join("public", "data", "exams")
    all_issues = []
    count = 0
    for path in iter_exam_jsons(root):
        count += 1
        all_issues.extend(validate_file(path))
    target = os.path.join("public", "data", "exams", "111-2", "medicine-2.json")
    explanation_issues = validate_explanations(target)
    report = {
        "files_checked": count,
        "dataset_issue_count": len(all_issues),
        "dataset_issues": all_issues[:50],
        "target_explanation_issue_count": len(explanation_issues),
        "target_explanation_issues": explanation_issues[:50],
    }
    with io.open(os.path.join("reports", "dataset-quality-compat-111-2-medicine-2.json"), "w", encoding="utf-8") as fh:
        json.dump(report, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if all_issues or explanation_issues:
        sys.exit(1)


if __name__ == "__main__":
    main()
