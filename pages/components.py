from selenium.webdriver.common.by import By
from pages.locators import components as loc

from base_page import BasePage


class Components(BasePage):

    def get_toast_text(self):
        return self.locate_element(loc.TOP_RIGHT_TOST_NOTIFICATION_LOCATOR).text