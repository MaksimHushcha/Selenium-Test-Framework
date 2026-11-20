from selenium.webdriver.common.by import By

TOP_RIGHT_TOST_NOTIFICATION_LOCATOR = (By.CLASS_NAME, "toast-message")
CARD_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[data-test=nav-cart]")
CARD_QUANTITY_LOCATOR = (By.CSS_SELECTOR, "[data-test=cart-quantity]")
CARD_CO2_RATING = (By.XPATH, "//span[contains(@class, 'co2-letter') and contains(@class, 'active')]")

# comparison bar
COMPARISON_BAR = (By.CSS_SELECTOR, "[data-test=comparison-bar]")
CLEAR_COMPARISON_BUTTON = (By.CSS_SELECTOR, "[data-test=clear-comparison]")
COMPARE_NOW_BUTTON = (By.CSS_SELECTOR, "[data-test=compare-link]")

NAV_MENU = (By.CSS_SELECTOR, "[data-test=nav-menu]")

LANGUAGE_SELECT = (By.CSS_SELECTOR, "[data-test=language-select]")
DE = (By.CSS_SELECTOR, "[data-test=lang-de]")
EL = (By.CSS_SELECTOR, "[data-test=lang-el]")
EN = (By.CSS_SELECTOR, "[data-test=lang-en]")
ES = (By.CSS_SELECTOR, "[data-test=lang-es]")
FR = (By.CSS_SELECTOR, "[data-test=lang-fr]")
NL = (By.CSS_SELECTOR, "[data-test=lang-nl]")
TR = (By.CSS_SELECTOR, "[data-test=lang-tr]")
LANGUAGE_OPTION_TEMPLATE = (By.CSS_SELECTOR, "[data-test=lang-{locale}]")