from tkc_api_rest.package.models import Package


def create_package(package_code: str, created_at: str, weight: int, volume: int):
    return Package.objects.create(
        code=package_code, created_at=created_at, weight=weight, volume=volume
    )
