from django.apps import AppConfig
from django.utils.translation import gettext


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'
    verbose_name = 'Пользователи'
