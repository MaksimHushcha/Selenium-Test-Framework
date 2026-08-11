from pages.base_page import BasePage
from pages.locators import main_page_locators as loc


class MainBasePage(BasePage):

    def click_dynamic_id(self):
        self.click_element(loc.DYNAMIC_ID_LINK)

    def click_class_attribute(self):
        self.click_element(loc.CLASS_ATTRIBUTE_LINK)

    def click_hidden_layers(self):
        self.click_element(loc.HIDDEN_LAYERS_LINK)

    def click_load_delay(self):
        self.click_element(loc.LOAD_DELAY_LINK)

    def click_ajax_data(self):
        self.click_element(loc.AJAX_DATA_LINK)

    def click_client_side_delay(self):
        self.click_element(loc.CLIENT_SIDE_DELAY_LINK)

    def click_click_link(self):
        self.click_element(loc.CLICK_LINK)

    def click_test_input_link(self):
        self.click_element(loc.TEST_INPUT_LINK)

    def click_scrollbars(self):
        self.click_element(loc.SCROLLBARS_LINK)

    def click_dynamic_table(self):
        self.click_element(loc.DYNAMIC_TABLE_LINK)

    def click_verify_text(self):
        self.click_element(loc.VERIFY_TEXT_LINK)

    def click_progress_bar(self):
        self.click_element(loc.PROGRESS_BAR_LINK)