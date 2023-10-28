from django.db.models import QuerySet
from django.core.cache import cache
from django.conf import settings

from datetime import datetime
from requests.models import Response

from utils.request import Request
from utils.cache.recommendations import get_cache_recommendation_key_of
from products.models import Product
from .constants import URL_DMREC_SERVICE_PRODUCTS
from .authentication import AuthRecommendationService


def get_recommended_products(product_id: int) -> QuerySet:
    limit = settings.DEFAULT_RECOMMENDATIONS_PRODUCT
    cache_key = get_cache_recommendation_key_of(product_id, limit)
    recommended_id_list = cache.get(cache_key)
    if recommended_id_list is None:
        recommended_id_list = _fetch_recommended_products(product_id, limit)
        cache.set(cache_key, recommended_id_list)
    products = Product.objects.filter(id__in=recommended_id_list)
    return products


def _fetch_recommended_products(product_id: int, limit: int) -> list[int]:
    response = _get_response(product_id, limit)
    if response.status_code == 200:
        recommended_id_list = response.json().get('recommendations')
        return recommended_id_list
    return []


def _get_response(product_id: int, limit:int) -> Response:
    params = {'product_id': product_id, 'limit': limit}
    headers = _get_headers()
    request = Request.Builder(URL_DMREC_SERVICE_PRODUCTS) \
        .with_headers(headers) \
        .with_params(params) \
        .build()
    response = request.send()
    return response

def _get_headers() -> dict:
    token = _get_auth_token_for_service()
    return {'Authorization': f'Bearer {token}'}


def _get_auth_token_for_service() -> str:
    now = datetime.now()
    auth = AuthRecommendationService()
    token = auth.get_token()

    is_expired = token.expiry_time > now
    if is_expired:
        token = auth.refresh_and_get_token()
    return token.value