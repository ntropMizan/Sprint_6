# Sprint_6
Проект по автоматизации тестирования для Яндекс.Самокат

## Описание
Автоматизация тестирования веб-приложения Яндекс.Самокат с использованием Selenium WebDriver и Python.

## Тестовые сценарии
1. Проверка выпадающего списка в разделе «Вопросы о важном»
2. Тестирование процесса заказа самоката
3. Проверка работы логотипов (переходы на главную Самоката и Дзен)

## Технологии
- Python 3
- Selenium WebDriver
- PyTest
- Allure для отчетов

## Структура проекта
- `/pages` - Page Object Models
- `/tests` - тестовые файлы
- `/locators` - локаторы элементов
- `/data` - тестовые данные
- `/allure-report` - отчеты о тестировании

## Запуск тестов
1. Установить зависимости:
```bash
pip install -r requirements.txt
```

2. Запустить тесты:
```bash
pytest tests/
```

3. Сгенерировать Allure-отчет:
```bash
pytest tests/ --alluredir=allure-results
allure generate allure-results --clean -o allure-report
``` 