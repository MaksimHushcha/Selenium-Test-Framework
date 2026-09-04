import random

import pytest

def test_page_title_starts_with_product_name(product_page, get_available_product_id):
    product_page.load(get_available_product_id)
    product_title = product_page.get_item_title()
    page_title = product_page.get_page_title()
    assert page_title.startswith(product_title), f"Expected page title to start with {product_title}, but got {page_title}"

def test_user_is_unable_to_add_to_favourites_unauthorized(product_page, components, get_available_product_id):
    product_page.load(get_available_product_id)
    product_page.add_to_favourites()
    toast_text = components.get_toast_text()
    expected_toast_text = "Unauthorized, can not add product to your favorite list."
    assert toast_text == expected_toast_text, \
        f"Toast text: {toast_text}, Expected: {expected_toast_text}"

def test_adding_multiple_items_to_card(product_page, components, get_available_product_id, checkout):
    product_page.load(get_available_product_id)
    random_amount_to_add = random.randint(2, 6)
    for i in range(random_amount_to_add):
        product_page.increase_quantity()
    product_page.add_to_cart()
    number_of_items_in_cart = components.get_number_of_items_on_cart_icon()
    assert random_amount_to_add + 1 == number_of_items_in_cart, \
        f"Expected number on cart icon to be {random_amount_to_add + 1}, but got {number_of_items_in_cart}"
    assert components.get_toast_text() == "Product added to shopping cart."
    components.dismiss_toast()
    components.open_cart()
    assert checkout.get_quantity_of_an_item_in_cart() == random_amount_to_add + 1


# TODO - idea to implement full spec verification
def test_items_have_a_spec(product_page, get_available_product_id):
    product_page.load(get_available_product_id)
    specs = product_page.get_item_specs()
    assert None not in specs, f"Expected specs to be not empty, but got {specs}"
