from django.apps import AppConfig


class PackageConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tkc_api_rest.package"

    def ready(self):
        import tkc_api_rest.package.listeners
