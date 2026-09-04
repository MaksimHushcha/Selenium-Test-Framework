from urllib.parse import urljoin

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import product_page_locators as loc, product_page_locators


class ProductPage(BasePage):
    endpoint = "product"

    def load(self, product_id):
        target_url = f"{self.base_url}/{self.endpoint}/{product_id}"
        try:
            self.driver.get(target_url)
            self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        except TimeoutException:
            print("Page failed to load within the timeout period.")
        return self

    # Actions with products

    def add_to_favourites(self):
        self.click_element(loc.ADD_TO_FAVOURITES_BUTTON_LOCATOR)

    def add_to_cart(self):
        self.click_element(loc.ADD_TO_CARD_BUTTON_LOCATOR)

    def increase_quantity(self):
        self.click_element(loc.INCREASE_QUANTITY_LOCATOR)

    def decrease_quantity(self):
        self.click_element(loc.DECREASE_QUANTITY_LOCATOR)

    def add_to_comparison(self):
        self.click_element(loc.ADD_TO_COMPARISON_LOCATOR)

    # Getting info

    def get_item_specs(self) -> list:
        specs = self.locate_multiple_elements(loc.SPECS_LOCATOR)
        return [spec.text for spec in specs]