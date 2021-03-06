from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)


    # Need to verify two verification points
    # If first one fails,code will not go to next verification point
    # If assert fails,it stops current  test execution and moves to the next test method
    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyTitle()
        assert result1 == True
        result2 = self.lp.verifyLoginSuccessful()
        assert result2 == True


    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("", "invalidPassword")
        result = self.lp.verifyLoginFailed()
        assert result == True


""" 
To run test set up PYTHONPATH(setPYTHONPATH=r'C:path to the project or file')
Then py.test -s -v tests/home/login_tests.py or any other location where test is located
"""