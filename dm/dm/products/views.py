# Django
from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.db.models import Q

# Own
from .models import Product, Category
from .utils.views import get_recommedations_products
from user_information.models import Queries
from utils.normalize import normalize_text


def search_by_category(category_id):
    """Search by category
    @param: str
    @return: QuerySet or list
    """

    try:
        if category_id != "0":
            c = Category.objects.get(id=category_id)
            products = Product.objects.filter(category__id=c.id)
        else:
            products = Product.objects.all()

    except (Category.DoesNotExist, ValueError):
        products = []

    return products


def search_by_words(query):
    """Search by category
    @param: str
    @return: QuerySet
    """
    print(query)

    Queries.objects.create(query=query)

    query = normalize_text(query)

    products = Product.objects.filter(
        Q(normalized_name__icontains=query) | Q(
            code__icontains=query) | Q(brand_name__icontains=query)
    )

    return products


def conver_to_dic(products, domain):
    """Convert list or QuerySet to list of diccionaries
    @param: QuerySet or list, str
    """

    product_list = []

    for p in products:
        product = {
            "id": p.id,
            "name": p.name,
            "normalized_name": p.normalized_name,
            "price": p.price,
            "code": p.code,
            "img": f"http://{domain}{p.img.url}"
        }
        product_list.append(product)

    return product_list


def ProductsView(request):
    """ Products View.

    Get Product JSON list
    @return: json
    """

    category_id = request.GET.get('category', False)
    query = request.GET.get('query', False)

    if category_id:
        products = search_by_category(category_id)
    elif query:
        products = search_by_words(query)
    else:
        products = Product.objects.all()

    products = conver_to_dic(products, request.get_host())

    return JsonResponse(products, safe=False)


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
