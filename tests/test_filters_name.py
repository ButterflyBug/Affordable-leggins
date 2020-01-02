from affordable_leggins.filters import filter_name
from fixtures import (
    leggin_with_size_xs,
    leggin_with_size_s,
    leggin_with_size_m,
    leggins,
)


def test_filter_names(leggins, leggin_with_size_xs):
    name = "Bezszwowe"
    assert leggin_with_size_xs not in filter_name(leggins, name, reject=True)


def test_filter_other_names(leggins, leggin_with_size_s):
    name = "Power Curve"
    assert leggin_with_size_s not in filter_name(leggins, name, reject=True)


def test_filter_included_names(leggins, leggin_with_size_s):
    name = "Power Curve"
    assert leggin_with_size_s in filter_name(leggins, name, reject=False)
