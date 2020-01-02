from affordable_leggins.filters import filter_size
from fixtures import (
    leggin_with_size_xs,
    leggin_with_size_s,
    leggin_with_size_m,
    leggins,
)


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
