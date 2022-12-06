from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from config import config

class LoginPage(BasePage):
    # class attribute
    username_field = By.CSS_SELECTOR, "[type = 'email']"
    password_field = By.CSS_SELECTOR, "[type = 'password']"
    submit_button = By.CSS_SELECTOR, "[type = 'submit']"
    
    
    # constructed Method
    def __init__(self, driver) -> None:
        self.driver = driver
        
    def login(self,username,password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.submit_button).click()
        
        
    def user_login(self):
        # self.login('Demo-User', 'Demo-Access1') is replaced by 
        self.login(config.User, config.User_Password)
        
    def admin_login(self):
        # self.login('Bank-Admin', 'Demo-Access1')
        self.login(config.Admin, config.Admin_password)
        
        
    # def login_with_blank_username(self):
    #     self.login('', 'Demo-Access1')
     
        
    # def login_with_incorrect_credentials(self):
    #     self.login('Test', 'Wrong')
    