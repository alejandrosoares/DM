REGEX_EMAIL = "^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$"
REGEX_PHONE = r"\+?1?\d{9,16}$"

import re

def validate_email(email):

    if re.search(REGEX_EMAIL, email):
        return True

    return False


def validate_phone(phone):

    if re.search(REGEX_PHONE, phone):
        return True

    return False
