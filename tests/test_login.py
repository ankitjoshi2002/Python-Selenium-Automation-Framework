from pages.login_page import LoginPage
from utils import config_reader

def test_valid_login(driver):
    login = LoginPage(driver)
    login.open_url(config_reader.get("app","base_url"))
    login.input_credentials(config_reader.get("credentials", "username"),
                            config_reader.get("credentials", "password"))
    login.click_submit_btn()
    login.check_is_loggedin()