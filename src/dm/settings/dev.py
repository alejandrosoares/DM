from .base import *


DOMAIN = "http://localhost:8000"

DEBUG = True

ALLOWED_HOSTS = ['*']

# MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

INSTALLED_APPS += ['debug_toolbar']

INTERNAL_IPS = [
    '127.0.0.1',
]

CACHE_TIMEOUT = 3600 * 24 * 7  # one week
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",
        "KEY_PREFIX": "DM",
    }
}
