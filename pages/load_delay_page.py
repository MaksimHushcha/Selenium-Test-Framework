from pages.locators import load_delay_locators as loc
from pages.base_page import BasePage

class LoadDelayPage(BasePage):

    page_endpoint = "loaddelay/"

    def click_button_appearing_after_delay(self):
        self.click_element(loc.DELAY_BUTTON)

