from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from faker import Faker
from conftest import *
import pytest

faker = Faker()

def test_input(chrome_driver):
    chrome_driver.get("https://testpages.eviltester.com/")
    assert chrome_driver.current_url == "https://testpages.eviltester.com/"
    assert chrome_driver.title == "Software Testing Practice Pages, Apps, and Challenges"

    chrome_driver.get("https://testpages.eviltester.com/pages/input-elements/text-inputs/")
    assert chrome_driver.current_url == "https://testpages.eviltester.com/pages/input-elements/text-inputs/"
    assert chrome_driver.title == "Text Input Elements - Events Display Test Page | Test Pages"

    text_input = chrome_driver.find_element(By.ID, value="text-input")
    random_input = faker.word()
    text_input.send_keys(random_input)
    assert text_input.is_displayed()

    WebDriverWait(chrome_driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "text-input-value-value"), random_input)
    )


####

def test_form(chrome_driver):
    chrome_driver.get("https://testpages.eviltester.com/pages/forms/text-inputs/")

    text_input_form_text = chrome_driver.find_element(By.ID, value="text-input")
    text_input_form_search = chrome_driver.find_element(By.CSS_SELECTOR, value="#search-input")
    text_input_form_password = chrome_driver.find_element(By.NAME, value="password")
    text_input_form_email = chrome_driver.find_element(By.XPATH, value='//*[@id="email-input"]')
    text_input_form_url = chrome_driver.find_element(By.ID, value="url-input")
    text_input_form_tel = chrome_driver.find_element(By.ID, value="tel-input")
    text_input_form_text_default = chrome_driver.find_element(By.ID, value="text-default-input")

    text_data = faker.word()
    text_input_form_text.send_keys(text_data)

    search_data = faker.word()
    text_input_form_search.send_keys(search_data)

    password_data = faker.word()
    text_input_form_password.send_keys(password_data)

    email_data = faker.email()
    text_input_form_email.send_keys(email_data)

    url_data = faker.url()
    text_input_form_url.send_keys(url_data)

    phone_data = faker.phone_number()
    text_input_form_tel.send_keys(phone_data)

    default_text_data = faker.word()
    text_input_form_text_default.send_keys(default_text_data)

    text_input_form_submit_button = chrome_driver.find_element(By.XPATH, value="//*[@id='ajax-submitted-form']/div[2]/input[2]")
    chrome_driver.execute_script("arguments[0].click();", text_input_form_submit_button)

    assert chrome_driver.current_url == "https://testpages.eviltester.com/pages/forms/submit"
    assert chrome_driver.title == "Form Submission | Test Pages"

    submitted_text = chrome_driver.find_element(By.ID, value="_valuetext")
    assert submitted_text.is_displayed()
    assert submitted_text.text == text_data

    submitted_search = chrome_driver.find_element(By.ID, value="_valuesearch")
    assert submitted_search.is_displayed()
    assert submitted_search.text == search_data

    submitted_password = chrome_driver.find_element(By.ID, value="_valuepassword")
    assert submitted_password.is_displayed()
    assert submitted_password.text == password_data

    submitted_password = chrome_driver.find_element(By.ID, value="_valuepassword")
    assert submitted_password.is_displayed()
    assert submitted_password.text == password_data

    submitted_email = chrome_driver.find_element(By.ID, value="_valueemail")
    assert submitted_email.is_displayed()
    assert submitted_email.text == email_data

    submitted_url = chrome_driver.find_element(By.ID, value="_valueurl")
    assert submitted_url.is_displayed()
    assert submitted_url.text == url_data

    submitted_tel = chrome_driver.find_element(By.ID, value="_valuetel")
    assert submitted_tel.is_displayed()
    assert submitted_tel.text == phone_data

    submitted_default_text_data = chrome_driver.find_element(By.ID, value="_valuetext-default")
    assert submitted_default_text_data.is_displayed()
    assert submitted_default_text_data.text == default_text_data

    submitted_submit_button = chrome_driver.find_element(By.ID, value="_valuesubmitbutton")
    assert submitted_submit_button.is_displayed()
    assert submitted_submit_button.text == "submit"