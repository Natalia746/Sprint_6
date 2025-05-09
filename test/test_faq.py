import pytest
import allure
from locators.faq_page_locators import FAQLocators


@allure.epic("Тесты раздела FAQ")
@allure.feature("Проверка вопросов и ответов")
class TestFAQ:
    @pytest.mark.parametrize("question_id", [0, 1, 2, 3, 4, 5, 6, 7])
    @allure.title("Тест вопроса #{question_id}: {expected_question}")
    def test_faq_question_and_answer(self, faq_page, question_id):
        with allure.step("Получаем ожидаемые тексты вопроса и ответа"):
            expected_question = FAQLocators.EXPECTED_QUESTIONS[question_id]
            expected_answer = FAQLocators.EXPECTED_ANSWERS[question_id]

        with allure.step("Проверяем текст вопроса"):
            question_text = faq_page.get_question_text(question_id)
            allure.dynamic.description(f'Вопрос: "{expected_question}"')
            assert question_text == expected_question, f"Текст вопроса не совпадает"

        with allure.step("Кликаем по вопросу и проверяем ответ"):
            faq_page.click_question(question_id)
            answer_text = faq_page.get_answer_text(question_id)

            allure.attach(
                f"Ожидаемый ответ: {expected_answer}\nФактический ответ: {answer_text}",
                name="Сравнение ответов",
                attachment_type=allure.attachment_type.TEXT
            )

        assert FAQLocators.EXPECTED_ANSWERS[question_id] in answer_text, \
        f"Текст '{FAQLocators.EXPECTED_ANSWERS[question_id]}' не найден в ответе"



