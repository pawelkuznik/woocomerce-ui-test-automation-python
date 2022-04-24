from selenium.webdriver.common.by import By
import logging
import utilities.custom_logger as cl
from base.base_page import BasePage
from pages.home.navigation_page import NavigationPage


class LoginPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # locators
    _my_account_label = "(//a[contains(text(),'My account')])[1]"
    _my_account_after_login_label = "//h1[contains(text(),'My account')]"
    _my_account_after_failed_login_alert = "//*[contains(@class, 'woocommerce-error')]/li"
    _username_field = "username"
    _password_field = "password"
    _login_button = "//button[contains(text(),'Log in')]"

    # def click_my_account_label(self):
    #     self.element_click(self._my_account_label, locator_type="xpath")

    def enter_username(self, username):
        self.send_keys(username, self._username_field)

    def enter_password(self, password):
        self.send_keys(password, self._password_field)

    def click_login_button(self):
        self.element_click(self._login_button, locator_type="xpath")

    def login(self, username="", password=""):
        self.nav.click_my_account_label()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def verify_login_successful(self):
        result = self.is_element_presence(self._my_account_after_login_label, locator_type="xpath")
        return result

    def verify_login_failed(self):
        result = self.is_element_presence(self._my_account_after_failed_login_alert, locator_type="xpath")
        return result

    def register_with_random_email(self):
        self.nav.click_my_account_label()
        self

