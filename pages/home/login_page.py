from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _my_account_label = "(//a[contains(text(),'My account')])[1]"
    _my_account_after_login_label = "//h1[contains(text(),'My account')]"
    _my_account_after_failed_login_alert = "//*[contains(@class, 'woocommerce-error')]/li"
    _username_field = "username"
    _password_field = "password"
    _login_button = "//button[contains(text(),'Log in')]"

    def click_my_account_label(self):
        self.element_click(self._my_account_label, locator_type="xpath")

    def enter_username(self, username):
        self.send_keys(username, self._username_field)

    def enter_password(self, password):
        self.send_keys(password, self._password_field)

    def click_login_button(self):
        self.element_click(self._login_button, locator_type="xpath")

    def login(self, username="", password=""):
        self.click_my_account_label()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def verify_login_successful(self):
        result = self.is_element_presence(self._my_account_after_login_label, locator_type="xpath")
        return result

    def verify_login_failed(self):
        result = self.is_element_presence(self._my_account_after_failed_login_alert, locator_type="xpath")
        return result

