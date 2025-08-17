from events import Event


class OrderEvent(Event):
    def __init__(self, event_type, **kwargs):
        self.event_type = event_type
        self.data = kwargs
        pass
