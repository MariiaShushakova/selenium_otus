import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

URL = "https://konflic.github.io/examples/pages/iframes.html#"


@pytest.fixture
def driver():
    service = Service()
    wd = webdriver.Chrome(service=service)
    #wd = webdriver.Firefox(executable_path=GECKODRIVER)
    wd.get(URL)
    wd.implicitly_wait(3)
    yield wd
    wd.quit()


def test_basic_alert(driver):
    frames = driver.find_elements(By.CSS_SELECTOR, "iframe")

    driver.switch_to.frame(frames[0])
    driver.find_element(By.NAME, "search").send_keys("MacBook")
    driver.switch_to.default_content()