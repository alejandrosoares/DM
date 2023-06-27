from django.db.models import Q
from django.views.decorators.http import require_http_methods
from django.db.models.query import QuerySet
from django.core.paginator import Paginator
from django.urls import reverse
from django.conf import settings
from django.core.cache import cache

from utils.normalize import normalize_query_string
from utils.response import ResponseJsonBuilder
from utils.cache.constants import CACHE_KEY_MOD_PRODUCTS
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
        products = cache.get_or_set(CACHE_KEY_MOD_PRODUCTS, Product.objects.all())

    products, pagination = get_pagination(request.GET, products)
    products_list = make_list_of(products)
    res_builder.obj = {
        'products': products_list,
        'pagination': pagination
    }
    return res_builder.get_response()


def search_by_category(category_id: str) -> QuerySet:
    try:
        c = Category.objects.get(id=category_id)
    except (Category.DoesNotExist, ValueError):
        products = Product.objects.all()
    else:
        products = c.product_set.all()
    return products


def search_by_words(query: str) -> QuerySet:
    query = normalize_query_string(query)
    products = Product.objects.filter(
        Q(normalized_name__icontains=query) | Q(code__icontains=query)
    )
    return products


def make_list_of(products: QuerySet) -> list[dict]:
    url = settings.DOMAIN
    product_list = []
    for product in products:
        item = {
            'id': product.id,
            'name': product.name,
            'normalizedName': product.normalized_name,
            'price': product.price,
            'code': product.code,
            'img': {
                'url': f'{url}{product.img_small_webp.url}',
                'width': product.img_small_webp.width,
                'height': product.img_small_webp.height
            },
            'productLink': reverse('products:product', kwargs={'product_id': product.id})
        }
        product_list.append(item)
    return product_list


def get_pagination(request_get: dict, query: QuerySet) -> tuple[QuerySet, dict]:
    page_param = request_get.get('page', 1)
    items_param = request_get.get('items', 12)
    paginator = Paginator(query, items_param)
    page = paginator.page(page_param)
    pagination = {
        'page': page_param,
        'hasPrevious': page.has_previous(),
        'hasNext': page.has_next(),
        'numPages': paginator.num_pages
    }
    return page.object_list, pagination
