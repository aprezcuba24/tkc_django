from events import EventListener
from ..events import PackageEvent

class PackageListener(EventListener):
    listensFor = [
        PackageEvent,
    ]

    def handle(self, event):
        print("Package created: ", event.event_type, event.data)
