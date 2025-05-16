import allure
from .base_page import BasePage
from locators.faq_page_locators import FAQLocators


class FAQPage(BasePage):

    @allure.step("Получить текст вопроса")
    def get_question_text(self, question_id):
        return self.get_element_text(FAQLocators.FAQ_QUESTIONS[question_id])

    @allure.step("Нажать вопрос")
    def click_question(self, question_id):
        self.scroll_to_element(FAQLocators.FAQ_QUESTIONS[question_id])
        self.click_element(FAQLocators.FAQ_QUESTIONS[question_id])

    @allure.step("Получить текст ответа")
    def get_answer_text(self, question_id):
        return self.get_element_text(FAQLocators.FAQ_ANSWERS[question_id])