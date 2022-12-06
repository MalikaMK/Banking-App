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
    # sleep(5)
    # assert 'Login' in driver.page_source
    assert log_page.text_exists ('logout') 
    
def test_admin_login(setup):
    driver = setup
    log_page = LoginPage(driver)
    sleep(5)
    log_page.admin_login()
    # sleep(5)
    # assert 'Log Out' in driver.page_source
    assert log_page.text_exists ('log Out') 
  
        # we don`t need that case because we parametrize and keep test cases with invalid and blank data values `
# def test_login_with_blank_username(setup):
#     driver = setup
#     log_page = LoginPage(driver)
#     log_page.login_with_blank_username()
#     assert 'Field is required' in driver.page_source
    
          # we don`t need that case because we parametrize and keep test cases with invalid and blank data values `   
# def test_login_with_incorrect_credentials(setup):
#     driver = setup
#     log_page= LoginPage(driver)
#     sleep(5)
#     log_page.login_with_incorrect_credentials()
#     assert 'Wrong username or password.' in driver.page_source


# preparing test data
invalid_login_data = [
    ('', '', 'Field is required'),
    ('test' , 'Demo-Access1' ,'Wrong username or password.'),
    ('abc', 'wrong' , 'Should be minimum 4 chars.')
]

@pytest.mark.parametrize("username, password, checkpoint", invalid_login_data)
def test_invalid_login(setup, username, password, checkpoint):
    driver = setup
    log_page = LoginPage(driver)
    # sleep(3)
    log_page.login(username, password)
    # sleep(3)
    # assert checkpoint in driver.page_source
    assert log_page.text_exists (checkpoint)