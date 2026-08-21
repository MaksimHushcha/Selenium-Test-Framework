import pytest
from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


def test_sort_desc(main_page):
    main_page.load()
    main_page.sort_items_by_name_desc()
    main_page.assert_cards_are_sorted_by_title_in_reverse_order()
