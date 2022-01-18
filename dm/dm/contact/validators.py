import re
REGEX_EMAIL = "^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$"
REGEX_PHONE = r"\+?1?\d{9,16}$"


def validate_email(email):
    """Validate Email
    @param: str
    @return: bool
    """

    if re.search(REGEX_EMAIL, email):
        return True

    return False


def validate_phone(phone):
    """Validate Phone
    @param: str
    @return: bool
    """

    if re.search(REGEX_PHONE, phone):
        return True

    return False
