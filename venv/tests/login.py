from selenium.webdriver.common.by import By

def test_login(driver):
    driver = HudlHomepage

    PAGE_BODY = (By.CSS_SELECTOR, 'body[class="mobile-first"]')

    page_body = self.find(PAGE_BODY)
    username = test_user.username
    password = test_user.password

    login_page = Homepage(driver)\
        .click_login()\
        .type_username(username=username)\
        .type_password(password=password)\
        .submit_login()

    assert page_body is not None

