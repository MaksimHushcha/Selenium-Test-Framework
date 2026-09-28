import pytest
import random
from utils import helpers

@pytest.mark.parametrize('search_item', ["hammer", "pliers", "chisels", "Drill", "Screwdriver"])
def test_search_returns_relevant_items(main_page, search_item):
    main_page.load()
    main_page.search_an_item(search_item)
    search_result_cards = main_page.get_list_of_card_titles()
    search_result_count = main_page.get_search_result_count()
    search_result_term = main_page.get_search_term_value()
    assert search_result_term == search_item
    assert search_result_count >= len(search_result_cards), \
        f"Expected search result count to be {search_result_count} above {len(search_result_cards)}"
    for card in search_result_cards:
        assert search_item.lower() in card.lower(), \
            f"Expected all search items to carry {search_item}, but got {search_result_cards} instead"


def test_invalid_search_returns_no_products_message(main_page):
    expected_message = "There are no products found."
    main_page.load()
    main_page.search_an_item("HarcodedSearchDataToRemove")
    receive_message = main_page.get_no_products_found_message()
    assert receive_message == expected_message, \
        f"Expected no products found message to be {expected_message}, but got {receive_message}"


def test_reset_search_reverts_search(main_page):
    main_page.load()
    initial_wares = main_page.get_list_of_card_titles()
    main_page.search_an_item("Pliers")
    main_page.reset_search()
    wares_after_reset = main_page.get_list_of_card_titles()
    assert initial_wares == wares_after_reset, \
        f"Expected search to revert, but got {wares_after_reset} instead of {initial_wares}"


def test_card_items_sorted_by_title_asc_with_filter(main_page):
    main_page.load()
    main_page.sort_items_by_name_asc()
    titles = main_page.get_list_of_card_titles()
    assert helpers.verify_list_is_sorted(list_to_sort=titles, reverse_order=False), \
        f"Expected titles to be sorted in ascending order, but got {titles} instead"


def test_card_items_sorted_by_title_desc_with_filter(main_page):
    main_page.load()
    main_page.sort_items_by_name_desc()
    titles = main_page.get_list_of_card_titles()
    assert helpers.verify_list_is_sorted(list_to_sort=titles, reverse_order=True), \
        f"Expected titles to be sorted in descending order, but got {titles} instead"


def test_card_items_sorted_by_price_asc_with_filter(main_page):
    main_page.load()
    main_page.sort_items_by_price_asc()
    prices = main_page.get_list_of_prices_on_cards()
    assert helpers.verify_list_is_sorted(list_to_sort=prices, reverse_order=False), \
        f"Expected prices to be sorted in ascending order, but got {prices} instead"


def test_card_items_sorted_by_price_desc_with_filter(main_page):
    main_page.load()
    main_page.sort_items_by_price_desc()
    prices = main_page.get_list_of_prices_on_cards()
    assert helpers.verify_list_is_sorted(list_to_sort=prices, reverse_order=True), \
        f"Expected prices to be sorted in descending order, but got {prices} instead"


def test_card_items_sorted_by_co2_asc_with_filter(main_page):
    main_page.load()
    main_page.sort_items_by_co2_asc()
    co2_values = main_page.get_list_of_co2_values_on_cards()
    assert helpers.verify_list_is_sorted(list_to_sort=co2_values, reverse_order=False), \
        f"Expected co2 values to be sorted in ascending order, but got {co2_values} instead"


def test_card_items_sorted_by_co2_desc_with_filter(main_page):
    main_page.load()
    main_page.sort_items_by_co2_desc()
    co2_values = main_page.get_list_of_co2_values_on_cards()
    assert helpers.verify_list_is_sorted(list_to_sort=co2_values, reverse_order=True), \
        f"Expected co2 values to be sorted in descending order, but got {co2_values} instead"


# Pagination has a bug with <next-page> being unset after applying the eco filter,
# you need to press next button twice.
# Since it's a training web-site with no bug-fixes, we will use an early break to not cycle through the pages.
def test_only_eco_friendly_are_displayed_when_filter_is_applied(main_page):
    main_page.load()
    main_page.select_eco_friendly_products()
    for _ in range(10):
        eco_badges = main_page.get_cards_with_eco_badge()
        containers = main_page.get_cards_on_the_page()
        assert len(containers) == len(eco_badges), \
            f"Expected every card to have ECO badge ({len(eco_badges)}, but got {len(containers)} instead"
        break
        main_page.go_to_next_page()


def test_only_prices_of_selected_items_are_displayed(main_page):
    min_price = random.randint(5, 50)
    max_price = random.randint(70, 170)

    main_page.load()
    main_page.set_price_filter(min_price, max_price)
    prices = main_page.get_list_of_prices_on_cards()
    assert all(min_price <= price <= max_price for price in prices), \
        f"Expected prices to be in filter range, but {prices} are not in {min_price}, {max_price} range"

