# Django
from django.http import Http404, JsonResponse
from django.shortcuts import render

# Own
from .models import Product, Category
from .utils.views import get_recommedations_products


def ProductsView(request):
    """ Products View.
    Get Product JSON list
    @return: json
    """
    DOMAIN = request.get_host()
    product_list = []
    products = Product.objects.all()

    category_id = request.GET.get('category', False)

    if category_id:
        try:
            c = Category.objects.get(id=category_id)

            products = products.filter(category__id=c.id)

        except (Category.DoesNotExist, ValueError):
            pass

    for p in products:
        product = {
            "id": p.id,
            "name": p.name,
            "normalized_name": p.normalized_name,
            "price": p.price,
            "code": p.code,
            "img": f"http://{DOMAIN}{p.img.url}"
        }
        product_list.append(product)

    return JsonResponse(product_list, safe=False)


def ProductView(request, product_id):
    """Product View."""

    try:
        product = Product.objects.get(id=product_id)
        categories = product.category.all()
        recommendations = get_recommedations_products(categories)

        context = {
            "product": product,
            "recommendations": recommendations
        }

    except Product.DoesNotExist:
        raise Http404("Product Not Found")

    return render(request, "products/product.html", context)
