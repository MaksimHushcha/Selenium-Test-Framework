import pytest

# ids are generated randomly and update at a certain interval - to investigate the strategy here

def test_page_title_starts_with_product_name(product_page):
    product_id = "01M1HYRGJF6BKJM8C8A33E212B"
    product_page.load(product_id)
    product_title = product_page.get_item_title()
    page_title = product_page.get_page_title()
    assert page_title.startswith(product_title), f"Expected page title to start with {product_title}, but got {page_title}"

def test_user_is_unable_to_add_to_favourites_unauthorized(product_page, components):
    product_page.load("01M1HYRGJF6BKJM8C8A33E212B")
    product_page.add_to_favourites()
    toast_text = components.get_toast_text()
    expected_toast_text = "Unauthorized, can not add product to your favorite list."
    assert toast_text == expected_toast_text, \
        f"Toast text: {toast_text}, Expected: {expected_toast_text}"