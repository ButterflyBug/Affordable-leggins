import pytest
from affordable_leggins.leggins_list import get_rrp_from_single_site
from affordable_leggins.leggins_list import get_list_of_leggins_from_page
from affordable_leggins.leggins_list import get_list_of_leggins
from affordable_leggins.store import store_data
import json
import os


@pytest.mark.vcr("tests/cassettes/test_leggins_list/test_get_list_of_leggins.yaml")
def test_get_rrp_from_single_site_when_rrp_available():
    """ Test function when rrp found on the website """
    assert get_rrp_from_single_site(11869784) == 159.0


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
        'leggin_id': '12068032',
        'leggin_name': 'Legginsy Curve - Czarne',
        'leggin_price': 122.0,
        'leggin_rrp': 159.0
    }
    assert single_leggin in get_list_of_leggins_from_page(1)


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
        'leggin_name': 'Legginsy Curve - Czarne',
        'leggin_id': '12068032',
        'leggin_price': 122.0,
        'leggin_rrp': 159.0
    }

    leggin_from_second_page = {
        'leggin_name': 'Bezszwowe legginsy Contrast - Białe',
        'leggin_id': '12016444',
        'leggin_price': 199.0,
        'leggin_rrp': 199.0
    }

    assert leggin_from_first_page in list_of_leggins
    assert leggin_from_second_page in list_of_leggins


@pytest.mark.vcr("tests/cassettes/test_leggins_list/test_get_list_of_leggins.yaml")
def test_store_data():
    """Tests if file with data is created and checks existing of a product"""

    leggin_in_file = {
        "leggin_name": "Legginsy Curve - Czarne",
        "leggin_id": "12068032",
        "leggin_price": 122.0,
        "leggin_rrp": 159.0
    }

    file = store_data()
    file_path = os.path.abspath(file.name)
    opened_file = open(file_path, "r")
    loaded_elements = json.load(opened_file)

    assert leggin_in_file in loaded_elements