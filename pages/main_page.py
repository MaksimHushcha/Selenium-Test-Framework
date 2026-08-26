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

    # DO NOT SET MIN PRICE ABOVE MAX PRICE, LOCATORS BEHAVING UNPREDICTABLY
    def move_min_price_slider_to_price(self, target_price: int):
        current_price = int(self.locate_element(loc.MINPRICE_VALUE_CURRENT_LOCATOR).text)
        old_product = self.driver.find_element(
            *loc.CARD_LOCATOR
        )
        self._queue_price_slider_key_presses(current_price, target_price, loc.MIN_PRICE_SLIDER_LOCATOR)
        WebDriverWait(self.driver, 10).until(EC.staleness_of(old_product))

    def move_max_price_slider_to_price(self, target_price: int):
        current_price = int(self.locate_element(loc.MAXPRICE_VALUE_CURRENT_LOCATOR).text)
        old_product = self.driver.find_element(
            *loc.CARD_LOCATOR
        )
        self._queue_price_slider_key_presses(current_price, target_price, loc.MAX_PRICE_SLIDER_LOCATOR)
        WebDriverWait(self.driver, 10).until(EC.staleness_of(self.driver.find_element(*loc.CARD_LOCATOR)))

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
