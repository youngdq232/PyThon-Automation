from SeleniumCustom.custom.keywork.selenium_keyword import SeleniumKeyword


class KeywordManager:

    keyList = ["SeleniumDriver"]

    def get_keyword_type(self, class_name):
        if class_name in self.keyList:
            if class_name is self.keyList[0]:
                return SeleniumKeyword
