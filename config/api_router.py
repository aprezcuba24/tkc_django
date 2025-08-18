from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from tkc_api_rest.users.api.views import UserViewSet
from tkc_api_rest.package.api.views import PackageViewSet
from tkc_api_rest.driver.api.views import DriverViewSet
from tkc_api_rest.orders.api.views import OrderViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register(
    "packages/(?P<package_id>[^/.]+)/orders", OrderViewSet, basename="package-orders"
)
router.register(
    "orders", OrderViewSet
)  # Keep the original endpoint for backward compatibility
router.register("packages", PackageViewSet)
router.register("drivers", DriverViewSet)


app_name = "api"
urlpatterns = router.urls
