import os

from selenium.common import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    endpoint = ""


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = os.getenv("BASE_URL")


    def load(self, *args):
        full_url = f"{self.base_url}{self.endpoint}"
        try:
            self.driver.get(full_url)
            self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        except TimeoutException:
            print("Page failed to load within the timeout period.")
        return self

    def get_expected_page_url(self):
        return f"{self.base_url}{self.endpoint}"

    def get_current_url(self) -> str:
        return self.driver.current_url

    def get_page_title(self):
        page_title = self.driver.title
        return page_title


    def locate_element(self, locator: tuple[str,str]) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))


    def locate_multiple_elements(self, locator: tuple[str,str]) -> list[WebElement]:
        return self.wait.until(EC.presence_of_all_elements_located(locator))


    def click_by_locator(self, locator: tuple[str, str]):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        return self


    def click_by_web_element(self, element: WebElement):
        self.wait.until(EC.element_to_be_clickable(element)).click()
        return self
    
    
    def click__element_from_multiple(self, element: WebElement):
        self.wait.until(EC.element_to_be_clickable(element)).click()


    def fill_field(self, locator: tuple[str,str], text: str):
        self.locate_element(locator).send_keys(text)
        return self


    def get_hex_color_of_element(self, css_property: str, locator: tuple[str,str] = None,
                                 element: WebElement = None) -> str | None:
        if locator is not None:
            target_element = self.locate_element(locator)
            rgba_value = target_element.value_of_css_property(css_property)
            return Color.from_string(rgba_value).hex

        if element is not None:
            rgba_value = element.value_of_css_property(css_property)
            return Color.from_string(rgba_value).hex

        return None


    def wait_for_element_visibility(self, locator: tuple[str,str]):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self


    def wait_for_text_presence(self, locator: tuple[str,str]):
        self.wait_for_element_visibility(locator)
        self.wait.until_not(EC.text_to_be_present_in_element(locator, ""))
        return self

    def is_element_visible(self, locator: tuple[str,str]):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_element_not_visible(self, locator: tuple[str,str]):
        try:
            self.wait.until_not(EC.visibility_of_element_located(locator))
            return self
        except TimeoutException:
            return False

    # --- SESSION STORAGE HELPERS ---

    def set_item_in_session_storage(self, key, value):
        self.driver.execute_script(f"window.sessionStorage.setItem('{key}', '{value}')")

    def get_item_from_session_storage(self, key: str):
        value = self.driver.execute_script(f"return window.sessionStorage.getItem('{key}');")
        return value
