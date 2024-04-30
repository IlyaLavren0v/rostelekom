import unittest
from pages.login_page import LoginPage
from utils.webdriver_utils import WebDriverUtils


class TestInputForms(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriverUtils.get_driver()
        cls.login_page = LoginPage(cls.driver)
        cls.login_page.go_to_authorization_password_page()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_input_forms_username_displayed(self):
        """Проверка наличия форм ввода номера/логина/почты/лицевого счета"""
        self.assertTrue(self.login_page.is_input_forms_username_displayed(),
                        "Формы для ввода номера/логина/почты/лицевого счета не отображаются на странице")


if __name__ == "__main__":
    unittest.main()
