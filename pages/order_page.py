# order_page.py
from .base_page import BasePage
from locators.order_page_locators import *
from data_generator import generate_cyrillic_surname, generate_phone_number, generate_tomorrow_date, generate_date
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import WebDriverWait


class OrderPage(BasePage):
    def click_header_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_HEADER)

    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    def scroll_to_button_bottom(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_FOOTER)

    def fill_personal_data(self, name="Илья", address="г. Москва, ул. Профсоюзная"):
        self.fill_field(OrderPageLocators.NAME_INPUT, name)
        self.fill_field(OrderPageLocators.SURNAME_INPUT, generate_cyrillic_surname())
        self.fill_field(OrderPageLocators.ADDRESS_INPUT, address)
        self._select_metro_station()
        self.fill_field(OrderPageLocators.PHONE_INPUT, generate_phone_number())
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    def _select_metro_station(self):
        self.click_element(OrderPageLocators.METRO_INPUT)
        self.click_element(OrderPageLocators.METRO_STATION)

    def fill_rental_data(self):
        self.fill_field(OrderPageLocators.DATE_INPUT, generate_tomorrow_date())
        date_field = self.wait.until(
            EC.visibility_of_element_located(OrderPageLocators.DATE_INPUT)
        )
        date_field.send_keys(Keys.ENTER)

        # Ожидание закрытия календаря
        self.wait.until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "react-datepicker"))
        )
        self.click_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_element(OrderPageLocators.RENTAL_OPTION)
        self.click_element(OrderPageLocators.COLOR_CHECKBOX_BLACK)
        self.fill_field(OrderPageLocators.COMMENT_INPUT, "Я вас жду у магазина")
        self.click_element(OrderPageLocators.ORDER_BUTTON_BOTTOM)

    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)
        return self.is_element_visible(OrderPageLocators.SUCCESS_TITLE).is_displayed()

    def fill_personal_data_for_bottom(self, name="александр"):

        self.fill_field(OrderPageLocators.NAME_INPUT, name)
        self.fill_field(OrderPageLocators.SURNAME_INPUT, generate_cyrillic_surname())
        self.fill_field(OrderPageLocators.ADDRESS_INPUT, "Большая Якиманка, 38")
        self._select_metro_station()
        self.fill_field(OrderPageLocators.PHONE_INPUT, generate_phone_number())
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    def fill_rental_data_for_bottom(self):
        self.fill_field(OrderPageLocators.DATE_INPUT, generate_date())
        date_field = self.wait.until(
            EC.visibility_of_element_located(OrderPageLocators.DATE_INPUT)
        )
        date_field.send_keys(Keys.ENTER)


        self.wait.until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "react-datepicker"))
        )
        self.click_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_element(OrderPageLocators.RENTAL_OPTION)
        self.click_element(OrderPageLocators.COLOR_CHECKBOX_GREY)
        self.fill_field(OrderPageLocators.COMMENT_INPUT, "")
        self.click_element(OrderPageLocators.ORDER_BUTTON_BOTTOM)


