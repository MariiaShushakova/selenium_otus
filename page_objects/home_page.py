from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.base_page import BasePage


class HomePage(BasePage):

    def check_title(self):
        self.browser.get(self.browser.base_url)
        assert "Home Page" in self.browser.title

    def check_5_elements(self):
        self.browser.get(self.browser.base_url)
        # 1) button "Shop Now"
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".ui-top-0 .ui-items-center span.ui-justify-center span")))
        # 2) label Oura
        self.browser.find_element(By.CSS_SELECTOR, "header div.ui-fill-current")
        # 3) tab Experience
        self.browser.find_element(By.CSS_SELECTOR, "[data-cy='nav_ouraexperience']")
        # 4) tab Membership
        self.browser.find_element(By.CSS_SELECTOR, "[data-cy='nav_membership']")
        # 3) tab Community
        self.browser.find_element(By.CSS_SELECTOR, "[data-cy='nav_pulseblog']")

    def verify_another_lang(self):
        shop_now_fi = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".ui-top-0 .ui-items-center span.ui-justify-center span")))

        assert shop_now_fi.text == "Osta nyt"