import unittest
from SeleniumCustom.custom.driver.driver_manager import  get_driver, DriverList
from SeleniumCustom.custom.keywork.selenium_keyword import SeleniumKeyword
from SeleniumCustom.custom.multiple_asserts.multiple_asserts import expect as multiple_assert, assert_expectations as assert_verify
from SeleniumAndPyUnit.pages.page_generator import get_page, PageList


class LoginPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver(DriverList.CHROME_DRIVER).create_driver()
        self.loginPage = get_page(PageList.LOGIN_PAGE, self.driver)
        self.keyword = SeleniumKeyword(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login_to_admin_page_successful(self):
        self.loginPage.txt_email.input_text("admin@phptravels.com")
        self.loginPage.txt_password.input_text("demoadmin")
        self.loginPage.btn_login.click()

        dash_board_page = get_page(PageList.DASH_BOARD, self.driver)
        multiple_assert(self.keyword.is_element_displayed(dash_board_page.lbl_dash_board),
                        'Dash board label is not show')
        multiple_assert(self.keyword.is_element_displayed(dash_board_page.btn_quick_booking),
                        'Quick Booking label is not show')
        multiple_assert(self.keyword.is_element_displayed(dash_board_page.lbl_user_name), 'Username is not hsow')
        assert_verify()

    def test_multiple_assert_eeeeee(self):
        multiple_assert(not(self.keyword.is_element_displayed(self.loginPage.txt_email)), "tao thich failed!!! Y Kien?")
        multiple_assert(1 == 2, "test choi 1")
        multiple_assert(1 == 2, "test choi 2")
        multiple_assert(1 == 2, "test choi 3")
        multiple_assert(1 == 2, "test choi 4")
        assert_verify()

if __name__ == '__main__':
    unittest.main()