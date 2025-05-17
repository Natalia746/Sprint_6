import allure
from .base_page import BasePage
from locators.order_page_locators import *
from data_generator import *


class OrderPage(BasePage):

    @allure.step("Нажать на верхнюю кнопку Заказать")
    def click_header_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    @allure.step("Скролл до нижней кнопки Заказать")
    def scroll_to_button_bottom(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_FOOTER)

    @allure.step("Заполнить поля имя, фамилия, адрес, станция метро, номер телефона")
    def fill_personal_data(self, name="Илья", address="г. Москва, ул. Профсоюзная"):
        self.fill_field(OrderPageLocators.NAME_INPUT, name)
        self.fill_field(OrderPageLocators.SURNAME_INPUT, generate_cyrillic_surname())
        self.fill_field(OrderPageLocators.ADDRESS_INPUT, address)
        self._select_metro_station()
        self.fill_field(OrderPageLocators.PHONE_INPUT, generate_phone_number())
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Выбрать станцию метро")
    def _select_metro_station(self):
        self.click_element(OrderPageLocators.METRO_INPUT)
        self.click_element(OrderPageLocators.METRO_STATION)

    @allure.step("Заполнить поля дата начало аренды, срок аренды, цвет, комментарий")
    def fill_rental_data(self):
        self.fill_field(OrderPageLocators.DATE_INPUT, generate_tomorrow_date())
        date_field = self.is_element_visible(OrderPageLocators.DATE_INPUT)
        self.press_enter(OrderPageLocators.DATE_INPUT)
        self.wait_for_element_invisibility(OrderPageLocators.CALENDAR)
        self.click_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_element(OrderPageLocators.RENTAL_OPTION)
        self.click_element(OrderPageLocators.COLOR_CHECKBOX_BLACK)
        self.fill_field(OrderPageLocators.COMMENT_INPUT, "Я вас жду у магазина")
        self.click_element(OrderPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Появления окна с сообщением о заказе")
    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)
        return self.is_element_visible(OrderPageLocators.SUCCESS_TITLE)

    @allure.step("Заполнить поля имя, фамилия, адрес, станция метро, номер телефона")
    def fill_personal_data_for_bottom(self, name="александр"):

        self.fill_field(OrderPageLocators.NAME_INPUT, name)
        self.fill_field(OrderPageLocators.SURNAME_INPUT, generate_cyrillic_surname())
        self.fill_field(OrderPageLocators.ADDRESS_INPUT, "Большая Якиманка, 38")
        self._select_metro_station()
        self.fill_field(OrderPageLocators.PHONE_INPUT, generate_phone_number())
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить поля дата начало аренды, срок аренды, цвет, комментарий")
    def fill_rental_data_for_bottom(self):
        self.fill_field(OrderPageLocators.DATE_INPUT, generate_date())
        date_field = self.is_element_visible(OrderPageLocators.DATE_INPUT)
        self.press_enter(OrderPageLocators.DATE_INPUT)
        self.wait_for_element_invisibility(OrderPageLocators.CALENDAR)
        self.click_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_element(OrderPageLocators.RENTAL_OPTION)
        self.click_element(OrderPageLocators.COLOR_CHECKBOX_GREY)
        self.fill_field(OrderPageLocators.COMMENT_INPUT, "")
        self.click_element(OrderPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Нажать на нижнюю кнопку Заказать")
    def click_button_order_bottom(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_FOOTER)

