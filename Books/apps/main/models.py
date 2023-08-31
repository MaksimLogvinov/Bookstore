from django.db import models


class Storages(models.Model):
    stor_country = models.CharField(
        verbose_name="Страна хранилища",
        max_length=250
    )
    stor_region = models.CharField(
        verbose_name="Регион хранилища",
        max_length=250
    )
    stor_city = models.CharField(
        verbose_name="Город хранилища",
        max_length=250
    )
    stor_postal_code = models.CharField(
        verbose_name="Почтовый код",
        max_length=12
    )

    class Meta:
        unique_together = ('stor_city', 'stor_region', 'stor_country')
        verbose_name = "Хранилище товаров"
        verbose_name_plural = "Хранилища товаров"
