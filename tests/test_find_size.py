import pytest
from affordable_leggins.leggins_list import find_size


AVAILABLE_SIZES = ["XXS", "XS", "S", "M", "L", "XL", "XXL"]


@pytest.mark.vcr()
def test_find_size():
    leggin_id = "12068050"
    assert find_size(leggin_id) == AVAILABLE_SIZES


@pytest.mark.vcr()
def test_find_one_limited_size():
    leggin_other_id = "12605008"
    assert find_size(leggin_other_id) == ["L", "XXL"]


@pytest.mark.vcr()
def test_find_no_size():
    leggin_id = "0"
    assert find_size(leggin_id) is None
