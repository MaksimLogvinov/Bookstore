from django.apps import AppConfig
from django.utils.translation import gettext


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.products'
    verbose_name = 'Каталог товаров'
