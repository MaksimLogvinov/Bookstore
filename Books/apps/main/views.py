from datetime import datetime, timedelta

from django.utils.translation import gettext
from django.views.generic import ListView

from apps.main.models import Storages
from apps.orders.models import ReservationProduct
from apps.products.models import Products


class HomePage(ListView):
    template_name = "main/home_page.html"
    model = Products

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"title": gettext("Начальная страница"),
                        'header_text': gettext("Добро пожаловать")})

        (ReservationProduct.objects
         .filter(res_time_out__lte=datetime.now()-timedelta(days=1)).delete())
        return context


class OurShops(ListView):
    model = Products
    template_name = "main/our_shops.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"title": gettext("Наши магазины")})


class ContactSupportView(ListView):
    model = Storages
    template_name = 'main/contact_support.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты и поддержка'
        return context
