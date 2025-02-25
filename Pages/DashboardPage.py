import os.path
import time

from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from Configuration.TestData import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


from Pages.LoginPage import LoginPage
from Configuration.CostumeLogger import CostumeLogger
from selenium.common.exceptions import TimeoutException



class DashboardPage(BasePage):
    log = CostumeLogger.log()

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self.login = LoginPage(self.driver)
            self.login.login('Admin', 'admin123')
        finally:
            self.driver.get(TestData.DASHBOARD_URL)

    def does_exists(self,locator,elem):
        txt = self.get_element_text((locator, elem))
        self.log.info("Element: " + txt)
        return self.is_visible((locator,elem))



    def find_element_title(self,locator):
        elem = self.driver.find_element(By.CSS_SELECTOR, locator)
        return elem.text

    def clickable_elements(self, locator):
        elem = self.driver.find_element(By.CSS_SELECTOR, locator)
        self.log.info('Element under test:'+elem.text)
        elem.click()
        return self.driver.current_url


    def scroll_inside_widget(self):
        widget = self.driver.find_element(By.CSS_SELECTOR, TestData.BUZZ_POST_SCROLL)
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", widget)
        scroll_position = self.driver.execute_script("return arguments[0].scrollTop;", widget)
        scroll_height = self.driver.execute_script("return arguments[0].scrollHeight;", widget)

        return scroll_position + widget.size["height"] >= scroll_height

    def scroll_to_top_widget(self):
        widget = self.driver.find_element(By.CSS_SELECTOR, TestData.BUZZ_POST_SCROLL)
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", widget)
        self.driver.execute_script("arguments[0].scrollTop = 0;", widget)
        scroll_position = self.driver.execute_script("return arguments[0].scrollTop;", widget)

        return scroll_position

    def scroll_with_keys(self):
        widget = self.driver.find_element(By.CSS_SELECTOR, TestData.BUZZ_POST_SCROLL)
        self.driver.execute_script("arguments[0].scrollIntoView();", widget)

        actions = ActionChains(self.driver)
        actions.move_to_element(widget).click().perform()
        time.sleep(2)

        widget.send_keys(Keys.PAGE_DOWN)
        widget.send_keys(Keys.PAGE_DOWN)
        scroll_position = self.driver.execute_script("return arguments[0].scrollTop;", widget)
        return scroll_position


    def verify_last_feed_item(self):
        widget = self.driver.find_element(By.CSS_SELECTOR, TestData.BUZZ_POST_SCROLL)
        self.driver.execute_script("arguments[0].scrollIntoView();", widget)

        feed_items = self.driver.find_elements(By.CSS_SELECTOR, ".oxd-grid-item.oxd-grid-item--gutters.orangehrm-buzz-widget-card")
        last_item = feed_items[-1]

        self.driver.execute_script("arguments[0].scrollIntoView();", last_item)
        time.sleep(1)

        return last_item.is_displayed()

    def employee_on_leave_pop_up(self):
        self.do_click((By.CSS_SELECTOR, TestData.EMP_ON_LEAVE_SETTINGS_BTN))
        flag = self.is_visible((By.CSS_SELECTOR, TestData.EMP_ON_LEAVE_SETTINGS_POPUP))
        return flag

    def emp_on_leave_settings_window(self):
        self.do_click((By.CSS_SELECTOR, TestData.EMP_ON_LEAVE_SETTINGS_BTN))
        time.sleep(1)
        self.do_click((By.CSS_SELECTOR, TestData.SLIDING_BUTTON))
        self.do_click((By.CSS_SELECTOR, TestData.ACCESSABLE_EMP_CANCLE_BTN))
        self.do_click((By.CSS_SELECTOR, TestData.EMP_ON_LEAVE_SETTINGS_BTN))
        slider = self.driver.find_element(By.CSS_SELECTOR, TestData.SLIDING_BUTTON)
        return slider


    def employee_on_leave_popup_functions(self,locator):
        self.do_click((By.CSS_SELECTOR, TestData.EMP_ON_LEAVE_SETTINGS_BTN))
        self.do_click((By.CSS_SELECTOR,TestData.SLIDING_BUTTON))
        self.do_click((By.CSS_SELECTOR, TestData.ACCESSABLE_EMP_SAVE_BTN))
        notification = self.get_notfication(locator)
        return notification


    def capture_the_screenshot(self, locator,elem,file_name,chart):
        file_path = os.getcwd() + "\\Screenshots\\"+file_name
        try:
            element = WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((locator, chart)))
            WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((locator, elem))).click()
        except ElementClickInterceptedException:
            ActionChains(self.driver).move_to_element(element).click().perform()
        except (NoSuchElementException, TimeoutException) as e:
            self.log.info("Element not found")
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView({block: \"center\", inline: \"center\"});", element)
        element.screenshot( file_path )
        return os.path.exists(file_path)

    def click_all_and_capture_screenshot(self,  locator,list_elem,file_name,chart):
        file_path = os.getcwd() + "\\Screenshots\\" + file_name
        for i in list_elem:
            try:
                element = WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((locator, chart)))
                WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((locator, i))).click()
            except ElementClickInterceptedException:
                ActionChains(self.driver).move_to_element(element).click().perform()
            except  TimeoutException:
                self.log.info("Element not found")
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView({block: \"center\", inline: \"center\"});",element)
        element.screenshot(file_path)
        return os.path.exists(file_path)

    def locate_pie_chart_elements(self, locator):
        elem = self.driver.find_element(By.CSS_SELECTOR, TestData.EMP_DIST_SUB_PIE_CHART)
        self.driver.execute_script("arguments[0].scrollIntoView();",elem)
        self.log.info("Element under test: "+elem.text)
        return self.is_visible(locator)





