import django_filters

from apps.products.models import Categories, Books, Magazines, TextBooks


class CategoriesFilter(django_filters.FilterSet):
    class Meta:
        model = Categories
        fields = {
            'prod_price': ['lt', 'gt'],
            'prod_is_active': ['exact'],
            'prod_author': ['icontains'],
            'prod_year_publication': ["lt", 'gt']
        }


class BooksFilter(django_filters.FilterSet):
    class Meta:
        model = Books
        fields = {
            'prod_price': ['lt', 'gt'],
            'prod_is_active': ['exact'],
            'prod_author': ['icontains'],
            'prod_year_publication': ["lt", 'gt'],
            'book_genre': ['exact']
        }


class MagazinesFilter(django_filters.FilterSet):
    class Meta:
        model = Magazines
        fields = {
            'prod_price': ['lt', 'gt'],
            'prod_is_active': ['exact'],
            'prod_author': ['icontains'],
            'prod_year_publication': ["lt", 'gt'],
            'magazine_genre': ['exact']
        }


class TextbooksFilter(django_filters.FilterSet):
    class Meta:
        model = TextBooks
        fields = {
            'prod_price': ['lt', 'gt'],
            'prod_is_active': ['exact'],
            'prod_author': ['icontains'],
            'prod_year_publication': ["lt", 'gt'],
            'textbook_class': ['exact']
        }
