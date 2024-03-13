from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.base_page import BasePage


class StylePage(BasePage):
    BTN_ACCEPT = "#accept"

    def open_style_page(self):
        self.browser.get(self.browser.base_url + "/product/rings/heritage")
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.BTN_ACCEPT))).click()  # accept cookies

    def choose_style(self, style):
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-cy='pdp-style-option']"))).click()
        self.browser.find_element(By.CSS_SELECTOR, "[data-cy='button-next']").click()
