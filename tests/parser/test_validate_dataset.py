import json
from pathlib import Path

from scripts.exams.validate_dataset import validate_dataset


def test_validate_dataset_reports_clean_fixture(tmp_path: Path):
    dataset = {
        "id": "sample",
        "title": "Sample",
        "questions": [
            {
                "id": "sample_001",
                "question_number": 1,
                "question_text": "題幹",
                "options": {"A": "甲", "B": "乙", "C": "丙", "D": "丁"},
                "correct_answer": "A",
            }
        ],
    }
    path = tmp_path / "dataset.json"
    path.write_text(json.dumps(dataset, ensure_ascii=False), encoding="utf-8")

    report = validate_dataset(path)

    assert report["question_count"] == 1
    assert report["issue_count"] == 0


def test_validate_dataset_flags_missing_answer(tmp_path: Path):
    dataset = {
        "id": "sample",
        "questions": [
            {
                "id": "sample_001",
                "question_number": 1,
                "question_text": "題幹",
                "options": {"A": "甲", "B": "乙", "C": "丙", "D": "丁"},
                "correct_answer": None,
            }
        ],
    }
    path = tmp_path / "dataset.json"
    path.write_text(json.dumps(dataset, ensure_ascii=False), encoding="utf-8")

    report = validate_dataset(path)

    assert report["issue_count"] == 1
    assert report["issues"][0]["code"] == "missing_answer"
