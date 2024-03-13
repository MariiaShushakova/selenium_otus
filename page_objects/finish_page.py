from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.base_page import BasePage


class FinishPage(BasePage):

    def choose_color(self):
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-cy='pdp-finish-option']"))).click()
        self.browser.find_element(By.CSS_SELECTOR, "[data-cy='button-next']").click()
