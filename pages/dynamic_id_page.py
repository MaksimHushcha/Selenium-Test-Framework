from pages.locators import dynamic_id_page_locators as loc

from pages.base_page import BasePage


class DynamicIdBasePage(BasePage):

    page_endpoint = "dynamicid/"
    def click_button_with_dynamic_id(self):
        self.click_element(loc.BUTTON_WITH_DYNAMIC_ID)


