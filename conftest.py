import pytest
from selenium import webdriver

from pages.class_attribute_page import ClassAttributePage
from pages.dynamic_id_page import DynamicIdBasePage
from pages.hidden_layers_page import HiddenLatersPage
from pages.load_delay_page import LoadDelayPage
from pages.main_page import MainBasePage
from tests.selenium_framework import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('window-size=1920x1080')
    options.add_experimental_option("detach", True)  # to prevent browser from closing
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(3)
    chrome_driver.set_window_size(1920, 1080)
    yield chrome_driver
    #chrome_driver.quit()

@pytest.fixture
def main_page(driver):
    return MainBasePage(driver)

@pytest.fixture
def dynamic_id_page(driver):
    return DynamicIdBasePage(driver)

@pytest.fixture
def class_attribute_page(driver):
    return ClassAttributePage(driver)

@pytest.fixture
def hidden_layers_page(driver):
    return HiddenLatersPage(driver)

@pytest.fixture
def load_delay_page(driver):
    return LoadDelayPage(driver)