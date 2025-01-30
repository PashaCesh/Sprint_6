class OrderPageLocators:

    #Поле для ввода "* Имя"
    INPUT_NAME_FIELD = '//input[@placeholder="* Имя"]'

    #Поле для ввода "* Фамилия"
    INPUT_SURNAME_FIELD = '//input[@placeholder="* Фамилия"]'

    #Поле для ввода "* Адрес: куда привезти заказ"
    INPUT_ADDRESS_FIELD = '//input[@placeholder="* Адрес: куда привезти заказ"]'

    #Поле для ввода станции метро
    INPUT_SUBWAY_STATION_FIELD = '//input[@class="select-search__input"]'

    #Элемент выпадающего списка при поиске станции метро
    SUBWAY_STATION_DROPDOWN_LIST = '//div[@class="select-search__select"]'

    #Поле для ввода "* Телефон: на него позвонит курьер"
    INPUT_PHONE_NUMBER_FIELD = '//input[@placeholder="* Телефон: на него позвонит курьер"]'

    #Кнопка "Далее"
    CONTINUE_BUTTON = '//button[text()="Далее"]'

    #Поле для ввода "* Когда привезти самокат"
    INPUT_DATE_FIELD = '//input[@placeholder="* Когда привезти самокат"]'

    #Поле "* Срок аренды"
    RENTAL_PERIOD_FIELD = '//span[@class="Dropdown-arrow"]'

    #Вариант "двое суток" в выпадающем списке
    TWO_DAYS_RENTAL_PERIOD_VARIANT = '//div[text()="двое суток"]'

    #Вариант "трое суток" в выпадающем списке
    THREE_DAYS_RENTAL_PERIOD_VARIANT = '//div[text()="трое суток"]'

    #Чекбокс "чёрный жемчуг"
    CHECKBOX_BLACK_PEARL = '//label[@for="black"]'

    #Чекбокс "серая безысходность"
    CHECKBOX_GRAY_HELPLESSNESS = '//label[@for="grey"]'

    #Поле для ввода "Комментарий для курьера"
    COMMENT_FOR_COURIER_FIELD = '//input[@placeholder="Комментарий для курьера"]'

    # Кнопка "Заказать"
    ORDER_BUTTON = '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]'

    # Кнопка "Да"
    CONFIRM_BUTTON = '//div[@class="Order_Buttons__1xGrp"]/button[text()="Да"]'

    #Заголовок "Заказ оформлен"
    HEADER_ORDER_STATUS = '//div[@class="Order_ModalHeader__3FDaJ"]'