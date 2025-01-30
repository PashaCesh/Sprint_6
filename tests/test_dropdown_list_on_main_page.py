import allure
import pytest

from constants import *
from pages.main_page import MainPage


@allure.title("Проверка текста в блоках вопросов в выпадающем списке в разделе «Вопросы о важном»")
class TestDropdownListOnMainPage:

    @allure.title("Проверка текста в блоке по нажатию на вопрос")
    @pytest.mark.parametrize('question',LIST_OF_QUESTIONS)
    def test_click_and_check_text_of_question(self, run_driver, question):
        main_page = MainPage(run_driver).open_site()
        main_page.click_on_accepting_cookie_button()
        main_page.click_and_check_question_text_in_dropdown_list(question)