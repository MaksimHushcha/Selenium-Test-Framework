from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker
from conftest import *
import pytest

faker = Faker()


def test_input(driver):
    driver.get("https://testpages.eviltester.com/")
    assert driver.current_url == "https://testpages.eviltester.com/"
    assert driver.title == "Software Testing Practice Pages, Apps, and Challenges"

    driver.get("https://testpages.eviltester.com/pages/input-elements/text-inputs/")
    assert driver.current_url == "https://testpages.eviltester.com/pages/input-elements/text-inputs/"
    assert driver.title == "Text Input Elements - Events Display Test Page | Test Pages"

    text_input = driver.find_element(By.ID, value="text-input")
    random_input = faker.word()
    text_input.send_keys(random_input)
    assert text_input.is_displayed()

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "text-input-value-value"), random_input)
    )

    tags_cloud = driver.find_elements(By.CLASS_NAME, value ="taxonomy-term")
    for tag in tags_cloud:
        print(tag.get_attribute("text"))
        assert tag.is_displayed()
####

def test_form(driver):
    driver.get("https://testpages.eviltester.com/pages/forms/text-inputs/")

    text_input_form_text = driver.find_element(By.ID, value="text-input")
    text_input_form_search = driver.find_element(By.CSS_SELECTOR, value="#search-input")
    text_input_form_password = driver.find_element(By.NAME, value="password")
    text_input_form_email = driver.find_element(By.XPATH, value='//*[@id="email-input"]')
    text_input_form_url = driver.find_element(By.ID, value="url-input")
    text_input_form_tel = driver.find_element(By.ID, value="tel-input")
    text_input_form_text_default = driver.find_element(By.ID, value="text-default-input")

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

    text_input_form_submit_button = driver.find_element(By.XPATH, value="//*[@id='ajax-submitted-form']/div[2]/input[2]")
    driver.execute_script("arguments[0].click();", text_input_form_submit_button)

    assert driver.current_url == "https://testpages.eviltester.com/pages/forms/submit"
    assert driver.title == "Form Submission | Test Pages"

    submitted_text = driver.find_element(By.ID, value="_valuetext")
    assert submitted_text.is_displayed()
    assert submitted_text.text == text_data

    submitted_search = driver.find_element(By.ID, value="_valuesearch")
    assert submitted_search.is_displayed()
    assert submitted_search.text == search_data

    submitted_password = driver.find_element(By.ID, value="_valuepassword")
    assert submitted_password.is_displayed()
    assert submitted_password.text == password_data

    submitted_password = driver.find_element(By.ID, value="_valuepassword")
    assert submitted_password.is_displayed()
    assert submitted_password.text == password_data

    submitted_email = driver.find_element(By.ID, value="_valueemail")
    assert submitted_email.is_displayed()
    assert submitted_email.text == email_data

    submitted_url = driver.find_element(By.ID, value="_valueurl")
    assert submitted_url.is_displayed()
    assert submitted_url.text == url_data

    submitted_tel = driver.find_element(By.ID, value="_valuetel")
    assert submitted_tel.is_displayed()
    assert submitted_tel.text == phone_data

    submitted_default_text_data = driver.find_element(By.ID, value="_valuetext-default")
    assert submitted_default_text_data.is_displayed()
    assert submitted_default_text_data.text == default_text_data

    submitted_submit_button = driver.find_element(By.ID, value="_valuesubmitbutton")
    assert submitted_submit_button.is_displayed()
    assert submitted_submit_button.text == "submit"

def test_select(driver):
    driver.get("https://testpages.eviltester.com/pages/forms/other-text/")
    select = driver.find_element(By.ID, value="select-input")
    dropdown = Select(select)
    selected_option = dropdown.options[3].get_attribute("value")
    dropdown.select_by_index(3)

    submit_button = driver.find_element(By.CSS_SELECTOR, value="[value=submit]")
    driver.execute_script("arguments[0].click();", submit_button)
    submitted_dropdown = driver.find_element(By.ID, value="_valuedropdown")
    assert submitted_dropdown.is_displayed()
    assert submitted_dropdown.text == selected_option

def test_wait_for(driver):
    driver.get("https://testpages.eviltester.com/apps/basiccart/?page=1&limit=10")
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "view")))
    driver.find_element(By.CLASS_NAME, "view").click()

def test_open_in_new_tab(driver):
    driver.get("https://testpages.eviltester.com/")
    privacy_policy = driver.find_element(By.LINK_TEXT, "Privacy Policy")
    driver.execute_script("arguments[0].click();", privacy_policy)
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == "https://www.eviltester.com/page/privacy/"

def test_iframe(driver):
    driver.get("https://testpages.eviltester.com/pages/embedded-pages/iframes/")
    iframe = driver.find_element(By.ID, value="alist")
    driver.switch_to.frame(iframe)
    driver.find_element(By.ID, "iframe44").click()
    driver.switch_to.default_content()

def test_hover(driver):
    driver.get("https://www.onliner.by/")
    wait = WebDriverWait(driver, 5)

    news_xpath = "//a[span[@class='b-main-navigation__text' and text()='Новости']]"
    news = wait.until(EC.presence_of_element_located((By.XPATH, news_xpath)))

    ActionChains(driver).move_to_element(news).perform()

    tech_xpath = "//a[@class='b-main-navigation__dropdown-title-link' and contains(., 'Технологии')]"
    technology = wait.until(EC.visibility_of_element_located((By.XPATH, tech_xpath)))
    technology.click()

