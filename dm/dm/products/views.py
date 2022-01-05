# Django
from django.http.response import Http404
from django.shortcuts import render

# Own
from .models import Product


def ProductView(request, product_id):
   """Product View."""

   try:
      product = Product.objects.get(id=product_id)
      context = {"product": product}

   except Product.DoesNotExist:
      raise Http404("Product Not Found")

   return render(request, "products/product.html", context)
