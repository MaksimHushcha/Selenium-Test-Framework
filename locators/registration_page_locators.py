from selenium.webdriver.common.by import By

FIRST_NAME_LOCATOR = (By.CSS_SELECTOR, "[data-test=first-name]")
LAST_NAME_LOCATOR = (By.CSS_SELECTOR, "[data-test=last-name]")
DOB_LOCATOR = (By.CSS_SELECTOR, "[data-test=dob]")
COUNTRY_DROPDOWN_LOCATOR = (By.CSS_SELECTOR, "[data-test=country]")
POSTAL_CODE_LOCATOR = (By.CSS_SELECTOR, "[data-test=postal_code]")
HOUSE_NUMBER_LOCATOR = (By.CSS_SELECTOR, "[data-test=house_number]")
STREET_FIELD_LOCATOR = (By.CSS_SELECTOR, "[data-test=street]")
CITY_LOCATOR = (By.CSS_SELECTOR, "[data-test=city]")
STATE_LOCATOR = (By.CSS_SELECTOR, "[data-test=state]")
PHONE_LOCATOR = (By.CSS_SELECTOR, "[data-test=phone]")
EMAIL_ADDRESS = (By.CSS_SELECTOR, "[data-test=email]")

PASSWORD_LOCATOR = (By.CSS_SELECTOR, "[data-test=password]")
SHOW_PASSWORD = (By.CLASS_NAME, "btn-outline-secondary")
PASSWORD_STRENGTH_LOCATOR = (By.CLASS_NAME, "strength-bar")

SUBMIT_REGISTRATION_LOCATOR = (By.CSS_SELECTOR, "[data-test=register-submit]")

REGISTRATION_ERROR_LOCATOR = (By.CSS_SELECTOR, "[data-test=register-error]")