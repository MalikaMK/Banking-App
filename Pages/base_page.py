from time import sleep
from config import config

class BasePage:
   
    #separate variable recomended for for standart timeout
    TIMEOUT = config.TIMEOUT 
    
    
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
    