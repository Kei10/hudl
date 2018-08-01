from selenium.webdriver.common import By

class HudlHomepage():
    # Methods unique to this page lives here
    def click_login():
        LOGIN_BUTTON = (By.CSS_SELECTOR, 'a[class="btn__light--ghost mobile-login"]')

        self.click(LOGIN_BUTTON)
        return LoginPage