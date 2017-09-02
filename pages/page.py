
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class Page(object):

    def __init__(self, browser):
        self.driver = browser.driver
        # self.webdriver_handle = browser

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

    def fill_text_box(self, locator, text):
        """

        :param locator:
        :param text:
        :return:
        """
        self.find_element(locator).send_keys(text)

    def press_enter_key(self, locator):
        """

        :param locator:
        :return:
        """
        self.find_element(locator).send_keys(Keys.ENTER)
        print "Enter key pressed"


    def wait_text_visible(self, text, time_out = 10):
        """

        :param text:
        :param time_out
        :return:
        """
        try:
            element = WebDriverWait(self.driver, timeout=time_out).until(lambda element: self.driver.find_element(By.XPATH, "//*contains(text(),'%s')"%text))
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


