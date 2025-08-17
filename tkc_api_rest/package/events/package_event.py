from events import Event

class PackageEvent(Event):
    def __init__(self, event_type, **kwargs):
        self.event_type = event_type
        self.data = kwargs
        pass
