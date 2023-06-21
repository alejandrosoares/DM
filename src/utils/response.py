from typing import Any
from enum import Enum
from json import loads

from django.core.serializers import serialize
from django.db.models.query import QuerySet
from django.http import JsonResponse


class StatusResponse(Enum):
    SUCCESS = 'ok'
    FAIL = 'fail'


class ResponseJsonBuilder:
    """Makes a response with default success message"""

    def __init__(self, message: str = 'success', obj: Any = None):
        self._status = StatusResponse.SUCCESS
        self._message = message
        self._obj = obj

    @property
    def status(self) -> StatusResponse:
        return self._status

    @property
    def message(self) -> str:
        return self._message

    @property
    def obj(self) -> Any:
        return self._obj

    @status.setter
    def status(self, status: StatusResponse) -> None:
        self._status = status

    @message.setter
    def message(self, message: str) -> None:
        self._message = message

    @obj.setter
    def obj(self, obj: Any) -> None:
        self._obj = obj

    def set_error_with(self, message: str) -> None:
        self._status = StatusResponse.FAIL
        self.message = message

    def get_response(self, safe=True) -> JsonResponse:
        data = {
            'status': self.status.value,
            'message': self.message,
            'obj': self.obj
        }
        return JsonResponse(data, safe=safe)


def get_dict_from(query: QuerySet, fields: list[str] = None) -> list:
    data = serialize('json', query, fields=fields)
    return loads(data)
