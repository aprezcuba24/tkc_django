from tkc_api_rest.driver.models import Driver


def create_driver(driver_id: str, name: str):
    if Driver.objects.filter(external_id=driver_id).exists():
        return Driver.objects.get(external_id=driver_id)
    return Driver.objects.create(external_id=driver_id, name=name)
