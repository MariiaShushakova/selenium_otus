from page_objects.base_page import BasePage
from page_objects.membership_page import MembershipPage


def test_login_logout(browser):
    BasePage(browser).turn_base_url_to_membership()
    MembershipPage(browser).verify_5_elements()

    MembershipPage(browser).login("mariia.shushakova+alex@gmail.com", "Qwerty123")
    MembershipPage(browser).verify_user("mariia.shushakova+alex@gmail.com")
    MembershipPage(browser).logot()







