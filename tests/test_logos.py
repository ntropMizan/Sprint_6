import allure
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
        assert order_page.check_current_url_is_base()

    @allure.title('Проверка перехода по клику на логотип Яндекса')
    def test_yandex_logo_click(self, driver):
        """Проверка перехода на Дзен при клике на логотип Яндекса"""
        order_page = OrderPage(driver)
        order_page.open_page()
        order_page.click_yandex_logo()
        order_page.switch_to_new_window()
        assert order_page.wait_for_dzen_redirect() 