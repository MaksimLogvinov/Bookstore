from django import forms

from apps.products.models import Categories


class SearchResultForm(forms.ModelForm):
    search_prod = forms.CharField()

    class Meta:
        model = Categories
        fields = ('prod_title',)
