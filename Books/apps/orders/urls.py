from django.urls import path

from apps.orders.views import (
    CreateOrderView, PaymentOrderView,
    OrderSuccessView, OrderFailedView)

urlpatterns = [
    path("create/", CreateOrderView.as_view(), name="order_create"),
    path("paid-order/", PaymentOrderView.as_view(), name="paid_order"),
    path("order-success/", OrderSuccessView.as_view(), name="order_success"),
    path("order-failed/", OrderFailedView.as_view(), name="order_failed"),
]
