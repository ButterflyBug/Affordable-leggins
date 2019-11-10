import pytest
from affordable_leggins.leggins_list import get_rrp_from_single_site
from affordable_leggins.leggins_list import get_list_of_leggins_from_page


def test_get_rrp_from_single_site_when_rrp_available():
    """ Test function when rrp found on the website """
    assert get_rrp_from_single_site(11869784) == 159.0


def test_get_rrp_from_single_site_when_rrp_not_available():
    """ Test function when there is no rrp """
    assert get_rrp_from_single_site(12053031) is None


def test_get_rrp_from_single_site_when_leggin_not_available():
    """ Test function when there is no product """
    assert get_rrp_from_single_site(99999999) is None


def test_get_list_of_leggins_from_existing_page():
    """ Test function when page exists """
    single_leggin = {
        'leggin_id': '12068032',
        'leggin_name': 'Legginsy Curve - Czarne',
        'leggin_price': 122.0,
        'leggin_rrp': 159.0
    }
    assert single_leggin in get_list_of_leggins_from_page(1)

def test_get_list_of_leggins_from_nonexisting_page():
    """ Test function when page does not exist """
    assert get_list_of_leggins_from_page(120) == []
