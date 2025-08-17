from events import EventListener
from ..events import PackageEvent
from ..services import create_package


class PackageListener(EventListener):
    listensFor = [
        PackageEvent,
    ]

    def handle(self, event):
        if event.event_type == "PACKAGE_DISTRIBUTION":
            package = create_package(
                event.package_code, event.created_at, event.weight, event.volume
            )
            print("Package created: ", package)
