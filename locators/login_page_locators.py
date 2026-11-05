from selenium.webdriver.common.by import By

EMAIL_ADDRESS_FIELD = (By.CSS_SELECTOR, "[data-test=email]")
PASSWORD_FIELD = (By.CSS_SELECTOR, "[data-test=password]")
SHOW_PASSWORD = (By.CLASS_NAME, "btn-outline-secondary")
LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[data-test=login-submit]")
REGISTER_LINK_BUTTON = (By.CSS_SELECTOR, "[data-test=register-link]")
FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "[data-test=forgot-password-link]")
LOGIN_ERROR = (By.CSS_SELECTOR, "[data-test=login-error]")