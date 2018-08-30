from selenium.webdriver.remote.webelement import WebElement


class WebObject(WebElement):

    def __init__(self):
        pass

    def input_text(self, text):
        try:
            self.send_keys(text)
        except Exception as e:
            print(str(e))

    def click_element(self):
        """
        wrap the click function
        """
        try:
            self.click()
        except Exception as e:
            print(str(e))
