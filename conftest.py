import pytest
from selenium import webdriver
from pages.main_page import MainBasePage
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('window-size=1920x1080')
    #options.add_argument("--auto-open-devtools-for-tabs")
    options.add_experimental_option("detach", True)  # to prevent browser from closing
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(3)
    chrome_driver.set_window_size(1280, 800)
    yield chrome_driver
    #chrome_driver.quit()

@pytest.fixture
def main_page(driver):
    return MainBasePage(driver)