from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.base_page import BasePage


class CartPage(BasePage):
    PRODUCT_TITLE = "[data-cy='product-title']"
    SHOPPING_CART = "[data-cy='shopping-cart']"
    CART_TITLE = "[data-cy='cart-title']"
    PRODUCT_PRICE = "[data-cy='product-detail-price']"
    PRODUCT_IMAGE = "[data-cy='product-image']"

    def assert_cart(self):
        WebDriverWait(self.browser, 2).until(EC.title_is("Oura Ring Cart"))
        product_title = WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.PRODUCT_TITLE))).text

        assert product_title == "Oura Ring Gen3"

    def check_5_elements(self):
        # cart icon
        self.browser.find_element(By.CSS_SELECTOR, self.SHOPPING_CART)
        # cart title
        self.browser.find_element(By.CSS_SELECTOR, self.CART_TITLE)
        # product title
        self.browser.find_element(By.CSS_SELECTOR, self.PRODUCT_TITLE)
        # total price
        self.browser.find_element(By.CSS_SELECTOR, self.PRODUCT_PRICE)
        # product image
        self.browser.find_element(By.CSS_SELECTOR, self.PRODUCT_IMAGE)
