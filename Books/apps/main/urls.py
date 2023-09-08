from django.urls import path, include

from apps.main.views import HomePage, OurShops

urlpatterns = [
    path(
        "",
        HomePage.as_view(),
        name="home_page"
    ),
    path(
        "catalog/",
        include("apps.categories.urls")
    ),
    path(
        "cart/",
        include(("apps.cart.urls", "apps.cart"), namespace='cart'),
    ),
    path(
        "order/",
        include("apps.orders.urls"),
    ),
    path(
        'user/',
        include("apps.users.urls")
    ),
    path(
        'shops/',
        OurShops.as_view(),
        name='shops'
    ),
    path(
        "product/",
        include('apps.products.urls')
    )
]
