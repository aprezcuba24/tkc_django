import pytest
from tkc_api_rest.driver.services import create_driver
from tkc_api_rest.driver.models import Driver


@pytest.mark.django_db
def test_create_driver():
    driver = create_driver(1, "John Doe")
    assert driver is not None
    driver_2 = create_driver(1, "John Doe")
    assert driver_2 is not None
    assert driver == driver_2
    assert len(Driver.objects.all()) == 1
