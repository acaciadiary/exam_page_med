from pathlib import Path

from scripts.exams.parse_answers import parse_answers, parse_correction_notes


def test_parse_answers_fixture():
    raw = Path("scripts/exams/fixtures/sample_answer_text.txt").read_text(
        encoding="utf-8"
    )

    assert parse_answers(raw)[2] == "B"


def test_parse_official_answer_grid_text():
    raw = """
    測驗式試題標準答案
    題號
    答案 Ｃ Ｂ Ａ Ｃ Ａ Ｂ Ｃ Ｄ Ｂ Ｃ
    題號
    答案 Ｄ Ｂ Ｂ Ａ Ａ Ｂ Ｃ Ａ Ｂ Ａ
    01 02 03 04 05 06 07 08 09 10
    11 12 13 14 15 16 17 18 19 20
    """

    answers = parse_answers(raw)

    assert answers[1] == "C"
    assert answers[2] == "B"
    assert answers[10] == "C"
    assert answers[11] == "D"
    assert answers[20] == "A"


def test_parse_compact_corrected_answer_grid_text():
    raw = """
    題號
    01 - 10
    答案
    ABCADCBBDD
    01 02 03 04 05 06 07 08 09 10
    """

    answers = parse_answers(raw)

    assert answers[1] == "A"
    assert answers[5] == "D"
    assert answers[10] == "D"


def test_parse_correction_grid_and_notes():
    raw = """
    測驗題標準答案更正
    標準答案:答案標註#者,表該題有更正答案,其更正內容詳備註。
    題序
    答案 # B B D D D B # D D
    備註:
    題序
    答案
    01 02 03 04 05 06 07 08 09 10
    第1題答A或C或AC者均給分,第8題答C或D或CD者均給分
    第10題除未作答者不給分外,其餘均給分
    """

    answers = parse_answers(raw)
    notes = parse_correction_notes(raw)

    assert answers[1] == "#"
    assert answers[10] == "D"
    assert notes[1]["accepted_answers"] == ["A", "C"]
    assert notes[8]["accepted_answers"] == ["C", "D"]
    assert notes[10]["accepted_answers"] == ["A", "B", "C", "D"]
