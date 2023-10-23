from django.test import TestCase

import requests
from unittest.mock import patch, Mock

from utils.request import Request


class TestRequest(TestCase):

    def setUp(self) -> None:
        self.url = 'https://jsonplaceholder.typicode.com/todos/1'
        self.mock_response = {
            'id': 1,
            'title': 'delectus aut autem',
            'completed': False
        }
        self.mock_data = {'title': 'foo', 'body': 'bar', 'userId': 1}
        self.mock_params = {'page': 1, 'items': 10}

    def test_with_data(self):
        request = Request.Builder(self.url).with_data(
            self.mock_data).with_post_method().build()
        self.assertEqual(request.data, self.mock_data)

    def test_with_params(self):
        request = Request.Builder(self.url).with_params(self.mock_params).build()
        self.assertEqual(request.params, self.mock_params)

    def test_send_get_request(self):
        request = Request.Builder(self.url).build()
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = self.mock_response
        with patch.object(requests, 'get', return_value=response_mock) as mock_method:
            response = request.send()
            mock_method.assert_called_once_with(self.url, params=None)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), self.mock_response)

    def test_send_post_request(self):
        builder = Request.Builder(self.url).with_data(self.mock_data).with_post_method()
        request = builder.build()
        response_mock = Mock()
        response_mock.status_code = 201
        response_mock.json.return_value = self.mock_response
        with patch.object(requests, 'post', return_value=response_mock) as mock_method:
            response = request.send()
            mock_method.assert_called_once_with(self.url, json=self.mock_data)
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json(), self.mock_response)
