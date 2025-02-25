"""This script is used to store testing data"""
from selenium.webdriver.common.by import By


class TestData:
    BASE_URL = 'https://opensource-demo.orangehrmlive.com'
    LOGIN_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

    """Testing credentials for login"""
    EMAIL_GOOD = 'Admin'
    EMAIL_BAD = 'ExampleUser'
    PASSWORD_GOOD = 'admin123'
    PASSWORD_BAD = 'examplepassword'

    EMAIL ="div.oxd-form-row:nth-child(2) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)"
    PASSWORD = "div.oxd-form-row:nth-child(3) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)"

    LOGIN_BTN = '.oxd-button'
    ACC_BTN = '.oxd-userdropdown-tab'
    LOGOUT_BTN = '.oxd-dropdown-menu > li:nth-child(4) > a:nth-child(1)'

    """Dashboard content"""

    DASHBOARD_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    """CSS selectors for dashboard content"""
    TIME_AT_WORK = ".orangehrm-dashboard-grid > div:nth-child(1) > div:nth-child(1)"
    TAW_TITLE = 'Time at Work'

    MY_ACTIONS = "div.orangehrm-dashboard-widget:nth-child(2) > div:nth-child(1)"
    MA_TITLE = 'My Actions\nNo Pending Actions to Perform'


    QUICK_LAUNCH = "div.orangehrm-dashboard-widget:nth-child(3) > div:nth-child(1)"
    QL_TITLE = "Quick Launch"

    BUZZ_POSTS = "div.orangehrm-dashboard-widget:nth-child(4) > div:nth-child(1)"
    BP_TITLE = 'Buzz Latest Posts'

    EMP_ON_LEAVE = ".emp-leave-chart"
    EOL_TITLE = 'Employees on Leave Today'

    EMP_DIST_SUB_UNIT = "div.orangehrm-dashboard-widget:nth-child(6)"
    EDSU_TITLE ='Employee Distribution by Sub Unit'

    EMP_DIST_LOCATION = "div.oxd-grid-item:nth-child(7) > div:nth-child(1)"
    EDL_TITLE = 'Employee Distribution by Location'

    """Time at work elements"""
    TIME_BTN = 'button.oxd-icon-button:nth-child(2)'
    TIME_WIDGET_PunchIn = 'https://opensource-demo.orangehrmlive.com/web/index.php/attendance/punchIn'
    TIME_WIDGET_PunchOut = 'https://opensource-demo.orangehrmlive.com/web/index.php/attendance/punchOut'

    """My actions elements"""
    """Here is  note that icon for pending self review and link Pending self review goes to different web pages
    So potentially this could be a bug if that behaviour isn't expected"""
    EMPLOYEE_REVIEW_BTN = '.oxd-icon-button--danger'
    EMPLOYEE_REVIEW_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/performance/searchEvaluatePerformanceReview'

    SELF_REVIEW_LINK = 'div.orangehrm-todo-list-item:nth-child(1) > p:nth-child(2)'
    SELF_REVIEW_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/performance/myPerformanceReview'

    CANDIDATES_BTN = '.oxd-icon-button--info'
    CANDIDATES_LINK = 'div.orangehrm-todo-list-item:nth-child(2) > p:nth-child(2)'

    CANDIDATES_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates?statusId=4'



    """Quick launch elements"""
    ASSIGN_LEAVE_BTN = 'div.orangehrm-quick-launch-card:nth-child(1) > button:nth-child(1) > svg:nth-child(1)'
    LEAVE_LIST = 'div.orangehrm-quick-launch-card:nth-child(2) > button:nth-child(1) > svg:nth-child(1)'
    TIMESHEETS = 'div.orangehrm-quick-launch-card:nth-child(3) > button:nth-child(1) > svg:nth-child(1)'
    APPLY_LEAVE = 'div.orangehrm-quick-launch-card:nth-child(4) > button:nth-child(1) > svg:nth-child(1)'
    MY_LEAVE = 'div.orangehrm-quick-launch-card:nth-child(5) > button:nth-child(1) > svg:nth-child(1)'
    MY_TIMESHEET = 'div.orangehrm-quick-launch-card:nth-child(6) > button:nth-child(1) > svg:nth-child(1)'

    ASSIGN_LEAVE_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/leave/assignLeave'
    LEAVE_LIST_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveList'
    TIMESHEETS_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/time/viewEmployeeTimesheet'
    APPLY_LEAVE_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/leave/applyLeave'
    MY_LEAVE_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewMyLeaveList'
    MY_TIMESHEET_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/time/viewMyTimesheet'

    """Buzz post elements - scroll"""
    BUZZ_POST_SCROLL = '.--scroll-visible'
    BUZZ_LAST_POST = 'div.orangehrm-buzz-widget-card:nth-child(4)'
    BUZZ_POST_MIDDLE = 'div.orangehrm-buzz-widget-card:nth-child(3)'

    """Employee on the leave widget"""
    EMP_ON_LEAVE_SETTINGS_BTN = '.bi-gear-fill'
    EMP_ON_LEAVE_SETTINGS_POPUP = '.oxd-dialog-sheet'

    """Pop-up window buttons"""
    SLIDING_BUTTON= '.oxd-switch-input'
    ACCESSABLE_EMP_SAVE_BTN = 'button.oxd-button:nth-child(2)'
    ACCESSABLE_EMP_CANCLE_BTN = 'button.oxd-button:nth-child(1)'
    NOTIFICATION_ID  = 'oxd-toaster_1'



    """Employee Distribution by Sub Unit - pie-chart locators"""

    EMP_DIST_SUB_PIE_CHART = 'div.orangehrm-dashboard-widget:nth-child(6) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)'
    LEGEND_ITEMS = 'oxd-chart-legend-key'
    ENGINEERING_BTN = 'div.orangehrm-dashboard-widget:nth-child(6) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > span:nth-child(2)'
    HR_BTN = 'div.orangehrm-dashboard-widget:nth-child(6) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(2) > li:nth-child(2) > span:nth-child(2)'
    ADMIN_BTN = 'div.orangehrm-dashboard-widget:nth-child(6) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(2) > li:nth-child(3) > span:nth-child(2)'
    CLI_SERVICE_BTN = 'div.orangehrm-dashboard-widget:nth-child(6) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(2) > li:nth-child(4) > span:nth-child(2)'
    UNASSINGED_BTN = 'div.orangehrm-dashboard-widget:nth-child(6) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(2) > li:nth-child(5) > span:nth-child(2)'



    """Employee Distribution by Location - pie-chart loacators"""
    EMP_DIST_LOC_CHART = 'div.oxd-grid-item:nth-child(7)'
    TEXAS = 'div.oxd-grid-item:nth-child(7) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > span:nth-child(2)'
    NY = 'div.oxd-grid-item:nth-child(7) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(2) > li:nth-child(2) > span:nth-child(2)'
    UNASS  = 'div.oxd-grid-item:nth-child(7) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > ul:nth-child(2) > li:nth-child(3) > span:nth-child(2)'




    """Menue content"""
    MENU = ".oxd-sidepanel-body"
    SEARCH_ELEMENT = ".oxd-main-menu-search"
    ADMIN = "li.oxd-main-menu-item-wrapper:nth-child(1) > a:nth-child(1)"
    PIM = "li.oxd-main-menu-item-wrapper:nth-child(2) > a:nth-child(1)"
    LEAVE = "li.oxd-main-menu-item-wrapper:nth-child(3) > a:nth-child(1)"
    TIME = "li.oxd-main-menu-item-wrapper:nth-child(4) > a:nth-child(1)"
    RECRUITMENT = "li.oxd-main-menu-item-wrapper:nth-child(5) > a:nth-child(1)"
    MY_INFO = "li.oxd-main-menu-item-wrapper:nth-child(6) > a:nth-child(1)"
    PERFORMANCE = "li.oxd-main-menu-item-wrapper:nth-child(7) > a:nth-child(1)"
    DASHBOARD = "li.oxd-main-menu-item-wrapper:nth-child(8) > a:nth-child(1)"
    DIRECTORY = "li.oxd-main-menu-item-wrapper:nth-child(9) > a:nth-child(1)"
    MEINTENENCE = "li.oxd-main-menu-item-wrapper:nth-child(10) > a:nth-child(1)"
    CLAIM = "li.oxd-main-menu-item-wrapper:nth-child(11) > a:nth-child(1)"
    BUZZ = "li.oxd-main-menu-item-wrapper:nth-child(12) > a:nth-child(1)"


    """Menue content urls"""

    ADMIN_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers'
    PIM_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"
    LEAVE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveList"
    TIME_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/time/viewEmployeeTimesheet"
    RECRUITMENT_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates"
    MY_INFO_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7"
    PERFORMANCE_URL= "https://opensource-demo.orangehrmlive.com/web/index.php/performance/searchEvaluatePerformanceReview"
    DASHBOARD_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    DIRECTORY_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/directory/viewDirectory"
    MEINTENENCE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/maintenance/purgeEmployee"
    CLAIM_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/claim/viewAssignClaim"
    BUZZ_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz"