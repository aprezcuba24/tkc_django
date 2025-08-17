import pytest
from tkc_api_rest.package.events import PackageEvent
from tkc_api_rest.package.models import Package
from tkc_api_rest.driver.models import Driver
from tkc_api_rest.orders.models import Order


@pytest.mark.django_db
def test_package_listener():
    PackageEvent.Dispatch(
        event_type="PACKAGE_DISTRIBUTION",
        package_code="123",
        created_at="2025-08-17 16:06:22",
        weight=10,
        volume=10,
        orders=[
            {
                "order_code": "123",
                "created_at": "2025-08-17 16:06:22",
                "weight": 10,
                "volume": 10,
                "products": [
                    {
                        "product_id": 1,
                        "name": "Product 1",
                    }
                ],
            }
        ],
        driver={
            "driver_id": 1,
            "name": "John Doe",
        },
    )
    package = Package.objects.get(code="123")
    driver = Driver.objects.get(external_id=1)
    assert package is not None
    assert driver is not None
    assert len(Order.objects.filter(package=package)) == 1
