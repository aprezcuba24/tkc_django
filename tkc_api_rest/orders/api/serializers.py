from rest_framework import serializers

from tkc_api_rest.orders.models import Order


class OrderSerializer(serializers.ModelSerializer[Order]):
    class Meta:
        model = Order
        fields = [
            "id",
            "code",
            "created_at",
            "weight",
            "volume",
        ]

        extra_kwargs = {
            "url": {"view_name": "api:order-detail", "lookup_field": "pk"},
        }
