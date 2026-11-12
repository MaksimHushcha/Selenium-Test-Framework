from pages.registration_page import RegistrationFields
from tests.conftest import registration_page


def test_field_fill(registration_page):
    registration_page.load()
    data = registration_page.fill_all_registration_data(fields_to_exclude=[RegistrationFields.first_name])
    print(data)