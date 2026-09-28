from base_page import BasePage
from locators import comparison_page_locators as loc


class ComparisonPage(BasePage):
    endpoint = "comparison"

    def clear_comparison(self):
        self.click_element(loc.CLEAR_COMPARISON_BUTTON)

    def press_browse_products(self):
        self.click_element(loc.BROWSE_PRODUCTS_BUTTON)

    def click_comparison_image(self):
        self.click_element(loc.COMPARISON_IMAGE)

    def is_comparison_empty_visible(self):
        return self.wait_for_element_visibility(loc.COMPARISON_EMPTY)

    def get_comparison_item_title(self):
        return self.locate_element(loc.COMPARISON_ITEM_TITLE).text


