from pages.base_page import BasePage
from locators import comparison_page_locators as loc


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
        if not isinstance(number_of_items_in_comparison, int) or isinstance(number_of_items_in_comparison, bool):
            raise TypeError("number_of_items_in_comparison must be an integer")
        if number_of_items_in_comparison <= 0:
            raise ValueError("number_of_items_in_comparison must be a positive integer")
        specs = self.locate_multiple_elements(loc.COMPARISON_SPECS)

        return [
            [item.text for item in specs[slice_index::number_of_items_in_comparison]]
            for slice_index in range(number_of_items_in_comparison)
        ]


    def remove_comparison_item(self, order_of_item_to_remove: int):
        if not isinstance(order_of_item_to_remove, int) or order_of_item_to_remove < 1:
            raise ValueError("order_of_item_to_remove must be a positive integer")

        all_elements = self.locate_multiple_elements(loc.REMOVE_FROM_COMPARISON_BUTTON)
        index_of_item_to_remove = int(order_of_item_to_remove) - 1

        if index_of_item_to_remove >= len(all_elements):
            raise Exception("order_of_item_to_remove is out of Index")

        self.click_by_web_element(all_elements[index_of_item_to_remove])
