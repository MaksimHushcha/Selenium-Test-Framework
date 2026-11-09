from pages.base_page import BasePage
from locators import registration_page_locators as loc
from selenium.webdriver.support.select import Select
from faker import Faker

fake = Faker()

class RegistrationPage(BasePage):

    endpoint = "auth/register"
    #select = Select(loc.COUNTRY_DROPDOWN_LOCATOR)

    def input_first_name(self, first_name):
        self.fill_field(loc.FIRST_NAME_LOCATOR, first_name)

    def input_last_name(self, last_name):
        self.fill_field(loc.FIRST_NAME_LOCATOR, last_name)

    def input_date_of_birth(self, dob):
        self.fill_field(loc.DOB_LOCATOR, dob)

    # def select_country(self, country_code):
    #     self.click_by_locator(loc.COUNTRY_DROPDOWN_LOCATOR)
    #     self.select.select_by_value(country_code)

    def input_postal_code(self, postal_code):
        self.fill_field(loc.POSTAL_CODE_LOCATOR, postal_code)

    def input_house_number(self, house_number):
        self.fill_field(loc.HOUSE_NUMBER_LOCATOR, house_number)

    def input_street_address(self, street_address):
        self.fill_field(loc.STREET_FIELD_LOCATOR, street_address)

    def input_city(self, city):
        self.fill_field(loc.CITY_LOCATOR, city)

    def input_state(self, state):
        self.fill_field(loc.STATE_LOCATOR, state)

    def input_phone_number(self, phone_number):
        self.fill_field(loc.PHONE_LOCATOR, phone_number)

    def input_email(self, email):
        self.fill_field(loc.EMAIL_ADDRESS, email)

    def input_password(self, password):
        self.fill_field(loc.PASSWORD_LOCATOR, password)

    def submit_registration_form(self):
        self.click_by_locator(loc.SUBMIT_REGISTRATION_LOCATOR)
        
    # TODO - to refactor
    def fill_all_contact_data(self, fields_to_exclude=None):
        if fields_to_exclude is None:
            fields_to_exclude = []
        if not isinstance(fields_to_exclude, list):
            raise ValueError("Invalid input for fill_contact_fields")
        if "First Name" not in fields_to_exclude:
            self.input_first_name(fake.first_name())
        if "Last Name" not in fields_to_exclude:
            self.input_last_name(fake.last_name())
        if "Date of Birth" not in  fields_to_exclude:
            self.input_date_of_birth(fake.date_of_birth())
        if "Postal Code" not in  fields_to_exclude:
            self.input_postal_code(fake.postal_code())
