from __future__ import annotations

import argparse
import json
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import Request, urlopen

try:
    from .moex_sources import get_preset
except ImportError:
    from moex_sources import get_preset

MOEX_SEARCH_URL = "https://wwwq.moex.gov.tw/exam/wFrmExamQandASearch.aspx"


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []
        self._href: str | None = None
        self._text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        href = dict(attrs).get("href")
        if href:
            self._href = href
            self._text = []

    def handle_data(self, data: str) -> None:
        if self._href:
            self._text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "a" and self._href:
            self.links.append((" ".join(part.strip() for part in self._text if part.strip()), self._href))
            self._href = None
            self._text = []


def fetch_bytes(url: str) -> bytes:
    request = Request(url, headers={"User-Agent": "medical-exam-prep/0.1"})
    with urlopen(request, timeout=60) as response:
        return response.read()


def discover_pdf_links(year: str, keyword: str) -> list[tuple[str, str]]:
    html = fetch_bytes(MOEX_SEARCH_URL).decode("utf-8", errors="replace")
    parser = LinkParser()
    parser.feed(html)
    links: list[tuple[str, str]] = []

    for label, href in parser.links:
        candidate = f"{label} {href}"
        if year in candidate and keyword in candidate and ".pdf" in href.lower():
            links.append((label or Path(href).name, urljoin(MOEX_SEARCH_URL, href)))

    return links


def download_links(links: list[tuple[str, str]], out_dir: Path) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    saved: list[Path] = []

    for index, (label, url) in enumerate(links, start=1):
        filename = f"{index:02d}_{safe_filename(label)}.pdf"
        target = out_dir / filename
        target.write_bytes(fetch_bytes(url))
        saved.append(target)

    return saved


def download_url(url: str, target: Path) -> Path:
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(fetch_bytes(url))
    return target


def download_preset(name: str, out_dir: Path) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for subject in get_preset(name):
        subject_dir = out_dir / subject.year / subject.subject
        question_path = download_url(subject.question_url, subject_dir / "questions.pdf")
        answer_path = download_url(subject.answer_url, subject_dir / "answers.pdf")
        record = {
            "id": subject.id,
            "year": subject.year,
            "title": subject.title,
            "subject": subject.subject,
            "group": subject.group,
            "question_pdf": str(question_path),
            "answer_pdf": str(answer_path),
            "question_url": subject.question_url,
            "answer_url": subject.answer_url,
        }
        if subject.has_correction:
            correction_path = download_url(subject.correction_url, subject_dir / "corrections.pdf")
            record["correction_pdf"] = str(correction_path)
            record["correction_url"] = subject.correction_url
        records.append(record)
    return records


def safe_filename(value: str) -> str:
    cleaned = "".join(ch if ch.isalnum() or ch in "-_." else "_" for ch in value)
    return cleaned[:96] or "moex_exam"


def main() -> None:
    parser = argparse.ArgumentParser(description="Discover and download MOEX PDFs.")
    parser.add_argument("--year", required=True, help="ROC year, for example 115")
    parser.add_argument("--keyword", default="醫師")
    parser.add_argument("--out-dir", default="downloads/moex")
    parser.add_argument("--preset", default=None)
    args = parser.parse_args()

    if args.preset:
        records = download_preset(args.preset, Path(args.out_dir))
        print(json.dumps(records, ensure_ascii=False, indent=2))
    else:
        links = discover_pdf_links(args.year, args.keyword)
        saved = download_links(links, Path(args.out_dir) / args.year)
        for path in saved:
            print(path)


if __name__ == "__main__":
    main()
