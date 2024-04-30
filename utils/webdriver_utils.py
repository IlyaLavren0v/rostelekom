from selenium import webdriver

class WebDriverUtils:
    @staticmethod
    def get_driver():
        return webdriver.Chrome()  # Замените эту строку на вашу логику получения драйвера

    # Дополнительные методы для работы с веб-драйвером можно добавить здесь
