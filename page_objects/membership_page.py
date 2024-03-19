from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.base_page import BasePage


class MembershipPage(BasePage):

    def verify_5_elements(self):
        BasePage(self.browser).turn_base_url_to_membership()

        self.browser.find_element(By.XPATH, "//h1[text()='Membership Hub']")
        self.browser.find_element(By.CSS_SELECTOR, "[alt='Ouraring']")
        self.browser.find_element(By.XPATH, "//a[text()='Forgot password?']")
        self.browser.find_element(By.CSS_SELECTOR, "[type=submit]")
        self.browser.find_element(By.CSS_SELECTOR, "footer")

    def login(self, mail, key):
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#email"))).send_keys(mail)
        self.browser.find_element(By.CSS_SELECTOR, "[name='password']").send_keys(key)
        self.browser.find_element(By.CSS_SELECTOR, "[type=submit]").click()

    def verify_user(self, user):
        username = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located((By.XPATH, "//h3[text()='Email']/../p")))
        assert username.text == user

    def logot(self):
        self.browser.find_element(By.CSS_SELECTOR, "#accept").click()  # accept cookies
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located((By.XPATH, "//button[text()='Logout']"))).click()