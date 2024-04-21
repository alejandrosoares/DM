from django.http import Http404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Product


@require_http_methods(["GET"])
def product_view(request, product_id):

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404("Product Not Found")
    else:
        context = {
            "product": product,
        }
    return render(request, "products/product.html", context)
