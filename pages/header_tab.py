import allure

from constants import *
from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class HeaderTab(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = ORDER_PAGE_URL

    @allure.step("Кликнуть на логотоп 'Самокат' и проверить переход на главную страницу")
    def click_on_scooter_logo(self):
        self.click_on_element(HeaderLocators.scooter_logo)
        assert self.driver.current_url == URL

    @allure.step("Кликнуть на логотоп 'Яндекс' и проверить переход на Яндекс.Дзен")
    def click_on_yandex_logo(self):
        self.click_on_element(HeaderLocators.yandex_logo)
        self.switch_tab()
        assert self.find_element(HeaderLocators.yandex_search_field).is_displayed()
