# Create your views here.
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from tkc_api_rest.package.models import Package

from .serializers import PackageSerializer


class PackageViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = PackageSerializer
    queryset = Package.objects.all()
    lookup_field = "pk"

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).select_related("driver")
