from selenium import webdriver
from time import sleep
from Pages.login_page import LoginPage
from Pages.home_page import HomePage
import pytest

def test_logout (setup):
    driver = setup
    log_page = LoginPage(driver)
    log_page.user_login()
    hom_page = HomePage(driver)
    hom_page.logout()
    sleep(5)
    assert 'Login' in driver.page_source
    