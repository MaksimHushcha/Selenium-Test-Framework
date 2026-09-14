from selenium.webdriver.common.by import By

# product info locators
PRODUCT_NAME_LOCATOR = (By.CSS_SELECTOR, "[data-test=product-name]")
PRODUCT_DESCRIPTION_LOCATOR = (By.CSS_SELECTOR, "[data-test=product-description]")
PRODUCT_PRICE_LOCATOR = (By.CSS_SELECTOR, "[data-test=unit-price]")
SORT_CO2_RATING_BADGE_LOCATOR = (By.CSS_SELECTOR, "[data-test=co2-rating-badge]")
PRODUCT_PICTURE = (By.CLASS_NAME, "figure-img")
SPECS_LOCATOR = (By.CSS_SELECTOR, "[data-test=spec-value-text]")
TAGS_LOCATOR = (By.CLASS_NAME, "rounded-pill")

# navigation locators
ADD_TO_FAVOURITES_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[data-test=add-to-favorites]")
ADD_TO_CARD_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[data-test=add-to-cart]")
INCREASE_QUANTITY_LOCATOR = (By.CSS_SELECTOR, "[data-test=increase-quantity]")
DECREASE_QUANTITY_LOCATOR = (By.CSS_SELECTOR, "[data-test=decrease-quantity]")
ADD_TO_COMPARISON_LOCATOR = (By.CSS_SELECTOR, "[data-test=add-to-compare]")
