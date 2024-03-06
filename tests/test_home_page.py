from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_title(browser):
    browser.get(browser.base_url)
    assert "Home Page" in browser.title


def test_check_5_elements(browser):
    browser.get(browser.base_url)
    # 1) button "Shop Now"
    WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".ui-top-0 .ui-items-center span.ui-justify-center span")))
    # 2) label Oura
    browser.find_element(By.CSS_SELECTOR, "header div.ui-fill-current")
    # 3) tab Experience
    browser.find_element(By.CSS_SELECTOR, "[data-cy='nav_ouraexperience']")
    # 4) tab Membership
    browser.find_element(By.CSS_SELECTOR, "[data-cy='nav_membership']")
    # 3) tab Community
    browser.find_element(By.CSS_SELECTOR, "[data-cy='nav_pulseblog']")


def test_switch_languages(browser):
    """test instead of switching currency"""
    browser.get(browser.base_url + "/fi")

    shop_now_fi = WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".ui-top-0 .ui-items-center span.ui-justify-center span")))

    assert shop_now_fi.text == "Osta nyt"