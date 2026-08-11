
class BasePage:
    base_url = "http://www.uitestingplayground.com/"
    page_endpoint = None

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(f"{self.base_url}{self.page_endpoint}")
        return self

    def check_current_url_is(self, expected_url):
        actual_url = self.driver.current_url
        assert actual_url == expected_url, f"URL mismatch! Expected: '{expected_url}', Actual: '{actual_url}'"
        return self

    def locate_element(self, locator):
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        self.driver.find_element(*locator).click()
        return self