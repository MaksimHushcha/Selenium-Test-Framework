from selenium.webdriver.common.by import By

PRODUCT_NAME_LOCATOR = (By.CSS_SELECTOR, "[data-test=product-name]")
PRODUCT_DESCRIPTION_LOCATOR = (By.CSS_SELECTOR, "[data-test=product-description]")
PRODUCT_PRICE_LOCATOR = (By.CSS_SELECTOR, "[data-test=unit-price]")
SORT_CO2_RATING_BADGE_LOCATOR = (By.CSS_SELECTOR, "[data-test=co2-rating-badge]")
PRODUCT_PICTURE = (By.CLASS_NAME, "figure-img")
