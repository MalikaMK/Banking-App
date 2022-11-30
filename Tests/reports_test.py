from selenium import webdriver
from time import sleep
from Pages.login_page import LoginPage
from Pages.reports_page import ReportsPage
import pytest

def test_reports(setup):
    driver = setup
    log_page = LoginPage(driver)
    log_page.user_login()
    report_page = ReportsPage(driver)
    report_page.reports()
    sleep(5)
    assert 'All Accounts Transactions' in driver.page_source