from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click_header_order_button(self):
        self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_HEADER)
        ).click()

    def click_scooter_logo(self):
        self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.SCOOTER_LOGO)
        ).click()

    def click_yandex_logo(self):
        self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.YANDEX_LOGO)
        ).click()

    def scroll_to_element (self):
        button = self.wait.until(
            EC.presence_of_element_located(MainPageLocators.ELEMENT)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)

    def click_bottom_order_button(self):
        self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_FOOTER)
        ).click()