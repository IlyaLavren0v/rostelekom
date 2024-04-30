import unittest
from pages.login_page import LoginPage
from utils.webdriver_utils import WebDriverUtils


class TestProductSlogan(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriverUtils.get_driver()
        cls.driver.maximize_window()
        cls.login_page = LoginPage(cls.driver)
        cls.login_page.go_to_authorization_password_page()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_product_slogan_displayed(self):
        """Проверка наличия продуктового слогана"""
        self.assertTrue(self.login_page.is_product_slogan_displayed(),
                        "Продуктовый слоган не отображается на странице")


if __name__ == "__main__":
    unittest.main()
