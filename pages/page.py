from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

URL = "https://www.surveymonkey.com/"

class Page(object):

    def __init__(self, driver):
        self._driver = driver

    @property
    def driver(self):
        return self._driver

    def open_web_page(self, url):
        """
        Open the web page as per given url
        :param url:
        :return:
        """
        self.driver.get(url)

    def find_element(self, locator):
        """
        :param locator:
        :return:
        """

        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        """
        :param locator:
        :return:
        """
        return self.driver.find_elements(*locator)

    def click(self, locator):
        """
        :param locator:
        :return:
        """
        self.find_element(locator).click()

    def get_page_title(self):
        """
        Get page title
        :return:
        """
        page_title = self.driver.title
        if page_title:
            return page_title
        return None

    def fill_text_box(self, locator, text):
        """
        :param locator:
        :param text:
        :return:
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def press_enter_key(self, locator):
        """
        :param locator:
        :return:
        """
        self.find_element(locator).send_keys(Keys.ENTER)
        print "Enter key pressed"

    def wait_text_visible(self, text, time_out=10):
        """
        :param text:
        :param time_out
        :return:
        """
        try:
            element = WebDriverWait(self.driver, timeout=time_out).until(
                lambda element: self.driver.find_element(By.XPATH, "//*contains(text(),'%s')" % text))
            if element:
                return True
        except:
            return False

    def is_element_present(self, locator):
        """
        :param locator:
        :return:
        """
        try:
            self.find_element(locator)
            return True
        except NoSuchElementException:
            return False

    def scroll_to_element_visible(self, locator):
        is_scroll = False
        if self.find_element(locator).location_once_scrolled_into_view:
            is_scroll = True
            return is_scroll
        return is_scroll

    def page_reload(self):
        self.driver.refresh()
        print "Page reloaded"

