from registration_page import RegistrationFields
from tests.conftest import registration_page


def test_field_fill(registration_page):
    registration_page.load()
    fields = registration_page.fill_all_contact_data(fields_to_exclude=[RegistrationFields.first_name])


def test_select_random_country(registration_page):
    registration_page.load()
    registration_page.select_random_country()

def test_select_country_by_value(registration_page):
    registration_page.load()
    registration_page.select_country_by_value("PL")