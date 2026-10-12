from src.models.student import Student
from src.models.student_card import StudentCard
from src.views.card_renderer import CardRenderer


def test_render_html_contains_student_fields() -> None:
    student = Student("674259018", "ภูศิษฏ์", "ภูศิษฏ์ ไพบูรณ์สมบัติ ", "PHUSIT", "PHAIBUNSOMBAT", "วิศวกรรมซอฟต์แวร์")
    card = StudentCard(student, card_number="5789 4856 1752 3659")
    html = CardRenderer(card).render_html()
    assert "ภูศิษฏ์ ไพบูรณ์สมบัติ " in html
    assert "674259018" in html
    assert "5789 4856 1752 3659" in html
    assert "CVV" not in html