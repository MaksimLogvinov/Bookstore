import os
from decimal import Decimal

from django.shortcuts import redirect

from apps.orders.models import Orders, OrderItem
from apps.products.models import Products


def payment_order(method, cart, form, user):
    if method == "POST" and form.is_valid():
        create_order(user, form, cart)
        get_cashback(user, cart)
        return redirect("order_success")
    return redirect("order_failed")


def get_cashback(user, cart):
    cashback_percent = int(os.environ.get("cashback_percent")) / 100
    user.user_profile.balance += (
            cart.get_total_price() * Decimal(cashback_percent)
    )
    user.save()


def create_order(user, form, cart):
    update_quantity_prod = []
    order_items = []

    if not form.is_valid():
        raise ValueError("Оформление заказа прервалось")
    order = Orders.objects.create(**form.cleaned_data, ord_user_id=user)
    for item in cart:
        order_items.append(OrderItem(
            ordit_order_id=order,
            ordit_product=item["product"],
            ordit_price=item["price"],
            ordit_quantity=item["quantity"],
        ))
        item["product"].prod_quantity_on_stock -= item["quantity"]
        update_quantity_prod.append(item["product"])

    OrderItem.objects.bulk_create(order_items)
    Products.objects.bulk_update(
        update_quantity_prod,
        fields=["prod_quantity_on_stock"]
    )
    cart.clear()
    return order
