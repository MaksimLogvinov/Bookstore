from django.views.generic import CreateView

from apps.cart.cart import Cart
from apps.orders.forms import OrderCreateForm
from apps.orders.services import order_create


class CreateOrderView(CreateView):
    form_class = OrderCreateForm
    template_name = "orders/create_order.html"

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        context = {"cart": Cart(self.request)}

    def post(self, request, *args, **kwargs):
        return None


class PaymentOrderView(CreateView):
    form_class = OrderCreateForm
    template_name = "orders/creation_order.html"

    def get_context_data(self, **kwargs):
        context = {'title': "Оплата заказа"}
        return context

    def post(self, request, *args, **kwargs):
        result = order_create(
            request.method,
            Cart(request),
            OrderCreateForm(request.POST),
            request.user
        )
        return result
