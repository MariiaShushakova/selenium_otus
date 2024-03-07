from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import re


def test_check_5_elements(browser):
    # need to modify base url
    browser.get(re.sub(r"(https://)ouraring.com", r"\1membership.ouraring.com", browser.base_url))
    assert "Oura Membership Hub" in browser.title

    browser.find_element(By.XPATH, "//h1[text()='Membership Hub']")
    browser.find_element(By.CSS_SELECTOR, "[alt='Ouraring']")
    browser.find_element(By.XPATH, "//a[text()='Forgot password?']")
    browser.find_element(By.CSS_SELECTOR, "[type=submit]")
    browser.find_element(By.CSS_SELECTOR, "footer")


def test_login_logout(browser):
    browser.get(re.sub(r"(https://)ouraring.com", r"\1membership.ouraring.com", browser.base_url))

    # LogIn
    WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#email"))).send_keys("mariia.shushakova+alex@gmail.com")
    browser.find_element(By.CSS_SELECTOR, "[name='password']").send_keys("Qwerty123")
    browser.find_element(By.CSS_SELECTOR, "[type=submit]").click()

    username = WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.XPATH, "//h3[text()='Email']/../p")))
    assert username.text == "mariia.shushakova+alex@gmail.com"

    # Logout
    browser.find_element(By.CSS_SELECTOR, "#accept").click()  # accept cookies
    WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.XPATH, "//button[text()='Logout']"))).click()
