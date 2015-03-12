from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = "pages/products.html"

    def get_queryset(self):
        return Product.objects.filter(available=True) \
            .select_related('galleries')
