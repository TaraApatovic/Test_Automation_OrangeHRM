import os
import openpyxl
import pytest
from Configuration.TestData import TestData
from Pages.LoginPage import LoginPage
from Tests.TestBase import BaseTest
from selenium.webdriver.common.by import By
from Configuration.CostumeLogger import CostumeLogger


class TestLoginPage(BaseTest):
    log = CostumeLogger.log()


    """First three methodes checks that are fields needed for login visible """
    @pytest.mark.parametrize('by_locator, elem',[
        (By.CSS_SELECTOR, TestData.LOGIN_BTN),
        (By.CSS_SELECTOR, TestData.EMAIL),
        (By.CSS_SELECTOR, TestData.PASSWORD)])
    @pytest.mark.element_visibility
    def test_element_visibility(self, by_locator, elem):
        self.log.info('--------------- Element visibility testing ---------------')
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.does_exists(by_locator, elem)
        if flag:
            self.log.info('--------------- Element visible ---------------')
        else:
            self.log.info('--------------- Element is not visible ---------------')

        assert flag, 'Element is not visible'


    """Parametizing test for login"""
    @pytest.mark.parametrize('username, password, expected_results',[
        (TestData.EMAIL_GOOD,TestData.PASSWORD_GOOD,True),
        (TestData.EMAIL_BAD,TestData.PASSWORD_GOOD, False),
        (TestData.EMAIL_GOOD,TestData.PASSWORD_BAD, False),
        ("","",False)])
    @pytest.mark.login
    def test_login(self,username,password,expected_results):
        self.log.info('--------------- Testing login ---------------')
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login(username, password)
        if self.driver.current_url == TestData.DASHBOARD_URL:
            login_success = True
            self.log.info('--------------- Login was successful ---------------')
            self.loginPage.logout()
        else:
            login_success = False
            self.log.info('--------------- Login was not successful ---------------')

        assert login_success == expected_results , 'Login was not successful!'
