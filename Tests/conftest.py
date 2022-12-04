import pytest
from selenium import webdriver
from datetime import datetime
import os
from Pages.login_page import LoginPage

def launch_app():
    driver = webdriver.Firefox()
    driver.get('https://demo.ebanq.com/log-in')
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

def teardown(driver):
    # take a screenshot
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
    timestamp = datetime.now().strftime('%m%d%y_%H%M%S')
    # for screenshot with timestamp variable 
    # driver.save_screenshot(f'.\evidence\{timestamp}.png') OR 
    driver.save_screenshot(fr'.\evidence\{test_name}_{timestamp}.png')   
    driver.quit()


@pytest.fixture()
def setup():
    driver = launch_app()
    yield driver
    teardown(driver)

@pytest.fixture()
def user_setup():
    # # steps you run before each test case 
    # driver = webdriver.Firefox()
    # driver.get('https://demo.ebanq.com/log-in')
    # driver.maximize_window()
    # driver.implicitly_wait(10) those steps were replaced by driver = launch_app
    driver = launch_app()
    log_page = LoginPage(driver)
    log_page.user_login()
    yield driver
    teardown(driver)

    
@pytest.fixture()
def admin_setup():
    driver = launch_app()
    log_page = LoginPage(driver)
    log_page.admin_login()
    yield driver
    teardown(driver)