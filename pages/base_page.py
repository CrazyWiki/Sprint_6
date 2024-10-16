import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import links
import locators.base_page_locators as locbase
from pages.home_page import HomePage


class BasePage(HomePage):
    @allure.step('Нажатие кнопки логотипа Самокат')
    def click_logo_button(self):
        self.driver.find_element(*locbase.BasePageLocators.bp_logo_button_locator).click()
    @allure.step('Нажатие кнопки Статус заказа в Header')
    def click_status_orden_button(self):
        self.driver.find_element(*locbase.BasePageLocators.bp_order_button_status_locator).click()
    @allure.step('Нажатие кнопки GO появляющейся после нажатия статуса заказа')
    def click_go_button(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locbase.BasePageLocators.bp_go_button_locator))
        self.driver.find_element(*locbase.BasePageLocators.bp_go_button_locator).click()

    @allure.step('Нажатие кнопки Яндекс')
    def click_yandex_button(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locbase.BasePageLocators.bp_yandex_button_locator))
        self.driver.find_element(*locbase.BasePageLocators.bp_yandex_button_locator).click()
    @allure.step('Ввод номера заказа после нажатия кнопки Статус заказа')
    def input_order_number(self, order_number):
        self.driver.find_element(*locbase.BasePageLocators.bp_field_for_insert_order_number_locator).send_keys(order_number)

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(links.Links.home_page))
    def wait_for_load_status_order_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(links.Links.order_status_page))

    @allure.step('Смена вкладки браузера')
    def change_tab(self, tab_num: int):
        return self.driver.switch_to.window(self.driver.window_handles[tab_num])

    def wait_url_load(self, time=10):
        return WebDriverWait(self.driver, time).until_not(expected_conditions.url_to_be('about:blank'))
