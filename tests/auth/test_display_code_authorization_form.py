import unittest
from selenium import webdriver
from pages.auth_page import AuthPage


class TestAuthorizationByTemporaryCode(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.auth_page = AuthPage(cls.driver)
        cls.auth_page.go_to_auth_page()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_display_code_authorization_form(self):
        """Проверка отображения формы "Авторизация по коду" со всеми необходимыми элементами"""
        self.assertTrue(self.auth_page.go_to_temporary_code_authorization_form(),
                        "Форма авторизации не соответствует")


if __name__ == "__main__":
    unittest.main()
