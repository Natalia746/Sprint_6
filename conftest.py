import pytest
from selenium import webdriver
from pages.faq_page import FAQPage
from pages.order_page import OrderPage
from curl import *

@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def faq_page(driver, base_url):
    page = FAQPage(driver, base_url)
    page.open()
    return page

@pytest.fixture
def order_page(driver, base_url):
    page = OrderPage(driver, base_url)
    yield page
    # Автоматический возврат к исходному окну после теста
    if len(driver.window_handles) > 1:
        page.switch_to_default_window()

