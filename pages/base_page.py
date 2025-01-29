from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from constants import URL


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = URL

    def open_site(self):
        self.driver.get(self.url)
        return self

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located((By.XPATH, locator)),
                                                      message=f'Could not to find element {locator}')

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located((By.XPATH, locator)),
                                                      message=f'Could not to find elements {locator}')

    def click_on_element(self, locator):
        self.driver.find_element(By.XPATH, locator).click()

    def input_data(self, locator, data):
        self.driver.find_element(By.XPATH, locator).send_keys(data)

    def switch_tab(self, time=10):
        wait = WebDriverWait(self.driver, time)
        wait.until(ec.number_of_windows_to_be(2))
        all_windows = self.driver.window_handles
        new_tab_handle = all_windows[-1]
        self.driver.switch_to.window(new_tab_handle)
