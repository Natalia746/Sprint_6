from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import *
from data_generator import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def fill_personal_data(self, name="Илья"):
        # Заполнение первой страницы
        self._fill_field(OrderPageLocators.NAME_INPUT, name)
        self._fill_field(OrderPageLocators.SURNAME_INPUT, generate_cyrillic_surname())
        self._fill_field(OrderPageLocators.ADDRESS_INPUT, "г. Москва, ул. Профсоюзная")
        self._select_metro_station()
        self._fill_field(OrderPageLocators.PHONE_INPUT, generate_phone_number())
        self._click(OrderPageLocators.NEXT_BUTTON)

    def fill_personal_data_for_bottom(self, name="александр"):
        # Заполнение первой страницы для нижней кнопки
        self._fill_field(OrderPageLocators.NAME_INPUT, name)
        self._fill_field(OrderPageLocators.SURNAME_INPUT, generate_cyrillic_surname())
        self._fill_field(OrderPageLocators.ADDRESS_INPUT, "Большая Якиманка, 38")
        self._select_metro_station()
        self._fill_field(OrderPageLocators.PHONE_INPUT, generate_phone_number())
        self._click(OrderPageLocators.NEXT_BUTTON)

    def fill_rental_data(self):
        # Заполнение второй страницы
        self._fill_field(OrderPageLocators.DATE_INPUT, generate_tomorrow_date())

        # Явное закрытие календаря через Enter + проверка
        date_field = self.wait.until(
            EC.visibility_of_element_located(OrderPageLocators.DATE_INPUT)
        )
        date_field.send_keys(Keys.ENTER)

        # Ожидание закрытия календаря
        self.wait.until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "react-datepicker"))
        )

        # Остальные действия
        self._select_rental_period()
        self._click(OrderPageLocators.COLOR_CHECKBOX_BLACK)
        self._fill_field(OrderPageLocators.COMMENT_INPUT, "Я вас жду у магазина")
        self._click(OrderPageLocators.ORDER_BUTTON_BOTTOM)

    def fill_rental_data_for_bottom(self):
        # Заполнение второй страницы
        self._fill_field(OrderPageLocators.DATE_INPUT, generate_date())

        # Явное закрытие календаря через Enter + проверка
        date_field = self.wait.until(
            EC.visibility_of_element_located(OrderPageLocators.DATE_INPUT)
        )
        date_field.send_keys(Keys.ENTER)

        # Ожидание закрытия календаря
        self.wait.until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "react-datepicker"))
        )

        # Остальные действия
        self._select_rental_period_bottom()
        self._click(OrderPageLocators.COLOR_CHECKBOX_GREY)
        self._fill_field(OrderPageLocators.COMMENT_INPUT, " ")
        self._click(OrderPageLocators.ORDER_BUTTON_BOTTOM)

    def confirm_order(self):
        # Подтверждение заказа
        self.wait.until(EC.visibility_of_element_located(OrderPageLocators.MODAL_WINDOW))
        self._click(OrderPageLocators.CONFIRM_BUTTON)
        return self.wait.until(
            EC.visibility_of_element_located(OrderPageLocators.SUCCESS_TITLE)
        ).is_displayed()

    def _fill_field(self, locator, value):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(value)

    def _click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def _select_metro_station(self):
        self._click(OrderPageLocators.METRO_INPUT)
        self._click(OrderPageLocators.METRO_STATION)

    def _select_rental_period(self):
        self._click(OrderPageLocators.RENTAL_PERIOD)
        self._click(OrderPageLocators.RENTAL_OPTION)

    def _select_rental_period_bottom(self):
        self._click(OrderPageLocators.RENTAL_PERIOD)
        self._click(OrderPageLocators.RENTAL_OPTION_BOTTOM)