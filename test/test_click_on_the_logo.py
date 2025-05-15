import allure
from curl import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@allure.epic("Переход на главную страницу при нажатии на логотип Самоката")
class TestTrafficFromClick:
    @allure.feature("Нажатие на логотип Самоката")
    @allure.story("Позитивный сценарий оформления")
    def test_successful_transition_click_logo(self, order_page):
        with allure.step("Инициализация страницы заказа"):
            order_page.open()
        with allure.step("Переход на главную страницу"):
            order_page.click_scooter_logo()
            assert order_page.driver.current_url == base_url

    @allure.feature("Нажатие на логотип Яндекса")
    @allure.story("Позитивный сценарий оформления")
    def test_successful_transition_link_dzen(self, order_page):
        with allure.step("Инициализация страницы заказа"):
            order_page.open()

        with allure.step("Переход на страницу Дзена"):
            order_page.click_yandex_logo()

            # Ожидание открытия нового окна
            WebDriverWait(order_page.driver, 15).until(
                EC.number_of_windows_to_be(2)
            )

            # Переключение на новую вкладку
            order_page.driver.switch_to.window(
                order_page.driver.window_handles[1]
            )

            # Явное ожидание загрузки Dzen
            WebDriverWait(order_page.driver, 15).until(
                EC.url_contains("dzen.ru")
            )

            # Проверка URL
            assert "dzen.ru" in order_page.driver.current_url

        with allure.step("Возврат в исходное окно"):
            order_page.driver.close()
            order_page.driver.switch_to.window(
                order_page.driver.window_handles[0]
            )