from selenium.webdriver.common.by import By

TOP_RIGHT_TOST_NOTIFICATION_LOCATOR = (By.CLASS_NAME, "toast-message")
CARD_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[data-test=nav-cart]")
CARD_QUANTITY_LOCATOR = (By.CSS_SELECTOR, "[data-test=cart-quantity]")
CARD_CO2_RATING = (By.XPATH, "//span[contains(@class, 'co2-letter') and contains(@class, 'active')]")

# comparison bar
COMPARISON_BAR = (By.CSS_SELECTOR, "[data-test=comparison-bar]")
CLEAR_COMPARISON_BUTTON = (By.CSS_SELECTOR, "[data-test=clear-comparison]")
COMPARE_NOW_BUTTON = (By.CSS_SELECTOR, "[data-test=compare-link]")