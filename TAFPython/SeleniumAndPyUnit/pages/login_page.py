from SeleniumAndPyUnit.locators.locator_generator import LocatorGenerator
from SeleniumAndPyUnit.pages.base_page import BasePage
from SeleniumCustom.custom.keywork.selenium_keyword import SeleniumKeyword


class LoginPage(BasePage):
    def __init__(self, driver):
        print('LoginPage')
        locator_generator = LocatorGenerator()
        self.locator = locator_generator.get_locator(type(self).__name__)
        self.driver = driver
        self.keyword = SeleniumKeyword(self.driver)
        self.keyword.navigate_to("https://www.phptravels.net/admin")
        self.txt_email = self.keyword.find_element(self.locator.txt_email)
        self.txt_password = self.keyword.find_element(self.locator.txt_password)
        self.btn_login = self.keyword.find_element(self.locator.btn_login)


