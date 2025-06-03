import pytest
import allure
from pages.questions_page import QuestionsPage
from data.questions_data import QUESTIONS_DATA

@allure.feature('Вопросы о важном')
class TestQuestions:
    @allure.title('Проверка текста ответа на вопрос "{test_data[title]}"')
    @pytest.mark.parametrize('test_data', QUESTIONS_DATA)
    def test_question_text(self, driver, test_data):
        questions_page = QuestionsPage(driver)
        questions_page.open_page()
        questions_page.scroll_to_questions()
        assert questions_page.check_answer_text(test_data['index']), \
            test_data['error_message']