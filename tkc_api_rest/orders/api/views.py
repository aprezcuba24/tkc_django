# Create your views here.
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from tkc_api_rest.orders.models import Order

from .serializers import OrderSerializer


class OrderViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = "pk"

    def get_queryset(self):
        queryset = super().get_queryset()
        package_id = self.request.query_params.get("package_id")
        if package_id:
            queryset = queryset.filter(package_id=package_id)
        return queryset
