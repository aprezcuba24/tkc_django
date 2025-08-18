from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from tkc_api_rest.users.api.views import UserViewSet
from tkc_api_rest.package.api.views import PackageViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("packages", PackageViewSet)


app_name = "api"
urlpatterns = router.urls
