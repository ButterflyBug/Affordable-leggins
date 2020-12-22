from pyannotate_runtime import collect_types
from affordable_leggins.filters import filter_size
from fixtures import (
    leggin_with_size_xs,
    leggin_with_size_s,
    leggin_with_size_m,
    leggins,
)


collect_types.init_types_collection()


def test_filter_size(leggins, leggin_with_size_s):
    collect_types.start()
    assert leggin_with_size_s in filter_size(leggins, "S")


def test_filter_other_size(leggins, leggin_with_size_m):
    assert leggin_with_size_m in filter_size(leggins, "M")


def test_filter_non_existing_size(leggins):
    assert filter_size(leggins, "XL") == []


def test_filter_other_non_existing_size(leggins):
    assert filter_size(leggins, "L") == []


def test_filter_leggins_with_multiple_sizes(leggins, leggin_with_size_s):
    assert leggin_with_size_s in filter_size(leggins, "S")
    collect_types.stop()
    collect_types.dump_stats("annotations")
