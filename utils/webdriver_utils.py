from selenium import webdriver


class WebDriverUtils:
    @staticmethod
    def get_driver():
        return webdriver.Chrome()
