from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from pages.home.login_page import LoginPage
from utilities.status_tests import StatusTests
import pytest


@pytest.mark.usefixtures("one_time_setup", "set_up")
class TestLogin:

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        self.lp = LoginPage(self.driver)
        self.ts = StatusTests(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login("itservices.pawelkuznik1", "Testowehaslo1!")
        result = self.lp.verify_login_successful()
        self.ts.mark_final("test_valid_login", result, "Login verification")
        assert result is True

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.lp.login("itservices.pawelkuznik1", "Zlehaslo1!")
        result = self.lp.verify_login_failed()
        assert result is True


