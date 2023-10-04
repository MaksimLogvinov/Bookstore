from django.contrib import admin

from apps.main.models import Storages


@admin.register(Storages)
class StoragesAdmin(admin.ModelAdmin):
    list_filter = ('stor_country', 'stor_region', 'stor_city',
                   'stor_postal_code')
