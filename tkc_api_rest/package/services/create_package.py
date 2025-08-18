from tkc_api_rest.package.models import Package
from tkc_api_rest.driver.models import Driver


def create_package(
    package_code: str, created_at: str, weight: int, volume: int, driver: Driver
):
    return Package.objects.create(
        code=package_code,
        created_at=created_at,
        weight=weight,
        volume=volume,
        driver=driver,
    )
