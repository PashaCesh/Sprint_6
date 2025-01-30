import allure
import pytest

from pages.main_page import MainPage
from constants import *


@allure.title("Создание заказа")
class TestOrderScooter:

    @allure.title("Создание заказа на аренду самоката")
    @pytest.mark.parametrize('button,name,surname,address,subway_station,phone_number,date_order,variant_rental_period,'
                             'checkbox,comment',
                             [
                                 [HEADER_BUTTON_PATH,NAME_FIRST,SURNAME_FIRST,ADDRESS_FIRST,SUBWAY_STATION_FIRST,
                                  PHONE_NUMBER_FIRST,DATE_FIRST,TWO_DAYS_RENT,BLACK_CHECKBOX,COMMENT_FIRST],
                                 [ROOT_BUTTON_PATH,NAME_SECOND,SURNAME_SECOND,ADDRESS_SECOND,SUBWAY_STATION_SECOND,
                                  PHONE_NUMBER_SECOND,DATE_SECOND,THREE_DAYS_RENT,GREY_CHECKBOX,COMMENT_SECOND]])
    def test_create_order(self,run_driver,button,name,surname,address,subway_station,phone_number,date_order,
                          variant_rental_period,checkbox,comment):
        main_page = MainPage(run_driver).open_site()
        main_page.click_on_accepting_cookie_button()
        order_page = main_page.click_on_order_buttons(button)
        order_page.enter_all_data_on_first_order_page(name,surname,address,subway_station,phone_number)
        order_page.enter_all_data_on_second_order_page(date_order,variant_rental_period,checkbox,comment)
        order_page.verify_header()