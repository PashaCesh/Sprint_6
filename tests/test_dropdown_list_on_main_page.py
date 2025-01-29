import allure

from constants import *
from pages.main_page import MainPage


@allure.title("Проверка текста в блоках вопросов в выпадающем списке в разделе «Вопросы о важном»")
class TestDropdownListOnMainPage:

    @allure.title("Проверка текста в блоке по нажатию на вопрос 'Сколько это стоит? И как оплатить?'")
    def test_click_and_check_text_of_question_about_cost(self, run_driver):
        main_page = MainPage(run_driver).open_site()
        main_page.click_on_accepting_cookie_button()
        main_page.click_and_check_question_text_in_dropdown_list(TEXT_OF_THE_COST_QUESTION)

    @allure.title("Проверка текста в блоке по нажатию на вопрос 'Хочу сразу несколько самокатов! Так можно?'")
    def test_click_and_check_text_of_question_about_multiple_scooters(self, run_driver):
        main_page = MainPage(run_driver).open_site()
        main_page.click_on_accepting_cookie_button()
        main_page.click_and_check_question_text_in_dropdown_list(TEXT_OF_MULTIPLE_SCOOTERS_QUESTION)

    @allure.title("Проверка текста в блоке по нажатию на вопрос 'Как рассчитывается время аренды?'")
    def test_click_and_check_text_of_question_about_calculating_time_rent(self, run_driver):
        main_page = MainPage(run_driver).open_site()
        main_page.click_on_accepting_cookie_button()
        main_page.click_and_check_question_text_in_dropdown_list(TEXT_OF_CALCULATING_TIME_RENT_QUESTION)

    @allure.title("Проверка текста в блоке по нажатию на вопрос 'Можно ли заказать самокат прямо на сегодня?'")
    def test_click_and_check_text_of_question_about_today_order(self, run_driver):
        main_page = MainPage(run_driver).open_site()
        main_page.click_on_accepting_cookie_button()
        main_page.click_and_check_question_text_in_dropdown_list(TEXT_OF_TODAY_ORDER_QUESTION)

    @allure.title("Проверка текста в блоке по нажатию на вопрос 'Можно ли продлить заказ или вернуть самокат раньше?'")
    def test_click_and_check_text_of_question_about_extend_order(self, run_driver):
        main_page = MainPage(run_driver).open_site()
        main_page.click_on_accepting_cookie_button()
        main_page.click_and_check_question_text_in_dropdown_list(TEXT_OF_EXTEND_ORDER_QUESTION)

    @allure.title("Проверка текста в блоке по нажатию на вопрос 'Вы привозите зарядку вместе с самокатом?'")
    def test_click_and_check_text_of_question_about_charger(self, run_driver):
        main_page = MainPage(run_driver).open_site()
        main_page.click_on_accepting_cookie_button()
        main_page.click_and_check_question_text_in_dropdown_list(TEXT_OF_CHARGER_QUESTION)

    @allure.title("Проверка текста в блоке по нажатию на вопрос 'Можно ли отменить заказ?'")
    def test_click_and_check_text_of_question_about_canceling_order(self, run_driver):
        main_page = MainPage(run_driver).open_site()
        main_page.click_on_accepting_cookie_button()
        main_page.click_and_check_question_text_in_dropdown_list(TEXT_OF_CANCELING_ORDER_QUESTION)

    @allure.title("Проверка текста в блоке по нажатию на вопрос 'Я жизу за МКАДом, привезёте?'")
    def test_click_and_check_text_of_question_about_long_distance_order(self, run_driver):
        main_page = MainPage(run_driver).open_site()
        main_page.click_on_accepting_cookie_button()
        main_page.click_and_check_question_text_in_dropdown_list(TEXT_OF_LONG_DISTANCE_QUESTION)