from selenium.webdriver.common.by import By


class DashBoardPageLocator:
    lbl_dashboard = (By.XPATH, "//*[@id='social-sidebar-menu']/li/a/strong")
    lbl_user_name = (By.XPATH, "//span[text() = 'Super Admin Admin' ]")
    btn_quick_booking = (By.XPATH, "//button[@class = 'btn btn-danger btn-block']")
