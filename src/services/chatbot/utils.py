from django.conf import settings


def get_persist_directory() -> str:
    return str(settings.MEDIA_ROOT / 'vectorstores')
