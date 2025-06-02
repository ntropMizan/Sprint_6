from selenium.webdriver.common.by import By

class QuestionsPageLocators:
    # Секция с вопросами
    QUESTIONS_SECTION = (By.XPATH, "//div[contains(@class, 'Home_FourPart__1uthg')]")
    
    # Словарь с локаторами вопросов и ответов
    QUESTIONS = {
        0: {
            'question': (By.ID, "accordion__heading-0"),
            'answer': (By.ID, "accordion__panel-0"),
            'expected_text': "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        },
        1: {
            'question': (By.ID, "accordion__heading-1"),
            'answer': (By.ID, "accordion__panel-1"),
            'expected_text': "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
        },
        2: {
            'question': (By.ID, "accordion__heading-2"),
            'answer': (By.ID, "accordion__panel-2"),
            'expected_text': "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        },
        3: {
            'question': (By.ID, "accordion__heading-3"),
            'answer': (By.ID, "accordion__panel-3"),
            'expected_text': "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        },
        4: {
            'question': (By.ID, "accordion__heading-4"),
            'answer': (By.ID, "accordion__panel-4"),
            'expected_text': "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        },
        5: {
            'question': (By.ID, "accordion__heading-5"),
            'answer': (By.ID, "accordion__panel-5"),
            'expected_text': "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
        },
        6: {
            'question': (By.ID, "accordion__heading-6"),
            'answer': (By.ID, "accordion__panel-6"),
            'expected_text': "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
        },
        7: {
            'question': (By.ID, "accordion__heading-7"),
            'answer': (By.ID, "accordion__panel-7"),
            'expected_text': "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        }
    } 