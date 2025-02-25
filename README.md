# Testing OrangeHRM - demo application
This project contains test cases for several pages on the OrangeHRM demo application using Pytest framework

## Features
* Pytest framework
* Page Object Model (POM)
* Automated logs
* HTML reports
* Data driven testing
* Multiple browser and headless browser support
* Parallel testing

## Test scenarios
* Login into the OrangeHRM site
* Testing dashboard elements
* Update employee details

## Libraries and tools
* Python
* pytest
* **allure-pytest** - automation test reporting tool 
* **html** - pytest plugin for generating html reports
* **rerunfailures** - pytest plugin to re-run failed tests
* **xdist** - pytest plugin for parallel execution
* **openpxl** - a Python library to read/write excel files

## Installation of required libraries
```
pip install -U pytest
pip install allure-pytest
pip install pytest-html
pip install pytest-rerunfailures
pip install pytest-xdist
pip install openpyxl
```
## Test execution
**Browser supported options:**
* Chrome (*--browser chrome*)
* Firefox (*--browser firefox*)

*Note: If no browser option is provided the tests will be executed on chrome!*

Both chrome and Firefox can be run in headless mode (*--headless*)

```
pytest .\Tests\test_login_page.py -s -v --html=./HtmlLogs/test_login_report.html
pytest .\Tests\test_login_page_DDT.py -s -v --html=./HtmlLogs/test_login_DDT_report.html
pytest .\Tests\test_dashboard.py -s -v --html=./HtmlLogs/test_dashboard_report.html
pytest .\Tests\test_my_page_info.py -s -v --html=./HtmlLogs/test_my_page_info_report.html
pytest .\Tests\test_update_personal_info_DDT.py -s -v --html=./HtmlLogs/test_update_my_info_report.html 
```
This will execute tests on chrome and create html reports.

For repeating failed test cases run previous lines with option *--lf*




