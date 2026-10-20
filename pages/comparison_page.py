from base_page import BasePage
from locators import comparison_page_locators as loc
import random


class ComparisonPage(BasePage):
    endpoint = "comparison"

    def clear_comparison(self):
        self.click_by_locator(loc.CLEAR_COMPARISON_BUTTON)

    def press_browse_products(self):
        self.click_by_locator(loc.BROWSE_PRODUCTS_BUTTON)

    def click_comparison_image(self):
        self.click_by_locator(loc.COMPARISON_IMAGE)

    def is_comparison_empty_visible(self):
        return self.wait_for_element_visibility(loc.COMPARISON_EMPTY)

    def get_comparison_item_title(self):
        return self.locate_element(loc.COMPARISON_ITEM_TITLE).text

    def get_all_comparison_pictures(self):
        return self.locate_multiple_elements(loc.COMPARISON_IMAGE)

    def show_differences_only(self):
        self.click_by_locator(loc.SHOW_DIFFERENT_ONLY_CHECKBOX)

    def get_comparison_specs(self, number_of_items_in_comparison: int):
        specs = self.locate_multiple_elements(loc.COMPARISON_SPECS)
        list_of_specs = []
        for index, item in enumerate(specs):
            inner_list = []
            if index % number_of_items_in_comparison == 0:
                inner_list.append(item.text)
            list_of_specs.append(inner_list)

    def remove_comparison_item(self, order_of_item_to_remove: int):
        if not isinstance(order_of_item_to_remove, int) or order_of_item_to_remove < 1:
            raise ValueError("order_of_item_to_remove must be a positive integer")

        all_elements = self.locate_multiple_elements(loc.REMOVE_FROM_COMPARISON_BUTTON)
        index_of_item_to_remove = int(order_of_item_to_remove) - 1

        if index_of_item_to_remove >= len(all_elements):
            raise Exception("order_of_item_to_remove is out of Index")

        self.click_by_web_element(all_elements[index_of_item_to_remove])
