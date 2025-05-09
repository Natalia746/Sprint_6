from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.faq_page_locators import FAQLocators
from curl import *


class FAQPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.base_url = base_url

    def open(self):
        self.driver.get(self.base_url)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_question(self, question_id):
        element = self.driver.find_element(*FAQLocators.FAQ_QUESTIONS[question_id])
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_question(self, question_id):
        self.scroll_to_question(question_id)
        question = self.wait.until(
            EC.element_to_be_clickable(FAQLocators.FAQ_QUESTIONS[question_id])
        )
        question.click()

    def get_question_text(self, question_id):
        return self.driver.find_element(*FAQLocators.FAQ_QUESTIONS[question_id]).text

    def get_answer_text(self, question_id):
        return self.wait.until(
            EC.visibility_of_element_located(FAQLocators.FAQ_ANSWERS[question_id])
        ).text