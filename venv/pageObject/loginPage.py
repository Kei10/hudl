from selenium.webdriver.common import By

class LoginPage(HudlHomePage):
    # Methods unique to this page lives here
    def type_username(self,username):
        USERNAME_FIELD = (By.CSS_SELECTOR, 'input[name="username"]')

        self.click(USERNAME_FIELD)
        self.type(username)
        return self

    def type_password(self,password):
        PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[name="password"]')
        
        self.click(PASSWORD_FIELD)
        self.type(password)
        return self

    def submit_login(self):
        SUBMIT_LOGIN_BUTTON = (By.CSS_SELECTOR, 'div[class="login-go"]')

        self.click(SUBMIT_LOGIN_BUTTON)
        return DashboardPage