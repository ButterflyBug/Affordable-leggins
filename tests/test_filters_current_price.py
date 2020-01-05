from affordable_leggins.filters import filter_current_price
from fixtures import *


def test_find_single_price(leggin_with_size_xs, leggins):
    price_range = range(40, 41)
    assert leggin_with_size_xs in filter_current_price(leggins, price_range)


def test_find_other_single_price(leggin_with_size_m, leggins):
    price_range = range(50, 51)
    assert leggin_with_size_m in filter_current_price(leggins, price_range)


def test_find_current_price_range(leggin_with_size_xs, leggin_with_size_m, leggins):
    price_range = range(40, 51)
    assert leggin_with_size_xs in filter_current_price(leggins, price_range)
    assert leggin_with_size_m in filter_current_price(leggins, price_range)


def test_find_price_in_non_existing_range(leggins):
    price_range = range(30, 40)
    assert [] == filter_current_price(leggins, price_range)
