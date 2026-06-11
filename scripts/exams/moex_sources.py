from __future__ import annotations

from dataclasses import dataclass
from urllib.parse import urlencode

MOEX_FILE_URL = "https://wwwq.moex.gov.tw/exam/wHandExamQandA_File.ashx"


@dataclass(frozen=True)
class MoexSubject:
    id: str
    year: str
    exam_code: str
    category_code: str
    subject_code: str
    title: str
    subject: str
    group: str
    has_correction: bool = False

    def url(self, kind: str) -> str:
        params = {
            "c": self.category_code,
            "code": self.exam_code,
            "q": "1",
            "s": self.subject_code,
            "t": kind,
        }
        return f"{MOEX_FILE_URL}?{urlencode(params)}"

    @property
    def question_url(self) -> str:
        return self.url("Q")

    @property
    def answer_url(self) -> str:
        return self.url("S")

    @property
    def correction_url(self) -> str:
        return self.url("M")


PHYSICIAN_115_FIRST: list[MoexSubject] = [
    MoexSubject(
        id="115-1-physician-medicine-1",
        year="115",
        exam_code="115020",
        category_code="301",
        subject_code="0101",
        title="115 年第一次醫師國考：醫學（一）",
        subject="medicine-1",
        group="醫師(一)",
        has_correction=True,
    ),
    MoexSubject(
        id="115-1-physician-medicine-2",
        year="115",
        exam_code="115020",
        category_code="301",
        subject_code="0102",
        title="115 年第一次醫師國考：醫學（二）",
        subject="medicine-2",
        group="醫師(一)",
    ),
    MoexSubject(
        id="115-1-physician-medicine-3",
        year="115",
        exam_code="115020",
        category_code="302",
        subject_code="0103",
        title="115 年第一次醫師國考：醫學（三）",
        subject="medicine-3",
        group="醫師(二)",
        has_correction=True,
    ),
    MoexSubject(
        id="115-1-physician-medicine-4",
        year="115",
        exam_code="115020",
        category_code="302",
        subject_code="0104",
        title="115 年第一次醫師國考：醫學（四）",
        subject="medicine-4",
        group="醫師(二)",
        has_correction=True,
    ),
    MoexSubject(
        id="115-1-physician-medicine-5",
        year="115",
        exam_code="115020",
        category_code="302",
        subject_code="0105",
        title="115 年第一次醫師國考：醫學（五）",
        subject="medicine-5",
        group="醫師(二)",
        has_correction=True,
    ),
    MoexSubject(
        id="115-1-physician-medicine-6",
        year="115",
        exam_code="115020",
        category_code="302",
        subject_code="0106",
        title="115 年第一次醫師國考：醫學（六）",
        subject="medicine-6",
        group="醫師(二)",
        has_correction=True,
    ),
]

PRESETS = {
    "physician-115-first": PHYSICIAN_115_FIRST,
}


def get_preset(name: str) -> list[MoexSubject]:
    try:
        return PRESETS[name]
    except KeyError as exc:
        choices = ", ".join(sorted(PRESETS))
        raise ValueError(f"Unknown preset {name!r}. Choices: {choices}") from exc
