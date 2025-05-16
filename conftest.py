import pytest
from selenium import webdriver
from pages.faq_page import FAQPage
from pages.order_page import OrderPage
import curl

@pytest.fixture
def base_url():
    return curl.base_url

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
    return page

