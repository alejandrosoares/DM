from django.core.cache import cache
from django.conf import settings

import re

from .constants import CACHE_PREFIX_RECOMMENDATIONS_PRODUCTS


def get_cache_recommendation_key_of(product_id: int, limit: int) -> str:
    return f'{CACHE_PREFIX_RECOMMENDATIONS_PRODUCTS}:{product_id}:{limit}'


def delete_all_cache_recommendations(version: int = 1):
    keys_to_delete = _get_all_recommendations_keys(version)
    cache.delete_many(keys_to_delete)


def _get_all_recommendations_keys(version: int) -> list[str]:
    regex = _get_regex(version)
    len_key_prefix = _get_prefix_len(version)
    keys = list(cache._cache.keys())
    keys_to_delete = [key[len_key_prefix:] for key in keys if re.match(regex, key)]
    return keys_to_delete


def _get_regex(version: int) -> str:
    regex = r'^{}:{}:{}:\d+:\d+$'.format(
        settings.CACHES['default']['KEY_PREFIX'],
        version,
        CACHE_PREFIX_RECOMMENDATIONS_PRODUCTS
    )
    return regex


def _get_prefix_len(version: int) -> int:
    key_prefix = f'{settings.CACHES["default"]["KEY_PREFIX"]}:{version}:'
    len_key_prefix = len(key_prefix)
    return len_key_prefix
