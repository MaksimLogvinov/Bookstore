from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView

from apps.cart.cart import Cart
from apps.cart.forms import CartAddProductForm
from apps.cart.services import (
    history_orders,
    update_quantity,
    delete_product_from_cart,
    add_product_in_cart,
)
from apps.orders.models import Orders


@require_POST
def cart_add(request, product_id):
    add_product_in_cart(Cart(request), CartAddProductForm(request.POST), product_id)
    return redirect("cart:cart_detail")


def cart_remove(request, product_id):
    delete_product_from_cart(Cart(request), product_id)
    return redirect("cart:cart_detail")


def cart_detail(request):
    cart = update_quantity(Cart(request))
    return render(request, "cart/detail.html", {"cart": cart})


class MoreInfo(ListView):
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
