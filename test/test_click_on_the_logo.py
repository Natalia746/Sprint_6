import allure
from curl import *

@allure.epic("Переход на главную страницу при нажатии на логотип Самоката")
class TestTrafficFromClick:
    @allure.feature("Нажатие на логотип Самоката")
    @allure.story("Позитивный сценарий оформления")
    @allure.title("Проверка перехода на главную страницу при нажатии на логотип Самоката")
    def test_successful_transition_click_logo(self, order_page, base_url):
        with allure.step("Инициализация страницы заказа"):
            order_page.open()

        with allure.step("Клик по логотипу Самоката"):
            order_page.click_scooter_logo()

        with allure.step("Проверка открывшейся страницы"):
            assert order_page.get_current_url() == BASE_URL

    @allure.feature("Нажатие на логотип Яндекса")
    @allure.story("Позитивный сценарий оформления")
    @allure.title("Проверка перехода на главную страницу dzen при нажатии на логотип Яндекса")
    def test_successful_transition_link_dzen(self, order_page):
        with allure.step("Инициализация страницы заказа"):
            order_page.open()

        with allure.step("Переход на страницу Дзена"):
            order_page.click_yandex_logo()
            order_page.wait_for_number_of_windows(2)
            order_page.switch_to_new_window(1)
            order_page.wait_for_url_contains("dzen.ru")
            assert "dzen.ru" in order_page.get_current_url()



