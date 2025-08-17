from events import EventListener
from ..events import OrderEvent


class OrderListener(EventListener):
    listensFor = [
        OrderEvent,
    ]

    def handle(self, event):
        print("Order created: ", event.event_type, event.data)
