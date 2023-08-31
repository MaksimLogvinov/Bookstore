from django.db import models

from apps.users.models import CustomUser
from apps.products.models import Categories


class Orders(models.Model):
    ord_user_id = models.ForeignKey(
        CustomUser,
        verbose_name="Номер пользователя",
        on_delete=models.CASCADE
    )
    ord_date_created = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now=True,
    )
    ord_description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
        max_length=300
    )
    ord_address_delivery = models.CharField(
        verbose_name="Адрес доставки",
        blank=False,
        max_length=150
    )
    ord_paid = models.BooleanField(
        verbose_name="Оплачено",
        default=False
    )

    class Meta:
        ordering = ("-ord_date_created",)
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.linkorder.all())


class OrderItem(models.Model):
    ordit_order_id = models.ForeignKey(
        Orders,
        related_name="linkorder",
        on_delete=models.CASCADE
    )
    ordit_product = models.ForeignKey(
        Categories,
        related_name='ordprod',
        on_delete=models.CASCADE
    )
    ordit_price = models.DecimalField(
        verbose_name="Цена",
        max_digits=8,
        decimal_places=2
    )
    ordit_quantity = models.PositiveIntegerField(
        verbose_name="Количество",
        default=1
    )

    def get_cost(self):
        return self.ordit_price * self.ordit_quantity

    class Meta:
        verbose_name = "Предметы заказа"
        verbose_name_plural = "Предметы заказов"
