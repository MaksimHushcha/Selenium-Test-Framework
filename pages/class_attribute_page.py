from pages.locators import class_attribute_locators as loc

from pages.base_page import BasePage


class ClassAttributePage(BasePage):

    page_endpoint = "classattr/"

    def click_warning_button(self):
        self.click_element(loc.WARNING_BUTTON_LOCATOR)

    def click_success_button(self):
        self.click_element(loc.SUCCESS_BUTTON_LOCATOR)

    def click_primary_button(self):
        self.click_element(loc.PRIMARY_BUTTON_LOCATOR)

    def get_color_of_warning_button(self):
        return self.get_hex_color_of_element(loc.WARNING_BUTTON_LOCATOR,"background-color")

    def get_color_of_success_button(self):
        return self.get_hex_color_of_element(loc.SUCCESS_BUTTON_LOCATOR, "background-color")

    def get_color_of_primary_button(self):
        return self.get_hex_color_of_element(loc.PRIMARY_BUTTON_LOCATOR, "background-color")

