import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

@pytest.fixture(scope="function")
def driver():
    """
    Фикстура для создания и управления драйвером браузера Firefox
    """
    # Создаем объект опций Firefox
    firefox_options = Options()
    
    # Создаем объект сервиса Firefox
    service = Service()
    
    # Инициализируем драйвер с нашими настройками
    driver = webdriver.Firefox(service=service, options=firefox_options)
    
    # Устанавливаем неявное ожидание
    driver.implicitly_wait(10)
    
    # Открываем сайт перед каждым тестом
    driver.get("https://qa-scooter.praktikum-services.ru/")
    
    # Максимизируем окно браузера
    driver.maximize_window()
    
    yield driver
    
    # Закрываем браузер после каждого теста
    driver.quit()

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep) 