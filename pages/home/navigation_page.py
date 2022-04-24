from selenium.webdriver.common.by import By
import logging
import utilities.custom_logger as cl
from base.base_page import BasePage


class NavigationPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

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

