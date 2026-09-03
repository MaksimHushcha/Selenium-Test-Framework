import random

from api_helpers.api_router import ApiRequest


def get_a_random_valid_product_id():
    api = ApiRequest()
    response_body = api.get(endpoint="/products").json_data
    available_product_ids = []
    for list_item in response_body["data"]:
        if list_item.get("in_stock") is True:
            available_product_ids.append(list_item.get("id"))
    return random.choice(available_product_ids)
