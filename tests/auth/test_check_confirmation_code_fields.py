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

    def test_check_confirmation_code_fields(self):
        """Проверка наличия шести отдельных полей для ввода кода подтверждения"""
        self.auth_page.enter_phone_get_code("+79998887766")
        self.auth_page.click_get_code_button()
        self.assertTrue(self.auth_page.are_confirmation_code_fields_displayed(), "Количество полей не равно 6")


if __name__ == "__main__":
    unittest.main()
