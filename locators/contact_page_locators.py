from selenium.webdriver.common.by import By

# FIELDS LOCATORS
FIRST_NAME_FIELD_LOCATOR = (By.CSS_SELECTOR, "[data-test=first-name]")
LAST_NAME_FIELD_LOCATOR = (By.CSS_SELECTOR, "[data-test=last-name]")
MESSAGE_FIELD_LOCATOR = (By.CSS_SELECTOR, "[data-test=message]")
EMAIL_FIELD_LOCATOR = (By.CSS_SELECTOR, "[data-test=email]")


# SUBJECT FIELD LOCATORS
SUBJECT_FIELD_LOCATOR = (By.CSS_SELECTOR, "[data-test=subject]")
CUSTOMER_SERVICE_SUBJECT_LOCATOR = (By.CSS_SELECTOR, "[value=customer-service]")
WEBMASTER_SERVICE_SUBJECT_LOCATOR = (By.CSS_SELECTOR, "[value=webmaster]")
RETURN_SERVICE_SUBJECT_LOCATOR = (By.CSS_SELECTOR, "[value=return]")
PAYMENTS_SERVICE_SUBJECT_LOCATOR = (By.CSS_SELECTOR, "[value=payments]")
WARRANTY_SERVICE_SUBJECT_LOCATOR = (By.CSS_SELECTOR, "[value=warranty]")
STATUS_OF_ORDER_SUBJECT_LOCATOR = (By.CSS_SELECTOR, "[value=warranty]")

# ATTACHMENTS_LOCATORS
ATTACHMENT_FIELD_LOCATOR = (By.CSS_SELECTOR, "input[type='file']")
ATTACHMENT_HELP_LOCATOR = (By.CSS_SELECTOR, "[id=attachmentHelp]")

SEND_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[data-test=contact-submit]")

# ERROR MESSAGES_LOCATORS
FIRST_NAME_ERROR = (By.CSS_SELECTOR, "[data-test=first-name-error]")
LAST_NAME_ERROR = (By.CSS_SELECTOR, "[data-test=last-name-error]")
EMAIL_ERROR = (By.CSS_SELECTOR, "[data-test=email-error]")
SUBJECT_ERROR = (By.CSS_SELECTOR, "[data-test=subject-error]")
MESSAGE_ERROR = (By.CSS_SELECTOR, "[data-test=message-error]")
ATTACHMENT_ERROR = (By.CSS_SELECTOR, "[data-test=attachment-error]")
HELP_BLOCK = (By.CLASS_NAME, "help-block")


ALERT_SUCCESS = (By.CLASS_NAME, "alert-success")

