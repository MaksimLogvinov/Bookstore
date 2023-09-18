from django.shortcuts import render
from django.views.generic import ListView

from apps.categories.filters import BooksFilter, \
    TextbooksFilter, MagazinesFilter
from apps.categories.services import (
    show_categories,
    categories
)
from apps.products.models import Books, TextBooks, Magazines
from apps.products.models import Products


class SearchResultView(ListView):
    model = Products
    template_name = "categories/categories.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Поиск товара"
        page_number = self.request.GET.get("page", 1)
        query = self.request.GET.get("search_prod")
        context = categories(
            page_number,
            self.request.GET,
            self.request.user,
            data=query,
        )
        return context


def magazine_catalog_view(request):
    page_number = request.GET.get("page", 1)
    context = categories(
        page_number,
        request.GET,
        request.user
    )
    return render(
        request,
        "categories/categories.html",
        context=context
    )


def show_books_view(request):
    page_number = request.GET.get("page", 1)
    filter_res = BooksFilter(request.GET, queryset=Books.objects.all())
    context = show_categories(page_number, filter_res)
    return render(
        request,
        "categories/categories.html",
        context=context
    )


def show_magazines_view(request):
    page_number = request.GET.get("page", 1)
    filter_res = MagazinesFilter(request.GET, queryset=Magazines.objects.all())
    context = show_categories(page_number, filter_res)
    return render(
        request,
        "categories/categories.html",
        context=context
    )


def show_textbooks_view(request):
    page_number = request.GET.get("page", 1)
    filter_res = TextbooksFilter(request.GET, queryset=TextBooks.objects.all())
    context = show_categories(page_number, filter_res)
    return render(
        request,
        "categories/categories.html",
        context=context
    )
