from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from SeleniumCustom.custom.driver.options_driver_variables import OptionsDriverVariables


class ChromeDriverManager:

    def __init__(self):
        self.chOptions = Options()
        self.optionDriverConstant = OptionsDriverVariables()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def get_default_options(self):
        self.chOptions.add_argument(self.optionDriverConstant.START_MAXIMIZE_WINDOW)
        self.chOptions.add_argument(self.optionDriverConstant.IGNORE_CERTIFICATE_ERROR)
        self.chOptions.add_argument(self.optionDriverConstant.DISABLE_POPUP_BLOCKING)
        self.chOptions.add_argument(self.optionDriverConstant.INCOGNITO_MODE)
        return self.chOptions

    def create_driver(self):
        return self.driver


