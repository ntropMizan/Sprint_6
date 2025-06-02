from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Локаторы для кнопок заказа
    ORDER_BUTTON_HEADER = (By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[contains(@class, 'Button_Button') and not(contains(@class, 'Header_Button'))]")
    ORDER_BUTTON_MIDDLE = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[contains(@class, 'Button_Button')]")
    
    # Локаторы для формы заказа
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_ITEM = (By.CLASS_NAME, "select-search__select")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    
    # Локаторы для второй страницы заказа
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-control")
    RENTAL_PERIOD_OPTIONS = (By.CLASS_NAME, "Dropdown-option")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    
    # Кнопки навигации и подтверждения
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    ORDER_FINAL_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[contains(@class, 'Button_Button') and contains(@class, 'Button_Middle') and not(contains(@class, 'Button_Inverted'))]")
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    
    # Локаторы для проверки результата
    ORDER_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    ORDER_SUCCESS_MESSAGE = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    
    # Локаторы для логотипов
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI") 