from pages.locators import components_locators as loc

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

