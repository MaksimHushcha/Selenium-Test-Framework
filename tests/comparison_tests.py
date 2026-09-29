from time import sleep

def test_go_to_comparison_from_a_component(components, seed_comparison_2_items, comparison_page, main_page):
    assert components.comparison_bar_is_displayed()
    components.go_to_compare_screen()
    current_url = main_page.get_current_url()
    current_title = main_page.get_page_title()
    assert current_url == comparison_page.get_expected_page_url()
    assert current_title == "Product Comparison - Practice Software Testing - Toolshop - v5.0"


def test_add_to_comparison_on_main_page(main_page, components):
    main_page.load()
    main_page.add_to_comparison_main()
    assert components.comparison_bar_is_displayed

def test_remove_from_comparison_on_main_page(main_page, components):
    main_page.load()
    main_page.add_to_comparison_main()
    assert components.comparison_bar_is_displayed()
    main_page.remove_from_comparison_main()
    assert components.comparison_bar_is_not_visible()

def test_clear_comparison_from_comparison_bar(comparison_page, seed_comparison_2_items, components):
    assert components.comparison_bar_is_displayed()
    components.clear_comparison()
    assert components.comparison_bar_is_not_visible()


def test_clear_comparison_from_comparison_page(comparison_page, seed_comparison_2_items):
    comparison_page.load()
    comparison_page.clear_comparison()
    assert comparison_page.is_comparison_empty_visible()


def test_empty_browse_products_button_on_empty_comparison_page_brings_to_main_page(comparison_page, main_page):
    comparison_page.load()
    comparison_page.press_browse_products()
    expected_url = main_page.get_expected_page_url()
    current_url = comparison_page.get_current_url()
    assert current_url == expected_url


def test_clicking_on_product_picture_opens_product_page(comparison_page, product_page, seed_comparison_2_items ):
    comparison_page.load()
    comparison_page_item_title = comparison_page.get_comparison_item_title()
    comparison_page.click_comparison_image()
    product_page_item_title = product_page.get_product_name()
    assert comparison_page_item_title == product_page_item_title

# TODO ADD ASSERT
def test_remove_comparison_on_comparison_page(comparison_page, seed_comparison_2_items):
    comparison_page.load()
    comparison_page.remove_comparison_item(order_of_item_to_remove=1)

