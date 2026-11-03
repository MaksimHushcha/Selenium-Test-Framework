import json
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
import datetime
from selenium.webdriver.chrome.options import Options
import dotenv
from pathlib import Path

dotenv.load_dotenv()

ARTIFACTS_DIR = Path("test-artifacts")


def safe_filename(name: str) -> str:
    filename = (datetime.datetime.now().strftime('%d_%m_%y') + "_" + name).replace("::", "_")
    return filename


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver is None:
            return

        # Separate artifacts by test and xdist worker.
        worker = os.environ.get("PYTEST_XDIST_WORKER", "local")
        test_name = safe_filename(item.nodeid)
        artifact_dir = ARTIFACTS_DIR / worker / test_name
        artifact_dir.mkdir(parents=True, exist_ok=True)

        try:
            driver.save_screenshot(str(artifact_dir / "screenshot.png"))

            browser_logs = driver.get_log("browser")
            cookies = driver.get_cookies()
            local_storage = driver.execute_script("return window.localStorage;")
            session_storage = driver.execute_script("return window.sessionStorage;")
            perf_logs = driver.get_log("performance")
            metadata = {
                            "current_url": driver.current_url,
                            "page_title": driver.title,
                            "window_size": driver.get_window_size(),
                            "viewport_size": driver.execute_script(
                                "return {width: window.innerWidth, height: window.innerHeight};"
                            ),
                            "capabilities": driver.capabilities,
                        }

            (artifact_dir / "console.json").write_text(json.dumps(browser_logs, indent=2))
            (artifact_dir / "cookies.json").write_text(json.dumps(cookies, indent=2))
            (artifact_dir / "local_storage.json").write_text(json.dumps(local_storage, indent=2))
            (artifact_dir / "cookies.json").write_text(json.dumps(session_storage, indent=2))
            (artifact_dir / "page.html").write_text(driver.page_source, encoding="utf-8")
            (artifact_dir / "metadatata.json").write_text(json.dumps(metadata, indent=2))
            (artifact_dir / "performance_raw.json").write_text(json.dumps(perf_logs, indent=2))

            print(f"\nBrowser diagnostics saved to: {artifact_dir}")
        except Exception as exc:
            print(f"\nCould not capture browser diagnostics: {exc}")

@pytest.fixture
def driver():
    options = Options()
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