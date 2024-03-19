from page_objects.base_page import BasePage
from page_objects.home_page import HomePage


def test_home_page(browser):
    HomePage(browser).check_title()
    HomePage(browser).check_5_elements()


def test_switch_languages(browser):
    """test instead of switching currency"""
    BasePage(browser).turn_base_url_to_fi()
    HomePage(browser).verify_another_lang()
