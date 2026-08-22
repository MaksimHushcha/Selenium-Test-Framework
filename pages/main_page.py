from pages.base_page import BasePage
from pages.locators import main_page_locators as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainBasePage(BasePage):

    def sort_items_by_name_desc(self):
        self.click_element(loc.SORT_DROPDOWN_LOCATOR)
        self.click_element(loc.SORT_NAME_DESC_LOCATOR)

    def sort_items_by_name_asc(self):
        self.click_element(loc.SORT_DROPDOWN_LOCATOR)
        self.click_element(loc.SORT_NAME_ASC_LOCATOR)

    def sort_items_by_price_asc(self):
        self.click_element(loc.SORT_DROPDOWN_LOCATOR)
        self.click_element(loc.SORT_PRICE_ASC_LOCATOR)

    def sort_items_by_price_desc(self):
        self.click_element(loc.SORT_DROPDOWN_LOCATOR)
        self.click_element(loc.SORT_PRICE_DESC_LOCATOR)

    def sort_items_by_co2_asc(self):
        self.click_element(loc.SORT_DROPDOWN_LOCATOR)
        self.click_element(loc.SORT_CO2_RATING_ASC_LOCATOR)

    def sort_items_by_co2_desc(self):
        self.click_element(loc.SORT_DROPDOWN_LOCATOR)
        self.click_element(loc.SORT_CO2_RATING_DESC_LOCATOR)

    def _wait_for_sorting(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(loc.SORTING_COMPLETED_LOCATOR))

    def get_list_of_card_titles(self):
        # we are checking if parent element is loaded before attempting to locate the titles
        self._wait_for_sorting()
        located_elements = self.driver.find_elements(*loc.CARD_TITLES_LOCATOR)
        return [element.text for element in located_elements]

    def get_list_of_prices_on_cards(self):
        self._wait_for_sorting()
        located_elements = self.driver.find_elements(*loc.CARD_PRICE_LOCATOR)
        return [float(element.text.replace("$", "")) for element in located_elements]

    def get_list_of_co2_values_on_cards(self):
        self._wait_for_sorting()
        located_elements = self.driver.find_elements(*loc.CARD_CO2_RATING)
        return [element.text for element in located_elements]

