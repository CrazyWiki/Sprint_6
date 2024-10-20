import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import links
import locators.home_page_locators as loc
import locators.base_page_locators as locbase
import locators.order_page_locators as locorder
from pages.base_page import BasePage

class HomePage(BasePage):

    @allure.step('Переход по на домашнюю страницу и скроллинг')
    def get_url_and_scroll(self):
        self.driver.get(links.Links.home_page)
        element = self.driver.find_element(*loc.HomePageLocators.hp_question_test)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step('Нажатие на вопрос')
    def click_question(self, number_of_question):
        question = self.driver.find_element(*loc.HomePageLocators.hp_questions.get(number_of_question))
        question.click()

    @allure.step('Скроллинг')
    def scroll_to(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step('Скроллинг до кнопки заказа в теле страницы')
    def scroll_to_order_button(self):
        order_button = self.driver.find_element(*loc.HomePageLocators.hp_order_button_locator)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(order_button))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", order_button)

    @allure.step('Нажатие кнопки Заказать в Header')
    def click_top_order_button(self):
        return self.driver.find_element(*locbase.BasePageLocators.bp_order_button_locator).click()

    @allure.step('Нажатие на кнопку Заказать в теле странице')
    def click_bottom_order_button(self):
        return self.driver.find_element(*loc.HomePageLocators.hp_order_button_locator).click()
    def wait_for_load_first_order_form(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                locorder.OrderPageLocators.op_order_form_with_characteristics_text))
