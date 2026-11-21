import json
from pathlib import Path
import pytest
from pages.registration_page import RegistrationFields, RegistrationPage
from tests.conftest import registration_page
from utils import helpers

LOCALES_DIR = Path(__file__).parent.parent / "locales"
locales = ["en", "de"]

def _load_registration_locales(locale: str):
    path = LOCALES_DIR / locale / "registration.json"
    return json.loads(path.read_text(encoding="utf-8"))


def _build_mandatory_fields_messages() -> list:
    params = []
    for locale in locales:
        data = _load_registration_locales(locale)
        for field in RegistrationFields:
            error_msg = data["fields"][field.name]["error_messages"]["missing_field"]
            params.append(pytest.param(locale, field, error_msg, id=f"{locale}-{field.name}"))
    return params


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


@pytest.mark.parametrize("locale, field, error_message", _build_mandatory_fields_messages())
def test_account_registration_fields_are_mandatory(registration_page, locale, field, error_message, components):
    registration_page.load()
    if locale != "en":
        components.switch_to_locale(locale)
    registration_data = registration_page.fill_all_registration_data(fields_to_exclude=[field])
    registration_page.submit_registration_form()
    assert registration_page.is_user_on_expected_page(), \
            (f"User is not on registration page page, registration data :"
             f" {registration_data}, current url is {registration_page.get_current_url()}")
    assert registration_page.get_field_error_text(error_field=field) == error_message, f"{registration_data}"

