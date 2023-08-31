from django.core.validators import validate_slug
from django.db import models

from apps.main.models import Storages


class Photos_product(models.Model):
    photo_link = models.TextField(verbose_name="Фото товара")


class ActiveProduct(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(prod_is_active=True)


class Categories(models.Model):
    prod_title = models.CharField(
        verbose_name="Название товара",
        max_length=200,
    )
    prod_description = models.TextField(
        verbose_name="Описание товара",
        max_length=500
    )
    prod_slug = models.SlugField(
        verbose_name="Слаг товара",
        validators=[validate_slug]
    )
    prod_price = models.DecimalField(
        verbose_name="Цена товара",
        max_digits=6,
        decimal_places=3
    )
    prod_photo_id = models.ForeignKey(
        Photos_product,
        verbose_name="Фото товара",
        on_delete=models.CASCADE
    )
    prod_number_pages = models.IntegerField(
        verbose_name="Кол-во страниц"
    )
    prod_author = models.CharField(
        verbose_name="Автор",
        max_length=200
    )
    prod_year_publication = models.DateField(
        verbose_name="Год публикации",
    )
    prod_quantity_on_stock = models.IntegerField(
        verbose_name="Количество на складе",
    )
    prod_storage_id = models.ManyToManyField(
        Storages,
        verbose_name="Хранилище товара",
    )
    prod_is_active = models.BooleanField(
        default=True,
        verbose_name="Есть в продаже"
    )

    active_objects = ActiveProduct()

    class Meta:
        verbose_name = "Категория товаров"
        verbose_name_plural = "Категории товаров"


class Genres(models.Model):
    genre_name = models.CharField(
        verbose_name="Название жанра",
        max_length=200
    )
    genre_description = models.TextField(
        verbose_name="Описание жанра",
        max_length=500
    )


class Books(Categories):
    book_genre = models.ForeignKey(
        Genres,
        verbose_name="Жанр книги",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class Classes(models.Model):
    class_type = models.CharField(
        verbose_name="Для каких классов",
        max_length=200
    )


class TextBook(Categories):
    textbook_class = models.ForeignKey(
        Classes,
        verbose_name="Учебники",
        on_delete=models.Model
    )

    class Meta:
        verbose_name = "Учебник"
        verbose_name_plural = "Учебники"


class Magazines(Categories):
    magazine_genre = models.ForeignKey(
        Genres,
        verbose_name="Жанр журнала",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Журнал"
        verbose_name_plural = "Журналы"
