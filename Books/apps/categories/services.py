from django.core.paginator import Paginator
from django.db.models import Q, Avg
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import register
from django.views.generic import CreateView

from apps.cart.forms import CartAddProductForm
from apps.products.models import Categories
from apps.categories.filters import CategoriesFilter


def base_data():
    context = {
        "count": 0,
        "cat": Categories.objects.order_by("prod_year_publication"),
        "cart_product_form": CartAddProductForm(),
    }
    return context


def search_magazine(query):
    context = {"title": "Поиск товара"}
    if query is None:
        object_list = Categories.objects.all()
    else:
        object_list = Categories.objects.filter(
            Q(prod_title__icontains=query) or Q(prod_slug__icontains=query)
        )
    context["prod"] = object_list
    context.update(context["prod"])
    return context


def magazine_catalog(page_number, get):
    context = base_data()
    context["cat_selected"] = 0
    prod = Categories.objects.order_by("prod_year_publication")
    paginator = Paginator(prod, 20)
    context["posts"] = paginator.page(page_number)
    context["prod"] = paginator.get_page(page_number)
    filter_res = CategoriesFilter(get, queryset=prod)
    context['filter'] = filter_res.qs
    context['form'] = filter_res.form
    return context


def show_categories(page_number, filter_res):
    context = base_data()
    paginator = Paginator(filter_res.qs, 20)
    context["posts"] = paginator.page(page_number)
    context["prod"] = paginator.get_page(page_number)
    context['filter'] = filter_res.qs
    context['form'] = filter_res.form
    return context


@register.filter
def rating(h, key):
    return h[key]
