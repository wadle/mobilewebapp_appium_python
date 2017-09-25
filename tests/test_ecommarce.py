import os
 
from time import sleep
from pages.ecommarce_page import EcommarcePage


class TestEcommarce:

    BASE_PAGE = "https://www.flipkart.com/"
    SEARCH_TEXT = "samsung"

    def test_search_samsung_mobile_on_flipkart(self, driver):

        obj = EcommarcePage(driver)
        obj.driver.get(self.BASE_PAGE)
        obj.fill_flipkart_search_text_box(self.SEARCH_TEXT)
        sleep(3)
        obj.click_on_mobile_link()
        obj.get_mobiles_details()
        sleep(10)
        print "pass"

    def test_(self):
        pass