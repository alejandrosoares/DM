import os
import re
from collections import namedtuple

from django.conf import settings
from django.core.cache import cache

from utils.cache.constants import CACHE_KEY_FN_STATICFILES_CONTEXT


StaticLink = namedtuple('StaticLink', ['var_name', 'filename'])
CSS_FILES = [
    StaticLink('static_main_css_url', 'compressed_main_css'),
    StaticLink('static_home_css_url', 'compressed_home_css'),
]


def staticfiles_context(request):
    context = cache.get_or_set(CACHE_KEY_FN_STATICFILES_CONTEXT, _get_context)
    return context


def _get_context():
    context = {}
    for file in CSS_FILES:
        context[file.var_name] = _get_compress_url_of(file.filename, 'css')
    return context


def _get_compress_url_of(filename: str, type: str) -> str:
    file_url = ''
    pattern = r"^{}.*\.{}$".format(filename, type)
    dir = _get_compress_dir(type)
    files = os.listdir(dir)
    for file in files:
        match = re.match(pattern, file)
        if match:
            compress_url = _get_compress_url()
            file_url = f'{compress_url}{type}/{file}'
            break
    return file_url


def _get_compress_dir(type: str) -> str:
    compressed_output_dir = settings.COMPRESS_OUTPUT_DIR
    static_root = settings.STATIC_ROOT
    compress_dir = os.path.join(static_root, compressed_output_dir)
    return os.path.join(compress_dir, type)


def _get_compress_url() -> str:
    static = settings.STATIC_URL
    compress = settings.COMPRESS_OUTPUT_DIR
    return f'{static}{compress}'
