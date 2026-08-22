import pytest
from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


def test_card_items_sorted_by_title_asc_with_filter(main_page):
    main_page.load()
    main_page.sort_items_by_name_asc()
    titles = main_page.get_list_of_card_titles()
    assert main_page.verify_list_is_sorted(list_to_sort=titles, reverse_order=False), (f"Expected titles to be sorted"
                                                                                  f"in ascending order, but got {titles} instead")

def test_card_items_sorted_by_title_desc_with_filter(main_page):
    main_page.load()
    main_page.sort_items_by_name_desc()
    titles = main_page.get_list_of_card_titles()
    assert main_page.verify_list_is_sorted(list_to_sort=titles, reverse_order=True), (f"Expected titles to be sorted"
                                                                                  f"in descending order, but got {titles} instead")

def test_card_items_sorted_by_price_asc_with_filter(main_page):
    main_page.load()
    main_page.sort_items_by_price_asc()
    prices = main_page.get_list_of_prices_on_cards()
    assert main_page.verify_list_is_sorted(list_to_sort=prices, reverse_order=False), (f"Expected prices to be sorted"
                                                                                      f"in ascending order, but got {prices} instead")
def test_card_items_sorted_by_price_desc_with_filter(main_page):
    main_page.load()
    main_page.sort_items_by_price_desc()
    prices = main_page.get_list_of_prices_on_cards()
    assert main_page.verify_list_is_sorted(list_to_sort=prices, reverse_order=True), (f"Expected prices to be sorted"
                                                                                      f"in descending order, but got {prices} instead")
def test_card_items_sorted_by_co2_asc_with_filter(main_page):
    main_page.load()
    main_page.sort_items_by_co2_asc()
    co2_values = main_page.get_list_of_co2_values_on_cards()
    assert main_page.verify_list_is_sorted(list_to_sort=co2_values, reverse_order=False), (f"Expected co2 values to be sorted"
                                                                                      f"in ascending order, but got {co2_values} instead")
def test_card_items_sorted_by_co2_desc_with_filter(main_page):
    main_page.load()
    main_page.sort_items_by_co2_desc()
    co2_values = main_page.get_list_of_co2_values_on_cards()
    assert main_page.verify_list_is_sorted(list_to_sort=co2_values, reverse_order=True), (f"Expected co2 values to be sorted"
                                                                                      f"in descending order, but got {co2_values} instead")


