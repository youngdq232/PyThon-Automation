from SeleniumAndPyUnit.pages.dash_board_page import DashBoardPage
from SeleniumAndPyUnit.pages.login_page import LoginPage
from enum import Enum


class PageList(Enum):
    LOGIN_PAGE = "LoginPage"
    DASH_BOARD = "DashBoardPage"


def get_page(class_name, driver):
    if class_name in PageList:
        if class_name is PageList.LOGIN_PAGE:
            return LoginPage(driver)
        elif class_name is PageList.DASH_BOARD:
            return DashBoardPage(driver)

