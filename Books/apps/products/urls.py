from apps.products.views import ProductInfoView


from django.urls import path

urlpatterns = [
    path(
        'info/<slug:prod_slug>/',
        ProductInfoView.as_view(),
        name='product_info'
    )
]
