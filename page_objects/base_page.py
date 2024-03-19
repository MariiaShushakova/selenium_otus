import re


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def turn_base_url_to_membership(self):
        self.browser.get(re.sub(r"(https://)ouraring.com", r"\1membership.ouraring.com", self.browser.base_url))
        assert "Oura Membership Hub" in self.browser.title

    def turn_base_url_to_fi(self):
        self.browser.get(self.browser.base_url + "/fi")