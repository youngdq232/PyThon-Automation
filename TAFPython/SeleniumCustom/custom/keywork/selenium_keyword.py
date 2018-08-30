from SeleniumCustom.custom.driver.web_object import WebObject


class SeleniumKeyword:

    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        web_object = self.driver.find_element(*locator)
        web_object.__class__ = WebObject
        return web_object

    @staticmethod
    def is_element_displayed(web_object):
        if web_object.is_displayed():
            return True
        else:
            return False



