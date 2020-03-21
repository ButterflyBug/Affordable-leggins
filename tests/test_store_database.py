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
from fixtures import leggin_with_size_xs, leggin_with_size_s


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
        ).count()
        != 0
    )


@mock.patch("affordable_leggins.store.get_list_of_leggins")
@pytest.mark.django_db
def test_store_leggin_with_its_size(mocked_get_list_of_leggins, leggin_with_size_xs):
    mocked_get_list_of_leggins.return_value = [leggin_with_size_xs]
    store_data_in_database()
    first_leggin = Leggin.objects.all()[0]

    assert first_leggin.sizes.all()[0].name == "XS"


@mock.patch("affordable_leggins.store.get_list_of_leggins")
@pytest.mark.django_db
def test_store_leggin_with_more_than_one_size(
    mocked_get_list_of_leggins, leggin_with_size_s
):
    mocked_get_list_of_leggins.return_value = [leggin_with_size_s]
    store_data_in_database()
    first_leggin = Leggin.objects.all()[0]

    assert first_leggin.sizes.all()[0].name == "S"
    assert first_leggin.sizes.all()[1].name == "M"
