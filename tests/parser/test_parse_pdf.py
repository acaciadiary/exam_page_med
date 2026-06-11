from scripts.exams.parse_answers import parse_answers
from scripts.exams.parse_pdf import load_repairs, parse_questions


def test_parse_sample_hypernatremia_question():
    raw = (
        "2..位 35歲的男性，因為意識不清被家.送.急診就醫，抽.檢查發現.鈉過."
        "（ 160 mEq/L，參考值 135～ 145 mEq/L）。有關..鈉（ hypernatremia）的處理，"
        "下列描述何者最適當？ A.估算全..量（ total-body water）：女性是體重的 60%，.男性是體重的 50%\n"
        "B.此病患若體重 70公.，計算 free water缺乏量（ free-water deficit）約 5000 c.c.\n"
        "C.不易感知的.分流失（ insensible losses）約5 mL/kg/day\n"
        "D..鈉的矯正儘量不超過 10 mM/day，以避免腦部.腫（ cerebral edema）"
    )

    questions = parse_questions(
        raw,
        year="115",
        subject="physician-stage-1-basic",
        answers={2: "B"},
        repairs=load_repairs(),
    )

    assert len(questions) == 1
    question = questions[0]
    assert question["id"] == "115_physician-stage-1-basic_002"
    assert question["question_number"] == 2
    assert "家屬送至急診" in question["question_text"]
    assert "高鈉血症" in question["question_text"]
    assert set(question["options"]) == {"A", "B", "C", "D"}
    assert "5000 c.c." in question["options"]["B"]
    assert question["correct_answer"] == "B"


def test_option_boundary_is_not_removed_by_dot_repairs():
    raw = "1..測試題幹？ A.第一 B.第二 C.第三 D..鈉的矯正"
    questions = parse_questions(raw, year="115", subject="sample", answers={1: "D"})

    assert questions[0]["options"]["D"].startswith("鈉的矯正")


def test_parse_questions_when_next_number_is_on_same_pdf_line():
    raw = """
    5.關於伸張反射（stretch reflex）之敘述，下列何者錯誤？
    A.其傳入纖維主要來自肌梭
    B.其傳入纖維主要為大型髓鞘神經纖維
    C.下運動神經元損傷可能導致伸張反射消失
    D.伸張反射為多突觸反射（multi-synaptic reflex） 6.下列何者不位於視覺傳導路徑上？
    A.外側膝狀體
    B.視徑
    C.上丘
    D.視神經
    """

    questions = parse_questions(raw, year="115", subject="medicine-1")

    assert len(questions) == 2
    assert questions[0]["question_number"] == 5
    assert questions[1]["question_number"] == 6
    assert questions[0]["options"]["D"].endswith("multi-synaptic reflex)")
    assert questions[1]["options"]["A"] == "外側膝狀體"


def test_parse_answers_from_text():
    answers = parse_answers("測驗式試題標準答案\n1 D\n2 B\n3 A\n")

    assert answers == {1: "D", 2: "B", 3: "A"}
