import pytest
import datetime
import mock
from affordable_leggins.store import (
    store_data,
    read_data,
    store_data_in_database,
    get_list_of_leggins,
)
from affordable_leggins.storage.models import Leggin
from fixtures import leggin_with_size_xs


@mock.patch("affordable_leggins.store.get_list_of_leggins")
@pytest.mark.django_db
def test_store_at_least_one_leggin_in_database(
    mocked_get_list_of_leggins, leggin_with_size_xs
):
    mocked_get_list_of_leggins.return_value = [leggin_with_size_xs]
    store_data_in_database()
    assert Leggin.objects.all().count() != 0


@mock.patch("affordable_leggins.store.get_list_of_leggins")
@pytest.mark.django_db
def test_store_specific_leggin_in_database(
    mocked_get_list_of_leggins, leggin_with_size_xs
):
    mocked_get_list_of_leggins.return_value = [leggin_with_size_xs]
    store_data_in_database()
    assert (
        Leggin.objects.filter(
            name="Bezszwowe",
            price=40.0,
            rrp=159.0,
            external_id="11871452",
            date=datetime.datetime.now(),
        ).count() != 0
    )
