from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--base_url", default="https://ouraring.com")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    base_url = request.config.getoption("--base_url")
    driver = None

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "ff":
        driver = webdriver.Firefox()

    driver.maximize_window()
    driver.base_url = base_url

    yield driver
    driver.close()

