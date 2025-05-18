import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import Keys
from curl import *

class BasePage:

    def __init__(self, driver: WebDriver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.base_url = BASE_URL

    @allure.step("Открыть url главной страницы")
    def open(self):
        self.driver.get(self.base_url)

    @allure.step("Нажать на элемент")
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Заполнить поле")
    def fill_field(self, locator, text):
        field = self.wait.until(EC.visibility_of_element_located(locator))
        field.clear()
        field.send_keys(text)

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Получить текст элемента")
    def get_element_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    @allure.step("Проверка видимости элемента")
    def is_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Получить текущий url")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self, window_index):
        self.driver.switch_to.window(self.driver.window_handles[window_index])



    @allure.step("Ожидание открытия {expected_number} окон/вкладок")
    def wait_for_number_of_windows(self, expected_number, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) == expected_number
        )

    @allure.step("Ожидание появления указанного текста в url")
    def wait_for_url_contains(self, text, timeout=15):

        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(text)
        )

    @allure.step("Ожидание невидимости элемента")
    def wait_for_element_invisibility(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Нажать Enter")
    def press_enter(self, locator):
        element = self.is_element_visible(locator)
        element.send_keys(Keys.ENTER)

    @allure.step("Вернуться к исходному окну")
    def switch_to_default_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])