import pytest
from tkc_api_rest.package.events import PackageEvent
from tkc_api_rest.package.models import Package


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
    assert package is not None
