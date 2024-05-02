import unittest
from pages.auth_page import AuthPage
from utils.webdriver_utils import WebDriverUtils


class TestNegativeAccountAuthenticationIncorrectAccount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriverUtils.get_driver()
        cls.auth_page = AuthPage(cls.driver)
        cls.auth_page.go_to_authorization_password_page()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_negative_account_authentication_incorrect_account(self):
        """Негативная авторизация по лицевому счету с некорректным счетом"""
        self.auth_page.enter_account("000000000000")  # 12 чисел
        self.auth_page.enter_password("valid_password")
        self.auth_page.click_login_button()
        self.assertTrue(self.auth_page.is_error_message_displayed(),
                        "Сообщение об ошибке не отображается")


if __name__ == "__main__":
    unittest.main()
