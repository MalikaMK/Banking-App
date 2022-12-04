from time import sleep

class BasePage:
    User = 'Demo-User'
    User_Password = 'Demo-Access1'
    Admin = 'Bank-Admin'
    Admin_password = 'Demo-Access1'
    TIMEOUT = 15   #separate variable recomended for for standart timeout
    
    def __init__(self, driver) -> None:
        self.driver = driver
             
    def text_exists(self, text):
        wait = 0
        while wait < self.TIMEOUT:
    # self.TIMEOUT because we have variable TIMEOUT instead of hard coding(while wait<15)
            if text.lower() not in self.driver.page_source.lower():
                sleep(1)
                wait+=1
            else:
                return True
        return False
    