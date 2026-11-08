from selenium.webdriver.common.by import By

class LoginPageLocators:
    USERNAME = (By.XPATH, "//input[@id='username']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    SUBMIT_BTN = (By.XPATH, "//button[@id='submit']")

    LOGGEDIN_TXT = (By.XPATH, "//h1[contains(text(),'Logged In Successfully')]")
    INVALID_USERNAME = (By.XPATH, "//div[@id='error' and contains(text(),'Your username is invalid!')]")
    INVALID_PASS     = (By.XPATH, "//div[@id='error' and contains(text(),'Your password is invalid!')]")