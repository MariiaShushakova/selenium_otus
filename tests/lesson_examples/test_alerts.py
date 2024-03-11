import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

URL = "https://konflic.github.io/examples/pages/alerts.html#"


@pytest.fixture
def driver():
    service = Service()
    wd = webdriver.Chrome(service=service)
    wd.get(URL)
    yield wd
    wd.quit()


def test_basic_alert(driver):
    driver.find_element(By.ID, "basic").click()
    alert = WebDriverWait(driver, 2).until(EC.alert_is_present())
    alert.dismiss() #accept()


def test_prompt_alert(driver):
    driver.find_element(By.ID, "prompt").click()
    prompt_alert = driver.switch_to.alert
    prompt_alert.send_keys("Hey!")
    alert = WebDriverWait(driver, 2).until(EC.alert_is_present())
    alert.accept()


def test_confirm_alert(driver):
    driver.find_element(By.ID, "confirm").click()
    confirm_alert = driver.switch_to.alert
    print(confirm_alert.text)
    confirm_alert.accept()


def test_custom_alert(driver):
    driver.find_element(By.CSS_SELECTOR, "a.button").click()
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.popup")))
    driver.find_element(By.CSS_SELECTOR, "a.close").click()
    WebDriverWait(driver, 1).until(EC.invisibility_of_element((By.CSS_SELECTOR, "div.popup")))
