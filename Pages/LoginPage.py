from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import logger

from Configuration.CostumeLogger import CostumeLogger
from Pages.BasePage import BasePage
from Configuration.TestData import TestData


class LoginPage(BasePage):

    """By locators"""
    EMAIL = (By.CSS_SELECTOR, "div.oxd-form-row:nth-child(2) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)")
    PASSWORD = (By.CSS_SELECTOR, "div.oxd-form-row:nth-child(3) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)")


    LOGIN_BTN = (By.CSS_SELECTOR, '.oxd-button')
    ACC_BTN = (By.CSS_SELECTOR, '.oxd-userdropdown-tab')
    LOGOUT_BTN = (By.CSS_SELECTOR, '.oxd-dropdown-menu > li:nth-child(4) > a:nth-child(1)')

    log = CostumeLogger.log()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.LOGIN_URL)

    """Checks if element is visible on the page"""
    def does_exists(self,locator,elem):
        return self.is_visible((locator,elem))


    def login(self, username, password):
        self.driver.get(TestData.LOGIN_URL)
        self.clear_element(self.EMAIL)
        self.log.info('--------------- Entering username ---------------')
        self.do_send_keys(self.EMAIL, username)
        self.clear_element(self.PASSWORD)
        self.log.info('--------------- Entering password ---------------')
        self.do_send_keys(self.PASSWORD, password)
        self.log.info('--------------- Logging in ---------------')
        self.do_click(self.LOGIN_BTN)


    def logout(self):
        self.do_click(self.ACC_BTN)
        self.log.info('--------------- Logging out ---------------')
        self.do_click(self.LOGOUT_BTN)
