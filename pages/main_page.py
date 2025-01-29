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
        self.click_on_element(MainPageLocators.accept_cookie_button)

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
            self.find_element(MainPageLocators.question_about_cost_in_dropdown_list).send_keys(Keys.PAGE_DOWN)
            self.click_on_question_field_in_dropdown_list(MainPageLocators.question_about_cost_in_dropdown_list)
            self.get_text_from_block(MainPageLocators.question_about_cost_block_with_text)
            self.verify_text_from_block(MainPageLocators.question_about_cost_block_with_text,
                                        TEXT_OF_THE_COST_QUESTION_BLOCK)
        elif question == 'Хочу сразу несколько самокатов! Так можно?':
            (self.find_element(MainPageLocators.question_about_multiple_scooters_in_dropdown_list)
             .send_keys(Keys.PAGE_DOWN))
            (self.click_on_question_field_in_dropdown_list
             (MainPageLocators.question_about_multiple_scooters_in_dropdown_list))
            self.get_text_from_block(MainPageLocators.question_about_multiple_scooters_block_with_text)
            self.verify_text_from_block(MainPageLocators.question_about_multiple_scooters_block_with_text,
                                        TEXT_OF_MULTIPLE_SCOOTERS_QUESTION_BLOCK)
        elif question == 'Как рассчитывается время аренды?':
            (self.find_element(MainPageLocators.question_about_calculating_time_rent_in_dropdown_list)
             .send_keys(Keys.PAGE_DOWN))
            (self.click_on_question_field_in_dropdown_list
             (MainPageLocators.question_about_calculating_time_rent_in_dropdown_list))
            self.get_text_from_block(MainPageLocators.question_about_calculating_time_rent_block_with_text)
            self.verify_text_from_block(MainPageLocators.question_about_calculating_time_rent_block_with_text,
                                        TEXT_OF_CALCULATING_TIME_RENT_QUESTION_BLOCK)
        elif question == 'Можно ли заказать самокат прямо на сегодня?':
            self.find_element(MainPageLocators.question_about_today_order_in_dropdown_list).send_keys(Keys.PAGE_DOWN)
            self.click_on_question_field_in_dropdown_list(MainPageLocators.question_about_today_order_in_dropdown_list)
            self.get_text_from_block(MainPageLocators.question_about_today_order_block_with_text)
            self.verify_text_from_block(MainPageLocators.question_about_today_order_block_with_text,
                                        TEXT_OF_TODAY_ORDER_QUESTION_BLOCK)
        elif question == 'Можно ли продлить заказ или вернуть самокат раньше?':
            self.find_element(MainPageLocators.question_about_extend_order_in_dropdown_list).send_keys(Keys.PAGE_DOWN)
            self.click_on_question_field_in_dropdown_list(MainPageLocators.question_about_extend_order_in_dropdown_list)
            self.get_text_from_block(MainPageLocators.question_about_extend_order_block_with_text)
            self.verify_text_from_block(MainPageLocators.question_about_extend_order_block_with_text,
                                        TEXT_OF_EXTEND_ORDER_QUESTION_BLOCK)
        elif question == 'Вы привозите зарядку вместе с самокатом?':
            self.find_element(MainPageLocators.question_about_charger_in_dropdown_list).send_keys(Keys.PAGE_DOWN)
            self.click_on_question_field_in_dropdown_list(MainPageLocators.question_about_charger_in_dropdown_list)
            self.get_text_from_block(MainPageLocators.question_about_charger_block_with_text)
            self.verify_text_from_block(MainPageLocators.question_about_charger_block_with_text,
                                        TEXT_OF_CHARGER_QUESTION_BLOCK)
        elif question == 'Можно ли отменить заказ?':
            (self.find_element(MainPageLocators.question_about_canceling_order_in_dropdown_list)
             .send_keys(Keys.PAGE_DOWN))
            (self.click_on_question_field_in_dropdown_list
             (MainPageLocators.question_about_canceling_order_in_dropdown_list))
            self.get_text_from_block(MainPageLocators.question_about_canceling_order_block_with_text)
            self.verify_text_from_block(MainPageLocators.question_about_canceling_order_block_with_text,
                                        TEXT_OF_CANCELING_ORDER_QUESTION_BLOCK)
        else:
            (self.find_element(MainPageLocators.question_about_long_distance_order_in_dropdown_list)
             .send_keys(Keys.PAGE_DOWN))
            (self.click_on_question_field_in_dropdown_list
             (MainPageLocators.question_about_long_distance_order_in_dropdown_list))
            self.get_text_from_block(MainPageLocators.question_about_long_distance_order_block_with_text)
            self.verify_text_from_block(MainPageLocators.question_about_long_distance_order_block_with_text,
                                        TEXT_OF_LONG_DISTANCE_QUESTION_BLOCK)

    @allure.step("Нажимаем на кнопку 'Заказать'")
    def click_on_order_buttons(self, button):
        if button == 'Вверху':
            self.click_on_element(MainPageLocators.order_button_header)
        else:
            self.click_on_element(MainPageLocators.order_button_root)
        return OrderPage(self.driver).validate_on_page()
