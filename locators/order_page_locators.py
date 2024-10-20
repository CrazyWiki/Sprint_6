from selenium.webdriver.common.by import By


class OrderPageLocators:
    op_first_form_for_order = [By.XPATH, './/div[contains(@class,"Order_Content__bmtHS")]']
    op_order_form_with_characteristics_text = [By.XPATH, ".//div[text()='Для кого самокат']"]
    op_order_form_with_transport_characteristics_text = [By.XPATH, ".//div[(text()='Про аренду') and contains(@class,'Order_Header')]"]
    op_order_form_confirm = [By.XPATH, './/div[contains(@class,"Order_Text__2broi")]']

    op_form_order_completed_text = [By.XPATH, ".//div[contains(text(),'Номер заказа:')]"]

    op_first_name_input_locator = [By.XPATH, ".//input[@placeholder='* Имя']"]
    op_second_name_input_locator = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    op_address_input_locator = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
    op_metro_station_input_locator = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
    op_phone_number_input_locator = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]

    op_first_name_error_message_locator = [By.XPATH, ".//input[contains(@placeholder,'Имя')]/parent::div/div"]
    op_second_name_error_message_locator = [By.XPATH, ".//input[@placeholder='* Фамилия']/parent::div/div"]
    op_address_error_message_locator = [By.XPATH,
                                        ".//input[@placeholder='* Адрес: куда привезти заказ']/parent::div/div"]
    op_metro_station_error_message_locator = [By.XPATH, ".//input[@placeholder='* Станция "
                                                        "метро']/parent::div/parent::div/parent::div/div["
                                                        "@class!='select-search']"]
    op_phone_number_error_message_locator = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит "
                                                       "курьер']/parent::div/div"]

    @staticmethod
    def op_metro_hint_button(metro_name: str):
        return [By.XPATH, f".//button[div[text()='{metro_name}']]"]

    op_next_button_locator = [By.XPATH, ".//button[text()='Далее']"]
    op_data_input_locator = [By.XPATH, ".//input[contains(@placeholder,'* Когда привезти')]"]

    op_rent_period_input_locator = [By.XPATH, ".//span[@class='Dropdown-arrow']"]
    #op_rent_period_list_locator = [By.XPATH, ".//div[@class='Dropdown-option']"]
    op_choosing_color_checkbox_locator = [By.XPATH, ".//div[contains(text(),'Цвет')]/parent::div//input"]
    op_comments_for_courier_input_locator = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]
    op_order_button_locator = [By.XPATH, ".//button[text()='Заказать']"]
    op_back_button_locator = [By.XPATH, ".//button[text()='Назад']"]
    op_final_order_button_locator=[By.XPATH,".//button[text()='Назад']/parent::div/button[text()='Заказать']"]
    op_orden_acception_button_locator = [By.XPATH, ".//button[text()='Да' and contains(@class,'Button_Middle')]"]
    op_orden_no_acception_button_locator = [By.XPATH, ".//button[text()='Нет' and contains(@class,'Button_Inverted')]"]
    op_orden_finished_text_locator = [By.XPATH,
                                      ".//div[contains(@class,'Order_Text') and contains(text(),'Номер заказа')]"]
    op_observe_status_button_locator = [By.XPATH,
                                        ".//button[contains(@class,'Button_Button') and contains(text(),'Посмотреть "
                                        "статус')]"]
