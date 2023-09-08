from django import forms


class OrderCreateForm(forms.Form):
    ord_description = forms.CharField(label="Комментарий")
    ord_address_delivery = forms.CharField(label="Адрес доставки")
    ord_paid = forms.BooleanField(label="Оплачено")
