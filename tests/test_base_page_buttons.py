import allure
import links
from pages.base_page import BasePage

class TestBasePageButtons:

    @allure.parent_suite('Функциональность верхнего меню Header')
    @allure.suite('Нажатие кнопки Логотипа')
    @allure.title('Позитивная проверка переадресации на домашнюю страницу при нажатии на логотип Самокат')
    @allure.description(
        'Сначала происходит переход на страницу описания заказа, затем поиск и нажатие на кнопку логотипа. Затем загрузка домашней страницы и проверка')
    def test_logo_button(self,driver):

        base_page = BasePage(driver)
        base_page.get_url()
        base_page.click_status_orden_button()
        base_page.input_order_number(891760)
        base_page.click_go_button()
        base_page.click_logo_button()
        base_page.wait_for_load_home_page()
        assert driver.current_url==links.Links.home_page

    @allure.suite('Нажатие кнопки Яндекс')
    @allure.title(
        'Позитивная проверка переадресации на страницу яндекс дзен при нажатии на кнопку яндекс рядом с логотипом Самокат')
    @allure.description(
        'На домашней страницы происзодит нажатие на кнопку Яндекс и открытие в соседней вкладке домашней страницы яндекс. Проверка адреса url на соответствие')
    def test_yandex_button(self,driver):
        base_page = BasePage(driver)
        base_page.get_url()
        base_page.click_yandex_button()
        base_page.change_tab(1)
        base_page.wait_url_load()
        assert 'yandex.ru' in driver.current_url