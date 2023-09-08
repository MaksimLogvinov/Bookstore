from django import forms


class SearchCatalogForm(forms.Form):
    Text = forms.CharField()
