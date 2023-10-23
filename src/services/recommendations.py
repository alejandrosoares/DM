from django.db.models import QuerySet
from django.core.cache import cache
from django.conf import settings

from utils.request import Request
from utils.cache.recommendations import get_cache_recommendation_key_of
from products.models import Product


URL_RECOMMENDATIONS_SERVICE = 'http://localhost:8001/api/v1/products'


def get_recommended_products(product_id: int) -> QuerySet:
    limit = settings.DEFAULT_RECOMMENDATIONS_PRODUCT
    cache_key = get_cache_recommendation_key_of(product_id, limit)
    recommended_id_list = cache.get_or_set(
        cache_key, fetch_recommended_products(
            product_id, limit
        )
    )
    products = Product.objects.filter(id__in=recommended_id_list)
    return products


def fetch_recommended_products(product_id: int, limit: int) -> list[int]:
    params = {'product_id': product_id, 'limit': limit}
    request = Request.Builder(URL_RECOMMENDATIONS_SERVICE) \
        .with_params(params) \
        .build()
    response = request.send()
    if response.status_code == 200:
        recommended_id_list = response.json().get('recommendations')
        return recommended_id_list
    return []
