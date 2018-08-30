from SeleniumCustom.custom.driver.chrome_driver_services import ChromeDriverManager
from enum import Enum


class DriverList(Enum):
    CHROME_DRIVER = "ChromeDriverManager"
    FIREFOX_DRIVER = "FirefoxDriverManager"


def get_driver(class_name):
    if class_name in DriverList:
        if class_name is DriverList.CHROME_DRIVER:
            return ChromeDriverManager()
