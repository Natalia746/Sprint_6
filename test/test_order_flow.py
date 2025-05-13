import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from curl import *
from locators.order_page_locators import *

from pages.order_page import OrderPage
from pages.main_page import MainPage

@allure.epic("Полный цикл оформления заказа")
class TestFullOrderFlow:
    @allure.feature("Заказ через верхнюю кнопку")
    @allure.story("Позитивный сценарий оформления")
    @allure.title("Проверка полного цикла заказа самоката через кнопку вверху страницы")
    def test_complete_order_flow(self, driver):
        with allure.step("1. Открыть главную страницу"):
            driver.get(base_url)

        with allure.step("2. Начать оформление заказа"):

            main_page = MainPage(driver)
            with allure.step("Нажать на верхнюю кнопку 'Заказать'"):
                main_page.click_header_order_button()

        with allure.step("3. Заполнить персональные данные"):

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
                EC.url_to_be(base_url)
            )

            # Проверка логотипа Яндекса
            main_page.click_yandex_logo()
            driver.switch_to.window(driver.window_handles[1])
            WebDriverWait(driver, 10).until(
                EC.url_contains(dzen_url)
            )

    @allure.feature("Заказ через нижнюю кнопку")
    @allure.story("Позитивный сценарий оформления")
    @allure.title("Проверка полного цикла заказа самоката через кнопку внизу страницы")
    def test_complete_order_flow_bottom_button(self, driver):
        with allure.step("1. Открыть главную страницу"):
            driver.get(base_url)

        with allure.step("2. Подготовить страницу к работе"):
            main_page = MainPage(driver)
            main_page.scroll_to_element()

        with allure.step("3. Нажать нижнюю кнопку заказа"):
            # Добавляем скролл с корректировкой положения
            button = main_page.wait.until(
                EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON_FOOTER)
            )
            driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'instant'});", button)

            # Кликаем через JavaScript
            driver.execute_script("arguments[0].click();", button)

        with allure.step("4. Заполнить персональные данные"):
            order_page = OrderPage(driver)
            order_page.fill_personal_data_for_bottom()

        with allure.step("5. Заполнить данные аренды"):
            order_page.fill_rental_data_for_bottom()

        with allure.step("6. Подтвердить заказ и проверить успешность"):
            assert order_page.confirm_order(), "Окно подтверждения не отобразилось"

        with allure.step("7. Проверить переходы по логотипам"):
            order_page._click(OrderPageLocators.STATUS_BUTTON)
            # Проверка логотипа Самоката
            with allure.step("Проверить переход на главную через лого Самоката"):
                main_page.click_scooter_logo()
                WebDriverWait(driver, 10).until(
                    EC.url_to_be(base_url)
                )

            # Проверка логотипа Яндекса
            with allure.step("Проверить переход на Дзен через лого Яндекса"):
                main_page.click_yandex_logo()
                driver.switch_to.window(driver.window_handles[1])
                WebDriverWait(driver, 10).until(
                    EC.url_contains(dzen_url)
                )
