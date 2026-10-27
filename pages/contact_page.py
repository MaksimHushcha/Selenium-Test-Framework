from pytest_check import is_not_none

from pages.base_page import BasePage
from locators import contact_page_locators as loc
import os
import random
from faker import Faker

fake = Faker()

class ContactPage(BasePage):
    endpoint = "contact"


    def fill_first_name(self, text: str):
        self.fill_field(loc.FIRST_NAME_FIELD_LOCATOR, text=text)


    def fill_last_name(self, text: str):
        self.fill_field(loc.LAST_NAME_FIELD_LOCATOR, text=text)


    def fill_email(self, text: str):
        self.fill_field(loc.EMAIL_FIELD_LOCATOR, text=text)


    def fill_message(self, text: str):
        self.fill_field(loc.MESSAGE_FIELD_LOCATOR, text=text)


    def select_subject(self, item_to_click: str):
        self.click_by_locator(loc.SUBJECT_FIELD_LOCATOR)
        match item_to_click:
            case "Customer Service":
                self.click_by_locator(loc.CUSTOMER_SERVICE_SUBJECT_LOCATOR)
            case "Webmaster":
                self.click_by_locator(loc.WEBMASTER_SERVICE_SUBJECT_LOCATOR)
            case "Return":
                self.click_by_locator(loc.RETURN_SERVICE_SUBJECT_LOCATOR)
            case "Payments":
                self.click_by_locator(loc.PAYMENTS_SERVICE_SUBJECT_LOCATOR)
            case "Warranty":
                self.click_by_locator(loc.WARRANTY_SERVICE_SUBJECT_LOCATOR)
            case "Status of my order":
                self.click_by_locator(loc.STATUS_OF_ORDER_SUBJECT_LOCATOR)
            case _:
                raise ValueError("Invalid input for select_subject")


    def select_customer_service_subject(self):
        self.select_subject("Customer Service")


    def select_webmaster_subject(self):
        self.select_subject("Webmaster")


    def select_payments_subject(self):
        self.select_subject("Payments")


    def select_warranty_subject(self):
        self.select_subject("Warranty")


    def select_status_of_order_subject(self):
        self.select_subject("Status of Order")


    def upload_file(self, file_name):
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


    def get_help_block_error(self):
        return self.locate_element(loc.HELP_BLOCK).text


    def fill_all_contact_data(self, fields_to_exclude=None):
        if fields_to_exclude is None:
            fields_to_exclude = []
        if not isinstance(fields_to_exclude, list):
            raise ValueError("Invalid input for fill_contact_fields")
        if "First Name" not in fields_to_exclude:
            self.fill_first_name(fake.first_name())
        if "Last Name" not in fields_to_exclude:
            self.fill_last_name(fake.last_name())
        if "Email" not in  fields_to_exclude:
            self.fill_email(fake.email())
        if "Message" not in  fields_to_exclude:
            self.fill_message(fake.text())
        if "File" not in fields_to_exclude:
            self.upload_file('empty_file.txt')
        if "Subject" not in fields_to_exclude:
            random_subject = random.choice(["Customer Service", "Webmaster", "Payments", "Warranty", "Status of my order" ])
            self.select_subject(random_subject)