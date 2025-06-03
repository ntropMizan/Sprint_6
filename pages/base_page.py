from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    @allure.step('Открытие базовой страницы')
    def open_page(self):
        self.driver.get(self.base_url)
        self.accept_cookies()
        return self

    @allure.step('Поиск элемента по локатору {locator}')
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    @allure.step('Поиск элементов по локатору {locator}')
    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )

    @allure.step('Поиск видимого элемента по локатору {locator}')
    def find_visible_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f"Can't find visible element by locator {locator}"
        )

    @allure.step('Прокрутка страницы к элементу')
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)

    @allure.step('Принятие cookies')
    def accept_cookies(self):
        try:
            cookie_btn = self.find_element((By.ID, "rcc-confirm-button"))
            cookie_btn.click()
            time.sleep(0.5)
        except:
            pass 