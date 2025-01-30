import allure

from conftest import run_driver
from pages.header_tab import HeaderTab

@allure.title("Проверка переходов на сайте")
class TestSiteTransitions:

    @allure.title("Перейти на главную страницу, нажав на логотипа 'Самокат'")
    def test_click_on_scooter_logo_and_redirect_to_main_page(self, run_driver):
        header_tab = HeaderTab(run_driver).open_site()
        header_tab.click_on_scooter_logo()
        header_tab.check_redirect_to_main_page()

    @allure.title("Перейти на Дзен, нажав на логотоп 'Яндекс'")
    def test_click_on_yandex_logo_and_redirect_to_dzen(self, run_driver):
        header_tab = HeaderTab(run_driver).open_site()
        header_tab.click_on_yandex_logo()
        header_tab.check_redirect_to_yandex_dzen()