from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from time import sleep

class HomePage(BasePage):
    
    def __init__(self, driver) -> None:
        self.driver = driver
        
    def logout(self):
        self.driver.find_element(By. CSS_SELECTOR, '.controls__logout > span').click()
        
    def get_side_menus(self):
        side_menus = self.driver.find_elements(By.CSS_SELECTOR, '.aside__label')
        return{menu.text.lower() for menu in side_menus}
        
    