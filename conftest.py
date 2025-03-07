from datetime import datetime

import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException


@pytest.fixture(scope='function')
def driver():
    driver = None
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        yield driver
    except WebDriverException as e:
        pytest.fail(f'Failed to initialize WebDriver: {e}')
    finally:
        if driver:
            attach = driver.get_screenshot_as_png()
            allure.attach(attach, name=f'Screenshot {datetime.today()}', attachment_type=allure.attachment_type.PNG)
            driver.quit()
