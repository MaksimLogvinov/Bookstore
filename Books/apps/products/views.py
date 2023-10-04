from django.views.generic import DetailView

from apps.products.models import Products
from apps.cart.forms import CartAddProductForm


class ProductInfoView(DetailView):
    template_name = "products/product_info.html"
    slug_url_kwarg = "prod_slug"
    model = Products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Информация о {context['categories'].prod_title}"
        context["cart_product_form"] = CartAddProductForm()
        context['photos'] = context['categories'].photos.select_related()
        return context
