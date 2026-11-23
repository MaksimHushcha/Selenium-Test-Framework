import os
import dotenv
import pytest
from utils import api_utils
dotenv.load_dotenv()


@pytest.fixture
def get_available_product_id():
    return api_utils.get_a_random_valid_product_id(amount_of_items=1)[0]


@pytest.fixture
def get_two_product_ids():
    return api_utils.get_a_random_valid_product_id(amount_of_items=2)


@pytest.fixture
def authenticated_user(driver):
    token = api_utils.AuthManager.get_access_token()
    driver.get(f"{os.getenv('BASE_URL')}contact")
    driver.execute_script(f"window.localStorage.setItem('auth-token', '{token}')")


@pytest.fixture
def seeded_two_comparison_items(main_page):
    ids_list = api_utils.get_random_product_ids(number_of_ids=2)
    main_page.load()
    # Verifying the page loaded before injecting the session to prevents flakiness in CI/CD
    assert main_page.is_user_on_expected_page()
    main_page.set_compare_ids_session_storage(ids_list)


@pytest.fixture
def seeded_two_measurements_items(main_page):
    ids_list = api_utils.get_measuring_items_for_comparison()
    main_page.load()
    main_page.set_compare_ids_session_storage(ids_list)


@pytest.fixture
def seeded_favorite_product(clear_favorites, get_available_product_id):
    favorites = api_utils.FavoritesAPI()
    favorites.add_item_to_favorites(get_available_product_id)
    return get_available_product_id


@pytest.fixture
def clear_favorites():
    favorites = api_utils.FavoritesAPI()
    favorites.clear_favorites()
    yield
    favorites.clear_favorites()