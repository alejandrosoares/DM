from requests.models import Response

from utils.request import Request
from .constants import URL_DMREC_SERVICE_PRODUCTS
from .authentication import AuthRecommendationService


def fetch_recommended_products(product_id: int, limit: int) -> list[int]:
    response = _get_response(product_id, limit)
    if response.status_code == 200:
        recommended_id_list = response.json().get('recommendations')
        return recommended_id_list
    return []


def _get_response(product_id: int, limit: int) -> Response:
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
    auth = AuthRecommendationService()
    token = auth.get_token()
    return token.value
