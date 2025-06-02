from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.questions_page_locators import QuestionsPageLocators

class QuestionsPage(BasePage):
    def open_page(self):
        """Открытие страницы"""
        self.driver.get(self.base_url)
        self.accept_cookies()
        return self

    def scroll_to_questions(self):
        """Прокрутка к секции с вопросами"""
        questions_section = self.find_element(QuestionsPageLocators.QUESTIONS_SECTION)
        self.scroll_to_element(questions_section)

    def get_answer_text(self, question_index):
        """Получение текста ответа на вопрос"""
        # Находим и кликаем по вопросу
        question = self.find_element(QuestionsPageLocators.QUESTIONS[question_index]['question'])
        question.click()
        
        # Ждем, пока ответ станет видимым и получаем его текст
        answer = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(QuestionsPageLocators.QUESTIONS[question_index]['answer'])
        )
        return answer.text

    def check_answer_text(self, question_index):
        """Проверка соответствия текста ответа ожидаемому"""
        actual_text = self.get_answer_text(question_index)
        expected_text = QuestionsPageLocators.QUESTIONS[question_index]['expected_text']
        print(f"\nВопрос {question_index}:")
        print(f"Ожидаемый текст: '{expected_text}'")
        print(f"Фактический текст: '{actual_text}'")
        return actual_text == expected_text 