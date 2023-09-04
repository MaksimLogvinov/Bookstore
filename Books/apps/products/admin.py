from django.contrib import admin

from apps.products.models import Categories, Books, Magazines, Photos_product


class ProdStorageInline(admin.TabularInline):
    model = Categories.prod_storage_id.through
    extra = 3


@admin.register(Photos_product)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_link']


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ["id", "prod_title", "prod_description", "prod_slug",
                    "prod_price", "prod_photo_id", "prod_number_pages",
                    "prod_author", "prod_year_publication",
                    "prod_quantity_on_stock", "get_tag", "prod_is_active"]
    inlines = [ProdStorageInline]
    list_filter = ('id', 'prod_is_active')

    def get_tag(self, instance):
        return [tag.stor_country for tag in instance.prod_storage_id.all()]


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ["categories_ptr_id", "book_genre"]


@admin.register(Magazines)
class MagazinesAdmin(admin.ModelAdmin):
    list_display = ["categories_ptr_id", "magazine_genre"]
