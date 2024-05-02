from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL, AUTHORIZATION_PASSWORD_URL


class AuthPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_auth_page(self):
        self.driver.get(BASE_URL)

    def go_to_authorization_password_page(self):
        self.driver.get(AUTHORIZATION_PASSWORD_URL)

    def go_to_temporary_code_authorization_form(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((
                    By.ID, "address"
                ))
            )

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((
                    By.XPATH,
                    '//*[@id="card-description" and contains(text(),"Укажите почту или номер телефона, на которые необходимо отправить код подтверждения")]'
                ))
            )

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((
                    By.ID, "otp_get_code"
                ))
            )

            return True
        except:
            return False

    def enter_phone(self, phone):
        phone_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "username"))
        )
        phone_input.clear()
        phone_input.send_keys(phone)

    def enter_phone_get_code(self, phone):
        phone_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "address"))
        )
        phone_input.clear()
        phone_input.send_keys(phone)

    def enter_email(self, email):
        email_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "username"))
        )
        email_input.clear()
        email_input.send_keys(email)

    def enter_login(self, login):
        login_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "username"))
        )
        login_input.clear()
        login_input.send_keys(login)

    def enter_account(self, ls):
        ls_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "username"))
        )
        ls_input.clear()
        ls_input.send_keys(ls)

    def enter_password(self, password):
        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        password_input.clear()
        password_input.send_keys(password)

    def click_login_password_button(self):
        login_password_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "standard_auth_btn"))
        )
        login_password_button.click()

    def click_login_button(self):
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "kc-login"))
        )
        login_button.click()
        WebDriverWait(self.driver, 10).until(EC.url_changes(AUTHORIZATION_PASSWORD_URL))

    def click_get_code_button(self):
        get_code = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "otp_get_code"))
        )
        get_code.click()

    def is_redirect_successful(self):
        """Проверить, прошла ли успешная переадресация"""
        return self.driver.current_url != AUTHORIZATION_PASSWORD_URL

    def is_error_message_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="form-error-message" and contains(text(),"Неверный логин или пароль")]')
                )
            )
            return True
        except:
            return False

    def is_account_error_message_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((
                    By.XPATH,
                    '//*[@id="username-meta" and contains(text(),"Проверьте, пожалуйста, номер лицевого счета")]'))
            )
            return True
        except:
            return False

    def is_account_number_field_empty(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((
                    By.XPATH, '//*[@id="username-meta" and contains(text(),"Введите номер вашего лицевого счета")]'))
            )
            return True
        except:
            return False

    def is_forgot_password_element_orange(self):
        try:
            forgot_password_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "forgot_password"))
            )
            # Получаем цвет элемента
            color = forgot_password_element.value_of_css_property("color")
            # Проверяем, является ли цвет оранжевым
            return "rgba(255, 79, 18, 1)" in color
        except:
            return False

    def is_code_sent_message_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((
                    By.XPATH, '//*[@id="card-title" and contains(text(),"Код подтверждения отправлен")]'))
            )

            return True
        except:
            return False

    def is_invalid_phone_error_message_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((
                    By.XPATH, '//*[@id="address-meta" and contains(text(),'
                              '"Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru")]'))
            )

            return True
        except:
            return False

    def are_confirmation_code_fields_displayed(self):
        try:
            inputs_code = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located((
                    By.CLASS_NAME,
                    'rt-input__input.rt-sdi-container__input.code-input__input.rt-input__input--rounded.rt-input__input--orange'))
            )

            return len(inputs_code) == 6
        except:
            return False

    def is_phone_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((
                    By.XPATH, '//*[@id="otp-code-form-description" and contains(text(), "+7 999 888-77-66")]'))

            )

            return True
        except:
            return False

    def is_change_contact_link_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((
                    By.ID, 'otp-back'))
            )

            return True
        except:
            return False

    def is_countdown_timer_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((
                    By.ID, 'otp-code-timeout'))
            )
            return True
        except:
            return False
