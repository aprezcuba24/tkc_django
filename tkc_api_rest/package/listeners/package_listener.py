from events import EventListener
from ..events import PackageEvent
from ..services import create_package
from tkc_api_rest.driver.services import create_driver
from tkc_api_rest.orders.services import create_orders
from tkc_api_rest.orders.models import Order
from tkc_api_rest.products.services import create_products


def create_product_by_orders(orders: list, order_instances: list[Order]):
    orders_by_id = {order.code: order for order in order_instances}
    for order in orders:
        create_products(orders_by_id[order["order_code"]], order["products"])


class PackageListener(EventListener):
    listensFor = [
        PackageEvent,
    ]

    def handle(self, event):
        if event.event_type == "PACKAGE_DISTRIBUTION":
            package = create_package(
                event.package_code, event.created_at, event.weight, event.volume
            )
            driver = create_driver(event.driver["driver_id"], event.driver["name"])
            orders = create_orders(package, event.orders)
            create_product_by_orders(event.orders, orders)
