from rest_framework import serializers

from tkc_api_rest.driver.models import Driver


class DriverSerializer(serializers.ModelSerializer[Driver]):
    class Meta:
        model = Driver
        fields = [
            "id",
            "name",
            "external_id",
        ]

        extra_kwargs = {
            "url": {"view_name": "api:driver-detail", "lookup_field": "pk"},
        }
