import pytest
from selenium import webdriver
from selenium_framework import Options


@pytest.fixture
def chrome_driver():
    options = Options()
    options.add_argument('window-size=1920x1080')
    options.add_experimental_option("detach", True)  # to prevent browser from closing
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(3)
    chrome_driver.set_window_size(1920, 1080)
    yield chrome_driver
    chrome_driver.quit()