from apps.orders.models import Orders, OrderItem


def order_create(method, cart, form, user):
    if method == "POST" and form.is_valid():
        obj = Orders()
        obj.user = user
        obj.description = form.cleaned_data["description"]
        obj.deliv_address = form.cleaned_data["deliv_address"]
        obj.paid = form.cleaned_data["paid"]
        obj.save()

        for item in cart:
            OrderItem.objects.create(
                order=obj,
                product=item["product"],
                price=item["price"],
                quantity=item["quantity"],
            )
        cart.clear()
        return True
    return False
