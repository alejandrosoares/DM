from django.test import TestCase

from utils.test.constants import (
    VALID_EMAILS, 
    VALID_PHONES,
    INVALID_EMAILS,
    INVALID_PHONES
)
from contact.utils import extract_valid_email_or_phone


class ContactViewTestCase(TestCase):

    def setUp(self) -> None:
        self.valid_emails = VALID_EMAILS
        self.invalid_emails = INVALID_EMAILS
        self.valid_phones = VALID_PHONES
        self.invalid_phones = INVALID_PHONES

    def test_extract_email_or_phone_with_valid_email_or_phone(self):

        for valid_email in self.valid_emails:
            result = extract_valid_email_or_phone(valid_email)
            self.assertIsNotNone(result.get('email'))
            self.assertIsNone(result.get('phone'))

        for valid_phone in self.valid_phones:
            result = extract_valid_email_or_phone(valid_phone)
            self.assertIsNotNone(result.get('phone'))
            self.assertIsNone(result.get('email'))

    def test_extract_email_or_phone_with_invalid_email_and_phone(self):

        for invalid_email in self.invalid_emails:
            result = extract_valid_email_or_phone(invalid_email)
            self.assertIsNone(result.get('email'))
            self.assertIsNone(result.get('phone'))

        for invalid_phone in self.invalid_phones:
            result = extract_valid_email_or_phone(invalid_phone)
            self.assertIsNone(result.get('phone'))
            self.assertIsNone(result.get('phone'))
