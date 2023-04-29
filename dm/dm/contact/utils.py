from utils.validators import validate_email, validate_phone


def extract_valid_email_or_phone(email_or_phone: str) -> dict:
    valid_email = validate_email(email_or_phone)
    valid_phone = validate_phone(email_or_phone)
    return {
        'email': email_or_phone if valid_email else None,
        'phone': email_or_phone if valid_phone else None,
    }