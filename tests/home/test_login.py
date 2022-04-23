from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from pages.home.login_page import LoginPage
import pytest


class TestLogin():
    base_url = "http://34.118.71.117"
    s = Service(r'C:\development\drivers\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.implicitly_wait(3)
    lp = LoginPage(driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login("itservices.pawelkuznik1", "Testowehaslo1!")
        result = self.lp.verify_login_successful()
        assert result is True
        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.driver.get(self.base_url)
        self.lp.login("itservices.pawelkuznik1", "Zlehaslo1!")
        result = self.lp.verify_login_failed()
        assert result is True


