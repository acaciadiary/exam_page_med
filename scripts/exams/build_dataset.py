from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

try:
    from .parse_answers import parse_answers, parse_correction_notes
    from .parse_pdf import extract_pdf_text, load_repairs, parse_questions
except ImportError:
    from parse_answers import parse_answers, parse_correction_notes
    from parse_pdf import extract_pdf_text, load_repairs, parse_questions


def read_text_or_pdf(path: str | Path) -> str:
    source = Path(path)
    if source.suffix.lower() == ".pdf":
        return extract_pdf_text(source)
    return source.read_text(encoding="utf-8")


def build_dataset(
    question_path: str | Path,
    answer_path: str | Path,
    year: str,
    subject: str,
    title: str | None = None,
    source: str = "MOEX",
    correction_path: str | Path | None = None,
) -> dict:
    answers = parse_answers(read_text_or_pdf(answer_path))
    questions = parse_questions(
        read_text_or_pdf(question_path),
        year=year,
        subject=subject,
        answers=answers,
        repairs=load_repairs(),
    )
    apply_answer_metadata(questions, answers, source_name="official_answer")

    if correction_path and Path(correction_path).exists():
        correction_text = read_text_or_pdf(correction_path)
        correction_answers = parse_answers(correction_text)
        correction_notes = parse_correction_notes(correction_text)
        apply_corrections(questions, correction_answers, correction_notes)

    return {
        "id": f"{year}_{subject}",
        "year": year,
        "title": title or f"{year} 年醫師國考 {subject}",
        "subject": subject,
        "source": source,
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "questions": questions,
    }


def apply_answer_metadata(
    questions: list[dict],
    answers: dict[int, str],
    source_name: str,
) -> None:
    for question in questions:
        answer = answers.get(question["question_number"])
        if answer in {"A", "B", "C", "D"}:
            question["correct_answer"] = answer
            question["correct_answers"] = [answer]
            question["answer_status"] = "standard"
            question["answer_source"] = source_name


def apply_corrections(
    questions: list[dict],
    correction_answers: dict[int, str],
    correction_notes: dict[int, dict],
) -> None:
    if not correction_answers:
        return

    for question in questions:
        number = question["question_number"]
        corrected = correction_answers.get(number)
        if not corrected:
            continue

        question["answer_source"] = "official_correction"
        if corrected in {"A", "B", "C", "D"}:
            question["correct_answer"] = corrected
            question["correct_answers"] = [corrected]
            question["answer_status"] = "standard"
            continue

        note = correction_notes.get(number)
        if note:
            accepted = note["accepted_answers"]
            question["correct_answers"] = accepted
            question["correct_answer"] = accepted[0] if accepted else None
            question["answer_status"] = note["status"]
            question["answer_note"] = note["note"]
        else:
            question["correct_answer"] = None
            question["correct_answers"] = []
            question["answer_status"] = "corrected_pending_review"
            question["answer_note"] = "官方更正答案標註 #，需人工確認備註。"


def main() -> None:
    parser = argparse.ArgumentParser(description="Build frontend exam dataset JSON.")
    parser.add_argument("--questions", required=True)
    parser.add_argument("--answers", required=True)
    parser.add_argument("--year", required=True)
    parser.add_argument("--subject", required=True)
    parser.add_argument("--title", default=None)
    parser.add_argument("--source", default="MOEX")
    parser.add_argument("--corrections", default=None)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    dataset = build_dataset(
        question_path=args.questions,
        answer_path=args.answers,
        year=args.year,
        subject=args.subject,
        title=args.title,
        source=args.source,
        correction_path=args.corrections,
    )

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(dataset, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
