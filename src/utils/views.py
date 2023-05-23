from json import loads

from django.db.models.query import QuerySet
from django.core.serializers import serialize


def get_data_from(request_body: bytes) -> dict:
    """Deserializes request body.
    JSONDecodeError is raised if this method cannot deserialize the argument.
    """
    data = loads(request_body)
    return data


def queryset_to_dict(query: QuerySet, fields: list[str]) -> list[dict]:
    json = serialize('json', query, fields=[*fields])
    return loads(json)
