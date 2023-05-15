from urllib.parse import unquote

from django.db.models import Q
from django.views.decorators.http import require_http_methods

from utils.normalize import normalize_text
from utils.response import ResponseJsonBuilder
from products.models import Product, Category


@require_http_methods(["GET"])
def get_categories(request):
    res_builder = ResponseJsonBuilder()
    categories = Category.objects.filter(enable=True)
    res_builder.obj = categories
    return res_builder.get_response()


@require_http_methods(["GET"])
def get_products_view(request):
    res_builder = ResponseJsonBuilder()
    category_id = request.GET.get('category', False)
    query = request.GET.get('query', False)
    
    if category_id:
        products = search_by_category(category_id)
    elif query:
        products = search_by_words(query)
    else:
        products = Product.objects.all()

    products = convert_to_dict(products, request.get_host())
    res_builder.obj = {'products': products}
    return res_builder.get_response()


def search_by_category(category_id):

    try:
        if category_id != "0":
            c = Category.objects.get(id=category_id)
            products = c.product_set.all()
        else:
            products = Product.objects.all()

    except (Category.DoesNotExist, ValueError):
        products = []

    return products


def search_by_words(query):
    query = unquote(query)
    query = normalize_text(query)

    products = Product.objects.filter(
        Q(normalized_name__icontains=query) |
        Q(code__icontains=query) 
    )

    return products


def convert_to_dict(products, domain):

    product_list = []
    append = product_list.append

    for p in products:

        product = {
            "id": p.id,
            "name": p.name,
            "normalized_name": p.normalized_name,
            "price": p.price,
            "code": p.code,
            "img": f"http://{domain}{p.img_small_webp.url}"
        }

        append(product)

    return product_list