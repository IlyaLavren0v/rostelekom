import unittest
from pages.auth_page import AuthPage
from utils.webdriver_utils import WebDriverUtils


class TestAuthPhoneNegative(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriverUtils.get_driver()
        cls.auth_page = AuthPage(cls.driver)
        cls.auth_page.go_to_authorization_password_page()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_negative_phone_authentication_incorrect_number(self):
        """Негативная авторизация по номеру телефона с некорректным номером"""
        self.auth_page.enter_phone("1234567890")  # Некорректный номер
        self.auth_page.enter_password("TestUser2024")  # Корректный пароль
        self.auth_page.click_login_button()
        self.assertTrue(self.auth_page.is_error_message_displayed(),
                        "Система не отобразила сообщение об ошибке при некорректном номере телефона")


if __name__ == "__main__":
    unittest.main()
