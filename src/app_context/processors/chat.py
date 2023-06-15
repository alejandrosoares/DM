from django.conf import settings
from django.core.cache import cache

from utils.cache.constants import CACHE_KEY_FN_CHAT_CONTEXT


def chat_context(request):
    context = cache.get_or_set(CACHE_KEY_FN_CHAT_CONTEXT, _get_context)
    return context


def _get_context():
    context = {
        'ENABLE_AUTOMATIC_CHATBOT': settings.ENABLE_AUTOMATIC_CHATBOT
    }
    return context
