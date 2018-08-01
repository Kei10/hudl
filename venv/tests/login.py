from selenium.webdriver.common.by import By

def test_login(driver):
    # Initiate a browser object that has all browser related methods in it
    driver = HudlHomepage

    PAGE_HEADER = (By.CSS_SELECTOR, 'nav[class="hui-webnav__grid-col--onewhole hui-globalnav"]')

    page_header = self.find(PAGE_HEADER)
    # Here I assumed I will be able to extract data from existing test data
    username = test_user.username
    password = test_user.password

    login_page = Homepage(driver)\
        .click_login()\
        .type_username(username=username)\
        .type_password(password=password)\
        .submit_login()

    assert page_header.is_displayed()

