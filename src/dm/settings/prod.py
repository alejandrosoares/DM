from .base import *


DOMAIN = "http://custom.domain.com"

DEBUG = False

ALLOWED_HOSTS = [DOMAIN]

STATIC_ROOT = BASE_DIR / 'static_root'


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
