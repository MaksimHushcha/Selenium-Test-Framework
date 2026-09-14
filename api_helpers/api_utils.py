import os
import random
import time
import json
import jwt

from api_helpers.api_router import ApiRequest
from dotenv import load_dotenv

load_dotenv()

def get_a_random_valid_product_id():
    api = ApiRequest()
    response_body = api.get(endpoint="/products").json_data
    available_product_ids = []
    for list_item in response_body["data"]:
        # Thor Hammer is one per customer, which may ruin some tests if a random item is chosen
        if list_item.get("in_stock") is True and list_item.get("name") != "Thor Hammer":
            available_product_ids.append(list_item.get("id"))
    return random.choice(available_product_ids)

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
        request_body = {"email":f"{os.getenv('USER_EMAIL')}","password":f"{os.getenv("USER_PASSWORD")}"}
        request_body = json.dumps(request_body)
        response_body = api.post(endpoint="/users/login", data=request_body).json_data
        try:
            cls._token = response_body.get("access_token")
            decoded_token = jwt.decode(cls._token, options={"verify_signature": False})
            cls._expired_on = decoded_token["exp"]
        except jwt.InvalidTokenError:
            print("Invalid token")