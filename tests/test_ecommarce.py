
from time import sleep
from pages.ecommarce_page import EcommarcePage


class TestEcommarce:
    """

    """
    BASE_PAGE = "https://www.flipkart.com/"
    SEARCH_TEXT = "samsung"

    def test_open_page(self, browser):

        obj = EcommarcePage(browser)
        obj.driver.get(self.BASE_PAGE)
        obj.fill_flipkart_search_text_box(self.SEARCH_TEXT)
        sleep(3)
        obj.click_on_mobile_link()
        obj.get_mobiles_details()

        sleep(10)
        print "pass"
