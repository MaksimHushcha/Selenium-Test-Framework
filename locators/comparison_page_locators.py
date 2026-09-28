from selenium.webdriver.common.by import By

# this locator is identical with component locator, but uses different source
CLEAR_COMPARISON_BUTTON = (By.CSS_SELECTOR, "[data-test=clear-comparison]")
SHOW_DIFFERENT_ONLY_CHECKBOX = (By.CSS_SELECTOR, "[data-test=show-differences]")
REMOVE_FROM_COMPARISON_BUTTON = (By.CSS_SELECTOR, "[data-test=remove-btn]")

COMPARISON_EMPTY = (By.CSS_SELECTOR, "[data-test=comparison-empty]")
COMPARISON_IMAGE = (By.CLASS_NAME, "comparison-img")

BROWSE_PRODUCTS_BUTTON = (By.XPATH, "//a[contains(@href, '/') and contains(@class, 'btn-primary')]")
COMPARISON_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test=product-name]")