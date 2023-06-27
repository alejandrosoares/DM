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


# Logging

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
    },
    "formatters": {
        "verbose": {
            "format": "{levelname} - {asctime} - {name} - {process:d} - {thread:d} - {message}",
            "style": "{",
        },
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "filters": ["require_debug_false"],
        },
        "file_error": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": "../logs/error.log",
            "formatter": "verbose"
        },
    },
    "loggers": {
        "mail_admins": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "error": {
            "handlers": ["file_error"],
            "level": "ERROR",
            "propagate": True,
        },
    },
    "root": {
        "handlers": ["file_error"],
        "level": "WARNING",
    },
}
