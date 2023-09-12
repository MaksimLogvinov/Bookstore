from django.shortcuts import redirect

from apps.orders.models import Orders, OrderItem
from apps.products.models import Categories


def payment_order(method, cart, form, user):
    if method == "POST" and form.is_valid():
        create_order(user, form, cart)
        return redirect('order_success')
    return redirect('order_failed')


def create_order(user, form, cart):
    form.is_valid()
    obj = Orders()
    obj.ord_user_id = user
    obj.ord_description = form.cleaned_data["ord_description"]
    obj.ord_address_delivery = form.cleaned_data["ord_address_delivery"]
    obj.ord_paid = form.cleaned_data["ord_paid"]
    obj.save()

    for item in cart:
        OrderItem.objects.create(
            ordit_order_id=obj,
            ordit_product=item["product"],
            ordit_price=item["price"],
            ordit_quantity=item["quantity"],
        )
        product = Categories.objects.get(id=item['product'].id)
        product.prod_quantity_on_stock -= item['quantity']
        product.save()
    cart.clear()
    return obj
