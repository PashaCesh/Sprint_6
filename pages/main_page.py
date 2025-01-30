import allure
from selenium.webdriver import Keys

from locators.main_page_locators import MainPageLocators
from constants import *
from pages.base_page import BasePage
from pages.order_page import OrderPage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажимаем кнопку 'да все привыкли', чтобы принять куки")
    def click_on_accepting_cookie_button(self):
        self.click_on_element(MainPageLocators.ACCEPT_COOKIE_BUTTON)

    @allure.step("Нажимаем кнопку с вопросом")
    def click_on_question_field_in_dropdown_list(self, question_field):
        self.click_on_element(question_field)

    @allure.step("Достаем текст из открывающегося блока")
    def get_text_from_block(self, block_with_text):
        return self.find_element(block_with_text).text

    @allure.step("Проверяем, что текст соответствует ожидаемому")
    def verify_text_from_block(self, block_with_text, expected_title):
        assert self.get_text_from_block(block_with_text).strip() == expected_title

    @allure.step("Нажимаем на вопрос в выпадающем списке и проверяем текст открывающегося блока")
    def click_and_check_question_text_in_dropdown_list(self, question):
        if question== 'Сколько это стоит? И как оплатить?':
            self.find_element(MainPageLocators.QUESTION_ABOUT_COST_IN_DROPDOWN_LIST).send_keys(Keys.PAGE_DOWN)
            self.click_on_question_field_in_dropdown_list(MainPageLocators.QUESTION_ABOUT_COST_IN_DROPDOWN_LIST)
            self.get_text_from_block(MainPageLocators.QUESTION_ABOUT_COST_BLOCK_WITH_TEXT)
            self.verify_text_from_block(MainPageLocators.QUESTION_ABOUT_COST_BLOCK_WITH_TEXT,
                                        TEXT_OF_THE_COST_QUESTION_BLOCK)
        elif question == 'Хочу сразу несколько самокатов! Так можно?':
            (self.find_element(MainPageLocators.QUESTION_ABOUT_MULTIPLE_SCOOTERS_IN_DROPDOWN_LIST)
             .send_keys(Keys.PAGE_DOWN))
            (self.click_on_question_field_in_dropdown_list
             (MainPageLocators.QUESTION_ABOUT_MULTIPLE_SCOOTERS_IN_DROPDOWN_LIST))
            self.get_text_from_block(MainPageLocators.QUESTION_ABOUT_MULTIPLE_SCOOTERS_BLOCK_WITH_TEXT)
            self.verify_text_from_block(MainPageLocators.QUESTION_ABOUT_MULTIPLE_SCOOTERS_BLOCK_WITH_TEXT,
                                        TEXT_OF_MULTIPLE_SCOOTERS_QUESTION_BLOCK)
        elif question == 'Как рассчитывается время аренды?':
            (self.find_element(MainPageLocators.QUESTION_ABOUT_CALCULATING_TIME_RENT_IN_DROPDOWN_LIST)
             .send_keys(Keys.PAGE_DOWN))
            (self.click_on_question_field_in_dropdown_list
             (MainPageLocators.QUESTION_ABOUT_CALCULATING_TIME_RENT_IN_DROPDOWN_LIST))
            self.get_text_from_block(MainPageLocators.QUESTION_ABOUT_CALCULATING_TIME_RENT_BLOCK_WITH_TEXT)
            self.verify_text_from_block(MainPageLocators.QUESTION_ABOUT_CALCULATING_TIME_RENT_BLOCK_WITH_TEXT,
                                        TEXT_OF_CALCULATING_TIME_RENT_QUESTION_BLOCK)
        elif question == 'Можно ли заказать самокат прямо на сегодня?':
            self.find_element(MainPageLocators.QUESTION_ABOUT_TODAY_ORDER_IN_DROPDOWN_LIST).send_keys(Keys.PAGE_DOWN)
            self.click_on_question_field_in_dropdown_list(MainPageLocators.QUESTION_ABOUT_TODAY_ORDER_IN_DROPDOWN_LIST)
            self.get_text_from_block(MainPageLocators.QUESTION_ABOUT_TODAY_ORDER_BLOCK_WITH_TEXT)
            self.verify_text_from_block(MainPageLocators.QUESTION_ABOUT_TODAY_ORDER_BLOCK_WITH_TEXT,
                                        TEXT_OF_TODAY_ORDER_QUESTION_BLOCK)
        elif question == 'Можно ли продлить заказ или вернуть самокат раньше?':
            self.find_element(MainPageLocators.QUESTION_ABOUT_EXTEND_ORDER_IN_DROPDOWN_LIST).send_keys(Keys.PAGE_DOWN)
            self.click_on_question_field_in_dropdown_list(MainPageLocators.QUESTION_ABOUT_EXTEND_ORDER_IN_DROPDOWN_LIST)
            self.get_text_from_block(MainPageLocators.QUESTION_ABOUT_EXTEND_ORDER_BLOCK_WITH_TEXT)
            self.verify_text_from_block(MainPageLocators.QUESTION_ABOUT_EXTEND_ORDER_BLOCK_WITH_TEXT,
                                        TEXT_OF_EXTEND_ORDER_QUESTION_BLOCK)
        elif question == 'Вы привозите зарядку вместе с самокатом?':
            self.find_element(MainPageLocators.QUESTION_ABOUT_CHARGER_IN_DROPDOWN_LIST).send_keys(Keys.PAGE_DOWN)
            self.click_on_question_field_in_dropdown_list(MainPageLocators.QUESTION_ABOUT_CHARGER_IN_DROPDOWN_LIST)
            self.get_text_from_block(MainPageLocators.QUESTION_ABOUT_CHARGER_BLOCK_WITH_TEXT)
            self.verify_text_from_block(MainPageLocators.QUESTION_ABOUT_CHARGER_BLOCK_WITH_TEXT,
                                        TEXT_OF_CHARGER_QUESTION_BLOCK)
        elif question == 'Можно ли отменить заказ?':
            (self.find_element(MainPageLocators.QUESTION_ABOUT_CANCELING_ORDER_IN_DROPDOWN_LIST)
             .send_keys(Keys.PAGE_DOWN))
            (self.click_on_question_field_in_dropdown_list
             (MainPageLocators.QUESTION_ABOUT_CANCELING_ORDER_IN_DROPDOWN_LIST))
            self.get_text_from_block(MainPageLocators.QUESTION_ABOUT_CANCELING_ORDER_BLOCK_WITH_TEXT)
            self.verify_text_from_block(MainPageLocators.QUESTION_ABOUT_CANCELING_ORDER_BLOCK_WITH_TEXT,
                                        TEXT_OF_CANCELING_ORDER_QUESTION_BLOCK)
        else:
            (self.find_element(MainPageLocators.QUESTION_ABOUT_LONG_DISTANCE_ORDER_IN_DROPDOWN_LIST)
             .send_keys(Keys.PAGE_DOWN))
            (self.click_on_question_field_in_dropdown_list
             (MainPageLocators.QUESTION_ABOUT_LONG_DISTANCE_ORDER_IN_DROPDOWN_LIST))
            self.get_text_from_block(MainPageLocators.QUESTION_ABOUT_LONG_DISTANCE_ORDER_BLOCK_WITH_TEXT)
            self.verify_text_from_block(MainPageLocators.QUESTION_ABOUT_LONG_DISTANCE_ORDER_BLOCK_WITH_TEXT,
                                        TEXT_OF_LONG_DISTANCE_QUESTION_BLOCK)

    @allure.step("Нажимаем на кнопку 'Заказать'")
    def click_on_order_buttons(self, button):
        if button == 'Вверху':
            self.click_on_element(MainPageLocators.ORDER_BUTTON_HEADER)
        else:
            self.click_on_element(MainPageLocators.ORDER_BUTTON_ROOT)
        return OrderPage(self.driver).validate_on_page()
