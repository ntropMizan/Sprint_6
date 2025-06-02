from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import time

class OrderPage(BasePage):
    def click_order_button(self, button_position="header"):
        """Нажатие на кнопку заказа"""
        button = OrderPageLocators.ORDER_BUTTON_HEADER if button_position == "header" else OrderPageLocators.ORDER_BUTTON_MIDDLE
        if button_position == "middle":
            # Прокручиваем страницу к кнопке заказа
            element = self.find_element(button)
            self.scroll_to_element(element)
        self.find_element(button).click()

    def fill_first_order_form(self, name, surname, address, metro, phone):
        """Заполнение первой формы заказа"""
        self.find_element(OrderPageLocators.NAME_INPUT).send_keys(name)
        self.find_element(OrderPageLocators.SURNAME_INPUT).send_keys(surname)
        self.find_element(OrderPageLocators.ADDRESS_INPUT).send_keys(address)
        
        metro_input = self.find_element(OrderPageLocators.METRO_STATION_INPUT)
        metro_input.click()
        metro_input.send_keys(metro)
        self.find_element((By.XPATH, f"//div[@class='select-search__select']//div[text()='{metro}']")).click()
        
        self.find_element(OrderPageLocators.PHONE_INPUT).send_keys(phone)
        self.find_element(OrderPageLocators.NEXT_BUTTON).click()

    def fill_second_order_form(self, date, rental_period, color, comment):
        """Заполнение второй формы заказа"""
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

    def get_order_success_message(self):
        """Получение текста сообщения об успешном заказе"""
        success_message = self.find_visible_element(OrderPageLocators.ORDER_SUCCESS_MESSAGE)
        return success_message.text

    def click_scooter_logo(self):
        """Клик по логотипу самоката"""
        self.find_element(OrderPageLocators.SCOOTER_LOGO).click()

    def click_yandex_logo(self):
        """Клик по логотипу Яндекса"""
        self.find_element(OrderPageLocators.YANDEX_LOGO).click() 