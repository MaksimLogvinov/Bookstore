from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView, CreateView

from apps.cart.cart import Cart
from apps.cart.forms import CartAddProductForm, OrderReverseForm
from apps.cart.services import (
    history_orders,
    update_quantity,
    delete_product_from_cart,
    add_product_in_cart,
)
from apps.orders.models import Orders, ReservationProduct
from apps.orders.services import create_order
from apps.orders.forms import OrderCreateForm


@require_POST
def cart_add(request, product_id):
    add_product_in_cart(
        Cart(request),
        CartAddProductForm(request.POST),
        product_id
    )
    return redirect("cart:cart_detail")


def cart_remove(request, product_id):
    delete_product_from_cart(Cart(request), product_id)
    return redirect("cart:cart_detail")


def cart_detail(request):
    cart = update_quantity(Cart(request))
    return render(
        request,
        "cart/detail.html",
        {"cart": cart, "title": "Корзина"}
    )


class HistoryOrder(ListView):
    model = Orders
    template_name = "cart/history-orders.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context.update(
            history_orders(
                context,
                self.request.user.id,
                self.request.GET.get("page", 1)
            )
        )
        return context


class OrderReserveView(CreateView):
    model = Orders
    template_name = 'cart/history-reserve.html'
    form_class = OrderReverseForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Бронь заказа'
        reserve = ReservationProduct.objects.filter(
            res_user_id=self.request.user
        )
        page_number = self.request.GET.get("page", 1)
        paginator = Paginator(reserve, 10)
        context["posts"] = paginator.page(page_number)
        context["reserve"] = paginator.get_page(page_number)
        return context

    def form_valid(self, form):
        order = create_order(
            self.request.user,
            OrderCreateForm(
                {'ord_description': '-',
                 'ord_address_delivery': '-',
                 'ord_paid': '-'}
            ),
            Cart(self.request),
        )
        ReservationProduct.objects.create(
            res_order_id=order,
            res_user_id=self.request.user,
            res_time_out=form.cleaned_data['res_time_out']
        )

        return redirect('cart:order_reserve')
