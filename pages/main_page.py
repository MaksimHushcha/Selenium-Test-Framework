from pages.base_page import BasePage
from pages.locators import main_page_locators as loc
from selenium.webdriver.support.wait import WebDriverWait


class MainBasePage(BasePage):

    def sort_items_by_name_desc(self):
        self.click_element(loc.SORT_DROPDOWN_LOCATOR)
        self.click_element(loc.SORT_NAME_DESC_LOCATOR)

    def get_list_of_card_titles(self):
        # Wait until elements are visible AND every element has non-empty text
        located_elements = WebDriverWait(self.driver, 10).until(
            lambda driver: [
                element for element in driver.find_elements(*loc.CARD_TITLES_LOCATOR)
                if element.is_displayed() and element.text.strip() != ""
            ]
        )
        return [element.text for element in located_elements]

    def assert_cards_are_sorted_by_title_in_reverse_order(self):
        card_titles = self.get_list_of_card_titles()
        assert card_titles == sorted(card_titles, reverse=True)
