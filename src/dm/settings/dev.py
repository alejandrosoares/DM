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
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_USER}:{REDIS_PASSWORD}@localhost:6379/0",
        "TIMEOUT": CACHE_TIMEOUT,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "cache"
    }
}
