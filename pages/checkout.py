from selenium.webdriver.common.by import By

from pages.locators import checkout_locators as loc

from base_page import BasePage


class Checkout(BasePage):
    endpoint = "checkout"

    def get_quantity_of_an_item_in_cart(self) -> int | None:
        value = self.locate_element(loc.ITEM_QUANTITY_LOCATOR).get_attribute("value")
        return int(value) if value else None
