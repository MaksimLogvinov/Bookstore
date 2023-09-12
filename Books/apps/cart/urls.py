from django.urls import path

from apps.cart.views import (
    cart_detail, cart_add, cart_remove, HistoryOrder,
    OrderReserveView)

urlpatterns = [
    path(
        "",
        cart_detail,
        name="cart_detail"
    ),
    path(
        "add/<int:product_id>/",
        cart_add,
        name="cart_add"
    ),
    path(
        "remove/<int:product_id>/",
        cart_remove,
        name="cart_remove"
    ),
    path(
        "history/",
        HistoryOrder.as_view(),
        name="history"
    ),
    path(
        'reserve/',
        OrderReserveView.as_view(),
        name='order_reserve'
    )
]
