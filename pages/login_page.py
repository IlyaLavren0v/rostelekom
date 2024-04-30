import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL, AUTHORIZATION_PASSWORD_URL
import time


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_login_page(self):
        self.driver.get(BASE_URL)

    def go_to_authorization_password_page(self):
        self.driver.get(AUTHORIZATION_PASSWORD_URL)

    def is_login_form_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "#page-right .card-container.otp-form-container.otp-form-container"))
            )
            return True
        except:
            return False

    def is_authentication_menu_displayed(self):
        """Проверка наличия меню выбора типа аутентификации"""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "t-btn-tab-phone")) and
                EC.presence_of_element_located((By.ID, "t-btn-tab-mail")) and
                EC.presence_of_element_located((By.ID, "t-btn-tab-login")) and
                EC.presence_of_element_located((By.ID, "t-btn-tab-ls"))
            )
            return True
        except:
            return False

    def is_input_forms_username_displayed(self):
        """Проверка наличия форм ввода номера/логина/почты/лицевого счета"""
        try:
            # Клик по номеру
            phone_tab = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "t-btn-tab-phone"))
            )
            phone_tab.click()

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='PHONE']"))
            )
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )

            # Клик по логину
            login_tab = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "t-btn-tab-login"))
            )
            login_tab.click()

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='LOGIN']"))
            )
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )

            # Клик по почте
            mail_tab = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "t-btn-tab-mail"))
            )
            mail_tab.click()

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='EMAIL']"))
            )
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )

            # Клик по лицевому счету
            ls_tab = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "t-btn-tab-ls"))
            )
            ls_tab.click()

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='LS']"))
            )
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )

            return True
        except:
            return False

    def is_input_forms_password_displayed(self):
        """Проверка наличия форм ввода номера/логина/почты/лицевого счета"""
        try:
            # Клик по номеру
            phone_tab = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "t-btn-tab-phone"))
            )
            phone_tab.click()

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='PHONE']"))
            )
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "password"))
            )

            # Клик по логину
            login_tab = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "t-btn-tab-login"))
            )
            login_tab.click()

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='LOGIN']"))
            )
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "password"))
            )

            # Клик по почте
            mail_tab = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "t-btn-tab-mail"))
            )
            mail_tab.click()

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='EMAIL']"))
            )
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "password"))
            )

            # Клик по лицевому счету
            ls_tab = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "t-btn-tab-ls"))
            )
            ls_tab.click()

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='LS']"))
            )
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "password"))
            )

            return True
        except:
            return False

    def is_product_slogan_displayed(self):
        """Проверка наличия продуктового слогана на странице"""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#page-left > div > div.what-is > p"))
            )
            return True
        except:
            return False

    def test_client_info_displayed(self):
        """Проверка наличия вспомогательной информации для клиента"""
        try:
            # Поиск элемента по CSS-селектору
            client_info_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".client-info"))
            )
            # Если элемент найден, то вспомогательная информация для клиента отображается
            self.assertTrue(client_info_element.is_displayed(),
                            "Вспомогательная информация для клиента не отображается")
        except Exception as e:
            # Если возникает ошибка, выводим сообщение об ошибке
            print("Ошибка:", e)
            self.fail("Тест завершился с ошибкой")