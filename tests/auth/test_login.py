import unittest
from pages.login_page import LoginPage
from utils.webdriver_utils import WebDriverUtils


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriverUtils.get_driver()
        cls.login_page = LoginPage(cls.driver)
        cls.login_page.go_to_login_page()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_form_displayed(self):
        """Проверка наличия формы авторизации"""
        self.login_page.go_to_login_page()
        self.assertTrue(self.login_page.is_login_form_displayed(), "Форма авторизации не отображается на странице")


if __name__ == "__main__":
    unittest.main()
