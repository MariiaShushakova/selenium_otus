from page_objects.cart_page import CartPage
from page_objects.finish_page import FinishPage
from page_objects.size_page import SizePage
from page_objects.style_page import StylePage


def test_put_ring_to_cart(browser):
    StylePage(browser).open_style_page()
    StylePage(browser).choose_style("heritage")
    FinishPage(browser).choose_color()
    SizePage(browser).choose_size()
    CartPage(browser).assert_cart()

    CartPage(browser).check_5_elements()


