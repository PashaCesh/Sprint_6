class OrderPageLocators:

    #Поле для ввода "* Имя"
    input_name_field = '//input[@placeholder="* Имя"]'

    #Поле для ввода "* Фамилия"
    input_surname_field = '//input[@placeholder="* Фамилия"]'

    #Поле для ввода "* Адрес: куда привезти заказ"
    input_address_field = '//input[@placeholder="* Адрес: куда привезти заказ"]'

    #Поле для ввода станции метро
    input_subway_station_field = '//input[@class="select-search__input"]'

    #Элемент выпадающего списка при поиске станции метро
    subway_station_dropdown_list = '//div[@class="select-search__select"]'

    #Поле для ввода "* Телефон: на него позвонит курьер"
    input_phone_number_field = '//input[@placeholder="* Телефон: на него позвонит курьер"]'

    #Кнопка "Далее"
    continue_button = '//button[text()="Далее"]'

    #Поле для ввода "* Когда привезти самокат"
    input_date_field = '//input[@placeholder="* Когда привезти самокат"]'

    #Поле "* Срок аренды"
    rental_period_field = '//span[@class="Dropdown-arrow"]'

    #Вариант "двое суток" в выпадающем списке
    two_days_rental_period_variant = '//div[text()="двое суток"]'

    #Вариант "трое суток" в выпадающем списке
    three_days_rental_period_variant = '//div[text()="трое суток"]'

    #Чекбокс "чёрный жемчуг"
    checkbox_black_pearl = '//label[@for="black"]'

    #Чекбокс "серая безысходность"
    checkbox_gray_hopelessness = '//label[@for="grey"]'

    #Поле для ввода "Комментарий для курьера"
    comment_for_courier_field = '//input[@placeholder="Комментарий для курьера"]'

    # Кнопка "Заказать"
    order_button = '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]'

    # Кнопка "Да"
    confirm_button = '//div[@class="Order_Buttons__1xGrp"]/button[text()="Да"]'

    #Заголовок "Заказ оформлен"
    header_order_status = '//div[@class="Order_ModalHeader__3FDaJ"]'