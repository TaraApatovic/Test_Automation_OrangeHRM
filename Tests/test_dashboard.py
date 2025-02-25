import time

import pytest
from selenium.webdriver.common.by import By
from Configuration.TestData import TestData
from Pages.DashboardPage import DashboardPage
from Tests.TestBase import BaseTest
from Configuration.CostumeLogger import CostumeLogger



class TestDashboard(BaseTest):
    log = CostumeLogger.log()

    """Looking for presence of elements on the dashboard"""
    @pytest.mark.parametrize('by_locator, elem',[
        (By.CSS_SELECTOR, TestData.TIME_AT_WORK),
        (By.CSS_SELECTOR, TestData.MY_ACTIONS),
        (By.CSS_SELECTOR, TestData.QUICK_LAUNCH),
        (By.CSS_SELECTOR, TestData.BUZZ_POSTS),
        (By.CSS_SELECTOR, TestData.EMP_ON_LEAVE),
        (By.CSS_SELECTOR, TestData.EMP_DIST_SUB_UNIT),
        (By.CSS_SELECTOR, TestData.EMP_DIST_LOCATION)
    ]) # password field
    @pytest.mark.element_testing_v
    def test_element_visibility(self, by_locator, elem):
        self.log.info("--------------- Dashboard element visibility testing ---------------")
        self.dashboard = DashboardPage(self.driver)
        flag = self.dashboard.does_exists(by_locator, elem)
        if flag:
            self.log.info("--------------- Element is visible ---------------")
            assert True
        else:
            self.log.info("--------------- Element is not visible ---------------")
            assert False

    """Testing widget titles"""
    @pytest.mark.parametrize('locator, expected_results',[
        (TestData.TIME_AT_WORK, TestData.TAW_TITLE),
        (TestData.MY_ACTIONS, TestData.MA_TITLE),
        (TestData.QUICK_LAUNCH, TestData.QL_TITLE),
        (TestData.BUZZ_POSTS, TestData.BP_TITLE),
        (TestData.EMP_ON_LEAVE, TestData.EOL_TITLE),
        (TestData.EMP_DIST_SUB_UNIT, TestData.EDSU_TITLE),
        (TestData.EMP_DIST_LOCATION, TestData.EDL_TITLE),
        ])
    @pytest.mark.element_testing_title
    def test_widget_title(self, locator, expected_results):
        self.dashboard = DashboardPage(self.driver)
        self.log.info("--------------- Testing widget title  ---------------")
        title = self.dashboard.find_element_title(locator)
        if title == expected_results:
            self.log.info(title)
            self.log.info("--------------- Title is expected  ---------------")

            assert True
        else:
            self.log.info("--------------- Title is not expected  ---------------")
            self.log.info('Expected: ' + expected_results)
            self.log.info("But got: " + title)
            assert False

    """Test time at work shortcut from dashboard"""
    @pytest.mark.time_at_work_widget
    def test_time_at_work_widget(self):
        self.dashboard = DashboardPage(self.driver)
        current_url = self.dashboard.clickable_elements(TestData.TIME_BTN)
        self.log.info("--------------- Testing time at work widget url  ---------------")
        if current_url == TestData.TIME_WIDGET_PunchIn or current_url == TestData.TIME_WIDGET_PunchOut:
            self.log.info("--------------- Time at work shortcut widget works ---------------")
            assert True
        else:
            self.log.info("--------------- Time at work shortcut widget doesnt work  ---------------")
            self.log.info('Current url: ' + current_url)
            self.log.info('Expected url: ' + TestData.TIME_WIDGET_URL )
            assert False

    """Test my actions widget buttons"""
    @pytest.mark.parametrize('locator, expected_url',[
        (TestData.EMPLOYEE_REVIEW_BTN, TestData.EMPLOYEE_REVIEW_URL),
        (TestData.SELF_REVIEW_LINK, TestData.SELF_REVIEW_URL),
        (TestData.CANDIDATES_BTN, TestData.CANDIDATES_URL),
        (TestData.CANDIDATES_LINK, TestData.CANDIDATES_URL)
    ])
    @pytest.mark.my_actions_widget
    def test_my_actions(self, locator, expected_url):
        self.dashboard = DashboardPage(self.driver)
        self.log.info("--------------- Testing My Action shortcut ---------------")
        current_url = self.dashboard.clickable_elements(locator)
        if current_url == expected_url:
            self.log.info("--------------- My Actions shortcut widget works ---------------")
            assert True
        else:
            self.log.info("--------------- My Actions shortcut widget doesnt work  ---------------")
            self.log.info('Expected url:' + expected_url)
            self.log.info('Current url:' + current_url)
            assert False

    """Testing quick launch links after clicking on icons"""
    @pytest.mark.parametrize('locator, expected_url',[
        (TestData.ASSIGN_LEAVE_BTN, TestData.ASSIGN_LEAVE_URL),
        (TestData.LEAVE_LIST, TestData.LEAVE_LIST_URL),
        (TestData.TIMESHEETS, TestData.TIMESHEETS_URL),
        (TestData.APPLY_LEAVE, TestData.APPLY_LEAVE_URL),
        (TestData.MY_LEAVE, TestData.MY_LEAVE_URL),
        (TestData.MY_TIMESHEET, TestData.MY_TIMESHEET_URL)
    ])
    @pytest.mark.quick_launch
    def test_quick_launch_shortcuts(self,locator, expected_url):
        self.dashboard = DashboardPage(self.driver)
        self.log.info("--------------- Quick launch shortcuts testing  ---------------")
        current_url = self.dashboard.clickable_elements(locator)
        if current_url == expected_url:
            self.log.info("--------------- Quick launch shortcut widget works ---------------")
            self.log.info('Expected url:' + expected_url)
            assert True
        else:
            self.log.info("--------------- Quick launch shortcut widget doesnt work  ---------------")
            self.log.info('Expected url:' + expected_url)
            self.log.info('Current url:' + current_url)
            assert False

    """Testing scroll widget - buzz latest posts"""
    @pytest.mark.scrolling_widget
    def test_scrolling_inside_widget(self):
        self.log.info("--------------- Scrolling inside widget testing  ---------------")
        self.dashboard = DashboardPage(self.driver)
        value = self.dashboard.scroll_inside_widget()
        if value:
            self.log.info("--------------- Scrolling success  ---------------")
            assert True
        else:
            self.log.info("--------------- Scrolling failed  ---------------")
            assert False

    @pytest.mark.scrolling_widget
    def test_scroll_to_top_widget(self):
        self.dashboard = DashboardPage(self.driver)
        self.log.info("--------------- Scrolling to the top of the widget testing  ---------------")
        position_value = self.dashboard.scroll_to_top_widget()
        if position_value == 0:
            self.log.info("--------------- Scrolling success  ---------------")
            assert True
        else:
            self.log.info("--------------- Scrolling failed  ---------------")
            assert False

    @pytest.mark.scrolling_widget
    def test_scrolling_with_keys(self):
        self.dashboard = DashboardPage(self.driver)
        self.log.info("--------------- Scrolling with the keys inside widget testing  ---------------")
        position_value = self.dashboard.scroll_with_keys()
        if position_value > 0:
            self.log.info("--------------- Scrolling success  ---------------")
            assert True
        else:
            self.log.info("--------------- Scrolling failed  ---------------")
            assert False

    @pytest.mark.scrolling_widget
    def test_last_item_visible(self):
        self.dashboard = DashboardPage(self.driver)
        self.log.info("--------------- Scrolling to the last item inside widget testing  ---------------")
        flag = self.dashboard.verify_last_feed_item()
        if flag:
            self.log.info("--------------- Scrolling success  ---------------")
            assert True
        else:
            self.log.info("--------------- Scrolling failed  ---------------")
            assert False

    """Testing settings of employee on the leave widget """
    @pytest.mark.emp_on_leave
    def test_popup_opens(self):
        self.dashboard = DashboardPage(self.driver)
        self.log.info("--------------- Testing employee on leave pop up ---------------")
        flag = self.dashboard.employee_on_leave_pop_up()
        if flag:
            self.log.info("--------------- Pop up window is visible  ---------------")
            assert True
        else:
            self.log.info("--------------- Pop up window is not visible  ---------------")
            assert False

    @pytest.mark.parametrize('locator, expected_msg', [
        ((By.ID, TestData.NOTIFICATION_ID), 'Successfully Updated')
    ])
    @pytest.mark.emp_on_leave
    def test_save_settings(self, locator, expected_msg):
        self.dashboard = DashboardPage(self.driver)
        self.log.info("--------------- Testing employee on leave save settings ---------------")
        notification = self.dashboard.employee_on_leave_popup_functions(locator)
        if expected_msg in notification.text:
            self.log.info("--------------- Settings are saved successfuly  ---------------")
            assert True
        else:
            self.log.info("---------------Settings are not saved  ---------------")
            assert False

    @pytest.mark.emp_on_leave
    def test_cancel_setting(self):
        self.dashboard = DashboardPage(self.driver)
        self.log.info("--------------- Testing employee on leave cancel settings ---------------")
        slider = self.dashboard.emp_on_leave_settings_window()

        if self.driver.execute_script("return arguments[0].checked;", slider) is None:
            self.log.info("--------------- Settings are canceled successfuly  ---------------")
            assert True
        else:
            self.log.info("---------------Settings are not canceled successfuly ---------------")
            assert False

    """Testing the presence of the pie-chart and legend"""
    @pytest.mark.parametrize('locator', [
        (By.CSS_SELECTOR, TestData.EMP_DIST_SUB_PIE_CHART),
        (By.CSS_SELECTOR, TestData.ENGINEERING_BTN),
        (By.CSS_SELECTOR, TestData.HR_BTN),
        (By.CSS_SELECTOR, TestData.ADMIN_BTN),
        (By.CSS_SELECTOR, TestData.CLI_SERVICE_BTN),
        (By.CSS_SELECTOR, TestData.UNASSINGED_BTN),
        (By.CSS_SELECTOR,TestData.EMP_DIST_LOC_CHART),
        (By.CSS_SELECTOR,TestData.TEXAS),
         (By.CSS_SELECTOR, TestData.NY),
        (By.CSS_SELECTOR,TestData.UNASS)])
    @pytest.mark.pie_chart
    def test_locate_pie_chart_elements(self, locator):
        self.dashboard = DashboardPage(self.driver)
        self.log.info("--------------- Testing pie-chart elements visibility ---------------")
        flag = self.dashboard.locate_pie_chart_elements(locator)
        if flag:
            self.log.info("--------------- Pie-chart element is visible ---------------")
            assert True
        else:
            self.log.info("--------------- Pie-chart element is not visible ---------------")
            assert False

        """Verifying pie-chart with screenshots """
    @pytest.mark.parametrize('locator, elem, file_name, chart', [
            (By.CSS_SELECTOR, TestData.ENGINEERING_BTN, 'Engineering_button_off_img.png', TestData.EMP_DIST_SUB_UNIT),
            (By.CSS_SELECTOR, TestData.HR_BTN, 'HR_button_off_img.png', TestData.EMP_DIST_SUB_UNIT),
            (By.CSS_SELECTOR, TestData.ADMIN_BTN, 'Admin_button_off_img.png', TestData.EMP_DIST_SUB_UNIT),
            (By.CSS_SELECTOR, TestData.CLI_SERVICE_BTN, 'Client_service_button_off_img.png', TestData.EMP_DIST_SUB_UNIT),
            (By.CSS_SELECTOR, TestData.UNASSINGED_BTN, 'Unassigned_button_off_img.png', TestData.EMP_DIST_SUB_UNIT),
            (By.CSS_SELECTOR, TestData.TEXAS, 'Texas_button_off_img.png',  TestData.EMP_DIST_LOC_CHART),
            (By.CSS_SELECTOR, TestData.NY, 'NewYork_button_off_img.png',  TestData.EMP_DIST_LOC_CHART),
            (By.CSS_SELECTOR, TestData.UNASS, 'Unassigned_button_2_off_img.png',  TestData.EMP_DIST_LOC_CHART)])
    @pytest.mark.pie_chart_ss
    def test_pie_chart_by_image(self, locator, elem, file_name, chart):
        self.dashboard = DashboardPage(self.driver)
        self.log.info("--------------- Capturing screenshot ---------------")
        flag = self.dashboard.capture_the_screenshot(locator, elem, file_name, chart)
        if flag:
            self.log.info("--------------- Screenshot captured ---------------")
            assert True
        else:
            self.log.info("--------------- Screenshot is not captured ---------------")
            assert False

    list_elem_chart1 = [TestData.ENGINEERING_BTN,TestData.HR_BTN,TestData.ADMIN_BTN,
                 TestData.CLI_SERVICE_BTN,TestData.UNASSINGED_BTN ]

    list_elem_chart2 = [TestData.TEXAS,TestData.NY,TestData.UNASS]
    @pytest.mark.parametrize('locator, list_elem, file_name, chart', [
            (By.CSS_SELECTOR, list_elem_chart1, 'First_chart_turn_off_all.png', TestData.EMP_DIST_SUB_UNIT),
            (By.CSS_SELECTOR, list_elem_chart2, 'Second_chart_turn_off_all.png', TestData.EMP_DIST_LOC_CHART)])
    @pytest.mark.pie_chart_all_ss
    def test_pie_chart_by_image_all(self, locator, list_elem, file_name, chart):
        self.dashboard = DashboardPage(self.driver)
        self.log.info("--------------- Capturing screenshot ---------------")
        flag = self.dashboard.click_all_and_capture_screenshot(locator, list_elem, file_name, chart)
        if flag:
            self.log.info("--------------- Screenshot captured ---------------")
            assert True
        else:
            self.log.info("--------------- Screenshot is not captured ---------------")
            assert False

    """Check the visibility of the menu content"""
    @pytest.mark.parametrize('by_locator, elem',[
        (By.CSS_SELECTOR, TestData.MENU),
        (By.CSS_SELECTOR, TestData.SEARCH_ELEMENT),
        (By.CSS_SELECTOR, TestData.ADMIN),
        (By.CSS_SELECTOR, TestData.PIM),
        (By.CSS_SELECTOR, TestData.LEAVE),
        (By.CSS_SELECTOR, TestData.TIME),
        (By.CSS_SELECTOR, TestData.RECRUITMENT),
        (By.CSS_SELECTOR, TestData.MY_INFO),
        (By.CSS_SELECTOR, TestData.PERFORMANCE),
        (By.CSS_SELECTOR, TestData.DASHBOARD),
        (By.CSS_SELECTOR, TestData.DIRECTORY),
        (By.CSS_SELECTOR, TestData.MEINTENENCE),
        (By.CSS_SELECTOR, TestData.CLAIM),
        (By.CSS_SELECTOR, TestData.BUZZ)
    ])
    @pytest.mark.menu_tests
    def test_menu_element_visibility(self, by_locator, elem):
        self.dashboard = DashboardPage(self.driver)
        self.log.info("--------------- Testing menu element visibility ---------------")
        flag = self.dashboard.does_exists(by_locator, elem)
        if flag:
            self.log.info("--------------- Element is visible ---------------")
            assert True
        else:
            self.log.info("--------------- Element is not visbile ---------------")
            assert False

        """Test my actions widget buttons"""
    @pytest.mark.parametrize('locator, expected_url',[
        (TestData.ADMIN, TestData.ADMIN_URL),
        (TestData.PIM, TestData.PIM_URL),
        (TestData.LEAVE, TestData.LEAVE_URL),
        (TestData.TIME, TestData.TIME_URL),
        (TestData.RECRUITMENT, TestData.RECRUITMENT_URL),
        (TestData.MY_INFO, TestData.MY_INFO_URL),
        (TestData.PERFORMANCE, TestData.PERFORMANCE_URL),
        (TestData.DASHBOARD, TestData.DASHBOARD_URL),
        (TestData.DIRECTORY, TestData.DIRECTORY_URL),
        (TestData.MEINTENENCE, TestData.MEINTENENCE_URL),
        (TestData.CLAIM, TestData.CLAIM_URL),
        (TestData.BUZZ, TestData.BUZZ_URL)
    ])
    @pytest.mark.menu_tests
    def test_menu_url(self, locator, expected_url):
        self.dashboard = DashboardPage(self.driver)
        self.log.info("--------------- Testing menu element url ---------------")
        current_url = self.dashboard.clickable_elements(locator)
        if current_url == expected_url:
            self.log.info("--------------- Menu element url is correct ---------------")
            assert True
        else:
            self.log.info("--------------- Menu element url is not correct ---------------")
            assert False

