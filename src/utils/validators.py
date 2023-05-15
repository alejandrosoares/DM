import re

from django.core.validators import RegexValidator

from utils.constants import REGEX_EMAIL, REGEX_PHONE


def validate_email_or_phone(email_or_phone: str) -> bool:
    valid_email = validate_email(email_or_phone)
    valid_phone = validate_phone(email_or_phone)
    return valid_email or valid_phone


def validate_email(email: str) -> bool:
    return True if re.search(REGEX_EMAIL, email) else False


def validate_phone(phone: str) -> bool:
    return True if re.search(REGEX_PHONE, phone) else False


phone_validator = RegexValidator(
    regex = REGEX_PHONE,
    message = "Format: +549999999999 o 549999999999 up to 16 digits."
)