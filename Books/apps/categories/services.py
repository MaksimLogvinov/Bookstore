from datetime import date

from django.core.paginator import Paginator
from django.db.models import Q
from django.template.defaultfilters import register

from apps.cart.forms import CartAddProductForm
from apps.categories.filters import CategoriesFilter
from apps.products.models import Categories


def base_data():
    context = {
        "cart_product_form": CartAddProductForm(),
    }
    return context


def categories(page_number, get, user=None, data=None):
    context = base_data()
    context["cat_selected"] = 0
    today = date.today()
    prod = Categories.objects.order_by("prod_year_publication")
    if not user.is_anonymous and user.user_profile.birth_date:
        birth_date = user.user_profile.birth_date
        user_age = (today.year - birth_date.year
                    - ((today.month, today.day) < (birth_date.month, birth_date.day)))
        prod = prod.filter(prod_age_restriction__lte=user_age)
    if data:
        prod = prod.filter(
            Q(prod_title__icontains=data) or Q(slug__icontains=data)
        )
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
