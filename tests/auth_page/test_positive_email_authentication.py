import unittest
from pages.auth_page import AuthPage
from utils.webdriver_utils import WebDriverUtils


class TestAuthEmailPositive(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriverUtils.get_driver()
        cls.auth_page = AuthPage(cls.driver)
        cls.auth_page.go_to_authorization_password_page()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_positive_email_authentication(self):
        """Позитивная авторизация по почте с корректными данными"""
        self.auth_page.enter_email("lavrilios16@gmail.com")
        self.auth_page.enter_password("TestUser2024")
        self.auth_page.click_login_button()
        self.assertTrue(self.auth_page.is_redirect_successful(), "Авторизация по почте не прошла успешно")


if __name__ == "__main__":
    unittest.main()
