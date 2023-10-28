from django.http import Http404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from services.recommendations.recommendations import get_recommended_products
from .models import Product


@require_http_methods(["GET"])
def product_view(request, product_id):

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404("Product Not Found")
    else:
        recommendations = get_recommended_products(product.id)
        context = {
            "product": product,
            "recommendations": recommendations
        }
    return render(request, "products/product.html", context)
