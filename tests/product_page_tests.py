import random

from utils.api_utils import FavoritesAPI


def test_page_title_starts_with_product_name(product_page, get_available_product_id):
    product_page.load(get_available_product_id)
    product_title = product_page.get_product_name()
    page_title = product_page.get_page_title()
    assert page_title.startswith(product_title), f"Expected page title to start with {product_title}, but got {page_title}"


def test_user_is_unable_to_add_to_favourites_unauthorized(product_page, components, get_available_product_id):

    product_page.load(get_available_product_id)
    product_page.add_to_favourites()
    toast_text = components.get_toast_text()
    expected_toast_text = "Unauthorized, can not add product to your favorite list."
    assert toast_text == expected_toast_text, \
        f"Toast text: {toast_text}, Expected: {expected_toast_text}"


def test_add_to_favourites(product_page, components, get_available_product_id, authenticated_user, clear_favorites):

    product_page.load(get_available_product_id)
    product_page.add_to_favourites()
    toast_text = components.get_toast_text()
    favorites = FavoritesAPI()
    current_favorites = favorites.get_products_in_favorites()
    assert toast_text == "Product added to your favorites list."
    assert get_available_product_id in current_favorites


def test_same_item_cannot_be_added_to_favourites_twice(
        product_page, components, authenticated_user, seeded_product):

    product_page.load(seeded_product)
    product_page.add_to_favourites()
    toast_text_error = components.get_toast_text()
    assert toast_text_error == "Product already in your favorites list."

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


def test_items_has_a_full_spec(product_page, get_available_product_id):
    product_page.load(get_available_product_id)
    specs = product_page.get_item_specs()
    tags = product_page.get_product_tags()
    description = product_page.get_item_description()
    co2_rating, co2_rating_color = product_page.get_co_2_rating()

    assert None not in specs, f"Expected specs to be not empty, but got {specs}"
    assert description is not None, f"Expected description to be not empty, but got {description}"
    assert any(char in co2_rating for char in {"A", "B", "C", "D", "E" })
    assert co2_rating_color == "#f97316", f"Expected color to be #f97316, but: {co2_rating_color}"
    assert None not in tags, f"Expected tags to be not empty, but got {tags}"

def test_adding_items_to_comparison_from_product_page(
        product_page, get_two_product_ids, comparison_page):
    product_id_1, product_id_2 = get_two_product_ids
    product_page.load(product_id_1)
    product_page.add_to_comparison()

    product_page.load(product_id_2)
    product_page.add_to_comparison()

    session_storage = product_page.get_item_from_session_storage("compare_ids")
    assert product_id_1 in session_storage and product_id_2 in session_storage
    assert comparison_page.comparison_bar_is_displayed()


def test_item_picture_is_loaded(product_page, get_available_product_id):
    product_page.load(get_available_product_id)
    assert product_page.is_picture_displayed()
