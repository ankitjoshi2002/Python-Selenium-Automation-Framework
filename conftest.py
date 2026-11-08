import pytest
from selenium import webdriver
from datetime import datetime
from pathlib import Path

import os
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    if os.getenv("HEADLESS") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.binary_location = os.getenv("CHROME_BIN", "/usr/bin/chromium")
        service = Service(os.getenv("CHROMEDRIVER_PATH", "/usr/bin/chromedriver"))
        driver = webdriver.Chrome(service=service, options=options)
    else:
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"reports/report_{stamp}.html"
    config.option.self_contained_html = True