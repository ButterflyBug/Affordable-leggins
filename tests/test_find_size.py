from affordable_leggins.leggins_list import find_size


AVAILABLE_SIZES = ["XS", "S", "M", "L", "XL"]


def test_find_size():
    leggin_id = "12068044"
    assert find_size(leggin_id) == AVAILABLE_SIZES


def test_find_one_limited_size():
    leggin_other_id = "12016456"
    assert find_size(leggin_other_id) == ["XS", "S", "M"]


def test_find_no_size():
    leggin_id = "0"
    assert find_size(leggin_id) is None
