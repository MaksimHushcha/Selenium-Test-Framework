import pytest
from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_button_with_dynamic_id(dynamic_id_page):
    dynamic_id_page.load()
    dynamic_id_page.click_button_with_dynamic_id()
    dynamic_id_page.check_current_url_is("http://www.uitestingplayground.com/dynamicid/")
    dynamic_id_page.check_page_title("Dynamic ID")

def test_class_attribute_test_alert_primary_button(class_attribute_page):
    class_attribute_page.load()
    class_attribute_page.click_primary_button()
    wait = WebDriverWait(class_attribute_page.driver, 2)
    alert = wait.until(EC.alert_is_present())
    text = alert.text
    expected_text = "Primary button pressed"
    alert.accept()
    assert text == expected_text, f"Alert text {text} does not match the expected text {expected_text}"

def test_success_button_is_green(class_attribute_page):
    class_attribute_page.load()
    expected_green_color = "#28a745"
    assert class_attribute_page.get_color_of_success_button() == expected_green_color

def test_warning_button_is_yellow(class_attribute_page):
    class_attribute_page.load()
    expected_yellow_color = "#ffc107"
    assert class_attribute_page.get_color_of_warning_button() == expected_yellow_color

def test_green_button_cannot_be_hit_twice(hidden_layers_page):
    hidden_layers_page.load()
    hidden_layers_page.click_button_on_top_layer()
    hidden_layers_page.click_hidden_button()
    with pytest.raises(ElementClickInterceptedException):
        hidden_layers_page.click_button_on_top_layer()