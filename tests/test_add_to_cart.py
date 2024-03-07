from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest


def test_login_logout(browser):
    browser.get(browser.base_url + "/product/rings/heritage")
    WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#accept"))).click()  # accept cookies

    # choose style of ring
    WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-cy='pdp-style-option']"))).click()
    browser.find_element(By.CSS_SELECTOR, "[data-cy='button-next']").click()
    # choose color of ring
    WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-cy='pdp-finish-option']"))).click()
    browser.find_element(By.CSS_SELECTOR, "[data-cy='button-next']").click()
    # choose size of ring
    WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-cy='SizingKit']"))).click()
    browser.find_element(By.CSS_SELECTOR, "[data-cy='button-add-to-cart']").click()

    # assert cart
    WebDriverWait(browser, 2).until(EC.title_is("Oura Ring Cart"))
    product_title = browser.find_element(By.CSS_SELECTOR, "[data-cy='product-title']")
    assert product_title.text == "Oura Ring Gen3"


def test_check_5_elements(browser):
    browser.get(browser.base_url + "/product/rings/heritage")
    WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#accept"))).click()  # accept cookies

    put_ring_to_cart(browser)

    # Elements:
    WebDriverWait(browser, 2).until(EC.title_is("Oura Ring Cart"))
    # cart icon
    browser.find_element(By.CSS_SELECTOR, "[data-cy='shopping-cart']")
    # cart title
    browser.find_element(By.CSS_SELECTOR, "[data-cy='cart-title']")
    # product title
    browser.find_element(By.CSS_SELECTOR, "[data-cy='product-title']")
    # total price
    browser.find_element(By.CSS_SELECTOR, "[data-cy='product-detail-price']")
    # product image
    browser.find_element(By.CSS_SELECTOR, "[data-cy='product-image']")


def put_ring_to_cart(browser):
    # choose style of ring
    WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-cy='pdp-style-option']"))).click()
    browser.find_element(By.CSS_SELECTOR, "[data-cy='button-next']").click()
    # choose color of ring
    WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-cy='pdp-finish-option']"))).click()
    browser.find_element(By.CSS_SELECTOR, "[data-cy='button-next']").click()
    # choose size of ring
    WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-cy='SizingKit']"))).click()
    browser.find_element(By.CSS_SELECTOR, "[data-cy='button-add-to-cart']").click()