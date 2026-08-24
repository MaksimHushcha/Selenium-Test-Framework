from selenium.webdriver.common.by import By


#sorting locators
SORT_DROPDOWN_LOCATOR = (By.CSS_SELECTOR, "[data-test=sort]")
SORT_NAME_ASC_LOCATOR = (By.CSS_SELECTOR, "[value*='name,asc']")
SORT_NAME_DESC_LOCATOR = (By.CSS_SELECTOR, "[value*='name,desc']")
SORT_PRICE_ASC_LOCATOR = (By.CSS_SELECTOR, "[value*='price,asc']")
SORT_PRICE_DESC_LOCATOR = (By.CSS_SELECTOR, "[value*='price,desc']")
SORT_CO2_RATING_ASC_LOCATOR = (By.CSS_SELECTOR, "[value*='co2_rating,asc']")
SORT_CO2_RATING_DESC_LOCATOR = (By.CSS_SELECTOR, "[value*='co2_rating,desc']")
SORTING_COMPLETED_LOCATOR = (By.CSS_SELECTOR, "[data-test=sorting_completed]")

#card locators
CARD_LOCATOR = (By.CLASS_NAME, "card")
CARD_TITLES_LOCATOR = (By.CLASS_NAME, "card-title")
CARD_PRICE_LOCATOR = (By.CSS_SELECTOR, "[data-test=product-price]")
CARD_CO2_RATING = (By.XPATH, "//span[contains(@class, 'co2-letter') and contains(@class, 'active')]")
ECO_BADGE_LOCATOR = (By.CSS_SELECTOR, "[data-test=eco-badge]")

#filter locators
ECO_FRIENDLY_CHECKBOX_LOCATOR = (By.CSS_SELECTOR, "[data-test=eco-friendly-filter]")
MIN_PRICE_SLIDER_LOCATOR = (By.CLASS_NAME, "ngx-slider-pointer-min")
PRICE_SLIDER_LOCATOR = (By.CLASS_NAME, "ngx-slider-full-bar")