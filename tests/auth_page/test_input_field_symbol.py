import unittest
from pages.auth_page import AuthPage
from utils.webdriver_utils import WebDriverUtils


class TestInputFieldLimit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriverUtils.get_driver()
        cls.auth_page = AuthPage(cls.driver)
        cls.auth_page.go_to_authorization_password_page()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_input_field_limit(self):
        """Проверка ограничения на ввод символов в поле ввода лицевого счета"""
        self.auth_page.enter_account("$#@kkhw")
        self.auth_page.enter_password("valid_password")
        self.auth_page.click_login_button()
        self.assertTrue(self.auth_page.is_account_number_field_empty(),
                        "Сообщение об ошибке не отображается")


if __name__ == "__main__":
    unittest.main()
