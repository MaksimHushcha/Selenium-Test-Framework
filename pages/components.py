from locators import components_locators as loc
from pages.base_page import BasePage


class Components(BasePage):

    def get_toast_text(self):
        return self.locate_element(loc.TOP_RIGHT_TOST_NOTIFICATION_LOCATOR).text

    def open_cart(self):
        self.click_by_locator(loc.CARD_BUTTON_LOCATOR)
        return self

    def get_number_of_items_on_cart_icon(self):
        return int(self.locate_element(loc.CARD_QUANTITY_LOCATOR).text)

    def dismiss_toast(self):
        self.click_by_locator(loc.TOP_RIGHT_TOST_NOTIFICATION_LOCATOR)
        return self

    def clear_comparison(self):
        self.click_by_locator(loc.CLEAR_COMPARISON_BUTTON)
        return self

    def go_to_compare_screen(self):
        self.click_by_locator(loc.COMPARE_NOW_BUTTON)
        return self

    def comparison_bar_is_not_visible(self):
        return self.is_element_not_visible(loc.COMPARISON_BAR)


    def comparison_bar_is_displayed(self):
        return self.is_element_visible(loc.COMPARISON_BAR)


    def get_navbar_username(self):
        return self.locate_element(loc.NAV_MENU).text


    def switch_to_locale(self, locale):
        if locale not in BasePage.SUPPORTED_UI_LOCALES:
            raise ValueError(f"supplied locale {locale} is not supported, expected one of {BasePage.SUPPORTED_UI_LOCALES}")

        BY, SELECTOR = loc.LANGUAGE_OPTION_TEMPLATE
        option_locator = (BY, SELECTOR.format(locale=locale.strip().lower()))
        self.click_by_locator(loc.LANGUAGE_SELECT)
        self.click_by_locator(option_locator)
        return self



