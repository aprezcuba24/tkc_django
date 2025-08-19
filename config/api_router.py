from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers
from django.urls import path, include
from tkc_api_rest.users.api.views import UserViewSet
from tkc_api_rest.package.api.views import PackageViewSet
from tkc_api_rest.driver.api.views import DriverViewSet
from tkc_api_rest.orders.api.views import OrderViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("packages", PackageViewSet)
orders_router = routers.NestedSimpleRouter(router, r"packages", lookup="package")
orders_router.register(r"orders", OrderViewSet, basename="package-orders")

router.register("drivers", DriverViewSet)


app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
    path("", include(orders_router.urls)),
]
