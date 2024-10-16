import allure
import pytest
from pages.home_page import HomePage
import locators.home_page_locators as loc

class TestQuestionsHomePage:
    @allure.title('Проверка вопросов и ответов на домашней странице')
    @allure.description('Проверка функциональности блока "Вопросы о важном" при нажатии на вопрос раскрывается ответ. Проверка соответствия текста ответа ожидаемому')
    @pytest.mark.parametrize("question_number, expected_answer",
                             [(1, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."), (2,
                                                                                                  "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
                              (3,
                               "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
                              (4, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."), (5,
                                                                                                      "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
                              (6,
                               "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
                              (7,
                               "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
                              (8, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")])
    def test_check_all_questions(self, driver, question_number, expected_answer):
        home_page = HomePage(driver)
        home_page.get_url_and_scroll()
        home_page.cookie_accept_click()
        home_page.click_question(question_number)
        current_answer = driver.find_element(*loc.HomePageLocators.hp_answers.get(question_number))
        assert current_answer.text == expected_answer and current_answer.is_displayed()
