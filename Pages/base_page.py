class BasePage:
    User = 'Demo-User'
    User_Password = 'Demo-Access1'
    Admin = 'Bank-Admin'
    Admin_password = 'Demo-Access1'
    TIMEOUT = 9
    
    def __init__(self, driver) -> None:
        self.driver = driver