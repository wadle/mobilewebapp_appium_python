from time import sleep
from pages.naukri_page import NaukriPage


class TestNaukri:
    """

    """
    EMAIL = "XXXXXXXXXX@XXXXXX.com"
    PASSWORD = "XXXXXXXXX"

    def test_login_successfully(self, browser):
        """
         """
        naukri_page_obj = NaukriPage(browser)
        naukri_page_obj.open_noukri_home_page()
        naukri_page_obj.click_on_login()
        assert naukri_page_obj.is_login_pop_up_open()
        naukri_page_obj.fill_email(self.EMAIL)
        naukri_page_obj.fill_password(self.PASSWORD)
        naukri_page_obj.click_on_login_button()
        assert "Mynaukri" ==  naukri_page_obj.driver.title

    def test_close_windows(self, browser):
        naukri_page_obj = NaukriPage(browser)
        naukri_page_obj.open_noukri_home_page()
        open_winsdows = naukri_page_obj.driver.window_handles
        print naukri_page_obj.closed_open_windows(open_winsdows)
        print "Window closed"

    def test_update_resume(self, browser):
        """

        :param webdriver_handle:
        :return:
        """
        naukri_page_obj = NaukriPage(browser)
        naukri_page_obj.open_noukri_home_page()
        naukri_page_obj.click_on_login()
        assert naukri_page_obj.is_login_pop_up_open()
        naukri_page_obj.fill_email(self.EMAIL)
        naukri_page_obj.fill_password(self.PASSWORD)
        naukri_page_obj.click_on_login_button()
        open_winsdows = naukri_page_obj.driver.window_handles
        if len(open_winsdows) > 1 :
            print naukri_page_obj.closed_open_windows(open_winsdows)
            print "Window closed"
        naukri_page_obj.click_on_view_profile_button()
        assert "Profile" in naukri_page_obj.driver.title
        naukri_page_obj.click_on_upload_new_resume()
        assert naukri_page_obj.is_upload_pop_up_open()
        path = "xxxxx/xxxxx"
        naukri_page_obj.upload_file(file=path)
        naukri_page_obj.click_on_save_button_in_upload_resume()





