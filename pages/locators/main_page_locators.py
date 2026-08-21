from selenium.webdriver.common.by import By

SORT_DROPDOWN_LOCATOR = (By.CSS_SELECTOR, "[data-test=sort]")
SORT_NAME_ASC_LOCATOR = (By.CSS_SELECTOR, "[value*='name,asc']")
SORT_NAME_DESC_LOCATOR = (By.CSS_SELECTOR, "[value*='name,desc']")
CARD_TITLES_LOCATOR = (By.CLASS_NAME, "card-title")