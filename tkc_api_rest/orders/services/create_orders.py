from tkc_api_rest.orders.models import Order
from tkc_api_rest.package.models import Package


def create_orders(package: Package, orders: list):
    order_instances = [
        Order(
            code=order["order_code"],
            created_at=order["created_at"],
            weight=order["weight"],
            volume=order["volume"],
            package=package,
        )
        for order in orders
    ]
    return Order.objects.bulk_create(order_instances)
