from tkc_api_rest.package.events import PackageEvent

def test_package_listener():
    PackageEvent.Dispatch(
        event_type="PACKAGE_DISTRIBUTION",
        package_code="123",
        orders=[
            {
                "order_code": "123",
                "products": [
                    {
                        "product_id": 1,
                        "name": "Product 1",
                    }
                ]
            }
        ],
        driver={
            "driver_id": 1,
            "name": "John Doe",
        }
    )
    assert 1 == 2