from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from SeleniumCustom.custom.driver.options_driver_variables import OptionsDriverVariables


class FirefoxDriverManager():

    def __init__(self):
        self.ffOptions = Options()
        self.optionDriverConstant = OptionsDriverVariables()
        self.get_default_options()
        self.driver = webdriver.Firefox()

    def get_default_options(self):
        return self.ffOptions

