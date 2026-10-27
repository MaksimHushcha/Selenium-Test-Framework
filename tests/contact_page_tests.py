from conftest import contact_page
from faker import Faker
fake = Faker()

def test_sending_contact_with_correct_info_correctly_sends_info(contact_page):
    contact_page.load()
    contact_page.fill_all_contact_data()
    contact_page.send_message()

    expected_message = "Thanks for your message! We will contact you shortly."
    received_message = contact_page.get_success_alert_text()
    assert received_message == expected_message, \
            f"Expected to see {expected_message}, but got {received_message}"


def test_first_name_is_mandatory_when_sending_contact_message(contact_page):
    contact_page.load()
    contact_page.fill_all_contact_data(fields_to_exclude=["First Name"])
    contact_page.send_message()

    expected_message = "First name is required"
    received_message = contact_page.get_first_name_error_message()
    assert received_message == expected_message, \
            f"Expected to see {expected_message}, but got {received_message}"


def test_first_name_121_char_long_is_not_accepted_when_sending_contact_info(contact_page):
    contact_page.load()
    contact_page.fill_all_contact_data(fields_to_exclude=["First Name"])
    contact_page.fill_first_name(121*"a")
    contact_page.send_message()

    expected_message = "The name field must not be greater than 120 characters"
    received_message = contact_page.get_help_block_error()
    assert received_message == expected_message, \
            f"Expected to see {expected_message}, but got {received_message}"


def test_first_name_120_char_long_is_accepted_when_sending_contact_info(contact_page):
    contact_page.load()
    contact_page.fill_all_contact_data(fields_to_exclude=["First Name"])
    contact_page.fill_first_name(120*"a")
    contact_page.send_message()

    expected_message = "Thanks for your message! We will contact you shortly."
    received_message = contact_page.get_success_alert_text()
    assert received_message == expected_message, \
            f"Expected to see {expected_message}, but got {received_message}"


def test_last_name_is_mandatory_when_sending_contact_message(contact_page):
    contact_page.load()
    contact_page.fill_all_contact_data(fields_to_exclude=["Last Name"])
    contact_page.send_message()

    expected_message = "Last name is required"
    received_message = contact_page.get_last_name_error_message()
    assert received_message == expected_message, \
            f"Expected to see {expected_message}, but got {received_message}"


def test_last_name_121_char_long_is_not_accepted_when_sending_contact_info(contact_page):
    contact_page.load()
    contact_page.fill_all_contact_data(fields_to_exclude=["Last Name"])
    contact_page.fill_last_name(121*"a")
    contact_page.send_message()

    expected_message = "The name field must not be greater than 120 characters."
    received_message = contact_page.get_help_block_error()
    assert received_message == expected_message, \
            f"Expected to see {expected_message}, but got {received_message}"


def test_last_name_120_char_long_is_accepted_when_sending_contact_info(contact_page):
    contact_page.load()
    contact_page.fill_all_contact_data(fields_to_exclude=["Last Name"])
    contact_page.fill_last_name(120*"a")
    contact_page.send_message()

    expected_message = "Thanks for your message! We will contact you shortly."
    received_message = contact_page.get_success_alert_text()
    assert received_message == expected_message, \
            f"Expected to see {expected_message}, but got {received_message}"


def test_email_address_is_mandatory_when_sending_contact_message(contact_page):
    contact_page.load()
    contact_page.fill_all_contact_data(fields_to_exclude=["Email"])
    contact_page.send_message()

    expected_message = "Email is required"
    received_message = contact_page.get_email_error_message()
    assert received_message == expected_message, \
            f"Expected to see {expected_message}, but got {received_message}"


def test_invalid_email_address_is_rejected_when_sending_contact_message(contact_page):
    contact_page.load()
    contact_page.fill_all_contact_data(fields_to_exclude=["Email"])
    contact_page.fill_email(fake.word() + "." + fake.word())
    contact_page.send_message()

    expected_message = "Email format is invalid"
    received_message = contact_page.get_email_error_message()
    assert received_message == expected_message, \
        f"Expected to see {expected_message}, but got {received_message}"


# it fails with an invalid format message, so i don't know real limits
def test_long_email_address_are_rejected_when_sending_contact_message(contact_page):
    contact_page.load()
    contact_page.fill_all_contact_data(fields_to_exclude=["Email"])
    contact_page.fill_email((100*fake.word()) + fake.email())
    contact_page.send_message()

    expected_message = "Email is too long"
    received_message = contact_page.get_email_error_message()
    assert received_message == expected_message, \
        f"Expected to see {expected_message}, but got {received_message}"


def test_files_above_0_kb_are_not_accepted_when_sending_contact_message(contact_page):
    contact_page.load()
    contact_page.upload_file("non_empty_file.txt")
    contact_page.fill_all_contact_data(fields_to_exclude=["File"])
    contact_page.send_message()

    expected_message = "File should be empty."
    received_message = contact_page.get_file_upload_error()
    assert received_message == expected_message, \
            f"Expected to see {expected_message}, but got {received_message}"


def test_non_txt_are_not_accepted_when_sending_contact_message(contact_page):
    contact_page.load()
    contact_page.upload_file("nontxt.svg")
    contact_page.fill_all_contact_data(fields_to_exclude=["File"])
    contact_page.send_message()

    expected_message = "File should have a txt extension."
    received_message = contact_page.get_file_upload_error()
    assert received_message == expected_message, \
            f"Expected to see {expected_message}, but got {received_message}"