from pages.locators import hidden_layers_locators as loc

from pages.base_page import BasePage


class HiddenLatersPage(BasePage):

    page_endpoint = "hiddenlayers/"

    def click_button_on_top_layer(self):
        self.click_element(loc.UNLAYERED_BUTTON)

    def click_hidden_button(self):
        self.click_element(loc.HIDDEN_BUTTON)


