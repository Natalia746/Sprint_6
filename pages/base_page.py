# base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    def __init__(self, driver: WebDriver, base_url, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.base_url = base_url

    def open(self):
        self.driver.get(self.base_url)

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def fill_field(self, locator, text):
        field = self.wait.until(EC.visibility_of_element_located(locator))
        field.clear()
        field.send_keys(text)

    def scroll_to_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_element_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_new_window(self, window_index):
        self.driver.switch_to.window(self.driver.window_handles[window_index])

    def close_current_window(self):
        self.driver.close()

    def wait_for_number_of_windows(self, expected_number, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) == expected_number
        )

    def wait_for_url_contains(self, text, timeout=15):
        """
        Ожидает, пока URL не будет содержать указанный текст.
        """
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(text)
        )