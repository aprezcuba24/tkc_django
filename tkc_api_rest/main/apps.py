from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tkc_api_rest.main'
    def ready(self):
        import tkc_api_rest.main.listeners
