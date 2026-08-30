from selenium.common import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    base_url = "https://practicesoftwaretesting.com/"
    page_endpoint = None

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def load(self):
        timeout = 10
        try:
            if self.page_endpoint is None:
                self.driver.get(f"{self.base_url}")
                return self
            else:
                self.driver.get(f"{self.base_url}{self.page_endpoint}")
                return self
        except TimeoutException:
            print(f"Didn't load the page in {timeout} seconds")



    def check_current_url_is(self, expected_url):
        actual_url = self.driver.current_url
        assert actual_url == expected_url, f"URL mismatch! Expected: '{expected_url}', Actual: '{actual_url}'"
        return self

    def check_page_title(self, expected_title):
        actual_title = self.driver.title
        assert expected_title == actual_title, f"Expected page title to be '{expected_title}', Actual: '{actual_title}'"
        return self

    def locate_element(self, locator: tuple):
        return self.driver.find_element(*locator)

    def locate_multiple_elements(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def click_element(self, locator: tuple):
        self.locate_element(locator).click()
        return self

    def get_hex_color_of_element(self, css_property, locator=None, element=None):
        if locator is not None:
            rgba_value_of_css_property = self.locate_element(locator).value_of_css_property(css_property)
            return Color.from_string(rgba_value_of_css_property).hex
        if element is not None:
            rgba_value_of_css_property = element.value_of_css_property(css_property)
            return Color.from_string(rgba_value_of_css_property).hex
        return None

    def verify_list_is_sorted(self, list_to_sort: list, reverse_order: bool) -> bool:
        return list_to_sort == sorted(list_to_sort, reverse=reverse_order)

    def wait_for_element_presence(self, locator: tuple):
        self.wait.until(EC.presence_of_element_located(locator))
        return self

    def wait_for_text_presence(self, locator: tuple):
        self.wait_for_element_presence(locator)
        self.wait.until_not(EC.text_to_be_present_in_element(locator, ""))
        return self

