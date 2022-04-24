from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
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


class WebDriverFactory:

    def __init__(self, browser):
        self.browser = browser

    def get_web_driver_instance(self):
        base_url = "http://34.118.71.117/"
        if self.browser == "zalenium":
            driver = webdriver.Remote(
                command_executor='http://34.118.54.87/wd/hub',
                options=webdriver.ChromeOptions()
            )
            driver.get(base_url)
            return driver
        elif self.browser == "chrome":
            s = Service(r'C:\development\drivers\chromedriver.exe')
            driver = webdriver.Chrome(service=s)
            # Setting Driver Implicit Time out for An Element
            driver.implicitly_wait(3)
            # Maximize the window
            driver.maximize_window()
            # Loading browser with App URL
            driver.get(base_url)
            return driver