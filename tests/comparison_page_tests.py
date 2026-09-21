
def test_go_to_comparison(comparison_page, add_two_items_to_comparison, main_page):
    main_page.load()
    add_two_items_to_comparison()
    assert comparison_page.comparison_bar_is_displayed()
    comparison_page.go_to_compare_screen()

    current_url = main_page.get_current_url()
    current_title = main_page.get_page_title()
    assert current_url == "https://practicesoftwaretesting.com/comparison"
    assert current_title == "Product Comparison - Practice Software Testing - Toolshop - v5.0"


def test_clear_comparison_from_comparison_bar(comparison_page, add_two_items_to_comparison, main_page):
    main_page.load()
    add_two_items_to_comparison()
    assert comparison_page.comparison_bar_is_displayed()
    comparison_page.clear_comparison()
    assert comparison_page.comparison_bar_is_not_visible()