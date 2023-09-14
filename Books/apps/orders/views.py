from django.views.generic import CreateView, ListView

from apps.cart.cart import Cart
from apps.orders.forms import OrderCreateForm
from apps.orders.models import Orders
from apps.orders.services import payment_order


class CreateOrderView(CreateView):
    form_class = OrderCreateForm
    template_name = "orders/create_order.html"
    model = Orders

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"cart": Cart(self.request)})
        return context


class PaymentOrderView(CreateView):
    form_class = OrderCreateForm
    template_name = "orders/creation_order.html"

    def get_context_data(self, **kwargs):
        context = {'title': "Оплата заказа"}
        return context

    def post(self, request, *args, **kwargs):
        result = payment_order(
            request.method,
            Cart(request),
            OrderCreateForm(request.POST),
            request.user
        )
        return result


class OrderSuccessView(ListView):
    model = Orders
    template_name = 'orders/order_success.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Заказ оформлен'
        return context


class OrderFailedView(ListView):
    model = Orders
    template_name = 'orders/order_failed.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Оформление заказа отклонено'
        return context
