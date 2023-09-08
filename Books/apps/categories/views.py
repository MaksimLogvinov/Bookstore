from django.shortcuts import render
from django.views.generic import ListView

from apps.products.models import Books, TextBooks, Magazines, Photos_product
from apps.categories.services import (
    search_magazine,
    show_categories,
    magazine_catalog
)
from apps.products.models import Categories
from apps.categories.filters import CategoriesFilter, BooksFilter, \
    TextbooksFilter, MagazinesFilter


class SearchResultView(ListView):
    model = Categories
    template_name = "catalog/search.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        query = self.request.GET.get("search_prod")
        context = search_magazine(query)
        return context


def magazine_catalog_view(request):
    page_number = request.GET.get("page", 1)
    context = magazine_catalog(page_number, request.GET)
    return render(
        request,
        "categories/categories.html",
        context=context
    )


def show_books_view(request):
    page_number = request.GET.get("page", 1)
    filter_res = BooksFilter(request.GET, queryset=Books.objects.all())
    context = show_categories(page_number, filter_res)
    print(context)
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
