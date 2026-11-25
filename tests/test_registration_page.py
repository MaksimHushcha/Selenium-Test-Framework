import os

import pytest

from pages.registration_page import RegistrationFields
from fixtures.pages_fixtures import registration_page
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


def test_account_registration_fields_are_mandatory(registration_page, components, locale, field, reg_empty_error_message):
    registration_page.load()
    if locale != "en":
        components.switch_to_locale(locale)
    fields_to_exclude = [field]

    # these fields are filled automatically when state is selected, so we need to keep state empty as well
    address_fields = {
        RegistrationFields.street_address,
        RegistrationFields.house_number,
        RegistrationFields.postal_code,
    }
    if field in address_fields:
        fields_to_exclude.append(RegistrationFields.country)

    registration_data = registration_page.fill_all_registration_data(fields_to_exclude=fields_to_exclude)
    registration_page.submit_registration_form()
    assert registration_page.is_user_on_expected_page(), \
            (f"User is not on registration page page, registration data :"
             f" {registration_data}, current url is {registration_page.get_current_url()}")
    assert registration_page.get_field_error_text(error_field=field) == reg_empty_error_message, f"{registration_data}"


@pytest.mark.skipif(os.getenv("GITHUB_ACTIONS") == "true", reason="Password strength is updated unpredictably, disabled"
                                                                  "until fixed (It will never")
def test_password_strength_is_enforced(registration_page, login_page):
    registration_page.load()
    registration_data = registration_page.fill_all_registration_data(fields_to_exclude=[RegistrationFields.password])
    registration_page.input_password("StrongPassword123123123@@@@@@@@@@")
    password_strength_class = registration_page.get_password_strength()
    assert password_strength_class == "excellent", f"Password is not marked as excellent : {registration_data}"

# the number of tests for registration form alone is too big