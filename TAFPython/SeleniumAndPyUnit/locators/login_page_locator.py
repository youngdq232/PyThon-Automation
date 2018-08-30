from selenium.webdriver.common.by import By


class LoginPageLocator:
    txt_email = (By.XPATH, "//input[@name = 'email' and @type = 'text']")
    txt_password = (By.XPATH, "//input[@type = 'password']")
    btn_login = (By.XPATH, "//button[@class = 'btn btn-primary btn-block ladda-button fadeIn animated']")




