import os
from faker import Faker
import dotenv
faker = Faker()

dotenv.load_dotenv()

def test_successful_login_as_user(login_page, components):
    login_page.load()
    login_page.login_as_user()
    assert components.get_navbar_username() == " Bob Smith "
    assert components.get_current_url().endswith("/account")


def test_successful_login_as_admin(login_page, components):
    login_page.load()
    login_page.login_as_admin()
    assert components.get_navbar_username() == "John Doe"
    assert components.get_current_url().endswith("/admin/dashboard")


def test_login_with_incorrect_password(login_page):
    login_page.load()
    login_page.input_email_address(os.getenv("USER_EMAIL"))
    login_page.input_password(faker.password())
    login_page.press_login_button()
    assert login_page.get_login_error_message() == "Invalid email or password"
    assert login_page.get_current_url().endswith("/login")


# I don't know the amount of attempts needed, temporary values, to investigate later
def test_login_with_incorrect_password_locks_account_out(login_page):
    number_of_attempts = 4
    for current_attempt in range(number_of_attempts):
        login_page.load()
        login_page.input_email_address(os.getenv("USER_EMAIL"))
        login_page.input_password(faker.password())
        login_page.press_login_button()
        assert login_page.get_login_error_message() == "Invalid email or password"
        if current_attempt == 4:
            assert login_page.get_login_error_message() == "Account locked, too many failed attempts. Please contact the administrator."



