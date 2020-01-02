import pytest


@pytest.fixture()
def leggins(leggin_with_size_xs, leggin_with_size_s, leggin_with_size_m):
    leggins = [leggin_with_size_xs, leggin_with_size_s, leggin_with_size_m]

    return leggins


@pytest.fixture()
def leggin_with_size_xs():
    leggin_with_size_xs = generate_leggins("Bezszwowe", ["XS"], 40)
    return leggin_with_size_xs


@pytest.fixture()
def leggin_with_size_m():
    leggin_with_size_m = generate_leggins("Szwowe Czarne", ["M"], 50)
    return leggin_with_size_m


@pytest.fixture()
def leggin_with_size_s():
    leggin_with_size_s = generate_leggins("Power Curve", ["S", "M"], 60)
    return leggin_with_size_s


def generate_leggins(name, sizes, price):
    leggins = {
        "leggin_name": name,
        "leggin_id": "11871452",
        "leggin_price": price,
        "leggin_rrp": 159.0,
        "sizes": sizes,
    }
    return leggins
