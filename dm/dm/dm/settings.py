from pathlib import Path
import os
import json
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')


ENABLE_AUTOMATIC_CHATBOT = False
DEBUG = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DOMAIN = 'https://b032f1195da6.ngrok.io'
APP_NAME = 'DM'
ALLOWED_HOSTS = ['*']
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
    'home',
    'products',
    'contact',
    'opening',
    'publications',
    'webp_converter',
    'dm',
    'chat',
]

THIRD_PARTY_APPS = []

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
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

LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files
"""
   Cambiar STATICFILE_DIRS antes de realizar el collectstatic y configurar el STATIC_ROOT
   Se toma los archivos estaticos del directorio static que esta en la base del proyecto
"""
STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]


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


# Pagination
INITIAL_START = 0
INITIAL_ITEMS = 8



# OPENAI

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
