import pytest
import allure
from data import Data


@allure.epic("Тесты раздела FAQ")
@allure.feature("Проверка вопросов и ответов")
class TestFAQ:
    @pytest.mark.parametrize("question_id", [0, 1, 2, 3, 4, 5, 6, 7])
    @allure.title("Тест вопроса #{question_id}")
    def test_faq_question_and_answer(self, faq_page, question_id):
        with allure.step(f"Получаем текст вопроса {question_id}"):
            expected_question = Data.EXPECTED_QUESTIONS[question_id]
            actual_question = faq_page.get_question_text(question_id)

            assert actual_question == expected_question, (
                f"Ожидался вопрос: '{expected_question}'\n"
                f"Фактический текст: '{actual_question}'"
            )

        with allure.step(f"Кликаем на вопрос {question_id} и проверяем ответ"):
            faq_page.click_question(question_id)
            actual_answer = faq_page.get_answer_text(question_id)
            expected_answer = Data.EXPECTED_ANSWERS[question_id]

            assert actual_answer == expected_answer, (
                f"Ожидался ответ: '{expected_answer}'\n"
                f"Фактический текст: '{actual_answer}'"
            )