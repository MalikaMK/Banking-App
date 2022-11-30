from selenium import webdriver
from time import sleep
from Pages.login_page import LoginPage
import pytest

def test_landing_page(setup):
    driver = setup
    sleep(5)
    assert driver.title == 'EBANQ'
    
    
def test_user_login(setup):
    driver = setup
    log_page = LoginPage(driver)
    log_page.user_login()
    sleep(5)
    assert 'Log Out' in driver.page_source
    
def test_admin_login(setup):
    driver = setup
    log_page = LoginPage(driver)
    sleep(5)
    log_page.admin_login()
    sleep(5)
    assert 'Log Out' in driver.page_source
   
def test_login_with_blank_username(setup):
    driver = setup
    log_page = LoginPage(driver)
    log_page.login_with_blank_username()
    assert 'Field is required' in driver.page_source
    

    
def test_login_with_incorrect_credentials(setup):
    driver = setup
    log_page = LoginPage(driver)
    log_page.login_with_incorrect_credentials()
    sleep(5)
    assert 'Wrong username or password.' in driver.page_source

# prepering test data
invalid_login_data = [
    ('', '', 'Field irequireds'),
    ('test', 'wrong' ,'Wrong username or password'),
    ('abc', 'wrong' , 'Should be minimum 4 chars')
]

@pytest.mark.parametrize("username, password, checkpoint", invalid_login_data)
def test_invalid_login(setup, username, password, checkpoint):
    driver = setup
    login_page = LoginPage(driver)
    login_page.login(username, password)