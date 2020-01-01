from affordable_leggins.min_current_price import find_min_current_price


def generate_leggins(price):
    leggins = {
        "leggin_name": "Bezszwowe Legginsy Inspire - Czarne",
        "leggin_id": "11871452",
        "leggin_price": price,
        "leggin_rrp": 159.0,
    }
    return leggins


def test_price():
    leggins = [generate_leggins(64)]
    assert find_min_current_price(leggins) == generate_leggins(64)


def test_price_equals_122():
    leggins = [generate_leggins(122)]
    assert find_min_current_price(leggins) == generate_leggins(122)


def test_price_of_empty_list():
    assert find_min_current_price([]) is None


def test_price_of_more_than_one():
    leggins = [generate_leggins(40), generate_leggins(20)]
    assert find_min_current_price(leggins) == generate_leggins(20)


def test_price_of_three_elements():
    leggins = [generate_leggins(20), generate_leggins(40), generate_leggins(60)]
    assert find_min_current_price(leggins) == generate_leggins(20)


def test_find_min_of_more_the_same_prices():
    leggins = [generate_leggins(20), generate_leggins(20), generate_leggins(60)]
    assert find_min_current_price(leggins) == generate_leggins(20)
