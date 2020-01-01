import pytest
from affordable_leggins.filters import filter_size


@pytest.fixture()
def leggins(leggin_with_size_xs, leggin_with_size_s, leggin_with_size_m):
    leggins = [leggin_with_size_xs, leggin_with_size_s, leggin_with_size_m]

    return leggins


@pytest.fixture()
def leggin_with_size_xs():
    leggin_with_size_xs = generate_leggins(40, ["XS"])
    return leggin_with_size_xs


@pytest.fixture()
def leggin_with_size_m():
    leggin_with_size_m = generate_leggins(60, ["M"])
    return leggin_with_size_m


@pytest.fixture()
def leggin_with_size_s():
    leggin_with_size_s = generate_leggins(50, ["S", "M"])
    return leggin_with_size_s


def generate_leggins(price, sizes):
    leggins = {
        "leggin_name": "Bezszwowe Legginsy Inspire - Czarne",
        "leggin_id": "11871452",
        "leggin_price": price,
        "leggin_rrp": 159.0,
        "sizes": sizes,
    }
    return leggins


def test_filter_size(leggins, leggin_with_size_s):
    assert leggin_with_size_s in filter_size(leggins, "S")


def test_filter_other_size(leggins, leggin_with_size_m):
    assert leggin_with_size_m in filter_size(leggins, "M")


def test_filter_non_existing_size(leggins):
    assert filter_size(leggins, "XL") is None


def test_filter_other_non_existing_size(leggins):
    assert filter_size(leggins, "L") is None


def test_filter_leggins_with_multiple_sizes(leggins, leggin_with_size_s):
    assert leggin_with_size_s in filter_size(leggins, "S")
