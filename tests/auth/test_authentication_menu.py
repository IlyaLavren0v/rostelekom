import unittest
from pages.login_page import LoginPage
from utils.webdriver_utils import WebDriverUtils


class TestAuthenticationMenu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriverUtils.get_driver()
        cls.login_page = LoginPage(cls.driver)
        cls.login_page.go_to_authorization_password_page()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_authentication_menu_displayed(self):
        """Проверка наличия меню выбора типа аутентификации"""
        self.assertTrue(self.login_page.is_authentication_menu_displayed(),
                        "Меню выбора типа аутентификации не отображается на странице")


if __name__ == "__main__":
    unittest.main()
