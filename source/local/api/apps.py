from django.apps import AppConfig


class LocalApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "local.api"
    label = "api"
    verbose_name = ("Api")

