from django.test import TestCase

from utils.validators import (
    validate_email_or_phone,
    validate_email,
    validate_phone,
)
from utils.test.constants import (
    VALID_EMAILS,
    INVALID_EMAILS,
    VALID_PHONES,
    INVALID_PHONES
)


class TestsUtilsValidators(TestCase):

    def setUp(self) -> None:
        self.valid_emails = VALID_EMAILS
        self.invalid_emails = INVALID_EMAILS
        self.valid_phones = VALID_PHONES
        self.invalid_phones = INVALID_PHONES

    def test_validate_email_with_valid_email(self):
        for valid_email in self.valid_emails:
            self.assertTrue(validate_email(valid_email))

    def test_validate_email_with_invalid_email(self):
        for invalid_email in self.invalid_emails:
            self.assertFalse(validate_email(invalid_email))

    def test_validate_phone_with_valid_phone(self):
        for valid_phone in self.valid_phones:
            self.assertTrue(validate_phone(valid_phone))

    def test_validate_phone_with_invalid_phone(self):
        for invalid_phone in self.invalid_phones:
            self.assertFalse(validate_phone(invalid_phone))

    def test_validate_email_or_phone_with_valid_email_or_phone(self):

        for valid_email in self.valid_emails:
            self.assertTrue(validate_email_or_phone(valid_email))

        for valid_phone in self.valid_phones:
            self.assertTrue(validate_email_or_phone(valid_phone))

    def test_validate_email_or_phone_with_invalid_email_and_phone(self):

        for invalid_email in self.invalid_emails:
            self.assertFalse(validate_email_or_phone(invalid_email))

        for invalid_phone in self.invalid_phones:
            self.assertFalse(validate_email_or_phone(invalid_phone))
