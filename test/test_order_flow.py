import allure
from locators.order_page_locators import MainPageLocators, OrderPageLocators

@allure.epic("Полный цикл оформления заказа")
class TestFullOrderFlow:
    @allure.feature("Заказ через верхнюю кнопку")
    @allure.story("Позитивный сценарий оформления")
    @allure.title("Проверка полного цикла заказа через верхнюю кнопку")
    def test_complete_order_flow_top_button(self, order_page):
        with allure.step("Инициализация страницы заказа"):
            order_page.open()

        with allure.step("Начало оформления заказа"):
            order_page.click_header_order_button()
        with allure.step("Заполнение формы Для кого самокат"):
            order_page.fill_personal_data()
        with allure.step("Заполнение формы Про аренду"):
            order_page.fill_rental_data()

        with allure.step("Подтверждение заказа"):
            assert order_page.confirm_order(), "Окно подтверждения заказа не отобразилось"


    @allure.feature("Заказ через нижнюю кнопку")
    @allure.story("Позитивный сценарий оформления")
    @allure.title("Проверка полного цикла заказа через нижнюю кнопку")
    def test_complete_order_flow_bottom_button(self, order_page):
        with allure.step("Инициализация страницы заказа"):
            order_page.open()

        with allure.step("Прокрутка и начало оформления"):
            order_page.scroll_to_button_bottom()
            order_page.click_element(MainPageLocators.ORDER_BUTTON_FOOTER)
        with allure.step("Заполнение формы Для кого самокат"):
            order_page.fill_personal_data_for_bottom()
        with allure.step("Заполнение формы Про аренду"):
            order_page.fill_rental_data_for_bottom()

        with allure.step("Подтверждение заказа"):
            assert order_page.confirm_order(), "Окно подтверждения заказа не отобразилось"


