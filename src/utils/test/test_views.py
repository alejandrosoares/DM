from json import dumps
from json.decoder import JSONDecodeError

from django.test import TestCase

from utils.views import (
    get_data_from,
)
from utils.test.constants import (
    VALID_EMAILS,
    INVALID_EMAILS,
    VALID_PHONES,
    INVALID_PHONES
)


class TestsUtilsViews(TestCase):

    def setUp(self) -> None:
        self.valid_emails = VALID_EMAILS
        self.invalid_emails = INVALID_EMAILS
        self.valid_phones = VALID_PHONES
        self.invalid_phones = INVALID_PHONES

    def test_get_data_from_with_valid_data(self):
        data = {"name": "John", "age": 30}
        request_body = dumps(data).encode('utf-8')
        extracted_data = get_data_from(request_body)
        self.assertEqual(extracted_data, data)

    def test_get_data_from_with_invalid_data(self):
        with self.assertRaises(JSONDecodeError):
            malformed_json = b'{"name": "John", "age": 30'
            _ = get_data_from(malformed_json)
