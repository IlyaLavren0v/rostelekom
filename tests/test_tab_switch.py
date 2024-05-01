import unittest
from pages.login_page import LoginPage
from utils.webdriver_utils import WebDriverUtils


class TestTabSwitch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriverUtils.get_driver()
        cls.login_page = LoginPage(cls.driver)
        cls.login_page.go_to_authorization_password_page()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_tab_switch(self):
        """Проверка автоматического изменения табов при вводе данных"""
        self.assertTrue(self.login_page.is_tab_switch(), "Табы не переключаются автоматически при вводе данных")


if __name__ == "__main__":
    unittest.main()
