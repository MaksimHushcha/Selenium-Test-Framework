import pytest

from pages.components import Components
from pages.comparison_page import ComparisonPage
from pages.checkout_page import Checkout
from pages.main_page import MainBasePage
from pages.product_page import ProductPage
from pages.contact_page import ContactPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


@pytest.fixture
def main_page(driver):
    return MainBasePage(driver)


@pytest.fixture
def product_page(driver):
    return ProductPage(driver)


@pytest.fixture
def components(driver):
    return Components(driver)


@pytest.fixture
def checkout(driver):
    return Checkout(driver)


@pytest.fixture
def comparison_page(driver):
    return ComparisonPage(driver)


@pytest.fixture
def contact_page(driver):
    return ContactPage(driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def registration_page(driver):
    return RegistrationPage(driver)
