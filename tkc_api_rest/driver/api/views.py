# Create your views here.
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from tkc_api_rest.driver.models import Driver

from .serializers import DriverSerializer


class DriverViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()
    lookup_field = "pk"
