from django.utils.translation import gettext
from django.views.generic import ListView

from apps.products.models import Categories


class HomePage(ListView):
    template_name = "main/home_page.html"
    model = Categories

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"title": gettext("Начальная страница"),
                        'header_text': gettext("Добро пожаловать")})
        return context


class OurShops(ListView):
    model = Categories
    template_name = "main/our_shops.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"title": gettext("Наши магазины")})
