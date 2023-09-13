from django import forms

from apps.orders.models import ReservationProduct


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
        label="Кол-во",
        initial=1,
        widget=forms.NumberInput(attrs={"class": "quantity"}),
    )
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )


class DiscountForm(forms.Form):
    discount_check = forms.BooleanField(initial=False, required=False)


class OrderReverseForm(forms.ModelForm):

    class Meta:
        model = ReservationProduct
        fields = ('res_time_out',)
