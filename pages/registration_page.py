import random

from faker.providers import phone_number

from pages.base_page import BasePage
from locators import registration_page_locators as loc
from selenium.webdriver.support.select import Select
from enum import Enum, auto
from faker import Faker

fake = Faker()

class RegistrationFields(Enum):
    first_name = auto()
    last_name = auto()
    date_of_birth = auto()
    country = auto()
    postal_code = auto()
    house_number = auto()
    street_address = auto()
    city = auto()
    state = auto()
    phone_number = auto()
    email = auto()
    password = auto()

class RegistrationPage(BasePage):

    endpoint = "auth/register"

    def input_first_name(self, first_name):
        self.fill_field(loc.FIRST_NAME_LOCATOR, first_name)

    def input_last_name(self, last_name):
        self.fill_field(loc.LAST_NAME_LOCATOR, last_name)

    def input_date_of_birth(self, dob):
        self.fill_field(loc.DOB_LOCATOR, dob)

    def select_country_by_value(self, country_code):
        select_element = self.locate_element(loc.COUNTRY_DROPDOWN_LOCATOR)
        select = Select(select_element)
        self.click_by_locator(loc.COUNTRY_DROPDOWN_LOCATOR)
        select.select_by_value(country_code)

    def select_random_country(self):
        select_element = self.locate_element(loc.COUNTRY_DROPDOWN_LOCATOR)
        select = Select(select_element)
        self.click_by_locator(loc.COUNTRY_DROPDOWN_LOCATOR)
        select.select_by_index(random.randint(1, len(select.options))-1)

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

        if fields_to_exclude is None: fields_to_exclude = []

        fields = {
            RegistrationFields.first_name : lambda: self.input_first_name(fake.first_name()),
            RegistrationFields.last_name : lambda: self.input_last_name(fake.last_name()),
            RegistrationFields.date_of_birth : lambda: self.input_date_of_birth(fake.date()),
            RegistrationFields.country: lambda: self.select_random_country(),
            RegistrationFields.postal_code : lambda: self.input_postal_code(fake.postcode()),
            RegistrationFields.house_number: lambda: self.input_house_number(random.randint(1, 222)),
            RegistrationFields.street_address: lambda: self.input_street_address(fake.street_address()),
            RegistrationFields.city: lambda: self.input_city(fake.city()),
            RegistrationFields.state : lambda: self.input_state(fake.state()),
            RegistrationFields.phone_number : lambda: self.input_phone_number(fake.msisdn()),
            RegistrationFields.email : lambda: self.input_email(fake.email()),
            RegistrationFields.password: lambda: self.input_password(fake.password()),

        }
        for field, action in fields.items():
            if field not in fields_to_exclude:
                action()

        return fields
