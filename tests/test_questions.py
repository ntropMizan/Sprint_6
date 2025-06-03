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

    @allure.title('Проверка вопроса о стоимости и способе оплаты')
    def test_question_1_cost_and_payment(self, driver):
        """Проверка текста ответа на вопрос о стоимости и способе оплаты"""
        questions_page = QuestionsPage(driver)
        questions_page.open_page()
        questions_page.scroll_to_questions()
        assert questions_page.check_answer_text(0), \
            "Текст ответа на вопрос о стоимости и способе оплаты не соответствует ожидаемому"

    @allure.title('Проверка вопроса о нескольких самокатах')
    def test_question_2_multiple_scooters(self, driver):
        """Проверка текста ответа на вопрос о нескольких самокатах"""
        questions_page = QuestionsPage(driver)
        questions_page.open_page()
        questions_page.scroll_to_questions()
        assert questions_page.check_answer_text(1), \
            "Текст ответа на вопрос о нескольких самокатах не соответствует ожидаемому"

    @allure.title('Проверка вопроса о времени аренды')
    def test_question_3_rental_time(self, driver):
        """Проверка текста ответа на вопрос о времени аренды"""
        questions_page = QuestionsPage(driver)
        questions_page.open_page()
        questions_page.scroll_to_questions()
        assert questions_page.check_answer_text(2), \
            "Текст ответа на вопрос о времени аренды не соответствует ожидаемому"

    @allure.title('Проверка вопроса о доставке сегодня')
    def test_question_4_today_delivery(self, driver):
        """Проверка текста ответа на вопрос о доставке сегодня"""
        questions_page = QuestionsPage(driver)
        questions_page.open_page()
        questions_page.scroll_to_questions()
        assert questions_page.check_answer_text(3), \
            "Текст ответа на вопрос о доставке сегодня не соответствует ожидаемому"

    @allure.title('Проверка вопроса о продлении заказа')
    def test_question_5_extend_rental(self, driver):
        """Проверка текста ответа на вопрос о продлении заказа"""
        questions_page = QuestionsPage(driver)
        questions_page.open_page()
        questions_page.scroll_to_questions()
        assert questions_page.check_answer_text(4), \
            "Текст ответа на вопрос о продлении заказа не соответствует ожидаемому"

    @allure.title('Проверка вопроса о зарядке самоката')
    def test_question_6_charger(self, driver):
        """Проверка текста ответа на вопрос о зарядке самоката"""
        questions_page = QuestionsPage(driver)
        questions_page.open_page()
        questions_page.scroll_to_questions()
        assert questions_page.check_answer_text(5), \
            "Текст ответа на вопрос о зарядке самоката не соответствует ожидаемому"

    @allure.title('Проверка вопроса об отмене заказа')
    def test_question_7_cancel_order(self, driver):
        """Проверка текста ответа на вопрос об отмене заказа"""
        questions_page = QuestionsPage(driver)
        questions_page.open_page()
        questions_page.scroll_to_questions()
        assert questions_page.check_answer_text(6), \
            "Текст ответа на вопрос об отмене заказа не соответствует ожидаемому"

    @allure.title('Проверка вопроса о доставке за МКАД')
    def test_question_8_outside_mkad(self, driver):
        """Проверка текста ответа на вопрос о доставке за МКАД"""
        questions_page = QuestionsPage(driver)
        questions_page.open_page()
        questions_page.scroll_to_questions()
        assert questions_page.check_answer_text(7), \
            "Текст ответа на вопрос о доставке за МКАД не соответствует ожидаемому" 