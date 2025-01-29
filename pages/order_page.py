import allure

from constants import ORDER_PAGE_URL
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Проверка, что мы на странице для создания заказа")
    def validate_on_page(self):
        assert ORDER_PAGE_URL == self.driver.current_url
        return self

    @allure.step("Написать имя в поле '* Имя'")
    def enter_name(self,name):
        self.input_data(OrderPageLocators.input_name_field, name)

    @allure.step("Написать фамилию в поле '* Фамилия'")
    def enter_surname(self, surname):
        self.input_data(OrderPageLocators.input_surname_field, surname)

    @allure.step("Написать адрес в поле '* Адрес: куда привезти заказ'")
    def enter_address(self, address):
        self.input_data(OrderPageLocators.input_address_field, address)

    @allure.step("Ввести станцию метро в поле '* Станция метро'")
    def enter_subway_station(self, subway_station):
        self.input_data(OrderPageLocators.input_subway_station_field, subway_station)

    @allure.step("Выбрать станцию метро из выпадающего списка")
    def click_on_station_from_dropdown_list(self):
        self.click_on_element(OrderPageLocators.subway_station_dropdown_list)

    @allure.step("Написать название станции и выбрать ее из списка")
    def enter_and_select_subway_station(self, subway_station):
        self.enter_subway_station(subway_station)
        self.click_on_station_from_dropdown_list()

    @allure.step("Написать телефон в поле '* Телефон: на него позвонит курьер'")
    def enter_phone_number(self, phone_number):
        self.input_data(OrderPageLocators.input_phone_number_field, phone_number)

    @allure.step("Нажать на кнопку 'Далее'")
    def click_on_continue_button(self):
        self.click_on_element(OrderPageLocators.continue_button)

    @allure.step("Заполнить все поля на первой странице заказа")
    def enter_all_data_on_first_order_page(self,name,surname,address,subway_station,phone_number):
        self.enter_name(name)
        self.enter_surname(surname)
        self.enter_address(address)
        self.enter_and_select_subway_station(subway_station)
        self.enter_phone_number(phone_number)
        self.click_on_continue_button()

    @allure.step("Ввести дату в поле 'Когда привезти самокат'")
    def enter_date_order(self, date_order):
        self.input_data(OrderPageLocators.input_date_field, date_order)

    @allure.step("Нажать на поле поле '* Срок аренды'")
    def click_on_rental_period_field(self):
        self.click_on_element(OrderPageLocators.rental_period_field)

    @allure.step("Выбрать количество дней аренды")
    def click_on_variant_rental_period(self, variant_rental_period):
        if variant_rental_period == 'двое суток':
            self.click_on_element(OrderPageLocators.two_days_rental_period_variant)
        else:
            self.click_on_element(OrderPageLocators.three_days_rental_period_variant)

    @allure.step("Выбрать срок аренды")
    def click_and_select_rental_period(self, variant_rental_period):
        self.click_on_rental_period_field()
        self.click_on_variant_rental_period(variant_rental_period)

    @allure.step("Выбрать вариант чекбокса цвета самоката")
    def click_on_checkbox(self, checkbox):
        if checkbox == 'Чёрный':
            self.click_on_element(OrderPageLocators.checkbox_black_pearl)
        else:
            self.click_on_element(OrderPageLocators.checkbox_gray_hopelessness)

    @allure.step("Написать комментарий в поле 'Комментарий для курьера'")
    def enter_comment_for_courier(self, comment):
        self.input_data(OrderPageLocators.comment_for_courier_field, comment)

    @allure.step("Нажать на кнопку 'Заказать'")
    def click_on_order_button(self):
        self.click_on_element(OrderPageLocators.order_button)

    @allure.step("Нажать на кнопку 'Да'")
    def click_on_confirm_button(self):
        self.click_on_element(OrderPageLocators.confirm_button)

    @allure.step("Заполнить все поля на второй странице заказа и оформить заказ")
    def enter_all_data_on_second_order_page(self,date_order,variant_rental_period,checkbox,comment):
        self.enter_date_order(date_order)
        self.click_and_select_rental_period(variant_rental_period)
        self.click_on_checkbox(checkbox)
        self.enter_comment_for_courier(comment)
        self.click_on_order_button()
        self.click_on_confirm_button()

    @allure.step("Проверить видимость окошко об успешном заказе самоката")
    def verify_header(self):
        assert self.find_element(OrderPageLocators.header_order_status).is_displayed()
