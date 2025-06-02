from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    def open_page(self):
        """Открытие базовой страницы"""
        self.driver.get(self.base_url)
        self.accept_cookies()
        return self

    def find_element(self, locator, timeout=10):
        """Поиск элемента с ожиданием"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, timeout=10):
        """Поиск элементов с ожиданием"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}")

    def find_visible_element(self, locator, timeout=10):
        """Поиск видимого элемента с ожиданием"""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Can't find visible element by locator {locator}")

    def scroll_to_element(self, element):
        """Прокрутка до элемента"""
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)

    def accept_cookies(self):
        """Принятие cookies"""
        try:
            cookie_btn = self.find_element((By.ID, "rcc-confirm-button"))
            cookie_btn.click()
            time.sleep(0.5)
        except:
            pass 