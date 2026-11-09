import os
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import login_page_locators as loc
from dotenv import load_dotenv

load_dotenv()

class LoginPage(BasePage):

    endpoint = "auth/login"

    def get_login_error_message(self):
        return self.locate_element(loc.LOGIN_ERROR).text

    def get_password_error_message(self):
        return self.locate_element(loc.PASSWORD_ERROR).text

    def get_email_error_message(self):
        return self.locate_element(loc.EMAIL_ERROR).text

    def input_email_address(self, email):
        self.fill_field(loc.EMAIL_ADDRESS_FIELD, email)

    def input_password(self, password):
        self.fill_field(loc.PASSWORD_FIELD, password)

    def press_login_button(self):
        self.click_by_locator(loc.LOGIN_SUBMIT_BUTTON)

    def press_register_link(self):
        self.click_by_locator(loc.REGISTER_LINK_BUTTON)

    def click_forgot_password_link(self):
        self.click_by_locator(loc.FORGOT_PASSWORD_LINK)

    def show_password(self):
        self.click_by_locator(loc.SHOW_PASSWORD)

    def login_as_user(self):
        self.input_email_address(os.getenv("USER_EMAIL"))
        self.input_password(os.getenv("USER_PASSWORD"))
        self.press_login_button()

    def login_as_admin(self):
        self.input_email_address(os.getenv("ADMIN_EMAIL"))
        self.input_password(os.getenv("ADMIN_PASSWORD"))
        self.press_login_button()

    def is_password_masked(self):
        if self.get_attribute("type", loc.PASSWORD_FIELD) == "password":
            return True
        else:
            return False

    def click_google_sso_button(self):
        original_handles = set(self.driver.window_handles)

        self.click_by_locator(loc.GOOGLE_SSO_BUTTON)

        self.wait.until(
            lambda driver: (
                    len(driver.window_handles) > len(original_handles)
                    or "google.com" in driver.current_url
            )
        )
        for handle in self.driver.window_handles:
            if handle not in original_handles:
                self.driver.switch_to.window(handle)
                break

        self.wait.until(EC.url_contains("google.com"))

