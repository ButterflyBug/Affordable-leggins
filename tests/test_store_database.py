import pytest
import datetime
from affordable_leggins.store import store_data, read_data
from affordable_leggins.storage.models import Leggin
from affordable_leggins.store import store_data_in_database


@pytest.mark.django_db
@pytest.mark.vcr("test_store_at_least_one_leggin_in_database")
def test_store_at_least_one_leggin_in_database():
    store_data_in_database()
    assert Leggin.objects.all().count() != 0


@pytest.mark.django_db
@pytest.mark.vcr("test_store_at_least_one_leggin_in_database")
def test_store_specific_leggin_in_database():
    store_data_in_database()
    assert (
        Leggin.objects.filter(
            name="Legginsy Curve - Czarne",
            price=159.0,
            rrp=159.0,
            external_id="12068032",
            date=datetime.datetime.now(),
        ).count() != 0
    )
