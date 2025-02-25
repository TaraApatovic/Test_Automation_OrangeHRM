import os
import time
from time import sleep

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Configuration.TestData_MyPageInfo import TestData_MyPageInfo
from Pages.BasePage import BasePage
from Configuration.CostumeLogger import CostumeLogger
from Pages.LoginPage import LoginPage
from selenium.webdriver.support import expected_conditions as EC


class PersonalPageInfo(BasePage):
    log = CostumeLogger.log()

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self.login = LoginPage(self.driver)
            self.login.login('Admin', 'admin123')
            self.driver.get(TestData_MyPageInfo.MY_PAGE_INFO_URL)
        except:
            print ('Already logged in')
        self.log.info("Getting my info page")
        self.driver.get(TestData_MyPageInfo.MY_PAGE_INFO_URL)


    def myinfo_element_visibility(self, locator,element):
        elem= WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((locator,element)))
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        self.log.info("Element: " + elem.text)
        return self.is_visible((locator, element))


    def set_first_name(self, name):
        self.log.info('Updating personal info')
        name_field = WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.CSS_SELECTOR,TestData_MyPageInfo.NAME_CSS)))
        self.clear_element_backspace(name_field)
        self.log.info("Inserting name: "+ name)
        name_field.send_keys(name)

    def set_middle_name(self, middle_name):
        middle_name_field = self.driver.find_element(By.CSS_SELECTOR, TestData_MyPageInfo.MIDDLE_NAME_CSS)
        self.clear_element_backspace(middle_name_field)
        self.log.info("Inserting middle name: "+ middle_name)
        middle_name_field.send_keys(middle_name)

    def set_last_name(self, last_name):
        last_name_field = self.driver.find_element(By.CSS_SELECTOR, TestData_MyPageInfo.LAST_NAME_CSS)
        self.clear_element_backspace(last_name_field)
        self.log.info("Inserting last name: " + last_name)
        last_name_field.send_keys(last_name)

    def set_employee_id(self, emp_id):
        emp_id_field = self.driver.find_element(By.CSS_SELECTOR, TestData_MyPageInfo.EMPLOYEE_ID_CSS)
        self.clear_element_backspace(emp_id_field)
        self.log.info("Inserting employee id: " + emp_id)
        emp_id_field.send_keys(emp_id)

    def set_other_id(self, other_id):
        other_id_field = self.driver.find_element(By.CSS_SELECTOR, TestData_MyPageInfo.OTHER_ID_CSS)
        self.clear_element_backspace(other_id_field)
        self.log.info("Inserting other id: " + other_id)
        other_id_field.send_keys(other_id)

    def set_drivers_license_number(self, drivers_license):
        drivers_license_field = self.driver.find_element(By.CSS_SELECTOR, TestData_MyPageInfo.DRIVERS_LICENSE_NUM_CSS)
        self.clear_element_backspace(drivers_license_field)
        self.log.info("Inserting drivers license number: " + drivers_license)
        drivers_license_field.send_keys(drivers_license)

    def set_license_expiration_date(self, expiration_date):
        expiration_date_field = self.driver.find_element(By.CSS_SELECTOR, TestData_MyPageInfo.LICENSE_EXPIRATION_DATE_CSS)
        self.clear_element_backspace(expiration_date_field)
        self.log.info("Inserting drivers license expiration date: " + expiration_date)
        expiration_date_field.send_keys(expiration_date)

    def set_nationality(self, nationality):
        nationality_dropdown = self.driver.find_elements(By.CSS_SELECTOR, TestData_MyPageInfo.NATIONALITY_CSS)
        for ele in nationality_dropdown:
            if ele.text == nationality:
                self.log.info("Selecting nationality: " + nationality)
                ele.click()
                break

    def set_marital_status(self, status):
        marital_status_dropdown = self.driver.find_elements(By.CSS_SELECTOR, TestData_MyPageInfo.MARITAL_STATUS_CSS)
        for ele in marital_status_dropdown:
            if ele.text == status:
                self.log.info("Selecting marital status: " + status)
                ele.click()
                break


    def set_birth_date(self, birth_date):
        birth_date_field = self.driver.find_element(By.CSS_SELECTOR, TestData_MyPageInfo.DATE_OF_BIRTH_CSS)
        self.clear_element_backspace(birth_date_field)
        self.log.info("Inserting birth date: " + birth_date)
        birth_date_field.send_keys(birth_date)

    def set_gender(self, gender):
        if gender.lower() == 'male':
            self.driver.find_element(By.CSS_SELECTOR, TestData_MyPageInfo.GENDER_MALE_CSS).click()
            self.log.info('Selecting gender male')
        elif gender.lower() == 'female':
            self.driver.find_element(By.CSS_SELECTOR, TestData_MyPageInfo.GENDER_FEMALE_CSS).click()
            self.log.info('Selecting gender female')
        else:
            self.log.info('Wrong gender selected')
            raise Exception ("Wrong input")

    def save_changes(self):
        self.log.info('Saving changes')
        save_btn = self.driver.find_element(By.CSS_SELECTOR, TestData_MyPageInfo.SAVE_BTN_CSS)
        self.driver.execute_script("arguments[0].scrollIntoView();", save_btn)
        self.driver.execute_script("arguments[0].click();", save_btn)
        notification = self.get_notfication((By.ID, TestData_MyPageInfo.NOTIFICATON_ID))
        return notification


    def set_blood_type(self, blood_type):
        dropdown = self.driver.find_element(By.CSS_SELECTOR, TestData_MyPageInfo.BLOOD_TYPE_CSS)
        dropdown.click()
        dd_list = self.driver.find_elements(By.CSS_SELECTOR, '.oxd-select-dropdown .oxd-select-option')
        self.log.info('Desired blood type: ' + blood_type)
        for option in dd_list:
            if option.text == blood_type.upper():
                self.log.info('Selected blood type: ' + option.text)
                option.click()
                break

    def set_test_field(self, test_msg):
        test_field = self.driver.find_element(By.CSS_SELECTOR, TestData_MyPageInfo.QE_FIELD_CSS)
        self.driver.execute_script("arguments[0].scrollIntoView();", test_field)
        self.clear_element_backspace(test_field)
        self.log.info("Inserting tekst to test field: " + test_msg)
        test_field.send_keys(test_msg)

    def saving_costum_fields(self):
        self.log.info('Saving changes')
        save_btn = self.driver.find_element(By.CSS_SELECTOR, TestData_MyPageInfo.BLOOD_TYPE_SAVE_BTN_CSS)
        self.driver.execute_script("arguments[0].scrollIntoView();", save_btn)
        save_btn.click()
        notification = self.get_notfication((By.ID, TestData_MyPageInfo.NOTIFICATON_ID))
        return notification

    def upload_image(self):
        self.log.info('Upload image')
        file_path =  os.path.join(os.getcwd(),'test-data', 'test_image.jpg')
        attachement_btn = WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.CSS_SELECTOR, TestData_MyPageInfo.ADD_ATTACHMENT)))
        self.driver.execute_script("arguments[0].scrollIntoView();", attachement_btn)
        attachement_btn.click()
        file_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        self.log.info('Uploading image')
        file_input.send_keys(file_path)

    def add_comment_to_img(self, comment):
        self.log.info('Adding a comment')
        comment_section = self.driver.find_element(By.CSS_SELECTOR, TestData_MyPageInfo.COMMENT_SECTION)
        comment_section.send_keys(comment)

    def save_image(self):
        self.log.info("Saving the image")
        save_image_btn =  WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.CSS_SELECTOR, TestData_MyPageInfo.SAVE_IMAGE_BTN)))
        self.driver.execute_script("arguments[0].scrollIntoView();", save_image_btn)
        save_image_btn.click()
        notification = self.get_notfication((By.ID, TestData_MyPageInfo.NOTIFICATON_ID))
        return notification