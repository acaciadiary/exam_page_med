from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path
from typing import Any

QUESTION_RE = re.compile(
    r"(?ms)(?:^|\n)\s*(?P<num>[1-9]\d{0,2})\s*[\.．、]{1,2}(?!\d)\s*"
    r"(?P<body>.*?)(?=(?:\n\s*[1-9]\d{0,2}\s*[\.．、]{1,2}(?!\d)\s*)|\Z)"
)

OPTION_START_RE = re.compile(
    r"(?:(?<=^)|(?<=[\s。？?（）()]))(?P<label>[A-D])\s*[\.\．、]\s*"
)

DEFAULT_REPAIRS = {
    "家.送.": "家屬送至",
    "抽.檢查": "抽血檢查",
    ".鈉過.": "高鈉血症",
    "..鈉": "高鈉",
    "全..量": "全身水體積",
    "公.": "公斤",
    ".分流失": "水分流失",
    "腦部.腫": "腦部水腫",
}


def load_repairs(path: str | Path | None = None) -> dict[str, str]:
    if path is None:
        path = Path(__file__).with_name("repair_dictionary.json")
    repair_path = Path(path)
    if not repair_path.exists():
        return DEFAULT_REPAIRS
    with repair_path.open("r", encoding="utf-8") as file:
        return {**DEFAULT_REPAIRS, **json.load(file)}


def normalize_text(raw: str, repairs: dict[str, str] | None = None) -> str:
    text = unicodedata.normalize("NFKC", raw)
    text = text.replace("\r", "\n")
    text = re.sub(r"(?<![A-Za-z0-9])([A-D])\.\.", r"\1.", text)
    text = re.sub(r"([a-z)])([A-D])\.", r"\1 \2.", text)
    text = re.sub(r"([一-龥）])([A-D])\.", r"\1 \2.", text)
    text = re.sub(
        r"\n\s*(\d+(?:\.\d+)?)\s*((?:mEq|mg|mmHg|ng|g|U|μIU|µIU|°C|%|/|pg|mmol|kg|mL|fl|mm)[^\n,，]*)",
        r" \1 \2",
        text,
    )
    # Fix the "question number + age" issue by inserting space: e.g. "16.55歲" -> "16. 55歲"
    text = re.sub(
        r"(\b[1-9]\d{0,2})\.(\d+)\s*(歲|週|個|天|月|日|-(?=[A-Za-z]))",
        r"\1. \2\3",
        text,
    )
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"(?<=[。？）)])\s+(\d{1,3})\.(?=[^\d\s])", r"\n\1.", text)
    text = re.sub(r"\n{2,}", "\n", text)
    text = re.sub(r"([一-龥])[ \t]+([一-龥])", r"\1\2", text)
    text = re.sub(r"\s+([，。；：！？、）])", r"\1", text)
    text = re.sub(r"([（])\s+", r"\1", text)
    for bad, fixed in (repairs or DEFAULT_REPAIRS).items():
        text = text.replace(bad, fixed)
    return text.strip()


def split_options(body: str) -> tuple[str, dict[str, str]]:
    starts = list(OPTION_START_RE.finditer(body))
    
    d_match = None
    c_match = None
    b_match = None
    a_match = None
    
    for m in reversed(starts):
        if m.group("label") == "D":
            d_match = m
            break
            
    if d_match:
        d_idx = starts.index(d_match)
        for m in reversed(starts[:d_idx]):
            if m.group("label") == "C":
                c_match = m
                break
                
    if c_match:
        c_idx = starts.index(c_match)
        for m in reversed(starts[:c_idx]):
            if m.group("label") == "B":
                b_match = m
                break
                
    if b_match:
        b_idx = starts.index(b_match)
        for m in reversed(starts[:b_idx]):
            if m.group("label") == "A":
                a_match = m
                break
                
    if not (a_match and b_match and c_match and d_match):
        raise ValueError("Cannot find A-D option boundaries")

    opt_starts = [a_match, b_match, c_match, d_match]
    question_text = body[: opt_starts[0].start()].strip()
    options: dict[str, str] = {}

    for index, match in enumerate(opt_starts):
        label = match.group("label")
        end = opt_starts[index + 1].start() if index + 1 < len(opt_starts) else len(body)
        options[label] = body[match.end() : end].strip()

    return question_text, options


def parse_questions(
    raw_text: str,
    year: str,
    subject: str,
    answers: dict[int, str] | None = None,
    repairs: dict[str, str] | None = None,
) -> list[dict[str, Any]]:
    text = normalize_text(raw_text, repairs)
    questions: list[dict[str, Any]] = []
    answer_map = answers or {}

    for match in QUESTION_RE.finditer(text):
        number = int(match.group("num"))
        body = match.group("body").strip()
        question_text, options = split_options(body)

        questions.append(
            {
                "id": f"{year}_{subject}_{number:03d}",
                "question_number": number,
                "question_text": question_text,
                "options": options,
                "correct_answer": answer_map.get(number),
                "explanation": "",
                "key_point": "",
                "flashcard_summary": "",
                "review_status": "empty",
            }
        )

    return questions


def extract_pdf_text(path: str | Path) -> str:
    pdf_path = Path(path)
    try:
        import fitz

        with fitz.open(pdf_path) as document:
            return "\n".join(page.get_text("text", sort=True) for page in document)
    except Exception:
        pass

    try:
        import pdfplumber

        with pdfplumber.open(pdf_path) as pdf:
            return "\n".join(page.extract_text() or "" for page in pdf.pages)
    except Exception:
        pass

    from pypdf import PdfReader

    reader = PdfReader(str(pdf_path))
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse MOEX question PDF/text.")
    parser.add_argument("input", help="PDF or plain text path")
    parser.add_argument("--year", required=True)
    parser.add_argument("--subject", required=True)
    parser.add_argument("--answers", default=None, help="Optional answers JSON path")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    input_path = Path(args.input)
    raw = extract_pdf_text(input_path) if input_path.suffix.lower() == ".pdf" else input_path.read_text(encoding="utf-8")
    answers = {}
    if args.answers:
        answers = {int(k): v for k, v in json.loads(Path(args.answers).read_text(encoding="utf-8")).items()}

    questions = parse_questions(raw, args.year, args.subject, answers, load_repairs())
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(questions, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
