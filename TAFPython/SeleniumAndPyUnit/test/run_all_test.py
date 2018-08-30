import unittest
from SeleniumAndPyUnit.test.login_page_test import LoginPageTest


def create_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTests(LoginPageTest())
    return test_suite


if __name__ == '__main__':
    suite = create_suite()

    runner = unittest.TextTestRunner()
    runner.run(suite)
