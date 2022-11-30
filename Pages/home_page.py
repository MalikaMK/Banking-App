from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from time import sleep

class HomePage(BasePage):
    
    def __init__(self, driver) -> None:
        self.driver = driver
        
    def logout(self):
        self.driver.find_element(By. CSS_SELECTOR, '.controls__logout > span').click()
        