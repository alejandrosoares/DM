from django.db.models import QuerySet
from django.core.cache import cache
from django.conf import settings

from utils.cache.recommendations import get_cache_recommendation_key_of
from products.models import Product
from .api_fetch import fetch_recommended_products


def get_recommended_products(product_id: int, limit: int = None) -> QuerySet:
    limit = settings.MICROSERVICES["DM_REC"]["DEFAULT_LIMIT"] if limit is None else limit
    if settings.MICROSERVICES["DM_REC"]["ENABLED"]:
        return _get_from_microservice(product_id, limit)
    return _get_random_products(product_id, limit)


def _get_from_microservice(product_id: int, limit: int) -> list[int]:
    cache_key = get_cache_recommendation_key_of(product_id, limit)
    recommended_id_list = cache.get(cache_key)
    if recommended_id_list is None:
        recommended_id_list = fetch_recommended_products(product_id, limit)
        cache.set(cache_key, recommended_id_list)
    products = Product.objects.filter(id__in=recommended_id_list)
    return products


def _get_random_products(product_id: int, limit: int) -> QuerySet:
    product_id_list = Product.objects.values_list('id', flat=True).exclude(id=product_id)
    products = Product.objects.filter(id__in=product_id_list)[:limit]
    return products
