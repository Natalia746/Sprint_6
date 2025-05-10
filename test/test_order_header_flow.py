import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import OrderPageLocators


@allure.epic("Полный цикл оформления заказа")
class TestFullOrderFlow:
    @allure.title("Проверка полного цикла заказа самоката")
    def test_complete_order_flow(self, driver):
        with allure.step("1. Открыть главную страницу"):
            driver.get("https://qa-scooter.praktikum-services.ru/")

        with allure.step("2. Начать оформление заказа"):
            from pages.main_page import MainPage
            main_page = MainPage(driver)
            main_page.click_header_order_button()

        with allure.step("3. Заполнить персональные данные"):
            from pages.order_page import OrderPage
            order_page = OrderPage(driver)
            order_page.fill_personal_data()

        with allure.step("4. Заполнить данные аренды"):
            order_page.fill_rental_data()

        with allure.step("5. Подтвердить заказ"):
            assert order_page.confirm_order(), "Окно подтверждения не отобразилось"

        with allure.step("6. Проверить переходы по логотипам"):
            order_page._click(OrderPageLocators.STATUS_BUTTON)

            # Проверка логотипа Самоката
            main_page.click_scooter_logo()
            WebDriverWait(driver, 10).until(
                EC.url_to_be("https://qa-scooter.praktikum-services.ru/")
            )

            # Проверка логотипа Яндекса
            main_page.click_yandex_logo()
            driver.switch_to.window(driver.window_handles[1])
            WebDriverWait(driver, 10).until(
                EC.url_contains("https://dzen.ru")
            )