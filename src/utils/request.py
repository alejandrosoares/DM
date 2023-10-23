from typing_extensions import Self
import requests
from requests.models import Response


class Request:

    def __init__(self, builder):
        self.url = builder.url
        self.data = builder.data
        self.method = builder.method
        self.headers = builder.headers
        self.params = builder.params

    def send(self) -> Response:
        if self.method == 'GET':
            response = requests.get(self.url, params=self.params)
        elif self.method == 'POST':
            response = requests.post(self.url, json=self.data)
        return response

    class Builder:

        def __init__(self, url: str):
            self.url = url
            self.method = 'GET'
            self.params = None
            self.data = None
            self.headers = None

        def with_data(self, data: dict) -> Self:
            self.data = data
            return self

        def with_params(self, params: dict = None) -> Self:
            self.params = params
            return self

        def with_post_method(self) -> Self:
            self.method = 'POST'
            return self

        def build(self) -> Self:
            return Request(self)
