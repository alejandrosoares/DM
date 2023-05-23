from urllib.parse import unquote


INVALID_CHARACTERS = (
    ("á", "a"),
    ("é", "e"),
    ("í", "i"),
    ("ó", "o"),
    ("ú", "u"),
)


def normalize_text(text: str) -> str:
    """Replaces special characters and capitalizes the text"""

    for pair in INVALID_CHARACTERS:
        text = text.replace(*pair)

    return text.upper()


def normalize_query_string(query_string: str) -> str:
    query = unquote(query_string)
    query = normalize_text(query)
    return query
