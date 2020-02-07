"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Exemple:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverFactoryInstance()
"""
import traceback
from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns :
            None
        """
        self.browser = browser
    """
        Set firefox driver and iexplorer environment based on OS (firefox gekodriver)
        firefox = r"path"
        self.firefox = webdriver.Firefox(r"path")
        
        PREFERRED: Set the path on the machine where browser will be executed 
    """


    def getWebDriverInstance(self):
        """
        Get WebDriver Instance based on the browser configuration
        :return:"WebDriver Instance"
        """
        baseUrl = "https://www.https://learn.letskodeit.com/"
        if self.browser == "chrome":
            chromedriver = r"C:\Users\Tamara\Desktop\chromedriver.exe"
            driver = webdriver.Chrome(chromedriver)
        elif self.browser == "firefox":
            # Set firefox driver
            driver = webdriver.Firefox()
        elif self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        else:
            chromedriver = r"C:\Users\Tamara\Desktop\chromedriver.exe"
            driver = webdriver.Chrome(chromedriver)
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(5)
        # Maximize the window
        driver.maximize_window()
        #Loading browser with App URL
        driver.get(baseUrl)
        return driver