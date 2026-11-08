from base.base_page import BasePage
from locator.login_locator import LoginPageLocators

class LoginPage(BasePage):

    def __init__(self, driver):
        # self.driver = driver
        super().__init__(driver)

    def open_url(self):
        self.navigate_to("https://practicetestautomation.com/practice-test-login/")

    def input_credentials(self, uname,pwd):
        self.enter_text(LoginPageLocators.USERNAME, uname)
        self.enter_text(LoginPageLocators.PASSWORD, pwd)

    def click_submit_btn(self):
        self.click_element(LoginPageLocators.SUBMIT_BTN)

    def check_is_loggedin(self):
        a = self.get_element_text(LoginPageLocators.LOGGEDIN_TXT)
        assert "Logged In Successfully" in a, f"Login is not sucecss"

    def username_error(self):
        a = self.get_element_text(LoginPageLocators.INVALID_USERNAME)
        assert "Your username is invalid!" in a, f"Getting invalid error msg **{a}**"

    def password_error(self):
        a = self.get_element_text(LoginPageLocators.INVALID_PASS)
        assert "Your password is invalid!" in a, f"Getting invalid error msg **{a}**"