from events import EventListener
from ..events import PackageEvent

class PackageListener(EventListener):
    listensFor = [
        PackageEvent,
    ]

    def handle(self, event):
        if event.event_type == "PACKAGE_DISTRIBUTION":
            print("Package created: ", event.event_type)
