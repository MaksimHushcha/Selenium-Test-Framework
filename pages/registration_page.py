import random
from dataclasses import dataclass

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

@dataclass
class RegistrationFormData:
    first_name: str
    last_name: str
    date_of_birth: str
    country: None
    postal_code: str
    house_number: int
    street_address: str
    city: str
    state: str
    phone_number: str
    email: str
    password: str

class RegistrationPage(BasePage):
    endpoint = "auth/register"

    def input_first_name(self, first_name: str):
        self.fill_field(loc.FIRST_NAME_LOCATOR, first_name)
        return self

    def input_last_name(self, last_name: str):
        self.fill_field(loc.LAST_NAME_LOCATOR, last_name)
        return self

    def input_date_of_birth(self, dob: str):
        self.fill_field(loc.DOB_LOCATOR, dob)
        return self

    def get_password_strength(self) -> str:
        locator = self.locate_element(loc.PASSWORD_STRENGTH_FILL)
        classes = locator.get_attribute("class")
        _, _, fill_class = classes.partition(" ")
        return fill_class


    def select_country_by_value(self, country_code: str):
        select_element = self.locate_element(loc.COUNTRY_DROPDOWN_LOCATOR)
        select = Select(select_element)
        self.click_by_locator(loc.COUNTRY_DROPDOWN_LOCATOR)
        select.select_by_value(country_code)

    def select_random_country(self) -> str | None:
        select_element = self.locate_element(loc.COUNTRY_DROPDOWN_LOCATOR)
        select = Select(select_element)
        self.click_by_locator(loc.COUNTRY_DROPDOWN_LOCATOR)
        select.select_by_index(random.randint(1, len(select.options)) - 1)
        return select.first_selected_option.get_attribute("value")

    def input_postal_code(self, postal_code: str):
        self.fill_field(loc.POSTAL_CODE_LOCATOR, postal_code)
        return self

    def input_house_number(self, house_number: str):
        self.fill_field(loc.HOUSE_NUMBER_LOCATOR, house_number)
        return self

    def input_street_address(self, street_address: str):
        self.fill_field(loc.STREET_FIELD_LOCATOR, street_address)
        return self

    def input_city(self, city: str):
        self.fill_field(loc.CITY_LOCATOR, city)
        return self

    def input_state(self, state: str):
        self.fill_field(loc.STATE_LOCATOR, state)
        return self

    def input_phone_number(self, phone_number: str):
        self.fill_field(loc.PHONE_LOCATOR, phone_number)
        return self

    def input_email(self, email: str):
        self.fill_field(loc.EMAIL_ADDRESS, email)
        return self

    def input_password(self, password: str):
        self.fill_field(loc.PASSWORD_LOCATOR, password)
        return self

    def submit_registration_form(self):
        self.click_by_locator(loc.SUBMIT_REGISTRATION_LOCATOR)
        return self

    def fill_all_registration_data(self, fields_to_exclude: list[str] | None = None) :
        if fields_to_exclude is None: fields_to_exclude = []


        data = RegistrationFormData(
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            date_of_birth = fake.date(end_datetime="-18y"),
            country = None,
            postal_code = fake.postcode(),
            house_number = random.randint(1, 222),
            street_address = fake.street_address(),
            city = fake.city(),
            state = fake.state(),
            phone_number = fake.msisdn(),
            email = fake.email(),
            password = fake.password(),
        )
        fields = {
            RegistrationFields.first_name: (self.input_first_name, data.first_name),
            RegistrationFields.last_name: (self.input_last_name, data.last_name),
            RegistrationFields.date_of_birth: (self.input_date_of_birth, data.date_of_birth),
            # US is hardcoded, because randomly generated zip code may fail with other countries.
            RegistrationFields.country: (lambda _: self.select_country_by_value("US"), None),
            RegistrationFields.postal_code: (self.input_postal_code, data.postal_code),
            RegistrationFields.house_number: (self.input_house_number, data.house_number),
            RegistrationFields.street_address: (self.input_street_address, data.street_address),
            RegistrationFields.city: (self.input_city, data.city),
            RegistrationFields.state: (self.input_state, data.state),
            RegistrationFields.phone_number: (self.input_phone_number, data.phone_number),
            RegistrationFields.email: (self.input_email, data.email),
            RegistrationFields.password: (self.input_password, data.password)
        }

        filled_data = {}
        for field, (action, value) in fields.items():
            if field not in fields_to_exclude:
                filled_data[field] = value
                action(value)
        return filled_data

    def get_field_error_text(self, error_field: RegistrationFields) -> str:
        locators = {
            RegistrationFields.first_name: loc.FIRST_NAME_ERROR_LOCATOR,
            RegistrationFields.last_name: loc.LAST_NAME_ERROR_LOCATOR,
            RegistrationFields.date_of_birth: loc.DOB_ERROR_LOCATOR,
            RegistrationFields.country: loc.COUNTRY_ERROR_LOCATOR,
            RegistrationFields.postal_code: loc.POSTAL_CODE_ERROR_LOCATOR,
            RegistrationFields.house_number: loc.HOUSE_NUMBER_ERROR_LOCATOR,
            RegistrationFields.street_address: loc.STREET_ERROR_LOCATOR,
            RegistrationFields.city: loc.CITY_ERROR_LOCATOR,
            RegistrationFields.state: loc.STATE_ERROR_LOCATOR,
            RegistrationFields.phone_number: loc.PHONE_ERROR_LOCATOR,
            RegistrationFields.email: loc.EMAIL_ERROR_LOCATOR,
            RegistrationFields.password: loc.PASSWORD_ERROR_LOCATOR
        }
        locator = locators.get(error_field)
        return self.locate_element(locator).text