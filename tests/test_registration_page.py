from pages.registration_page import RegistrationFields
from tests.conftest import registration_page
from utils import helpers


def test_account_registration_with_all_correct_data(registration_page, login_page):
    registration_page.load()
    registration_data = registration_page.fill_all_registration_data()
    registration_page.submit_registration_form()

    registration_email = registration_data.get(RegistrationFields.email)
    registration_password = registration_data.get(RegistrationFields.password)

    assert login_page.is_user_on_expected_page(), \
        f"User is not on login page, registration data : {registration_data}, current url is {registration_page.get_current_url()}"
    assert helpers.does_user_exist(registration_email, registration_password), \
         f"Failed to login with {registration_data}"

# TODO REFACTOR TO PARAMETRIZED TESTS
def test_account_registration_first_name_is_mandatory(registration_page):
    registration_page.load()
    registration_data = registration_page.fill_all_registration_data(fields_to_exclude=[RegistrationFields.first_name])
    registration_page.submit_registration_form()

    assert registration_page.get_first_name_error() == "First name is required", f"{registration_data}"
    assert registration_page.is_user_on_expected_page(), \
        f"User is not on registration page page, registration data : {registration_data}, current url is {registration_page.get_current_url()}"


def test_account_registration_last_name_is_mandatory(registration_page):
    registration_page.load()
    registration_data = registration_page.fill_all_registration_data(fields_to_exclude=[RegistrationFields.last_name])
    registration_page.submit_registration_form()

    assert registration_page.get_last_name_error() == "Last name is required", f"{registration_data}"
    assert registration_page.is_user_on_expected_page(), \
        f"User is not on registration page page, registration data : {registration_data}, current url is {registration_page.get_current_url()}"


def test_account_registration_date_of_birth_is_mandatory(registration_page):
    registration_page.load()
    registration_data = registration_page.fill_all_registration_data(fields_to_exclude=[RegistrationFields.date_of_birth])
    registration_page.submit_registration_form()

    assert registration_page.get_date_of_birth_error() == "Please enter a valid date in YYYY-MM-DD format.\nDate of Birth is required", f"{registration_data}"
    assert registration_page.is_user_on_expected_page(), \
        f"User is not on registration page page, registration data : {registration_data}, current url is {registration_page.get_current_url()}"


def test_account_registration_country_is_mandatory(registration_page):
    registration_page.load()
    registration_data = registration_page.fill_all_registration_data(fields_to_exclude=[RegistrationFields.country])
    registration_page.submit_registration_form()

    assert registration_page.get_country_error() == "Country is required", f"{registration_data}"
    assert registration_page.is_user_on_expected_page(), \
        f"User is not on registration page page, registration data : {registration_data}, current url is {registration_page.get_current_url()}"