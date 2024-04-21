from django.conf import settings


def get_limit(request_get: dict) -> int:
    limit = request_get.get('limit')
    try:
        limit = int(limit)
    except ValueError:
        limit = settings.MICROSERVICES["DM_REC"]["DEFAULT_LIMIT"]
    return limit
