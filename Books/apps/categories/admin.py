from django.contrib import admin

from apps.products.models import GenresBooks, GenresMagazines, ClassesTextbooks


@admin.register(GenresBooks)
class GenresAdmin(admin.ModelAdmin):
    list_display = ["id", "genre_name", "genre_description"]


@admin.register(GenresMagazines)
class GenresAdmin(admin.ModelAdmin):
    list_display = ["id", "genre_name", "genre_description"]


@admin.register(ClassesTextbooks)
class ClassesAdmin(admin.ModelAdmin):
    list_display = ["id", "class_type"]
