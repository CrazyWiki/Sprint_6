import allure
import pytest
from pages.home_page import HomePage
import locators.home_page_locators as loc
from data import HomePageData
class TestQuestionsHomePage:
    @allure.title('Проверка вопросов и ответов на домашней странице')
    @allure.description('Проверка функциональности блока "Вопросы о важном" при нажатии на вопрос раскрывается ответ. Проверка соответствия текста ответа ожидаемому')
    @pytest.mark.parametrize("question_number, expected_answer", HomePageData.questions)
    def test_check_all_questions(self, driver, question_number, expected_answer):
        home_page = HomePage(driver)
        home_page.get_url_and_scroll()
        home_page.cookie_accept_click()
        home_page.click_question(question_number)
        current_answer = driver.find_element(*loc.HomePageLocators.hp_answers.get(question_number))
        assert current_answer.text == expected_answer and current_answer.is_displayed()
