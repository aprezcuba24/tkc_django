from events import EventListener
from ..events import PackageEvent
from ..services import create_package
from tkc_api_rest.driver.services import create_driver
from tkc_api_rest.orders.services import create_orders


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
            create_orders(package, event.orders)
