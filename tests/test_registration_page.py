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
    registration_data = registration_page.fill_all_registration_data(fields_to_exclude=[field])
    registration_page.submit_registration_form()
    assert registration_page.is_user_on_expected_page(), \
            (f"User is not on registration page page, registration data :"
             f" {registration_data}, current url is {registration_page.get_current_url()}")
    assert registration_page.get_field_error_text(error_field=field) == reg_empty_error_message, f"{registration_data}"

