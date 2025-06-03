from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.questions_page_locators import QuestionsPageLocators
import allure

class QuestionsPage(BasePage):
    @allure.step('Открытие страницы')
    def open_page(self):
        self.driver.get(self.base_url)
        self.accept_cookies()
        return self

    @allure.step('Прокрутка к секции с вопросами')
    def scroll_to_questions(self):
        questions_section = self.find_element(QuestionsPageLocators.QUESTIONS_SECTION)
        self.scroll_to_element(questions_section)

    @allure.step('Получение текста ответа на вопрос {question_index}')
    def get_answer_text(self, question_index):
        # Находим и кликаем по вопросу
        question = self.find_element(QuestionsPageLocators.QUESTIONS[question_index]['question'])
        question.click()
        
        # Ждем, пока ответ станет видимым и получаем его текст
        answer = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(QuestionsPageLocators.QUESTIONS[question_index]['answer'])
        )
        return answer.text

    @allure.step('Проверка соответствия текста ответа ожидаемому для вопроса {question_index}')
    def check_answer_text(self, question_index):
        actual_text = self.get_answer_text(question_index)
        expected_text = QuestionsPageLocators.QUESTIONS[question_index]['expected_text']
        print(f"\nВопрос {question_index}:")
        print(f"Ожидаемый текст: '{expected_text}'")
        print(f"Фактический текст: '{actual_text}'")
        return actual_text == expected_text 