import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--plt", action="store", default="mobile", help="Enter platform type i.e web and mobile")


@pytest.fixture(scope="module", autouse=True)
def driver(request):
    platform = request.config.getoption("--plt")

    if platform == 'web':
        driver = webdriver.Chrome()
        driver.get("about:blank")
        request.addfinalizer(driver.quit)
        return driver
    elif platform == 'mobile':
        desired_caps={}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['browserName'] = 'chrome'
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        request.addfinalizer(driver.quit)
        return driver
    else:
        print 'only mobile and web plaforms are supported at the moment'
