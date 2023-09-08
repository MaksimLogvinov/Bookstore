from django.urls import path

from apps.orders.views import CreateOrderView, PaymentOrderView

urlpatterns = [
    path("create/", CreateOrderView.as_view(), name="order_create"),
    path("paid-order/", PaymentOrderView.as_view(), name="paid_order"),
]
