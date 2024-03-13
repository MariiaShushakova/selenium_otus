from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.base_page import BasePage


class SizePage(BasePage):
    SIZING_KIT_BTN = "[data-cy='SizingKit']"
    ADD_TO_CART_BTN = "[data-cy='button-add-to-cart']"

    def choose_size(self):
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.SIZING_KIT_BTN))).click()
        self.browser.find_element(By.CSS_SELECTOR, self.ADD_TO_CART_BTN).click()
