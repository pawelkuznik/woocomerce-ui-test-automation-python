from selenium.webdriver.chrome.service import Service

"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver


class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def get_web_driver_instance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        base_url = "http://34.118.71.117/"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            s = Service(r'C:\development\drivers\chromedriver.exe')
            driver = webdriver.Chrome(service=s)
        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(base_url)
        return driver