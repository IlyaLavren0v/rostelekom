from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL, AUTHORIZATION_PASSWORD_URL


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

    def is_support_info_displayed(self):
        """Проверка наличия вспомогательной информации для клиента"""
        try:
            # Поиск элемента по CSS-селектору
            client_info_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    By.CSS_SELECTOR, "#app-footer > div.rt-footer-right.rt-footer-side-item"))
            )

            return True
        except:
            return False

    def is_tab_switch(self):
        """Проверка автоматического изменения табов при вводе данных"""
        try:
            # Клик по полю ввода
            username_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            username_input.send_keys("test@test.ru")
            username_input.send_keys(Keys.TAB)

            # Проверка, что таб автоматически изменяется на почту
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='EMAIL']"))
            )

            # Клик по полю ввода
            username_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            username_input.click()

            # Скрипт для очистки поля
            self.driver.execute_script("arguments[0].value = '';", username_input)

            username_input.send_keys("89998887766")
            username_input.send_keys(Keys.TAB)

            # Проверка, что таб автоматически изменяется на номер
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='PHONE']"))
            )

            # Клик по полю ввода номер
            username_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            username_input.click()

            # Скрипт для очистки поля
            self.driver.execute_script("arguments[0].value = '';", username_input)

            username_input.send_keys("USER")
            username_input.send_keys(Keys.TAB)

            # Проверка, что таб автоматически изменяется на логин
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='LOGIN']"))
            )

            # Клик по полю ввода номер
            username_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            username_input.click()

            # Скрипт для очистки поля
            self.driver.execute_script("arguments[0].value = '';", username_input)

            username_input.send_keys("126598340965")
            username_input.send_keys(Keys.TAB)

            # Проверка, что таб автоматически изменяется на лицевой счет
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='LS']"))
            )
            return True
        except:
            return False
