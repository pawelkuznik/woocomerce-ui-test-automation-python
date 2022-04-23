from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from pages.home.login_page import LoginPage
import pytest


class TestLogin:

    def test_valid_login(self):
        base_url = "http://34.118.71.117"
        s = Service(r'C:\development\drivers\chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(base_url)
        lp = LoginPage(driver)
        lp.login("itservices.pawelkuznik1", "Testowehaslo1!")
        result = lp.verify_login_successful()
        assert result is True
        driver.quit()



