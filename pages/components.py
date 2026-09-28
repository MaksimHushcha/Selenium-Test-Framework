from locators import components_locators as loc

from base_page import BasePage


class Components(BasePage):


    def get_toast_text(self):
        return self.locate_element(loc.TOP_RIGHT_TOST_NOTIFICATION_LOCATOR).text


    def open_cart(self):
        self.click_element(loc.CARD_BUTTON_LOCATOR)


    def get_number_of_items_on_cart_icon(self):
        return int(self.locate_element(loc.CARD_QUANTITY_LOCATOR).text)


    def dismiss_toast(self):
        self.click_element(loc.TOP_RIGHT_TOST_NOTIFICATION_LOCATOR)

    def clear_comparison(self):
        self.click_element(loc.CLEAR_COMPARISON_BUTTON)


    def go_to_compare_screen(self):
        self.click_element(loc.COMPARE_NOW_BUTTON)


    def comparison_bar_is_not_visible(self):
        return self.is_element_not_visible(loc.COMPARISON_BAR)


    def comparison_bar_is_displayed(self):
        return self.is_element_visible(loc.COMPARISON_BAR)

