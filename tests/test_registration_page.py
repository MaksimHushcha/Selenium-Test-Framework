from pages.registration_page import RegistrationFields
from tests.conftest import registration_page
from utils.api_utils import AuthManager as Auth

def test_account_registration_with_all_correct_data(registration_page):
    registration_page.load()
    registration_data = registration_page.fill_all_registration_data()
    registration_page.submit_registration_form()

    registration_email = registration_data.get(RegistrationFields.email)
    registration_password = registration_data.get(RegistrationFields.password)

    response = Auth.login(email=registration_email,password=registration_password)

    assert response.status_code == 200
    assert isinstance(response.json_data, dict)
    assert len(response.json_data.get("access_token", "")) > 1