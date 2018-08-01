from selenium.webdriver.common import By

class HudlHomepage():
    def click_login():
        LOGIN_BUTTON = (By.CSS_SELECTOR, 'a[class="btn__light--ghost mobile-login"]')

        self.click(LOGIN_BUTTON)
        return LoginPage