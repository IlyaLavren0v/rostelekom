import unittest
from selenium import webdriver
from pages.auth_page import AuthPage


class TestAuthorizationByTemporaryCode(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.auth_page = AuthPage(cls.driver)
        cls.auth_page.go_to_auth_page()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_enter_incorrect_phone_and_get_code(self):
        """Ввод некорректного номера телефона и нажатие кнопки "Получить код" """
        self.auth_page.enter_phone_get_code("invalid_phone_number")
        self.auth_page.click_get_code_button()
        self.assertTrue(self.auth_page.is_invalid_phone_error_message_displayed(),
                        "Не выводится сообщение об ошибке")


if __name__ == "__main__":
    unittest.main()
