import allure

from constants import *
from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class HeaderTab(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = ORDER_PAGE_URL

    @allure.step("Кликнуть на логотоп 'Самокат'")
    def click_on_scooter_logo(self):
        self.click_on_element(HeaderLocators.SCOOTER_LOGO)

    @allure.step("Проверить переход на главную страницу")
    def check_redirect_to_main_page(self):
        assert self.driver.current_url == URL

    @allure.step("Кликнуть на логотоп 'Яндекс'")
    def click_on_yandex_logo(self):
        self.click_on_element(HeaderLocators.YANDEX_LOGO)
        self.switch_tab()

    @allure.step("Проверить переход на Яндекс.Дзен")
    def check_redirect_to_yandex_dzen(self):
        assert self.find_element(HeaderLocators.YANDEX_SEARCH_FIELD).is_displayed()
        assert self.driver.current_url == YANDEX_URL