from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

from apps.cart.forms import CartAddProductForm
from apps.orders.models import Orders
from apps.products.models import Categories
from django.template.defaultfilters import register, floatformat


def add_product_in_cart(cart, form, product_id):
    product = get_object_or_404(Categories, id=product_id)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd["quantity"],
            update_quantity=cd["update"]
        )


def delete_product_from_cart(cart, product_id):
    product = get_object_or_404(Categories, id=product_id)
    cart.remove(product)


def update_quantity(cart):
    for item in cart:
        item["update_quantity_form"] = CartAddProductForm(
            initial={"quantity": item["quantity"], "update": True}
        )
    return cart


@register.filter
def res_price(value, sub):
    if value - sub > 1:
        result = value - sub
    else:
        result = 1
    return result


@register.filter
def discount(sub, value):
    if value - sub > 1:
        result = sub
    else:
        max_disc = sub - value
        result = sub - max_disc - 1
    return result


@register.filter
def float_num(value):
    value = floatformat(value, arg=2)
    return str(value).replace(',', '.')


def history_orders(context, user_id, page_number):
    context.update({"title": "История заказов"})
    orders = Orders.objects.filter(
        ord_user_id=user_id).order_by("-ord_date_created"
                                      )
    paginator = Paginator(orders, 10)
    context["posts"] = paginator.page(page_number)
    context["orders"] = paginator.get_page(page_number)
    return context
