from django.apps import AppConfig
from django.utils.translation import gettext


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.orders'
    verbose_name = 'Заказы и история'
