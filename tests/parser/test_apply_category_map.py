import pytest

from scripts.exams.apply_category_map import (
    CategoryRange,
    apply_ranges,
    validate_ranges,
)


def dataset_fixture():
    return {
        "id": "115_medicine-3",
        "questions": [
            {"id": "q1", "question_number": 1},
            {"id": "q2", "question_number": 2},
            {"id": "q3", "question_number": 3, "category": "舊分類"},
        ],
    }


def test_apply_ranges_assigns_category_fields():
    dataset = dataset_fixture()
    stats = apply_ranges(
        dataset,
        [CategoryRange(start=1, end=2, category="心臟內科", category_group="內科學")],
        clear_unmatched=True,
    )

    assert stats == {"assigned": 2, "cleared": 1, "unassigned": 1}
    assert dataset["questions"][0]["category"] == "心臟內科"
    assert dataset["questions"][0]["category_group"] == "內科學"
    assert dataset["questions"][0]["category_source"] == "manual_range"
    assert dataset["questions"][2]["category_source"] == "unassigned"
    assert "category" not in dataset["questions"][2]


def test_validate_ranges_rejects_overlaps():
    with pytest.raises(ValueError, match="both"):
        validate_ranges(
            "115_medicine-3",
            [
                CategoryRange(start=1, end=3, category="心臟內科"),
                CategoryRange(start=3, end=5, category="胸腔內科"),
            ],
        )
