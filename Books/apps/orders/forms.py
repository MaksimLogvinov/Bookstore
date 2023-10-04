from django import forms

from apps.orders.models import Orders


class OrderCreateForm(forms.ModelForm):
    ord_description = forms.CharField(label="Комментарий")
    ord_address_delivery = forms.CharField(label="Адрес доставки")
    ord_paid = forms.BooleanField(label="Оплачено", required=False)
    ord_price = forms.DecimalField(label='Итоговая сумма', required=False)
    ord_discount = forms.DecimalField(label='Скидка', required=False)

    class Meta:
        model = Orders
        fields = (
            'ord_description',
            'ord_address_delivery',
            'ord_paid',
            'ord_price',
            'ord_discount'
        )
