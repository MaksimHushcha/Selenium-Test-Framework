from logging import raiseExceptions
from urllib.parse import urljoin

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import product_page_locators as product_page_locator
from pages.locators import components_locators as components_locators


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
        self.click_element(product_page_locator.ADD_TO_FAVOURITES_BUTTON_LOCATOR)

    def add_to_cart(self):
        self.click_element(product_page_locator.ADD_TO_CARD_BUTTON_LOCATOR)

    def increase_quantity(self):
        self.click_element(product_page_locator.INCREASE_QUANTITY_LOCATOR)

    def decrease_quantity(self):
        self.click_element(product_page_locator.DECREASE_QUANTITY_LOCATOR)

    def add_to_comparison(self):
        self.click_element(product_page_locator.ADD_TO_COMPARISON_LOCATOR)

    # Getting info

    def get_item_specs(self) -> list:
        specs = self.locate_multiple_elements(product_page_locator.SPECS_LOCATOR)
        return [spec.text for spec in specs]

    def get_item_description(self) -> str:
        description =  self.locate_element(product_page_locator.PRODUCT_DESCRIPTION_LOCATOR).text
        return description

    def get_co_2_rating(self) -> tuple:
        co2_rating = self.locate_element(components_locators.CARD_CO2_RATING).text
        co2_rating_color = self.get_hex_color_of_element("background-color", components_locators.CARD_CO2_RATING)
        return co2_rating, co2_rating_color

    def get_product_tags(self) -> list:
        tags = self.locate_multiple_elements(product_page_locator.TAGS_LOCATOR)
        return [tag.text for tag in tags]

    def get_item_id(self) -> str | None:
        current_url = self.get_current_url()
        try:
            item_id = current_url.split("/")[-1]
        except IndexError:
            return None
        return item_id