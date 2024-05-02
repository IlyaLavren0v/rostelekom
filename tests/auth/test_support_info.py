import unittest
from pages.login_page import LoginPage
from utils.webdriver_utils import WebDriverUtils


class TestClientInfo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriverUtils.get_driver()
        cls.login_page = LoginPage(cls.driver)
        cls.login_page.go_to_authorization_password_page()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_support_info_displayed(self):
        """Проверка наличия вспомогательной информации для клиента"""
        self.assertTrue(
            self.login_page.is_support_info_displayed(), "Вспомогательная информация для клиента не отображается"
        )


if __name__ == "__main__":
    unittest.main()
