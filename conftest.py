import os

import pytest
from selenium import webdriver
from api_helpers.api_utils import get_a_random_valid_product_id, AuthManager
from checkout import Checkout
from components import Components

from pages.main_page import MainBasePage
from pages.product_page import ProductPage
from selenium.webdriver.chrome.options import Options
from api_helpers import api_utils as api
import dotenv

dotenv.load_dotenv()

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
def checkout(driver):
    return Checkout(driver)

@pytest.fixture
def get_available_product_id(driver):
    product_id = get_a_random_valid_product_id()
    return product_id

@pytest.fixture
def authenticated_user(driver):
    token = AuthManager.get_access_token()
    driver.get(f"{os.getenv('BASE_URL')}/contact")
    driver.execute_script(f"window.localStorage.setItem('auth-token', '{token}')")

@pytest.fixture
def queue_clear_favorites(request, driver):
    api.clear_favorites()

    def _register_removal_from_favorites():
        request.addfinalizer(lambda: api.clear_favorites())

    return _register_removal_from_favorites
