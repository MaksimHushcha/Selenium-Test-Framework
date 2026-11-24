from pathlib import Path
import json
import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import allure
import re

ARTIFACTS_DIR = Path("artifacts/test-artifacts")


@pytest.fixture
def driver():
    options = Options()
    if os.getenv("GITHUB_ACTIONS"):
        options.add_argument("--headless=new")
    else:
        options.add_experimental_option("detach", True)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(3)
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

    if report.failed and report.when in ("setup", "call"):
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

