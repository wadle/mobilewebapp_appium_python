import pytest

from selenium import webdriver


class WebDriver(object):
    """
    Initilization of browser
    """

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("about:blank")
        self.driver.implicitly_wait(10)
        # self.driver.maximize_window()

    def quite(self):
        """
        Terminate the browser session
        :return:
        """
        self.driver.quit()


@pytest.fixture(scope="session")
def browser(request):
    driver = WebDriver()
    print "Browser initialized"
    request.addfinalizer(driver.quite)
    print "Browser teardown"
    return driver

def pytest_addoption(parser):
    print help(parser)


def pytest_generate_tests(metafunc):
    print getattr(metafunc.function, "test", None)
    # print (metafunc.funcargnames)
    # print metafunc.fixturenames
    print "demoooooooooooo"
