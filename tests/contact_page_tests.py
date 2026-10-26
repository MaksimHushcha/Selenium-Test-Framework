from conftest import contact_page
from faker import Faker
fake = Faker()


def test_sending_contact_with_correct_info_correctly_sends_info(contact_page):
    contact_page.load()
    contact_page.fill_and_submit_all_contact_data()
    expected_message = "Thanks for your message! We will contact you shortly."
    received_message = contact_page.get_success_alert_text()
    assert received_message == expected_message, \
            f"Expected to see {expected_message}, but got {received_message}"


def test_first_name_is_mandatory_when_sending_contact_message(contact_page):
    contact_page.load()
    contact_page.fill_and_submit_all_contact_data(fields_to_exclude=["First Name"])
    expected_message = "First name is required"
    received_message = contact_page.get_first_name_error_message()
    assert received_message == expected_message, \
            f"Expected to see {expected_message}, but got {received_message}"


def test_last_name_is_mandatory_when_sending_contact_message(contact_page):
    contact_page.load()
    contact_page.fill_and_submit_all_contact_data(fields_to_exclude=["Last Name"])
    expected_message = "Last name is required"
    received_message = contact_page.get_last_name_error_message()
    assert received_message == expected_message, \
            f"Expected to see {expected_message}, but got {received_message}"

def test_email_address_is_mandatory_when_sending_contact_message(contact_page):
    contact_page.load()
    contact_page.fill_and_submit_all_contact_data(fields_to_exclude=["Email"])
    expected_message = "Email is required"
    received_message = contact_page.get_email_error_message()
    assert received_message == expected_message, \
            f"Expected to see {expected_message}, but got {received_message}"