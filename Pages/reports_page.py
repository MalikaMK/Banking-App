from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from time import sleep

class ReportsPage(BasePage):
    def __init__(self, driver) -> None:
        self.driver = driver
        
    def reports(self):
        self.driver.find_element(By.CSS_SELECTOR, '[ng-reflect-router-link="/user-reports"]') .click()
        