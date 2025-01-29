import pytest

from selenium import webdriver

@pytest.fixture
def run_driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()