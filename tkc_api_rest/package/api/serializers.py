from rest_framework import serializers

from tkc_api_rest.package.models import Package
from tkc_api_rest.driver.models import Driver


class DriverSerializer(serializers.ModelSerializer[Driver]):
    class Meta:
        model = Driver
        fields = ["id", "name", "external_id"]


class PackageSerializer(serializers.ModelSerializer[Package]):
    driver = DriverSerializer(read_only=True)

    class Meta:
        model = Package
        fields = [
            "id",
            "code",
            "created_at",
            "weight",
            "volume",
            "package_type",
            "driver",
        ]
        extra_kwargs = {
            "url": {"view_name": "api:package-detail", "lookup_field": "pk"},
        }
