from SeleniumAndPyUnit.locators.dash_board_page_locator import DashBoardPageLocator
from SeleniumAndPyUnit.locators.login_page_locator import LoginPageLocator


class LocatorGenerator:

    page_list = ["LoginPage", "DashBoardPage"]

    def __init__(self):
        print('LocatorGenerator')

    def get_locator(self, class_name):
        if class_name in self.page_list:
            if class_name is self.page_list[0]:
                return LoginPageLocator()
            elif class_name is self.page_list[1]:
                return DashBoardPageLocator()


