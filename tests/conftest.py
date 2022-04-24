import pytest
from selenium import webdriver

from base.webdriverfactory import WebDriverFactory
@pytest.fixture()
def set_up():
    print("\nRunning method level setUp")
    yield
    print("\nRunning method level tearDown")


@pytest.fixture(scope="function")
def one_time_setup(request, browser):
    print("\nRunning one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.get_web_driver_instance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("\nRunning one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def os_type(request):
    return request.config.getoption("--osType")

