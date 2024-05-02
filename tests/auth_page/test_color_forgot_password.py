import unittest
from pages.auth_page import AuthPage
from utils.webdriver_utils import WebDriverUtils


class TestForgotPasswordElementColor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriverUtils.get_driver()
        cls.auth_page = AuthPage(cls.driver)
        cls.auth_page.go_to_authorization_password_page()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_forgot_password_element_color(self):
        """Проверка перекрашивания элемента "Забыл пароль" при ошибке"""
        self.auth_page.enter_phone("+79264786356")
        self.auth_page.enter_password("TestUser")
        self.auth_page.click_login_button()

        self.assertTrue(self.auth_page.is_forgot_password_element_orange(),
                        "Элемент 'Забыл пароль' не перекрашивается в оранжевый цвет при некорректной связке "
                        "Номер+Пароль.")


if __name__ == "__main__":
    unittest.main()
