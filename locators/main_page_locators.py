from selenium.webdriver.common.by import By

from locators.comparison_page_locators import REMOVE_FROM_COMPARISON_BUTTON
from locators.product_page_locators import ADD_TO_COMPARISON_LOCATOR

# sorting locators
SORT_DROPDOWN_LOCATOR = (By.CSS_SELECTOR, "[data-test=sort]")
SORT_NAME_ASC_LOCATOR = (By.CSS_SELECTOR, "[value*='name,asc']")
SORT_NAME_DESC_LOCATOR = (By.CSS_SELECTOR, "[value*='name,desc']")
SORT_PRICE_ASC_LOCATOR = (By.CSS_SELECTOR, "[value*='price,asc']")
SORT_PRICE_DESC_LOCATOR = (By.CSS_SELECTOR, "[value*='price,desc']")
SORT_CO2_RATING_ASC_LOCATOR = (By.CSS_SELECTOR, "[value*='co2_rating,asc']")
SORT_CO2_RATING_DESC_LOCATOR = (By.CSS_SELECTOR, "[value*='co2_rating,desc']")
SORTING_COMPLETED_LOCATOR = (By.CSS_SELECTOR, "[data-test=sorting_completed]")

# card locators
CARD_LOCATOR = (By.CLASS_NAME, "card")
CARD_GRID_LOCATOR = (By.CLASS_NAME, "container")
CARD_TITLES_LOCATOR = (By.CLASS_NAME, "card-title")
CARD_PRICE_LOCATOR = (By.CSS_SELECTOR, "[data-test=product-price]")
ECO_BADGE_LOCATOR = (By.CSS_SELECTOR, "[data-test=eco-badge]")
CARD_PRODUCT_LOCATOR = (By.CSS_SELECTOR, 'a.card[data-test^="product-"]')
AVAILABLE_PRODUCT_LINK_LOCATOR = (By.CSS_SELECTOR, 'a.card[href^="/product"]:not(:has([data-test="out-of-stock"])')
ADD_TO_COMPARISON_LOCATOR_MAIN = (By.CLASS_NAME, "compare-btn")
REMOVE_FROM_COMPARISON_MAIN = (By.CLASS_NAME, "compare-btn-active")

# filter locators
ECO_FRIENDLY_CHECKBOX_LOCATOR = (By.CSS_SELECTOR, "[data-test=eco-friendly-filter]")
MIN_PRICE_SLIDER_LOCATOR = (By.CLASS_NAME, "ngx-slider-pointer-min")
MAX_PRICE_SLIDER_LOCATOR = (By.CLASS_NAME, "ngx-slider-pointer-max")
MINPRICE_VALUE_CURRENT_LOCATOR = (By.CLASS_NAME, "ngx-slider-model-value")
MAXPRICE_VALUE_CURRENT_LOCATOR = (By.CLASS_NAME, "ngx-slider-model-high")
PRICE_SLIDER_LOCATOR = (By.CLASS_NAME, "ngx-slider-full-bar")

# navigation locators
PREV_PAGE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[data-test=pagination-prev]")
NEXT_PAGE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[data-test=pagination-next]")
PAGINATION_BUTTONS = (By.CLASS_NAME, "page-item")
ACTIVE_PAGE_LOCATOR = (By.XPATH, "//li[contains(@class, 'page-item') and contains(@class, 'active')]")

# search
SEARCH_INPUT_FIELD_LOCATOR = (By.CSS_SELECTOR, "[data-test=search-query]")
SEARCH_SUBMIT_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[data-test=search-submit]")
SEARCH_RESET_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[data-test=search-reset]")
SEARCH_COMPLETED_LOCATOR = (By.CSS_SELECTOR, "[data-test=search_completed]")
SEARCH_RESULT_COUNT_LOCATOR = (By.CSS_SELECTOR, "[data-test=search-result-count]")
NO_RESULT_MESSAGE_LOCATOR = (By.CSS_SELECTOR, "[data-test=no-results]")
SEARCH_TERM_LOCATOR = (By.CSS_SELECTOR, "[data-test=search-term]")
SEARCH_SUBMITTED_LOCATOR = (By.CLASS_NAME, "ng-submitted")