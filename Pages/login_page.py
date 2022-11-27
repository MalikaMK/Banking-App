from selenium.webdriver.common.by import By

class LoginPage:
    # constructed Method
    def __init__(self, driver) -> None:
        self.driver = driver
        
    def user_login(self):
        self.driver.find_element(By.CSS_SELECTOR, "[type = 'email']").send_keys('Demo-User')
        self.driver.find_element(By.CSS_SELECTOR, "[type = 'password']").send_keys('Demo-Access1')
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        
        