from redislite import StrictRedis
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = ')3zf)0_e+pivts3l0i*82*-&y2%v!132x^85tvywvmnlr%4-pw'

DEBUG = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DOMAIN = "http"

ALLOWED_HOSTS = ['*']
ADMINS = [('Alejandro','soaresalejandro@outlook.com')]
MANAGERS = [('Alejandro','soaresalejandro@outlook.com')]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_user_agents',
    'attention',
    'home',
    'products',
    'contact',
    'vendors',
    'user_information',
    'webp_converter',
]


# Redislite

redis_connection = StrictRedis('/tmp/cache.db')


CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': "unix://@%s" %(redis_connection.socket_file, ),
    }
}

#   Tiempo de vida de la cache 365 dias x 24 horas x 60 minutos x 60 segundos: 31536000
#   Si el valor es 0 la cache expira inmediantamente
#   Si el valor en None no expira nunca
CACHE_TTL = None

USER_AGENTS_CACHE = 'default'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
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

WSGI_APPLICATION = 'dm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

'''
    Cambiar STATICFILE_DIRS antes de realizar el collectstatic y configurar el STATIC_ROOT
    Se toma los archivos estaticos del directorio static que esta en la base del proyecto
'''
STATICFILES_DIRS = [
    BASE_DIR / 'static',
    # BASE_DIR / 'contact/static'
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

'''
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
'''
TOKEN_BITLY = '3792d49cc9a9c03651536c5420eadbf0fc0bd8a2'
DOMAIN = 'https://b032f1195da6.ngrok.io'