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
        self.auth = builder.auth

    def send(self) -> Response:
        if self.method == 'GET':
            response = requests.get(self.url, params=self.params, headers=self.headers)
        elif self.method == 'POST':
            response = requests.post(
                self.url, 
                data=self.data, 
                headers=self.headers,
                auth=self.auth
            )
        return response

    class Builder:

        def __init__(self, url: str):
            self.url = url
            self.method = 'GET'
            self.params = None
            self.data = None
            self.headers = None
            self.auth = None

        def with_data(self, data: dict) -> Self:
            self.data = data
            return self
        
        def with_auth(self, auth: tuple) -> Self:
            self.auth = auth
            return self

        def with_headers(self, headers: dict = None) -> Self:
            self.headers = headers
            return self

        def with_params(self, params: dict = None) -> Self:
            self.params = params
            return self

        def with_post_method(self) -> Self:
            self.method = 'POST'
            return self

        def build(self) -> Self:
            return Request(self)
