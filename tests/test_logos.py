import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.order_page import OrderPage

@allure.feature('Проверка логотипов')
class TestLogos:
    
    @allure.title('Проверка перехода по клику на логотип Самоката')
    def test_scooter_logo_click(self, driver):
        """Проверка перехода на главную страницу при клике на логотип Самоката"""
        order_page = OrderPage(driver)
        order_page.open_page()
        order_page.click_order_button()
        order_page.click_scooter_logo()
        assert driver.current_url == order_page.base_url

    @allure.title('Проверка перехода по клику на логотип Яндекса')
    def test_yandex_logo_click(self, driver):
        """Проверка перехода на Дзен при клике на логотип Яндекса"""
        order_page = OrderPage(driver)
        order_page.open_page()
        
        # Нажимаем на логотип Яндекса
        order_page.click_yandex_logo()
        
        # Ждем появления нового окна
        WebDriverWait(driver, 5).until(
            EC.number_of_windows_to_be(2)
        )
        
        # Переключаемся на новое окно (оно всегда последнее в списке)
        new_window = driver.window_handles[-1]
        driver.switch_to.window(new_window)
                
        # Ждем, пока URL станет содержать dzen.ru
        WebDriverWait(driver, 5).until(
            EC.url_contains("dzen.ru")
        )
        
        # Проверяем, что перешли на страницу Дзен
        assert "dzen.ru" in driver.current_url 