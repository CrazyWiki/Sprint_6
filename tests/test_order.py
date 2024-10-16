import allure
import pytest
from links import Links
from pages.home_page import HomePage
from pages.order_page import OrderPage
from data import OrderPageData

class TestOrder:
    @allure.title('Проверка точки входа на страницу заказа находящейся в Header')
    @allure.description('Поиск и нажатие кнопки Заказать в верхней панели сайта и ожидание перехода на страницу заказа')
    def test_verificacion_entry_point_top_button(self,driver):
        home_page = HomePage(driver)
        home_page.get_url()
        home_page.click_top_order_button()
        home_page.wait_for_load_first_order_form()
        assert driver.current_url ==Links.order_page

    @allure.title('Проверка точки входа на страницу заказа находящейся в теле страницы')
    @allure.description('Поиск и нажатие кнопки Заказать и ожидание перехода на страницу заказа')
    def test_verificacion_entry_point_home_page_button(self, driver):
        home_page = HomePage(driver)
        home_page.get_url()
        home_page.cookie_accept_click()
        home_page.scroll_to_order_button()
        home_page.click_bottom_order_button()
        home_page.wait_for_load_first_order_form()
        assert driver.current_url==Links.order_page

    @allure.title('Положительный флоу создания заказа и переход на страницу описания заказа')
    @allure.title('Проверка отображения заказа на странице заказа с присвоением ему номера при успешном оформлении')
    @pytest.mark.parametrize('data_set', ['data_set1', 'data_set2'])
    def test_successfull_orden_creation(self, data_set, driver):
        order_page = OrderPage(driver)
        order_page.get_url()
        order_page.click_order_button()
        order_page.wait_for_load_first_order_form()
        order_page.cookie_accept_click()
        order_page.add_client_data(OrderPageData.data[data_set].get('name'), OrderPageData.data[data_set].get('surname'), OrderPageData.data[data_set].get('address'), OrderPageData.data[data_set].get('metro_name'), OrderPageData.data[data_set].get('phone_number'))
        order_page.wait_for_load_order_form_with_characteristics()
        order_page.add_order_data(OrderPageData.data[data_set].get('data'),OrderPageData.data[data_set].get('rent_period'),OrderPageData.data[data_set].get('color'),OrderPageData.data[data_set].get('comment'))
        order_page.click_orden_aception_button()
        order_page.wait_for_load_form_order_completed()
        order_number=order_page.take_number_from_form()
        order_page.click_observe_status_button()
        order_page.wait_for_load_order_status_page()
        assert order_number in driver.current_url
    @allure.title('Проверка текста всплывающего окана при успешном оформлении заказа')
    @allure.description('Создается заказ и проверятся длина текста и присвоение номера заказа')
    @pytest.mark.parametrize('data_set', ['data_set1', 'data_set2'])
    def test_successfull_orden_creation_check_showing_order_info(self, data_set, driver):
        order_page = OrderPage(driver)
        order_page.get_url()
        order_page.click_order_button()
        order_page.wait_for_load_first_order_form()
        order_page.cookie_accept_click()
        order_page.add_client_data(OrderPageData.data[data_set].get('name'), OrderPageData.data[data_set].get('surname'), OrderPageData.data[data_set].get('address'), OrderPageData.data[data_set].get('metro_name'), OrderPageData.data[data_set].get('phone_number'))
        order_page.wait_for_load_order_form_with_characteristics()
        order_page.add_order_data(OrderPageData.data[data_set].get('data'),OrderPageData.data[data_set].get('rent_period'),OrderPageData.data[data_set].get('color'),OrderPageData.data[data_set].get('comment'))
        order_page.click_orden_aception_button()
        order_page.wait_for_load_form_order_completed()
        order_number=order_page.take_number_from_form()
        order_text=order_page.take_text_from_form()
        assert order_number!=0 and len(order_text)>0



