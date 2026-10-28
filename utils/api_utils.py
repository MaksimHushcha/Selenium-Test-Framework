import os
import random
import time
import json
import jwt
from selenium.webdriver.common.bidi import Network
from requests import ConnectionError
from utils.api_router import ApiRequest
from dotenv import load_dotenv

load_dotenv()


def get_random_product_ids(number_of_ids) -> list:
    product_ids = get_a_random_valid_product_id(amount_of_items=number_of_ids)
    return product_ids

def get_two_comparison_ids() -> list:
    product_id = get_measuring_items_for_comparison()
    return product_id

def get_a_random_valid_product_id(amount_of_items) -> list:
    api = ApiRequest()
    try:
        response_body = api.get(endpoint="products").json_data
        available_product_ids = []
        for list_item in response_body["data"]:
            # Thor Hammer is one per customer, which may ruin some tests if a random item is chosen
            if list_item.get("in_stock") is True and list_item.get("name") != "Thor Hammer":
                available_product_ids.append(list_item.get("id"))
        return random.sample(available_product_ids, amount_of_items)
    except (KeyError, TypeError) as e:
        raise Exception(f"API data structure error: missing or invalid keys. Details: {e}")

# Measuring items fit for show unique items in comparison, but category is likely dynamic so likely to fail
# to investigate
def get_measuring_items_for_comparison() -> list:
    api = ApiRequest()
    try:
        query = '{"q":"Tape"}'
        response_body = api.query(endpoint="products/search", data=query).json_data
        measurement_items = []
        for list_item in response_body["data"]:
            if list_item.get("name") == "Measuring Tape" or list_item.get("name") == "Tape Measure 5m":
                measurement_items.append(list_item.get("id"))
        return measurement_items
    except (KeyError, TypeError) as e:
        raise Exception(f"API data structure error: missing or invalid keys. Details: {e}")

class FavoritesAPI:

    def __init__(self):
        self.api = ApiRequest()
        self.token = AuthManager.get_access_token()

    def get_favorites(self):
        favorites_list = self.api.get(endpoint="favorites",
                                      headers={"Authorization": f"Bearer {self.token}"}).json_data
        return favorites_list

    def clear_favorites(self):
        try:
            favorites_list = self.get_favorites()
            ids_for_deletion = [deletion_id.get("id") for deletion_id in favorites_list]
            if not ids_for_deletion:
                return
            for deletion_id in ids_for_deletion:
                self.api.delete(endpoint=f"favorites/{deletion_id}",
                                headers={"Authorization": f"Bearer {self.token}"})
        except ConnectionError as e:
            raise Exception(f"Error deleting favorites: {e}")

    def get_products_in_favorites(self):
        try:
            favorites_list = self.get_favorites()
            product_ids = [product_ids.get("product_id") for product_ids in favorites_list]
            return product_ids
        except ConnectionError as e:
            raise Exception(f"Error fetching favorites: {e}")

    def add_item_to_favorites(self, product_id):
        try:
            self.api.post(
                endpoint="favorites",
                headers={"Authorization": f"Bearer {self.token}"},
                json={"product_id": f"{product_id}"})
        except ConnectionError as e:
            raise Exception(f"Error adding favorites: {e}")


class AuthManager:
    _token = None
    _expires_on = 0

    @classmethod
    def get_access_token(cls):
        buffer_seconds = 60
        current_time = time.time()
        if not cls._token or cls._expires_on - current_time > buffer_seconds:
            cls._get_a_fresh_token()
        return cls._token

    @classmethod
    def _get_a_fresh_token(cls):
        api = ApiRequest()
        request_body = {
            "email": os.getenv('USER_EMAIL'),
            "password": os.getenv("USER_PASSWORD")
        }
        request_body = json.dumps(request_body)
        try:
            response_body = api.post(endpoint="users/login", data=request_body).json_data
            cls._token = response_body.get("access_token")
            decoded_token = jwt.decode(cls._token, options={"verify_signature": False})
            cls._expires_on = decoded_token["exp"]
        except jwt.InvalidTokenError:
            print("Invalid token")