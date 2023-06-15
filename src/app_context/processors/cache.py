from django.conf import settings
from django.core.cache import cache

from utils.cache.constants import CACHE_KEY_FN_CACHE_CONTEXT


def cache_context(request):
    context = cache.get_or_set(CACHE_KEY_FN_CACHE_CONTEXT, _get_context)
    return context


def _get_context():
    context = {
        'CACHE_TIMEOUT': settings.CACHE_TIMEOUT
    }
    return context
