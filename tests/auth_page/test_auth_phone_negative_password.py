import unittest
from pages.auth_page import AuthPage
from utils.webdriver_utils import WebDriverUtils


class TestAuthPhoneNegativePassword(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriverUtils.get_driver()
        cls.auth_page = AuthPage(cls.driver)
        cls.auth_page.go_to_authorization_password_page()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_negative_password_authentication(self):
        """Негативная авторизация по номеру телефона с некорректным паролем"""
        self.auth_page.enter_phone("+79264786356")
        self.auth_page.enter_password("incorrect_password")
        self.auth_page.click_login_button()
        self.assertTrue(self.auth_page.is_error_message_displayed(),
                        "Ошибка неверного логина или пароля не отображается")


if __name__ == "__main__":
    unittest.main()
