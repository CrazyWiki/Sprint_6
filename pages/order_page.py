import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import links
import locators.order_page_locators as locorder
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Переход на страницу оформления заказа')
    def get_url_order_page(self):
        self.driver.get(links.Links.order_page)

    @allure.step('Ввод имени')
    def input_name(self, name):
        self.driver.find_element(*locorder.OrderPageLocators.op_first_name_input_locator).send_keys(name)

    @allure.step('Ввод фамилии')
    def input_surname(self, surname):
        self.driver.find_element(*locorder.OrderPageLocators.op_second_name_input_locator).send_keys(surname)

    @allure.step('Ввод адреса')
    def input_address(self, address):
        self.driver.find_element(*locorder.OrderPageLocators.op_address_input_locator).send_keys(address)

    @allure.step('Ввод метро')
    def input_metro(self, metro_name):
        self.driver.find_element(*locorder.OrderPageLocators.op_metro_station_input_locator).send_keys(metro_name)
        self.driver.find_element(*locorder.OrderPageLocators.op_metro_hint_button(metro_name)).click()

    @allure.step('Ввод номера телефона')
    def input_phone_number(self, phone_number):
        self.driver.find_element(*locorder.OrderPageLocators.op_phone_number_input_locator).send_keys(phone_number)

    @allure.step('Нажатие кнопки Далее для начала заполнения данных о деталях заказа')
    def click_next_button(self):
        self.driver.find_element(*locorder.OrderPageLocators.op_next_button_locator).click()

    @allure.step('Ввод даты заказа')
    def input_data_list(self, data):
        self.driver.find_element(*locorder.OrderPageLocators.op_data_input_locator).send_keys(data)

    @allure.step('Ввод периода аренды')
    def input_rent_period(self, rent_period: str):
        self.driver.find_element(*locorder.OrderPageLocators.op_rent_period_input_locator).click()
        desired_option = self.driver.find_element(By.XPATH, f".//div[text()='{rent_period}']")
        desired_option.click()

    @allure.step('Ввод цветы')
    def choose_color_checkbox(self, color: str):
        color_option = self.driver.find_element(By.XPATH, f".//div//input[contains(@id,'{color}')]")
        color_option.click()

    @allure.step('Ввод комментария')
    def input_comments_for_courier(self, comment):
        self.driver.find_element(*locorder.OrderPageLocators.op_comments_for_courier_input_locator).send_keys(comment)

    @allure.step('Нажатие кнопки заказать')
    def click_order_button(self):
        self.driver.find_element(*locorder.OrderPageLocators.op_order_button_locator).click()

    @allure.step('Нажатие кнопки завершения заказа')
    def click_final_order_button(self):
        self.driver.find_element(*locorder.OrderPageLocators.op_final_order_button_locator).click()

    @allure.step('Нажатие кнопки назад')
    def clik_back_button(self):
        self.driver.find_element(*locorder.OrderPageLocators.op_back_button_locator).click()

    @allure.step('Подтверждение заказа')
    def click_orden_aception_button(self):
        self.driver.find_element(*locorder.OrderPageLocators.op_orden_acception_button_locator).click()

    @allure.step('Заполнение данных клиента')
    def add_client_data(self, name, surname, address, metro, phone_number):
        self.input_name(name)
        self.input_surname(surname)
        self.input_address(address)
        self.input_metro(metro)
        self.input_phone_number(phone_number)
        self.click_next_button()

    @allure.step('Заполнение данных вренды')
    def add_order_data(self, data, rent_period, color, comment):
        self.input_data_list(data)
        self.input_rent_period(rent_period)
        self.choose_color_checkbox(color)
        self.input_comments_for_courier(comment)
        self.click_final_order_button()

    @allure.step('Получение номера заказа из формы подтверждения')
    def take_number_from_form(self):
        order_text = self.driver.find_element(*locorder.OrderPageLocators.op_form_order_completed_text).text
        number = ""
        for char in order_text:
            if char.isdigit():
                number += char
            elif number:
                break
        return number

    @allure.step('Получение текста из формы подтверждения')
    def take_text_from_form(self):
        order_text = self.driver.find_element(*locorder.OrderPageLocators.op_form_order_completed_text).text
        return order_text

    @allure.step('Нажатие кнопки просмотра заказа')
    def click_observe_status_button(self):
        self.driver.find_element(*locorder.OrderPageLocators.op_observe_status_button_locator).click()

    def wait_for_load_order_form_with_characteristics(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                locorder.OrderPageLocators.op_order_form_with_transport_characteristics_text))

    def wait_for_load_form_order_completed(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(locorder.OrderPageLocators.op_form_order_completed_text))
        WebDriverWait(self.driver, 3)

    def wait_for_load_order_status_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(links.Links.order_status_page))

    def wait_for_load_first_order_form(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                locorder.OrderPageLocators.op_order_form_with_characteristics_text))
