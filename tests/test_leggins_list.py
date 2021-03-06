import pytest
from affordable_leggins.leggins_list import get_rrp_from_single_site
from affordable_leggins.leggins_list import get_list_of_leggins_from_page
from affordable_leggins.leggins_list import get_list_of_leggins
from affordable_leggins.store import store_data, read_data, read_data_from_database
from affordable_leggins.storage.models import Leggin, Size
import json
import os
import datetime


@pytest.mark.vcr("tests/cassettes/test_leggins_list/test_get_list_of_leggins.yaml")
def test_get_rrp_from_single_site_when_rrp_available():
    """ Test function when rrp found on the website """
    assert get_rrp_from_single_site(12068050) == 179.0


@pytest.mark.vcr("tests/cassettes/test_leggins_list/test_get_list_of_leggins.yaml")
def test_get_rrp_from_single_site_when_rrp_not_available():
    """ Test function when there is no rrp """
    assert get_rrp_from_single_site(12053031) is None


@pytest.mark.vcr()
def test_get_rrp_from_single_site_when_leggin_not_available():
    """ Test function when there is no product """
    assert get_rrp_from_single_site(99999999) is None


@pytest.mark.vcr("tests/cassettes/test_leggins_list/test_get_list_of_leggins.yaml")
def test_get_list_of_leggins_from_existing_page():
    """ Test function when page exists """
    single_leggin = {
        "leggin_id": "12068050",
        "leggin_name": "Legginsy Curve - Szare",
        "leggin_price": 162.0,
        "leggin_rrp": 179.0,
        "sizes": ["XXS", "XS", "S", "M", "L", "XL", "XXL"],
    }

    matched_leggin = list(
        filter(
            lambda leggin: leggin["leggin_id"] == "12068050",
            get_list_of_leggins_from_page(1),
        )
    )
    assert matched_leggin[0] == single_leggin


@pytest.mark.vcr()
def test_get_list_of_leggins_from_nonexisting_page():
    """ Test function when page does not exist """
    assert get_list_of_leggins_from_page(120) == []


@pytest.mark.vcr("tests/cassettes/test_leggins_list/test_get_list_of_leggins.yaml")
def test_get_list_of_leggins():
    """
    Test if leggin from available pages can be found
    in a list of all leggins
    """
    list_of_leggins = get_list_of_leggins()

    leggin_from_first_page = {
        "leggin_id": "12068050",
        "leggin_name": "Legginsy Curve - Szare",
        "leggin_price": 162.0,
        "leggin_rrp": 179.0,
        "sizes": ["XXS", "XS", "S", "M", "L", "XL", "XXL"],
    }

    leggin_from_second_page = {
        "leggin_name": "Dżersejowe Legginsy MP - Danger",
        "leggin_id": "12459914",
        "leggin_price": 119.0,
        "leggin_rrp": 119.0,
        "sizes": ["L", "XL", "XXL"],
    }

    assert leggin_from_first_page in list_of_leggins
    assert leggin_from_second_page in list_of_leggins


@pytest.mark.vcr("tests/cassettes/test_leggins_list/test_get_list_of_leggins.yaml")
def test_store_data():
    """Tests if file with data is created and checks existing of a product"""

    leggin_in_file = {
        "leggin_id": "12068050",
        "leggin_name": "Legginsy Curve - Szare",
        "leggin_price": 162.0,
        "leggin_rrp": 179.0,
        "sizes": ["XXS", "XS", "S", "M", "L", "XL", "XXL"],
    }

    file = store_data("tests/data/test_leggins_list")
    file_path = os.path.abspath(file.name)
    opened_file = open(file_path, "r")
    loaded_elements = json.load(opened_file)

    assert leggin_in_file in loaded_elements


def test_read_data():
    leggin = {
        "leggin_name": "Legginsy siatkowe Power",
        "leggin_id": "11869780",
        "leggin_price": 179.0,
        "leggin_rrp": 179.0,
    }
    leggins_list = read_data("tests/data/test_leggins_list", "04", "06", "2019")
    assert leggins_list[1] == leggin


def test_read_data_with_integer_values():
    leggin = {
        "leggin_name": "Legginsy siatkowe Power",
        "leggin_id": "11869780",
        "leggin_price": 179.0,
        "leggin_rrp": 179.0,
    }
    leggins_list = read_data("tests/data/test_leggins_list", 4, 6, 2019)
    assert leggins_list[1] == leggin


@pytest.mark.django_db
def test_read_data_from_database():
    leggin = Leggin()
    leggin.name = "Legginsy siatkowe Power"
    leggin.external_id = "11869780"
    leggin.price = 179.0
    leggin.rrp = 179.0
    leggin.date = datetime.date(2020, 3, 22)
    leggin.save()
    size = Size()
    size.name = "S"
    size.save()
    leggin.sizes.add(size)

    converted_leggin = {
        "leggin_name": "Legginsy siatkowe Power",
        "leggin_id": 11869780,
        "leggin_price": 179.0,
        "leggin_rrp": 179.0,
        "sizes": ["S"],
    }
    assert read_data_from_database(22, 3, 2020) == [converted_leggin]


@pytest.mark.django_db
def test_read_data_from_database_non_existing_data():
    assert read_data_from_database(22, 3, 2050) == []
