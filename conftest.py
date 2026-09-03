import pytest
from selenium import webdriver
from api_helpers.api_utils import get_a_random_valid_product_id
from components import Components
from pages.main_page import MainBasePage
from pages.product_page import ProductPage

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

@pytest.fixture
def product_page(driver):
    return ProductPage(driver)

@pytest.fixture
def components(driver):
    return Components(driver)

@pytest.fixture
def get_available_product_id(driver):
    product_id = get_a_random_valid_product_id()
    return product_id
