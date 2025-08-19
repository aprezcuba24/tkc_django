# Create your views here.
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from django.utils.functional import cached_property
from django.shortcuts import get_object_or_404
from tkc_api_rest.package.models import Package
from tkc_api_rest.orders.models import Order

from .serializers import OrderSerializer

class OrderViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = "pk"

    @cached_property
    def package(self) -> Package:
        if "package_pk" in self.kwargs:
            return get_object_or_404(Package, pk=self.kwargs["package_pk"])

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.package:
            queryset = queryset.filter(package_id=self.package.id)
        return queryset
