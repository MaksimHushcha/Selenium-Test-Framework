import pytest
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


# TODO Refactor with localization file references
@pytest.mark.parametrize(
    "field, error_message",
    [
        (RegistrationFields.first_name, "First name is required"),
        (RegistrationFields.last_name, "Last name is required"),
        (RegistrationFields.date_of_birth, "Please enter a valid date in YYYY-MM-DD format.\nDate of Birth is required"),
        (RegistrationFields.country, "Country is required"),
        (RegistrationFields.postal_code, "Postcode is required"),
        (RegistrationFields.house_number, "House number is required"),
        (RegistrationFields.street_address, "Street is required"),
        (RegistrationFields.city, "City is required"),
        (RegistrationFields.state, "State is required"),
        (RegistrationFields.phone_number, "Phone is required."),
        (RegistrationFields.email, "Email is required"),
        (RegistrationFields.password, "Password is required\nPassword must be minimal 6 characters long.\nPassword can not include invalid characters."),
    ]
)
def test_account_registration_fields_are_mandatory(registration_page, field, error_message):
    registration_page.load()
    registration_data = registration_page.fill_all_registration_data(fields_to_exclude=[field])
    registration_page.submit_registration_form()
    assert registration_page.is_user_on_expected_page(), \
            (f"User is not on registration page page, registration data :"
             f" {registration_data}, current url is {registration_page.get_current_url()}")
    assert registration_page.get_field_error_text(error_field=field) == error_message, f"{registration_data}"

