from urllib.parse import urljoin

from selenium.common import TimeoutException

from pages.base_page import BasePage
from pages.locators import product_page_locators as loc, product_page_locators


class ProductPage(BasePage):
    path = "product"

    def __init__(self, driver):
        super().__init__(driver)
        self.product_id = None

    def load(self, product_id):
        target_url = f"{self.base_url}/{self.path}/{self.product_id}"
        try:
            self.driver.get(target_url)
            self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        except TimeoutException:
            print("Page failed to load within the timeout period.")
        return self
