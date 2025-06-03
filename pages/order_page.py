from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import time
import allure

class OrderPage(BasePage):
    @allure.step('Нажатие на кнопку заказа - {button_position}')
    def click_order_button(self, button_position="header"):
        button = OrderPageLocators.ORDER_BUTTON_HEADER if button_position == "header" else OrderPageLocators.ORDER_BUTTON_MIDDLE
        if button_position == "middle":
            # Прокручиваем страницу к кнопке заказа
            element = self.find_element(button)
            self.scroll_to_element(element)
        self.find_element(button).click()

    @allure.step('Заполнение первой формы заказа: {name} {surname}, {address}, {metro}, {phone}')
    def fill_first_order_form(self, name, surname, address, metro, phone):
        self.find_element(OrderPageLocators.NAME_INPUT).send_keys(name)
        self.find_element(OrderPageLocators.SURNAME_INPUT).send_keys(surname)
        self.find_element(OrderPageLocators.ADDRESS_INPUT).send_keys(address)
        
        metro_input = self.find_element(OrderPageLocators.METRO_STATION_INPUT)
        metro_input.click()
        metro_input.send_keys(metro)
        self.find_element((By.XPATH, f"//div[@class='select-search__select']//div[text()='{metro}']")).click()
        
        self.find_element(OrderPageLocators.PHONE_INPUT).send_keys(phone)
        self.find_element(OrderPageLocators.NEXT_BUTTON).click()

    @allure.step('Заполнение второй формы заказа: дата {date}, период {rental_period}, цвет {color}')
    def fill_second_order_form(self, date, rental_period, color, comment):
        # Заполняем дату
        date_input = self.find_element(OrderPageLocators.DATE_INPUT)
        date_input.click()
        date_input.send_keys(date)
        self.find_element((By.XPATH, "//div[contains(@class, 'react-datepicker__day--selected')]")).click()
        
        # Выбираем срок аренды
        self.find_element(OrderPageLocators.RENTAL_PERIOD).click()
        period_options = self.find_elements(OrderPageLocators.RENTAL_PERIOD_OPTIONS)
        for option in period_options:
            if option.text == rental_period:
                option.click()
                break
        
        # Выбираем цвет
        if color == "black":
            self.find_element(OrderPageLocators.COLOR_BLACK).click()
        else:
            self.find_element(OrderPageLocators.COLOR_GREY).click()
            
        # Добавляем комментарий, если есть
        if comment:
            self.find_element(OrderPageLocators.COMMENT_INPUT).send_keys(comment)
            
        # Нажимаем кнопку заказа и ждем появления модального окна
        order_button = self.find_element(OrderPageLocators.ORDER_FINAL_BUTTON)
        self.scroll_to_element(order_button)
        order_button.click()
        
        # Ждем появления модального окна
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(OrderPageLocators.ORDER_MODAL)
        )
        
        # Ждем появления и кликаем по кнопке "Да"
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(OrderPageLocators.YES_BUTTON)
        ).click()

    @allure.step('Получение текста сообщения об успешном заказе')
    def get_order_success_message(self):
        success_message = self.find_visible_element(OrderPageLocators.ORDER_SUCCESS_MESSAGE)
        return success_message.text

    @allure.step('Клик по логотипу самоката')
    def click_scooter_logo(self):
        self.find_element(OrderPageLocators.SCOOTER_LOGO).click()

    @allure.step('Клик по логотипу Яндекса')
    def click_yandex_logo(self):
        self.find_element(OrderPageLocators.YANDEX_LOGO).click()

    @allure.step('Проверка, что текущий URL совпадает с базовым')
    def check_current_url_is_base(self):
        return self.driver.current_url == self.base_url

    @allure.step('Ожидание и переключение на новое окно')
    def switch_to_new_window(self):
        WebDriverWait(self.driver, 5).until(
            EC.number_of_windows_to_be(2)
        )
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)

    @allure.step('Ожидание перехода на Дзен')
    def wait_for_dzen_redirect(self):
        WebDriverWait(self.driver, 5).until(
            EC.url_contains("dzen.ru")
        )
        return "dzen.ru" in self.driver.current_url 