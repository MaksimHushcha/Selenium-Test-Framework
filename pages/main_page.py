from selenium.common import StaleElementReferenceException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from pages.locators import main_page_locators as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainBasePage(BasePage):

    def sort_items_by_name_desc(self):
        self.click_element(loc.SORT_DROPDOWN_LOCATOR)
        self.click_element(loc.SORT_NAME_DESC_LOCATOR)
        self._wait_for_sorting()

    def sort_items_by_name_asc(self):
        self.click_element(loc.SORT_DROPDOWN_LOCATOR)
        self.click_element(loc.SORT_NAME_ASC_LOCATOR)
        self._wait_for_sorting()

    def sort_items_by_price_asc(self):
        self.click_element(loc.SORT_DROPDOWN_LOCATOR)
        self.click_element(loc.SORT_PRICE_ASC_LOCATOR)
        self._wait_for_sorting()

    def sort_items_by_price_desc(self):
        self.click_element(loc.SORT_DROPDOWN_LOCATOR)
        self.click_element(loc.SORT_PRICE_DESC_LOCATOR)
        self._wait_for_sorting()

    def sort_items_by_co2_asc(self):
        self.click_element(loc.SORT_DROPDOWN_LOCATOR)
        self.click_element(loc.SORT_CO2_RATING_ASC_LOCATOR)
        self._wait_for_sorting()

    def sort_items_by_co2_desc(self):
        self.click_element(loc.SORT_DROPDOWN_LOCATOR)
        self.click_element(loc.SORT_CO2_RATING_DESC_LOCATOR)
        self._wait_for_sorting()

    def go_to_next_page(self):
        self.click_element(loc.NEXT_PAGE_BUTTON_LOCATOR)

    #max_pages is a safeguard against endless loop. App has normally only 5 pages
    def go_to_all_page_till_last(self, max_pages=10):
        page_count = 0
        while page_count < max_pages:
            try:
                buttons = self.driver.find_elements(*loc.PAGINATION_BUTTONS)
                if not buttons:
                    break
                last_button = buttons[-1]
                if 'disabled' in last_button.get_attribute('class').split(' '):
                    return
                self.click_element(loc.NEXT_PAGE_BUTTON_LOCATOR)
                page_count += 1
            except StaleElementReferenceException:
                continue
        raise TimeoutError("Pagination clicks exceeded the maximum allowed number of pages.")

    def go_to_previous_page(self):
        self.click_element(loc.PREV_PAGE_BUTTON_LOCATOR)

    def select_eco_friendly_products(self):
        self.click_element(loc.ECO_FRIENDLY_CHECKBOX_LOCATOR)

    def _wait_for_sorting(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(loc.SORTING_COMPLETED_LOCATOR))

    def get_cards_on_the_page(self):
        located_elements = self.locate_multiple_elements(loc.CARD_LOCATOR)
        return [element for element in located_elements if element.is_displayed()]

    def get_list_of_card_titles(self):
        located_elements = self.locate_multiple_elements(loc.CARD_TITLES_LOCATOR)
        return [element.text for element in located_elements]

    def get_list_of_prices_on_cards(self):
        located_elements = self.locate_multiple_elements(loc.CARD_PRICE_LOCATOR)
        return [float(element.text.replace("$", "")) for element in located_elements]

    def get_list_of_co2_values_on_cards(self):
        located_elements = self.locate_multiple_elements(loc.CARD_CO2_RATING)
        return [element.text for element in located_elements]

    def get_cards_with_eco_badge(self):
        items_with_eco_badge = self.locate_multiple_elements(loc.ECO_BADGE_LOCATOR)
        return [element for element in items_with_eco_badge if element.is_displayed()]

    def set_price_filter(self, target_min_price: int, target_max_price: int):
        min_price_slider_element = self.locate_element(loc.MINPRICE_VALUE_CURRENT_LOCATOR)
        max_price_slider_element = self.locate_element(loc.MAXPRICE_VALUE_CURRENT_LOCATOR)
        current_min_price = int(min_price_slider_element.text)
        current_max_price = int(max_price_slider_element.text)
        self._queue_price_slider_key_presses(current_min_price, target_min_price, loc.MIN_PRICE_SLIDER_LOCATOR)
        self._queue_price_slider_key_presses(current_max_price, target_max_price, loc.MAX_PRICE_SLIDER_LOCATOR)
        self._wait_for_prices_to_be_in_range(target_min_price, target_max_price)

    def _queue_price_slider_key_presses(self, current_price: int, target_price: int, locator: tuple):
        if target_price == current_price:
            return
        key_to_press = (Keys.ARROW_RIGHT if target_price > current_price else Keys.ARROW_LEFT)
        number_of_key_presses = abs(target_price - current_price)

        slider = self.locate_element(locator)
        actions = ActionChains(self.driver)
        actions.click(slider)

        for _ in range(number_of_key_presses):
            actions.send_keys(key_to_press)
        actions.perform()

    def _wait_for_prices_to_be_in_range(self, min_price: int, max_price: int, timeout=5):
        def _prices_are_filtered(driver):
            try:
                price_elements = driver.find_elements(*loc.CARD_PRICE_LOCATOR)
                if not price_elements:
                    return False
                else:
                    prices = [float(element.text.replace("$", "")) for element in price_elements]
                    if len(prices) == len([price for price in prices if min_price <= price <= max_price]):
                        return True
            except StaleElementReferenceException:
                return False

        WebDriverWait(self.driver, timeout).until(_prices_are_filtered)