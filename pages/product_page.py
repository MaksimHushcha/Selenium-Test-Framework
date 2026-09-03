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

    def get_item_title(self):
        return self.locate_element(loc.PRODUCT_NAME_LOCATOR).text

    def add_to_favourites(self):
        self.click_element(loc.ADD_TO_FAVOURITS_BUTTON_LOCATOR)