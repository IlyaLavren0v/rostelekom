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

    def test_enter_correct_phone_and_get_code(self):
        """Ввод корректного номера телефона и нажатие кнопки "Получить код" """
        self.auth_page.enter_phone_get_code("+79264786356")
        self.auth_page.click_get_code_button()
        self.assertTrue(self.auth_page.is_code_sent_message_displayed(),
                        "Код для авторизации не отправлен")


if __name__ == "__main__":
    unittest.main()
