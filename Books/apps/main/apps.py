from django.apps import AppConfig
from django.utils.translation import gettext


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.main'
    verbose_name = 'Общее'
