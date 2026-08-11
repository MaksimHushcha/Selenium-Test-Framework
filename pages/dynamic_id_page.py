from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DynamicIdBasePage(BasePage):

    page_endpoint = "dynamicid/"
    BUTTON_WITH_DYNAMIC_ID = (By.CLASS_NAME, "btn-primary")

    def click_button_with_dynamic_id(self):
        self.click_element(self.BUTTON_WITH_DYNAMIC_ID)


