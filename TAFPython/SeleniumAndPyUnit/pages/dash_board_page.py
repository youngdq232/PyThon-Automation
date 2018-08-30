from SeleniumAndPyUnit.pages.base_page import BasePage
from SeleniumAndPyUnit.locators.locator_generator import LocatorGenerator
from SeleniumCustom.custom.keywork.selenium_keyword import SeleniumKeyword


class DashBoardPage(BasePage):
    def __init__(self, driver):
        print('LoginPage')
        locator_generator = LocatorGenerator()
        self.locator = locator_generator.get_locator(type(self).__name__)
        print(type(self.locator).__name__)
        self.driver = driver
        self.keyword = SeleniumKeyword(self.driver)
        self.lbl_dash_board = self.keyword.find_element(self.locator.lbl_dashboard)
        self.btn_quick_booking = self.keyword.find_element(self.locator.btn_quick_booking)
        self.lbl_user_name = self.keyword.find_element(self.locator.lbl_user_name)
