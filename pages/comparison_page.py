from base_page import BasePage
from locators import comparison_page_locators as loc


class ComparisonPage(BasePage):


    def clear_comparison(self):
        self.click_element(loc.CLEAR_COMPARISON_BUTTON)


    def go_to_compare_screen(self):
        self.click_element(loc.COMPARE_NOW_BUTTON)


    def comparison_bar_is_not_visible(self):
        return self.check_element_is_not_visible(loc.COMPARISON_BAR)


    def comparison_bar_is_displayed(self):
        return self.wait_for_element_presence(loc.COMPARISON_BAR)