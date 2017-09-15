
from pages.demo_page import DemoPage

class TestDemo:

    def test_open_page(self, browser):
        """

        :param browser:
        :return:
        """
        obj = DemoPage(browser)
        obj.open_page()


    def test_verify_page_title(self, browser):
        """

        :param browser:
        :return:
        """
        obj = DemoPage(browser)
        obj.open_page()
        assert obj.driver.title == "Google"

    def test_verify_page_title1(self, browser):
        """

        :param browser:
        :return:
        """
        obj = DemoPage(browser)
        obj.open_page()
        assert obj.driver.title == "Google"
