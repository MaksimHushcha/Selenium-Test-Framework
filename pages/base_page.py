from urllib.parse import urljoin

from selenium.common import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    base_url = "https://practicesoftwaretesting.com/"
    path = None

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def load(self, *args):
        target_url = f"{self.base_url.rstrip('/')}/{self.path}/"
        try:
            self.driver.get(target_url)
            self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        except TimeoutException:
            print("Page failed to load within the timeout period.")
        return self

    def check_current_url_is(self, expected_url):
        actual_url = self.driver.current_url
        assert actual_url == expected_url, f"URL mismatch! Expected: '{expected_url}', Actual: '{actual_url}'"
        return self

    def check_page_title(self, expected_title):
        actual_title = self.driver.title
        assert expected_title == actual_title, f"Expected page title to be '{expected_title}', Actual: '{actual_title}'"
        return self

    def locate_element(self, locator: tuple[str,str]) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def locate_multiple_elements(self, locator: tuple[str,str]) -> list[WebElement]:
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator: tuple[str,str]):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        return self

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

    def verify_list_is_sorted(self, list_to_sort: list, reverse_order: bool) -> bool:
        return list_to_sort == sorted(list_to_sort, reverse=reverse_order)

    def wait_for_element_presence(self, locator: tuple[str,str]):
        self.wait.until(EC.presence_of_element_located(locator))
        return self

    def wait_for_text_presence(self, locator: tuple[str,str]):
        self.wait_for_element_presence(locator)
        self.wait.until_not(EC.text_to_be_present_in_element(locator, ""))
        return self

