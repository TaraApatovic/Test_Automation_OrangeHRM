from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

""" This class is parent of all Page classes 
    It contains all of the generic methodes and utilities used by pages"""

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(by_locator))
        return  element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver,20).until(EC.title_is(title))
        return self.driver.title

    def clear_element(self,by_locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).clear()

    def get_notfication(self, by_locator):
        notification = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        return notification

    def clear_element_backspace(self, element):
        element.send_keys(Keys.CONTROL + "a")  # Select all text
        element.send_keys(Keys.BACKSPACE)

