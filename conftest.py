import pytest
from selenium import webdriver
from pages.faq_page import FAQPage

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def faq_page(driver):
    page = FAQPage(driver)
    page.open()
    return page