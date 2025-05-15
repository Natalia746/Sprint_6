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