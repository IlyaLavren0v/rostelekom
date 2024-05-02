import unittest
from selenium import webdriver
from pages.auth_page import AuthPage


class TestFormGetCode(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.auth_page = AuthPage(cls.driver)
        cls.auth_page.go_to_auth_page()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_check_confirmation_code_form_displayed(self):
        """Проверка отображения формы ввода кода с соответствующими элементами"""
        # Предположим, что метод enter_phone_get_code() уже реализован и открывает форму ввода кода
        self.auth_page.enter_phone_get_code("+79998887766")
        self.auth_page.click_get_code_button()

        # Проверяем наличие номера телефона/почты
        self.assertTrue(self.auth_page.is_phone_displayed(),
                        "Номер телефона/почты не отображается на странице")

        # Проверяем наличие ссылки "Изменить номер/почту"
        self.assertTrue(self.auth_page.is_change_contact_link_displayed(),
                        "Ссылка 'Изменить номер/почту' не отображается")

        # Проверяем наличие полей для ввода кода
        self.assertTrue(self.auth_page.are_confirmation_code_fields_displayed(),
                        "Количество полей не равно 6")

        # Проверяем наличие текста с обратным отсчетом времени
        self.assertTrue(self.auth_page.is_countdown_timer_displayed(),
                        "Текст с обратным отсчетом времени не отображается")


if __name__ == "__main__":
    unittest.main()
