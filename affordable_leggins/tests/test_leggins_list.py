import pytest
from affordable_leggins.leggins_list import get_rrp_from_single_site


def test_get_rrp_from_single_site_when_rrp_available():
    """ Test function when rrp found on the website """
    assert get_rrp_from_single_site(11869784) == 159.0

def test_get_rrp_from_single_site_when_rrp_not_available():
    """ Test function when there is no rrp """
    assert get_rrp_from_single_site(12053031) is None 

def test_get_rrp_from_single_site_when_leggin_not_available():
    """ Test function when there is no product """
    assert get_rrp_from_single_site(99999999) is None 

