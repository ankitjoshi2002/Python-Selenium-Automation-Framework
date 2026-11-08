from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.log = get_logger(self.__class__.__name__)

    def click_element(self, locator):
        self.log.info(f"Clicking {locator}")
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator, text):
        self.log.info(f"Inputting the text *{text}* in *{locator}*")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator):
        self.log.info(f"Getting the Element text: {locator}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def get_element(self, locator):
        self.log.info(f"Finding element {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))

    def navigate_to(self, url):
        self.log.info(f"Navigated to the URL: {url}")
        self.driver.get(url)