from time import sleep
import pytest

from pages.sm_page import CreateSurvey


def test_verify_survey_monkey_page_title(driver):
    obj = CreateSurvey(driver)
    obj.open_page_sm_home_page()
    assert "SurveyMonkey" in obj.driver.title


def test_verify_sign_in_page_title(driver):
    obj = CreateSurvey(driver)
    obj.open_page_sm_home_page()
    obj.click_on_harburger_menu()
    obj.click_on_sign_link()
    assert "Sign into your account" == obj.driver.title

def test_verify_successfully_login(driver):
    obj = CreateSurvey(driver)
    obj.open_page_sm_home_page()
    obj.click_on_harburger_menu()
    obj.click_on_sign_link()
    email = "xxxxxxx@xxxxxx"
    username = "xxxxxx"
    password = "xxxxxx"
    obj.fill_login_details(username=username, password=password)
    print "Pass"
    obj.click_on_sign_button()
    print "Pass"
    sleep(5)


