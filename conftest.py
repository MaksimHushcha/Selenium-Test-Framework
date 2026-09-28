import json
import os

import pytest
from selenium import webdriver
from utils.api_utils import get_a_random_valid_product_id, AuthManager, FavoritesAPI
from checkout_page import Checkout
from components import Components
from comparison_page import ComparisonPage

from pages.main_page import MainBasePage
from pages.product_page import ProductPage
from selenium.webdriver.chrome.options import Options
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
def comparison_page(driver):
    return ComparisonPage(driver)


@pytest.fixture
def get_available_product_id():
    product_id = get_a_random_valid_product_id(amount_of_items=1)
    product_id = product_id[0]
    return product_id


@pytest.fixture
def get_two_product_ids() -> list:
    product_id = get_a_random_valid_product_id(amount_of_items=2)
    return product_id



@pytest.fixture
def authenticated_user(driver):
    token = AuthManager.get_access_token()
    driver.get(f"{os.getenv('BASE_URL')}contact")
    driver.execute_script(f"window.localStorage.setItem('auth-token', '{token}')")


@pytest.fixture
def add_two_items_to_comparison(driver, get_two_product_ids):
    main_page = MainBasePage(driver)
    id1, id2 = get_two_product_ids
    def _add_two_items_to_comparison():
        main_page.set_item_in_session_storage('compare_ids', json.dumps([id1, id2]))

    return _add_two_items_to_comparison


@pytest.fixture
def seeded_product(clear_favorites, get_available_product_id):
    favorites = FavoritesAPI()
    favorites.add_item_to_favorites(get_available_product_id)
    return get_available_product_id


@pytest.fixture
def clear_favorites():
    favorites = FavoritesAPI()
    favorites.clear_favorites()
    yield
    favorites.clear_favorites()