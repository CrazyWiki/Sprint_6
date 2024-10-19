from selenium.webdriver.common.by import By

class BasePageLocators:
    bp_yandex_button_locator = [By.XPATH, ".//a[img[@src='/assets/ya.svg']]"]
    bp_logo_button_locator = [By.XPATH, "//a[img[@alt='Scooter']]"]
    bp_order_button_locator = [By.XPATH, './/div[starts-with(@class, "Header")]/button[text()="Заказать"]']
    bp_order_button_status_locator = [By.XPATH, ".//button[contains(@class,'Header_Link') and text()='Статус заказа']"]
    bp_cookies_accept_button_locator = [By.XPATH, ".//button[text()='да все привыкли']"]

    bp_field_for_insert_order_number_locator = [By.XPATH,".//input[contains(@placeholder,'Введите номер заказа')]"]
    bp_go_button_locator = [By.XPATH,".//button[text()='Go!']"]
