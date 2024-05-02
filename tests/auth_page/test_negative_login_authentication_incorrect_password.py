import unittest
from pages.auth_page import AuthPage
from utils.webdriver_utils import WebDriverUtils


class TestAuthLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriverUtils.get_driver()
        cls.auth_page = AuthPage(cls.driver)
        cls.auth_page.go_to_auth_page()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_negative_login_authentication_incorrect_password(self):
        """Негативная авторизация по логину с некорректным паролем"""
        self.auth_page.go_to_authorization_password_page()
        self.auth_page.enter_login("username")
        self.auth_page.enter_password("incorrect_password")
        self.auth_page.click_login_password_button()
        self.assertTrue(self.auth_page.is_error_message_displayed(), "Система не отобразила сообщение об ошибке")


if __name__ == "__main__":
    unittest.main()
