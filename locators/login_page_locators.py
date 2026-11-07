from selenium.webdriver.common.by import By

EMAIL_ADDRESS_FIELD = (By.CSS_SELECTOR, "[data-test=email]")
PASSWORD_FIELD = (By.CSS_SELECTOR, "[data-test=password]")
SHOW_PASSWORD = (By.CLASS_NAME, "btn-outline-secondary")

LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[data-test=login-submit]")
REGISTER_LINK_BUTTON = (By.CSS_SELECTOR, "[data-test=register-link]")
FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "[data-test=forgot-password-link]")

LOGIN_ERROR = (By.CSS_SELECTOR, "[data-test=login-error]")
EMAIL_ERROR = (By.CSS_SELECTOR, "[data-test=email-error]")
PASSWORD_ERROR = (By.CSS_SELECTOR, "[data-test=password-error]")

GOOGLE_SSO_BUTTON = (By.CLASS_NAME, "google-sign-in-button")
GOOGLE_SSO_INPUT_EMAIL = (By.XPATH, "//input[@type='text']")
GOOGLE_NEXT_BUTTON = (By.ID, "identifierNext")