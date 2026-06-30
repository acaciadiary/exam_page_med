import json
from pathlib import Path

from scripts.exams.export_gemini_prompts import export_prompts
from scripts.exams.import_gemini_explanations import import_outputs
from scripts.exams.validate_explanations import validate_dataset


def write_dataset(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(
            {
                "id": "115_sample",
                "year": "115",
                "title": "sample",
                "subject": "sample",
                "source": "fixture",
                "updated_at": "2026-06-09T00:00:00+00:00",
                "questions": [
                    {
                        "id": "115_sample_001",
                        "question_number": 1,
                        "question_text": "下列何者最適當？",
                        "options": {
                            "A": "選項一",
                            "B": "選項二",
                            "C": "選項三",
                            "D": "選項四",
                        },
                        "correct_answer": "B",
                        "explanation": "",
                        "key_point": "",
                        "flashcard_front": "",
                        "flashcard_back": "",
                        "flashcard_summary": "",
                        "review_status": "empty",
                    }
                ],
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )


def test_export_gemini_prompt_batches(tmp_path: Path):
    dataset_path = tmp_path / "data" / "115" / "sample.json"
    prompt_dir = tmp_path / "prompts"
    write_dataset(dataset_path)

    report = export_prompts([dataset_path], prompt_dir, batch_size=15, force=False)
    prompt = (prompt_dir / "115_sample_batch-001.md").read_text(encoding="utf-8")

    assert report["batch_count"] == 1
    assert report["question_count"] == 1
    assert "只回傳純 JSON" in prompt
    assert "allowed_categories" in prompt
    assert "category_confidence" in prompt
    assert "flashcard_front" in prompt
    assert "flashcard_back" in prompt
    assert "dataset_year" in prompt
    assert "其他" in prompt
    assert "115_sample_001" in prompt


def test_import_gemini_output_and_validate(tmp_path: Path):
    data_dir = tmp_path / "data"
    dataset_path = data_dir / "115" / "sample.json"
    output_path = tmp_path / "outputs" / "115_sample_batch-001.json"
    write_dataset(dataset_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(
            {
                "dataset_id": "115_sample",
                "batch_id": "115_sample_batch-001",
                "items": [
                    {
                        "question_id": "115_sample_001",
                        "question_number": 1,
                        "correct_answer": "B",
                        "category_group": "sample",
                        "category": "其他",
                        "category_confidence": "low",
                        "key_point": "本題核心考點。",
                        "explanation": "這是詳解內容，說明為何答案 B 正確。",
                        "flashcard_front": "關鍵線索",
                        "flashcard_back": "看到線索時要選 B 的判斷規則。",
                        "flashcard_summary": "關鍵字 -> B",
                    }
                ],
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    report = import_outputs(
        [output_path],
        data_dir=data_dir,
        dry_run=False,
        model_label="gemini-pro-manual",
    )
    updated = json.loads(dataset_path.read_text(encoding="utf-8"))
    question = updated["questions"][0]
    validation = validate_dataset(dataset_path)

    assert report["imported"] == 1
    assert question["category"] == "其他"
    assert question["category_group"] == "sample"
    assert question["category_confidence"] == "low"
    assert question["category_source"] == "auto"
    assert question["review_status"] == "ai_generated"
    assert question["flashcard_front"] == "關鍵線索"
    assert question["flashcard_back"] == "看到線索時要選 B 的判斷規則。"
    assert question["explanation_model"] == "gemini-pro-manual"
    assert validation["complete"] == 1
    assert validation["missing"] == 0


def test_validate_flags_nested_repeated_explanation(tmp_path: Path):
    dataset_path = tmp_path / "data" / "115" / "sample.json"
    write_dataset(dataset_path)
    data = json.loads(dataset_path.read_text(encoding="utf-8"))
    question = data["questions"][0]
    question["key_point"] = "考點"
    question["explanation"] = (
        "【題幹解析】第一次解析。\n\n"
        "【選項詳解】第一次選項。\n\n"
        "【核心考點】第一次考點。\n\n"
        "【題幹解析】第二次解析。\n\n"
        "【選項詳解】第二次選項。\n\n"
        "【核心考點】第二次考點。"
    )
    question["flashcard_front"] = "正面"
    question["flashcard_back"] = "背面"
    question["flashcard_summary"] = "摘要 -> 考點"
    question["review_status"] = "ai_generated"
    dataset_path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    validation = validate_dataset(dataset_path)

    assert validation["issue_count"] == 1
    assert validation["issues"][0]["code"] == "nested_repeated_explanation"


def test_import_rejects_changed_correct_answer(tmp_path: Path):
    data_dir = tmp_path / "data"
    dataset_path = data_dir / "115" / "sample.json"
    output_path = tmp_path / "outputs" / "bad.json"
    write_dataset(dataset_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(
            {
                "dataset_id": "115_sample",
                "batch_id": "bad",
                "items": [
                    {
                        "question_id": "115_sample_001",
                        "question_number": 1,
                        "correct_answer": "A",
                        "category_group": "sample",
                        "category": "其他",
                        "category_confidence": "low",
                        "key_point": "考點",
                        "explanation": "詳解",
                        "flashcard_summary": "關鍵字 -> A",
                    }
                ],
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    try:
        import_outputs([output_path], data_dir=data_dir, dry_run=False, model_label="gemini")
    except ValueError as error:
        assert "Correct answer mismatch" in str(error)
    else:
        raise AssertionError("Expected answer mismatch to fail")


def test_import_rejects_unlisted_category(tmp_path: Path):
    data_dir = tmp_path / "data"
    dataset_path = data_dir / "115" / "sample.json"
    output_path = tmp_path / "outputs" / "bad-category.json"
    write_dataset(dataset_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(
            {
                "dataset_id": "115_sample",
                "batch_id": "bad-category",
                "items": [
                    {
                        "question_id": "115_sample_001",
                        "question_number": 1,
                        "correct_answer": "B",
                        "category_group": "sample",
                        "category": "Gemini 自創科目",
                        "category_confidence": "high",
                        "key_point": "考點",
                        "explanation": "詳解",
                        "flashcard_summary": "關鍵字 -> B",
                    }
                ],
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    try:
        import_outputs([output_path], data_dir=data_dir, dry_run=False, model_label="gemini")
    except ValueError as error:
        assert "Invalid category" in str(error)
    else:
        raise AssertionError("Expected unlisted category to fail")
