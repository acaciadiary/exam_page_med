from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path
from typing import Any

try:
    from .parse_pdf import extract_pdf_text, normalize_text
except ImportError:
    from parse_pdf import extract_pdf_text, normalize_text

ANSWER_PAIR_RE = re.compile(r"(?<!\d)(?P<num>\d{1,3})\s*(?P<ans>[A-D#]+)(?=\s|$)")
ANSWER_LINE_RE = re.compile(r"^\s*(?:答案|蝑\?)\s*(?P<body>.+)$")
ANSWER_HEADER_RE = re.compile(r"^\s*(?:答案|蝑\?)\s*$")
NUMBER_LINE_RE = re.compile(r"^\s*(?:題序|憿?\s*)?(?P<body>(?:\d{1,3}\s+){4,}\d{1,3})\s*$")
ANSWER_TOKEN_RE = re.compile(r"[A-D#]+")
NUMBER_TOKEN_RE = re.compile(r"\d{1,3}")
MULTI_CREDIT_NOTE_RE = re.compile(r"第(?P<num>\d{1,3})題\s*答(?P<body>[A-D或]+)者均給分")
ALL_CREDIT_NOTE_RE = re.compile(r"第(?P<num>\d{1,3})題一律給分")
ANY_MARKED_CREDIT_NOTE_RE = re.compile(r"第(?P<num>\d{1,3})題除未作答者不給分外[，,]其餘均給分")


def parse_answers(raw_answer_text: str) -> dict[int, str]:
    text = prepare_text(raw_answer_text)
    grid_answers = parse_answer_grid(text)
    if grid_answers:
        return grid_answers

    return {
        int(match.group("num")): normalize_answer(match.group("ans"))
        for match in ANSWER_PAIR_RE.finditer(text)
    }


def parse_answer_grid(text: str) -> dict[int, str]:
    number_rows: list[list[int]] = []
    answer_rows: list[list[str]] = []
    
    number_re = re.compile(r"(?P<body>(?:\d{1,3}\s+){4,}\d{1,3})\s*$")
    answer_re = re.compile(r"(?P<body>(?:[A-D#]\s+){4,}[A-D#])\s*$")
    compact_answer_re = re.compile(r"^\s*(?P<body>[A-D#]{4,})\s*$")
    
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
            
        num_match = number_re.search(line)
        if num_match:
            row = [int(token) for token in re.findall(r"\d{1,3}", num_match.group("body"))]
            number_rows.append(row)
            continue
            
        ans_match = answer_re.search(line)
        if ans_match:
            row = [token for token in re.findall(r"[A-D#]", ans_match.group("body"))]
            answer_rows.append(row)
            continue

        compact_ans_match = compact_answer_re.match(line)
        if compact_ans_match:
            row = [normalize_answer(char) for char in compact_ans_match.group("body")]
            answer_rows.append(row)
            continue
            
    answers = [answer for row in answer_rows for answer in row]
    numbers = [number for row in number_rows for number in row]
    
    if not answers or len(answers) != len(numbers):
        return {}
        
    return dict(zip(numbers, answers))


def parse_answer_tokens(body: str) -> list[str]:
    tokens: list[str] = []
    for chunk in ANSWER_TOKEN_RE.findall(body):
        if len(chunk) == 1:
            tokens.append(normalize_answer(chunk))
        else:
            tokens.extend(normalize_answer(char) for char in chunk)
    return tokens


def parse_correction_notes(raw_answer_text: str) -> dict[int, dict[str, Any]]:
    text = prepare_text(raw_answer_text)
    notes: dict[int, dict[str, Any]] = {}

    for match in MULTI_CREDIT_NOTE_RE.finditer(text):
        accepted = unique_answers(ANSWER_TOKEN_RE.findall(match.group("body")))
        if accepted:
            note_text = re.sub(r"\s+", "", match.group(0))
            notes[int(match.group("num"))] = {
                "accepted_answers": accepted,
                "status": "multiple_correct",
                "note": note_text,
            }

    for match in ALL_CREDIT_NOTE_RE.finditer(text):
        notes[int(match.group("num"))] = {
            "accepted_answers": ["A", "B", "C", "D"],
            "status": "all_credit",
            "note": match.group(0),
        }

    for match in ANY_MARKED_CREDIT_NOTE_RE.finditer(text):
        notes[int(match.group("num"))] = {
            "accepted_answers": ["A", "B", "C", "D"],
            "status": "all_credit",
            "note": match.group(0),
        }

    return notes


def unique_answers(chunks: list[str]) -> list[str]:
    answers: list[str] = []
    for chunk in chunks:
        for char in chunk:
            answer = normalize_answer(char)
            if answer in {"A", "B", "C", "D"} and answer not in answers:
                answers.append(answer)
    return answers


def normalize_answer(value: str) -> str:
    return unicodedata.normalize("NFKC", value).replace("嚗?", "#").strip()


def prepare_text(raw_text: str) -> str:
    return unicodedata.normalize("NFKC", normalize_text(raw_text))


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse MOEX answer PDF/text.")
    parser.add_argument("input", help="PDF or plain text answer path")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    input_path = Path(args.input)
    raw = extract_pdf_text(input_path) if input_path.suffix.lower() == ".pdf" else input_path.read_text(encoding="utf-8")
    answers = parse_answers(raw)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(answers, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
