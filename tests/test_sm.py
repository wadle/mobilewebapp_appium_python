from time import sleep

from pages.sm_page import SMPage

def test_demo(driver):
    obj = SMPage(driver)
    print obj.driver.get("http://www.google.com")
    sleep(2)


