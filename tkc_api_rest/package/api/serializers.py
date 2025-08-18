from rest_framework import serializers

from tkc_api_rest.package.models import Package


class PackageSerializer(serializers.ModelSerializer[Package]):
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
