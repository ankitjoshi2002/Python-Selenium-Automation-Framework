from pages.login_page import LoginPage


def test_valid_login(driver):
    login = LoginPage(driver)
    login.open_url()
    login.input_credentials("student","Password123")
    login.click_submit_btn()
    login.check_is_loggedin()