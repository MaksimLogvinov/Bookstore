from django.apps import AppConfig
from django.utils.translation import gettext


class CategoriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.categories'
    verbose_name = 'Категория'
