import os

import pytest
from selenium import webdriver
from utils.api_utils import get_a_random_valid_product_id, get_measuring_items_for_comparison, get_random_product_ids, AuthManager, FavoritesAPI

from pages.components import Components
from pages.comparison_page import ComparisonPage
from pages.checkout_page import Checkout
from pages.main_page import MainBasePage
from pages.product_page import ProductPage
from pages.contact_page import ContactPage

from selenium.webdriver.chrome.options import Options
import dotenv

###
import os
import re
from pathlib import Path
###
dotenv.load_dotenv()


import pytest

#### GENERATED FOR TROUBLESHOOTING_REWRITE_BY_HAND_LATER
ARTIFACTS_DIR = Path("test-artifacts")


def safe_filename(name: str) -> str:
    """Convert a test node ID into a filesystem-safe filename."""
    return re.sub(r"[^a-zA-Z0-9_.-]+", "_", name)[:180]


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture browser diagnostics when a test fails."""
    outcome = yield
    report = outcome.get_result()

    # Capture failures during the test body, not setup or teardown.
    if report.when != "call" or not report.failed:
        return

    driver = item.funcargs.get("driver")
    if driver is None:
        return

    # Separate artifacts by test and xdist worker.
    worker = os.environ.get("PYTEST_XDIST_WORKER", "local")
    test_name = safe_filename(item.nodeid)
    artifact_dir = ARTIFACTS_DIR / worker / test_name
    artifact_dir.mkdir(parents=True, exist_ok=True)

    try:
        (artifact_dir / "url.txt").write_text(
            driver.current_url, encoding="utf-8"
        )
        (artifact_dir / "title.txt").write_text(
            driver.title, encoding="utf-8"
        )
        driver.save_screenshot(str(artifact_dir / "screenshot.png"))
        (artifact_dir / "page.html").write_text(
            driver.page_source, encoding="utf-8"
        )

        print(f"\nBrowser diagnostics saved to: {artifact_dir}")

    except Exception as exc:
        print(f"\nCould not capture browser diagnostics: {exc}")
###

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
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
def contact_page(driver):
    return ContactPage(driver)



@pytest.fixture
def get_available_product_id():
    product_id = get_a_random_valid_product_id(amount_of_items=1)
    product_id = product_id[0]
    return product_id


@pytest.fixture
def authenticated_user(driver):
    token = AuthManager.get_access_token()
    driver.get(f"{os.getenv('BASE_URL')}contact")
    driver.execute_script(f"window.localStorage.setItem('auth-token', '{token}')")


@pytest.fixture
def seeded_two_comparison_items(main_page):
    ids_list = get_random_product_ids(number_of_ids=2)
    main_page.load()
    main_page.set_compare_ids_session_storage(ids_list)

@pytest.fixture
def seeded_two_measurements_items(main_page):
    ids_list = get_measuring_items_for_comparison()
    main_page.load()
    main_page.set_compare_ids_session_storage(ids_list)


@pytest.fixture
def seeded_favorite_product(clear_favorites, get_available_product_id):
    favorites = FavoritesAPI()
    favorites.add_item_to_favorites(get_available_product_id)
    return get_available_product_id


@pytest.fixture
def clear_favorites():
    favorites = FavoritesAPI()
    favorites.clear_favorites()
    yield
    favorites.clear_favorites()