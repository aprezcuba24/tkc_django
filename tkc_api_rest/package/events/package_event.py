from events import Event

class PackageEvent(Event):
    # TODO: In the future we can validate this using Pydantic
    def __init__(self, event_type, package_code, orders, driver):
        self.event_type = event_type
        self.package_code = package_code
        self.orders = orders
        self.driver = driver
