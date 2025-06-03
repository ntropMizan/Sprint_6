import pytest
import allure
from pages.order_page import OrderPage
from data.order_data import ORDER_DATA

@allure.feature('Заказ самоката')
class TestOrderFlow:
    
    @allure.title('Заказ самоката через кнопку в шапке')
    @pytest.mark.parametrize('test_data', ORDER_DATA)
    def test_order_from_header(self, driver, test_data):
        """Проверка оформления заказа через кнопку в шапке сайта"""
        order_page = OrderPage(driver)
        order_page.open_page()
        order_page.click_order_button("header")
        order_page.fill_first_order_form(
            test_data['name'],
            test_data['surname'],
            test_data['address'],
            test_data['metro'],
            test_data['phone']
        )
        order_page.fill_second_order_form(
            test_data['date'],
            test_data['rental_period'],
            test_data['color'],
            test_data['comment']
        )
        assert "Заказ оформлен" in order_page.get_order_success_message()

    @allure.title('Заказ самоката через кнопку внизу страницы')
    @pytest.mark.parametrize('test_data', ORDER_DATA)
    def test_order_from_middle(self, driver, test_data):
        """Проверка оформления заказа через кнопку внизу страницы"""
        order_page = OrderPage(driver)
        order_page.open_page()
        order_page.click_order_button("middle")
        order_page.fill_first_order_form(
            test_data['name'],
            test_data['surname'],
            test_data['address'],
            test_data['metro'],
            test_data['phone']
        )
        order_page.fill_second_order_form(
            test_data['date'],
            test_data['rental_period'],
            test_data['color'],
            test_data['comment']
        )
        assert "Заказ оформлен" in order_page.get_order_success_message() 