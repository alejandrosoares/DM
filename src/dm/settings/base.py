from pathlib import Path
import os
from dotenv import load_dotenv


load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent.parent


SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'invalid-secret-key')

DEBUG = True
ENABLE_AUTOMATIC_CHATBOT = False
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
APP_NAME = 'DM'
ADMINS = [('Alejandro', 'soaresalejandro@outlook.com')]
MANAGERS = [('Alejandro', 'soaresalejandro@outlook.com')]


DJANGO_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'app_context',
    'home',
    'products',
    'contact',
    'opening',
    'dm',
    'chat',
    'questions'
]

THIRD_PARTY_APPS = [
    'webp_converter',
    'compressor'
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
]

ROOT_URLCONF = 'dm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'webp_converter.context_processors.webp_support',
                'app_context.processors.staticfiles.staticfiles_context',
                'app_context.processors.chat.chat_context',
                'app_context.processors.cache.cache_context'
            ],
        },
    },
]

ASGI_APPLICATION = 'dm.asgi.application'
WSGI_APPLICATION = 'dm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Zurich'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')


# Media Files

MEDIA_FOLDER = 'media'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / MEDIA_FOLDER


# Email

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')


# Bitly

BITLY_API_KEY = os.getenv('BITLY_API_KEY')
BITLY_URL = 'https://api-ssl.bitly.com/v4/bitlinks'


# Security

'''
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
'''


# OPENAI

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'invalid-token')


# DJANGO COMPRESSOR

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_ENABLED = True
COMPRESS_OUTPUT_DIR = 'compress/'
COMPRESS_CSS_HASHING_METHOD = 'content'
COMPRESS_OUTPUT_FILENAME = 'base.{extension}'
COMPRESS_REBUILD_TIMEOUT = 3600 * 24 * 365  # one year
COMPRESS_FILTERS = {
    'css': [
        'compressor.filters.css_default.CssAbsoluteFilter',
        'compressor.filters.cssmin.rCSSMinFilter',
    ],
    'js': [
        'compressor.filters.jsmin.JSMinFilter',
    ]
}
HTML_MINIFY = True
KEEP_COMMENTS_ON_MINIFYING = False


# REDIS

REDIS_USER = os.getenv('REDIS_USER',)
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')


API_VERSION = 'v1'


DEFAULT_RECOMMENDATIONS_PRODUCT = 4
