import json
import os
import time
import urllib.parse
import pytest
from faker import Faker
import dotenv
faker = Faker()


dotenv.load_dotenv()

def test_successful_login_as_user_forwards_to_user_profile(login_page, components):
    login_page.load()
    login_page.login_as_user()
    current_user = components.get_navbar_username()
    assert current_user == "Bob Smith"
    current_url = components.get_current_url()
    assert current_url.endswith("/account"), \
        f"Expected user to be forwarded to /account upon login, but the current url is {current_url} "



def test_successful_login_as_admin_forwards_to_admin_dashboard(login_page, components):
    login_page.load()
    login_page.login_as_admin()
    current_user = components.get_navbar_username()
    assert current_user == "John Doe"
    current_url = components.get_current_url()
    assert current_url.endswith("/admin/dashboard"), \
        f"Expected admin to be forwarded to /admin/dashboard upon login, but the current url is {current_url} "


def test_login_with_incorrect_password_displays_a_correct_error(login_page):
    login_page.load()
    login_page.input_email_address(os.getenv("USER_EMAIL"))
    login_page.input_password(faker.password())
    login_page.press_login_button()
    assert login_page.get_login_error_message() == "Invalid email or password"
    current_url = login_page.get_current_url()
    assert current_url.endswith("/login"), \
        f"Expected user to remain at /login, but the current url is {current_url} "


def test_login_with_valid_email_and_no_password_displays_a_correct_error(login_page):
    login_page.load()
    login_page.input_email_address(os.getenv("USER_EMAIL"))
    login_page.press_login_button()
    assert login_page.get_password_error_message() == "Password is required"


def test_login_with_valid_password_and_no_email_address_displays_a_correct_error(login_page):
    login_page.load()
    login_page.input_password(os.getenv("USER_PASSWORD"))
    login_page.press_login_button()
    assert login_page.get_email_error_message() == "Email is required"


def test_login_without_email_and_no_password_displays_both_messages(login_page):
    login_page.load()
    login_page.press_login_button()
    assert login_page.get_email_error_message() == "Email is required"
    assert login_page.get_password_error_message() == "Password is required"


def test_user_gets_a_hint_when_password_is_shorter_than_2_symbols(login_page):
    login_page.load()
    login_page.input_email_address(faker.email())
    login_page.input_password("ab")
    login_page.press_login_button()
    assert login_page.get_password_error_message() == "Password length is invalid"


@pytest.mark.parametrize("email", [
    "plainaddress",
    "@missingdomain.com",
    "two.dots@domain..com",
    "no.top.level.domain@domain"
])
def test_email_fields_verifies_email_format(login_page, email):
    login_page.load()
    login_page.input_email_address(email)
    login_page.input_password(os.getenv("USER_PASSWORD"))
    login_page.press_login_button()
    assert login_page.get_email_error_message() == "Email format is invalid"


def test_show_password_displays_the_password(login_page):
    login_page.load()
    login_page.input_email_address(os.getenv("USER_EMAIL"))
    login_page.input_password(os.getenv("USER_PASSWORD"))
    assert login_page.is_password_masked() == True, f"Expected password to be masked"
    login_page.show_password()
    assert login_page.is_password_masked() == False, f"Expected password to be unmasked after show_password"
    login_page.show_password()
    assert login_page.is_password_masked() == True, f"Expected password to be unmasked after second show_password"


def test_google_sso_redirect(login_page):
    login_page.load()

    login_page.click_google_sso_button()
    current_url = login_page.driver.current_url

    assert "accounts.google.com" in current_url
    assert "client_id=" in current_url
    assert "redirect_uri=" in current_url
    assert "response_type=code" in current_url



# I don't know the amount of attempts needed, temporary values, to investigate later
def test_login_with_incorrect_password_locks_account_out(login_page):
    number_of_attempts = 5
    for current_attempt in range(number_of_attempts):
        login_page.load()
        login_page.input_email_address(os.getenv("USER_EMAIL_ACCOUNT_LOCKOUT"))
        login_page.input_password(faker.password())
        login_page.press_login_button()
        if current_attempt == 5:
            assert login_page.get_login_error_message() == "Account locked, too many failed attempts. Please contact the administrator."
