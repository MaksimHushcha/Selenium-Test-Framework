import random
from typing import Any

from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver import ActionChains, Keys

from pages.base_page import BasePage
from locators import components_locators as component_locator, main_page_locators as product_page_locators

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainBasePage(BasePage):


    def _sort_by(self, sorting_option_locator: tuple[str,str]):
        self.click_by_locator(product_page_locators.SORT_DROPDOWN_LOCATOR)
        self.click_by_locator(sorting_option_locator)
        self._wait_for_sorting()


    def sort_items_by_name_desc(self):
        self._sort_by(product_page_locators.SORT_NAME_DESC_LOCATOR)


    def sort_items_by_name_asc(self):
        self._sort_by(product_page_locators.SORT_NAME_ASC_LOCATOR)


    def sort_items_by_price_asc(self):
        self._sort_by(product_page_locators.SORT_PRICE_ASC_LOCATOR)


    def sort_items_by_price_desc(self):
        self._sort_by(product_page_locators.SORT_PRICE_DESC_LOCATOR)


    def sort_items_by_co2_asc(self):
        self._sort_by(product_page_locators.SORT_CO2_RATING_ASC_LOCATOR)


    def sort_items_by_co2_desc(self):
        self._sort_by(product_page_locators.SORT_CO2_RATING_DESC_LOCATOR)


    def _wait_for_sorting(self):
        self.wait.until(EC.presence_of_element_located(product_page_locators.SORTING_COMPLETED_LOCATOR))


    def _pagination_helper(self, last_button=False, first_button=False):
        old_card = self.driver.find_element(*product_page_locators.CARD_LOCATOR)
        buttons = self.driver.find_elements(*product_page_locators.PAGINATION_BUTTONS)
        if not buttons:
            return
        if last_button:
            button_to_click = buttons[-1]
            if 'disabled' in button_to_click.get_attribute('class').split(' '):
                return
            self.click_by_locator(product_page_locators.NEXT_PAGE_BUTTON_LOCATOR)

        elif first_button:
            button_to_click = buttons[0]
            if 'disabled' in button_to_click.get_attribute('class').split(' '):
                return
            self.click_by_locator(product_page_locators.NEXT_PAGE_BUTTON_LOCATOR)

        self.wait.until(EC.staleness_of(old_card))
        self.wait.until(EC.presence_of_element_located(product_page_locators.CARD_LOCATOR))


    def go_to_next_page(self):
        self._pagination_helper(last_button=True, first_button=False)


    def go_to_previous_page(self):
        self._pagination_helper(last_button=False, first_button=True)


    def get_current_page_number(self) -> int:
        current_page = self.driver.find_element(*product_page_locators.ACTIVE_PAGE_LOCATOR).text
        return int(current_page)


    # max_pages is a safeguard against endless loop. App has normally only 5 pages
    def go_to_all_page_till_last(self, max_pages=10, function=None):
        page_count = 0
        while page_count < max_pages:
            try:
                buttons = self.locate_multiple_elements(product_page_locators.PAGINATION_BUTTONS)
                if not buttons:
                    break
                last_button = buttons[-1]
                old_card = self.driver.find_element(*product_page_locators.CARD_LOCATOR)

                if function is not None:
                    function()

                if 'disabled' in last_button.get_attribute('class').split(' '):
                    return
                self.click_by_locator(product_page_locators.NEXT_PAGE_BUTTON_LOCATOR)
                page_count += 1

                self.wait.until(EC.staleness_of(old_card))
                self.wait.until(EC.presence_of_element_located(product_page_locators.CARD_LOCATOR))

            except (StaleElementReferenceException, TimeoutException):
                continue
        raise TimeoutError("Pagination clicks exceeded the maximum allowed number of pages.")


    def select_eco_friendly_products(self):
        self.click_by_locator(product_page_locators.ECO_FRIENDLY_CHECKBOX_LOCATOR)


    def get_cards_on_the_page(self) -> list:
        located_elements = self.locate_multiple_elements(product_page_locators.CARD_LOCATOR)
        return [element for element in located_elements if element.is_displayed()]


    def get_list_of_card_titles(self)-> list[Any] | None:
        for attempt in range (50):
            try:
                located_elements = self.locate_multiple_elements(product_page_locators.CARD_TITLES_LOCATOR)
                if not located_elements:
                    continue

                if not located_elements[0].get_attribute("textContent").strip():
                    continue
                return [element.get_attribute("textContent").strip() for element in located_elements]
            except (StaleElementReferenceException, TimeoutException):
                if attempt == 49:
                    raise
        return None


    def get_list_of_prices_on_cards(self)-> list:
        located_elements = self.locate_multiple_elements(product_page_locators.CARD_PRICE_LOCATOR)
        return [float(element.text.replace("$", "")) for element in located_elements]


    def get_list_of_co2_values_on_cards(self)-> list:
        located_elements = self.locate_multiple_elements(component_locator.CARD_CO2_RATING)
        return [element.text for element in located_elements]


    def get_cards_with_eco_badge(self)-> list:
        items_with_eco_badge = self.locate_multiple_elements(product_page_locators.ECO_BADGE_LOCATOR)
        return [element for element in items_with_eco_badge if element.is_displayed()]


    def set_price_filter(self, target_min_price: int, target_max_price: int):
        min_price_slider_element = self.locate_element(product_page_locators.MINPRICE_VALUE_CURRENT_LOCATOR)
        max_price_slider_element = self.locate_element(product_page_locators.MAXPRICE_VALUE_CURRENT_LOCATOR)
        current_min_price = int(min_price_slider_element.text)
        current_max_price = int(max_price_slider_element.text)
        self._queue_price_slider_key_presses(current_min_price, target_min_price, product_page_locators.MIN_PRICE_SLIDER_LOCATOR)
        self._queue_price_slider_key_presses(current_max_price, target_max_price, product_page_locators.MAX_PRICE_SLIDER_LOCATOR)
        self._wait_for_prices_to_be_in_range(target_min_price, target_max_price)


    def search_an_item(self, search_query):
        self.fill_field(locator=product_page_locators.SEARCH_INPUT_FIELD_LOCATOR, text=search_query)
        self.click_by_locator(product_page_locators.SEARCH_SUBMIT_BUTTON_LOCATOR)
        self.wait.until(EC.presence_of_element_located(product_page_locators.SEARCH_COMPLETED_LOCATOR))


    def get_search_result_count(self) -> int:
        search_result_count = self.locate_element(product_page_locators.SEARCH_RESULT_COUNT_LOCATOR)
        return int(search_result_count.text[0])


    def get_search_term_value(self) -> str:
        searched_for_value = self.locate_element(product_page_locators.SEARCH_TERM_LOCATOR)
        return searched_for_value.text


    def reset_search(self):
        self.click_by_locator(product_page_locators.SEARCH_RESET_BUTTON_LOCATOR)
        self.wait.until_not(EC.presence_of_element_located(product_page_locators.SEARCH_SUBMITTED_LOCATOR))


    def get_no_products_found_message(self) -> str:
        return self.locate_element(product_page_locators.NO_RESULT_MESSAGE_LOCATOR).text


    def add_to_comparison_main(self):
        self.click_by_locator(product_page_locators.ADD_TO_COMPARISON_LOCATOR_MAIN)

    def remove_from_comparison_main(self):
        self.click_by_locator(product_page_locators.ADD_TO_COMPARISON_LOCATOR_MAIN)

    def _queue_price_slider_key_presses(self, current_price: int, target_price: int, locator: tuple[str,str]):
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
                price_elements = driver.find_elements(*product_page_locators.CARD_PRICE_LOCATOR)
                if not price_elements:
                    return False
                else:
                    prices = [float(element.text.replace("$", "")) for element in price_elements]
                    if len(prices) == len([price for price in prices if min_price <= price <= max_price]):
                        return True
            except StaleElementReferenceException:
                return False

        WebDriverWait(self.driver, timeout).until(_prices_are_filtered)



