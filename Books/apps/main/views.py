from django.views import View
from django.views.generic import DetailView, ListView

from apps.products.models import Categories


class HomePage(ListView):
    template_name = "main/home_page.html"
    model = Categories

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"title": "Начальная страница",
                        'header_text': "Добро пожаловать"})
        return context
