from time import sleep
from config import config
from Logs.logger import logger

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
                logger.info(f'Waited for [{wait}] seconds for the [{text}]....')
            else:
                logger.info(f'Found the [{text}] waited {wait} seconds....')
                return True
        logger.info (f'Text [{text}] was NOT found, waited {wait} seconds....')
        return False
