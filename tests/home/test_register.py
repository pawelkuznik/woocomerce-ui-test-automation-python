from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from pages.home.login_page import LoginPage
from utilities.status_tests import StatusTests
import pytest


@pytest.mark.usefixtures("one_time_setup", "set_up")
class TestRegister:

    def test_register(self):
        pass


