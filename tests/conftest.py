import json
import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.api_utils import get_a_random_valid_product_id, get_measuring_items_for_comparison, get_random_product_ids, AuthManager, FavoritesAPI
from pages.components import Components
from pages.comparison_page import ComparisonPage
from pages.checkout_page import Checkout
from pages.main_page import MainBasePage
from pages.product_page import ProductPage
from pages.contact_page import ContactPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage

from selenium.webdriver.chrome.options import Options
import dotenv
import allure
import re
from pathlib import Path

dotenv.load_dotenv()

ARTIFACTS_DIR = Path("test-artifacts")

@pytest.fixture
def driver():
    options = Options()
    #if os.getenv("GITHUB_ACTIONS"):
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
    options.add_experimental_option("detach", True)  # to prevent browser from closing
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(3)
    chrome_driver.set_window_size(1280, 800)
    yield chrome_driver
    chrome_driver.quit()

def safe_filename(nodeid: str) -> str:
    return re.sub(r"[^\w\-_.]", "_", nodeid)

def get_safe_log(driver, log_type: str):
    try:
        return driver.get_log(log_type)
    except Exception:
        return []


def get_safe_storage(driver, storage_type: str):
    try:
        return driver.execute_script(f"return window.{storage_type};") or {}
    except Exception:
        return {}

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver is None:
            return

        worker = os.environ.get("PYTEST_XDIST_WORKER", "local")
        test_name = safe_filename(item.nodeid)
        artifact_dir = ARTIFACTS_DIR / worker / test_name
        artifact_dir.mkdir(parents=True, exist_ok=True)

        try:
            screenshot_path = (str(artifact_dir / "screenshot.png"))
            body = driver.find_element(By.TAG_NAME, "body")
            body.screenshot(screenshot_path)
            allure.attach.file(screenshot_path, name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)

            html_file_path = (artifact_dir / "page.html")
            html_file_path.write_text(driver.page_source, encoding="utf-8")
            allure.attach.file(str(html_file_path), name="Page Source", attachment_type=allure.attachment_type.HTML)

            metadata = {
                "current_url": driver.current_url,
                "page_title": driver.title,
                "window_size": driver.get_window_size(),
                "viewport_size": driver.execute_script(
                    "return {width: window.innerWidth, height: window.innerHeight};"
                ),
                "capabilities": driver.capabilities,
            }

            diagnostics = {
                "Metadata": ("metadata.json", metadata),
                "Browser Console Logs": ("console.json", get_safe_log(driver, "browser")),
                "Performance Logs": ("performance_raw.json", get_safe_log(driver, "performance")),
                "Cookies": ("cookies.json", driver.get_cookies()),
                "Local Storage": ("local_storage.json", get_safe_storage(driver, "localStorage")),
                "Session Storage": ("session_storage.json", get_safe_storage(driver, "sessionStorage")),
            }

            for title, (file, data) in diagnostics.items():
                file_path = artifact_dir / file
                content = json.dumps(data, indent=2)
                file_path.write_text(content, encoding="utf-8")

                allure.attach(
                    content,
                    name=title,
                    attachment_type=allure.attachment_type.JSON,
                )

            print(f"\nBrowser diagnostics saved to: {artifact_dir}")
        except Exception as exc:
            print(f"\nCould not capture browser diagnostics: {exc}")




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
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def registration_page(driver):
    return RegistrationPage(driver)


@pytest.fixture
def get_available_product_id():
    product_id = get_a_random_valid_product_id(amount_of_items=1)
    product_id = product_id[0]
    return product_id


@pytest.fixture
def get_two_product_ids():
    product_id = get_a_random_valid_product_id(amount_of_items=2)
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