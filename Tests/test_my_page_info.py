import os
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Configuration.CostumeLogger import CostumeLogger
from Configuration.TestData_MyPageInfo import TestData_MyPageInfo
from Tests.TestBase import BaseTest
from Pages.PersonalInfoPage import PersonalPageInfo
from selenium.webdriver.support import expected_conditions as EC


class TestMyPersonalInfoPage(BaseTest):
    log = CostumeLogger.log()


    @pytest.mark.parametrize('locator, element',[
        (By.CSS_SELECTOR, TestData_MyPageInfo.NAME_CSS),
        (By.CSS_SELECTOR, TestData_MyPageInfo.MIDDLE_NAME_CSS),
        (By.CSS_SELECTOR, TestData_MyPageInfo.LAST_NAME_CSS),
        (By.CSS_SELECTOR, TestData_MyPageInfo.EMPLOYEE_ID_CSS),
        (By.CSS_SELECTOR, TestData_MyPageInfo.OTHER_ID_CSS),
        (By.CSS_SELECTOR, TestData_MyPageInfo.DRIVERS_LICENSE_NUM_CSS),
        (By.CSS_SELECTOR, TestData_MyPageInfo.LICENSE_EXPIRATION_DATE_CSS),
        (By.CSS_SELECTOR, TestData_MyPageInfo.NATIONALITY_CSS),
        (By.CSS_SELECTOR, TestData_MyPageInfo.MARITAL_STATUS_CSS),
        (By.CSS_SELECTOR, TestData_MyPageInfo.DATE_OF_BIRTH_CSS),
        (By.CSS_SELECTOR, TestData_MyPageInfo.GENDER_MALE_CSS),
        (By.CSS_SELECTOR, TestData_MyPageInfo.GENDER_FEMALE_CSS),
        (By.CSS_SELECTOR, TestData_MyPageInfo.SAVE_BTN_CSS),
        (By.CSS_SELECTOR, TestData_MyPageInfo.BLOOD_TYPE_CSS),  n
        (By.CSS_SELECTOR, TestData_MyPageInfo.TEST_FIELD_CSS),
        (By.CSS_SELECTOR, TestData_MyPageInfo.BLOOD_TYPE_SAVE_BTN_CSS)
        ])
    @pytest.mark.element_visibility_myinfo
    def test_element_visibility(self, locator, element):
        self.log.info('--------------- Element visibility testing ---------------')
        self.myinfopage = PersonalPageInfo(self.driver)
        flag = self.myinfopage.myinfo_element_visibility(locator, element)
        if flag:
            self.log.info('--------------- Element visible ---------------')
        else:
            self.log.info('--------------- Element is not visible ---------------')

        assert flag, 'Element is not visible'

    @pytest.mark.update_employee_info
    def test_update_employee_info(self):
        self.log.info('--------------- Update employee info testing ---------------')
        self.myinfopage = PersonalPageInfo(self.driver)
        self.myinfopage.set_first_name('Exsample User')
        self.myinfopage.set_middle_name('Middle name')
        self.myinfopage.set_last_name('Last Name')
        self.myinfopage.set_employee_id('123456')
        self.myinfopage.set_other_id('987654')
        self.myinfopage.set_drivers_license_number('123456')
        self.myinfopage.set_license_expiration_date('2025-05-12')
        self.myinfopage.set_nationality('Serbian')
        self.myinfopage.set_marital_status('Married')
        self.myinfopage.set_birth_date('1996-12-15')
        self.myinfopage.set_gender('Female')
        notification = self.myinfopage.save_changes()

        assert 'Successfully' in notification.text, "Changes are not saved"

    @pytest.mark.parametrize('bloodtype', ['A+','a-', 'B+', 'b-', 'AB+', 'ab-', 'o+', 'o-'])
    @pytest.mark.costume_field
    def test_costume_fields(self, bloodtype):
        self.log.info('--------------- Update costume fields ---------------')
        self.myinfopage = PersonalPageInfo(self.driver)
        self.myinfopage.set_blood_type(bloodtype)
        self.myinfopage.set_test_field('Test')
        notification = self.myinfopage.saving_costum_fields()
        assert 'Successfully' in notification.text, "Changes are not saved"

    @pytest.mark.upload_image
    def test_uploading_image(self):
        self.log.info('--------------- Upload image ---------------')
        self.myinfopage = PersonalPageInfo(self.driver)
        self.myinfopage.upload_image()
        self.myinfopage.add_comment_to_img('Uploading test image')
        notification = self.myinfopage.save_image()

        assert 'Successfully' in notification.text, "Changes are not saved"

        file_path = os.getcwd() + "\\Screenshots\\" + 'image_uploaded_successfully.png'
        element = WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.CSS_SELECTOR, TestData_MyPageInfo.IMG_TABLE)))
        time.sleep(1)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.screenshot(file_path)
