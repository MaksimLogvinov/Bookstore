from django.urls import path

from apps.categories.views import (
    magazine_catalog_view, show_books_view,
    show_magazines_view, show_textbooks_view,
    SearchResultView,
)

urlpatterns = [
    path(
        "",
        magazine_catalog_view,
        name="magazine_catalog"
    ),
    path(
        "books/",
        show_books_view,
        name="books"
    ),
    path(
        "magazines/",
        show_magazines_view,
        name="magazines"
    ),
    path(
        "textbooks/",
        show_textbooks_view,
        name="textbooks"
    ),
    path(
        "search/",
        SearchResultView.as_view(),
        name="search"
    ),
]
