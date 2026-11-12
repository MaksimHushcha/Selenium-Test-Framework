from enum import Enum, auto
from dataclasses import dataclass
from pages.base_page import BasePage
from locators import contact_page_locators as loc
import os
import random
from faker import Faker

fake = Faker()

class ContactFields(Enum):
    first_name = auto()
    last_name = auto()
    email = auto()
    message = auto()
    subject = auto()
    file = auto()

class ContactSubject(Enum):
    CUSTOMER_SERVICE = "Customer Service"
    WEBMASTER = "Webmaster"
    RETURN = "Return"
    PAYMENTS = "Payments"
    WARRANTY = "Warranty"
    STATUS_OF_ORDER = "Status of my order"

@dataclass
class ContactFormData:
    first_name: str
    last_name: str
    email: str
    message: str
    subject: ContactSubject
    file: str

class ContactPage(BasePage):
    endpoint = "contact"

    SUBJECT_LOCATORS = {
        ContactSubject.CUSTOMER_SERVICE: loc.CUSTOMER_SERVICE_SUBJECT_LOCATOR,
        ContactSubject.WEBMASTER: loc.WEBMASTER_SERVICE_SUBJECT_LOCATOR,
        ContactSubject.RETURN: loc.RETURN_SERVICE_SUBJECT_LOCATOR,
        ContactSubject.PAYMENTS: loc.PAYMENTS_SERVICE_SUBJECT_LOCATOR,
        ContactSubject.WARRANTY: loc.WARRANTY_SERVICE_SUBJECT_LOCATOR,
        ContactSubject.STATUS_OF_ORDER: loc.STATUS_OF_ORDER_SUBJECT_LOCATOR,
    }

    def fill_first_name(self, text: str):
        self.fill_field(loc.FIRST_NAME_FIELD_LOCATOR, text=text)

    def fill_last_name(self, text: str):
        self.fill_field(loc.LAST_NAME_FIELD_LOCATOR, text=text)

    def fill_email(self, text: str):
        self.fill_field(loc.EMAIL_FIELD_LOCATOR, text=text)

    def fill_message(self, text: str):
        self.fill_field(loc.MESSAGE_FIELD_LOCATOR, text=text)

    def select_subject(self, subject: ContactSubject):
        if subject not in self.SUBJECT_LOCATORS:
            raise ValueError(f"Invalid subject {subject}")
        self.click_by_locator(loc.SUBJECT_FIELD_LOCATOR)
        self.click_by_locator(self.SUBJECT_LOCATORS[subject])

    def upload_file(self, file_name: str):
        file_input = self.locate_element(loc.ATTACHMENT_FIELD_LOCATOR)
        if not isinstance(file_name, str):
            raise ValueError("Invalid input for upload_file")
        absolute_path = os.path.abspath(f"test_data/files/{file_name}")
        if not os.path.exists(absolute_path):
            raise ValueError("Invalid file for upload_file")
        file_input.send_keys(absolute_path)

    def send_message(self):
        self.click_by_locator(loc.SEND_BUTTON_LOCATOR)

    # ALERT MESSAGES
    def get_success_alert_text(self):
        return self.locate_element(loc.ALERT_SUCCESS).text

    def get_first_name_error_message(self):
        return self.locate_element(loc.FIRST_NAME_ERROR).text

    def get_last_name_error_message(self):
        return self.locate_element(loc.LAST_NAME_ERROR).text

    def get_email_error_message(self):
        return self.locate_element(loc.EMAIL_ERROR).text

    def get_file_upload_error(self):
        return self.locate_element(loc.ATTACHMENT_ERROR).text

    def get_message_upload_error(self):
        return self.locate_element(loc.MESSAGE_ERROR).text

    def get_help_block_error(self):
        return self.locate_element(loc.HELP_BLOCK).text

    def get_random_subject(self):
        return random.choice(list(self.SUBJECT_LOCATORS.keys()))

    def fill_all_contact_data(self, fields_to_exclude: list[ContactFields] = None) -> dict:
        if fields_to_exclude is None:
            fields_to_exclude = []

        data = ContactFormData(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            message=fake.text(),
            file="empty_file.txt",
            subject=self.get_random_subject(),
        )

        actions = {
            ContactFields.first_name : (self.fill_first_name, data.first_name),
            ContactFields.last_name : (self.fill_last_name, data.last_name),
            ContactFields.email : (self.fill_email, data.email),
            ContactFields.message : (self.fill_message, data.message),
            ContactFields.file : (self.upload_file, data.file),
            ContactFields.subject : (self.select_subject, data.subject)
        }
        filled_data = {}
        for field, (action, value) in actions.items():
            if field not in fields_to_exclude:
                filled_data[field] = value
                action(value)
        return filled_data
