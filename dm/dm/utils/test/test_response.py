from json import loads

from django.test import TestCase
from django.http import JsonResponse

from utils.response import StatusResponse, ResponseJsonBuilder


class TestsUtilsValidators(TestCase):

    def setUp(self) -> None:
        self.response_builder = ResponseJsonBuilder()

    def test_response_builder_type(self):
        response = self.response_builder.get_response()
        self.assertTrue(isinstance(response, JsonResponse))

    def test_response_builder_with_success_status(self):
        response = self.response_builder.get_response()
        data = loads(response.content)
        self.assertEqual(data['status'], StatusResponse.SUCCESS.value)
        self.assertEqual(data['message'], 'success')
        self.assertIsNone(data['obj'])
    
    def test_response_builder_with_custom_message(self):
        self.response_builder.message = 'Custom message'
        response = self.response_builder.get_response()
        data = loads(response.content)
        self.assertEqual(data['status'], StatusResponse.SUCCESS.value)
        self.assertEqual(data['message'], 'Custom message')
        self.assertIsNone(data['obj'])

    def test_response_builder_with_obj(self):
        self.response_builder.obj = { 'chatId': 1234}
        response = self.response_builder.get_response()
        data = loads(response.content)
        self.assertEqual(data['status'], StatusResponse.SUCCESS.value)
        self.assertEqual(data['message'], 'success')
        self.assertEqual(data['obj']['chatId'], 1234)

    def test_response_builder_with_failed_status(self):
        self.response_builder.set_error_with('Error message')
        response = self.response_builder.get_response()
        data = loads(response.content)
        self.assertEqual(data['status'], StatusResponse.FAIL.value)
        self.assertEqual(data['message'], 'Error message')


