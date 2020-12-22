from affordable_leggins.leggins_list import get_list_of_leggins


def test_smoke():
    assert len(get_list_of_leggins()) > 0
