from time import sleep
from pages.page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class EcommarcePage(Page):

    FLIPKART_SEARCH_BUTTON = (By.XPATH, "//input[@placeholder='Search for Products, Brands and More']")
    MENU = (By.XPATH, "//a[contains(@class,'_3N')]/img[@alt='menu']")
    MENU_ITEM_ELECTRONICS = (By.XPATH, "//span[text() = 'Electronics']")
    AMAZON_SEARCH_BUTTON = (By.ID, "twotabsearchtextbox")
    MOBILE_LINK_TEXT = (By.LINK_TEXT, 'Mobiles')
    NEXT_BUTTON_IN_FLIPKART = (By.XPATH, "//span[text()='Next']" )
    DEVICES_IMAGE_XPATH = (By.XPATH, "//a[@class='_1UoZlX']//div[@class='_3BTv9X']//img")
    DEVICES_DESCRIPTION_ROWS_LINKS = (By.CLASS_NAME, "_1UoZlX")
    DEVICES_DESCRIPTION_ROWS_DIVS = (By.XPATH, "//div[contains(@class,'_1-2')]")
    MOBILE_NAME_DIVS = (By.XPATH, "//div[@class ='_3wU53n']")

    def fill_flipkart_search_text_box(self, input_text):
        """

        :param input_text:
        :return: `
        """
        self.fill_text_box(self.FLIPKART_SEARCH_BUTTON, input_text)
        self.press_enter_key(self.FLIPKART_SEARCH_BUTTON)

    def fill_amazon_search_text_box(self, input_text):
        """

        :param input_text:
        :return:
        """
        self.fill_text_box(self.AMAZON_SEARCH_BUTTON, input_text)
        self.press_enter_key(self.AMAZON_SEARCH_BUTTON)

    def click_on_menu(self):
        self.click(self.MENU)
        print "Clicked in menu"

    def click_on_electronics(self):
        if self.scroll_to_element_visible(self.MENU_ITEM_ELECTRONICS):
            self.click(self.MENU_ITEM_ELECTRONICS)


    def click_on_mobile_link(self):
        self.click(self.MOBILE_LINK_TEXT)
        print "Clicked on mobile link"

    def click_on_next_button(self):
        """
        :return:
        """
        self.click(self.NEXT_BUTTON_IN_FLIPKART)
        print "Clicked on next"

    def get_mobiles_details(self):
        """

        :return:
        """
        result = {}
        sleep(5)
        # for index, div in enumerate(self.find_elements(self.DEVICES_DESCRIPTION_ROWS_DIVS)):
        for index, element in enumerate(self.find_elements(self.MOBILE_NAME_DIVS)):
                print element.text
                result[index] = element.text
        print result



