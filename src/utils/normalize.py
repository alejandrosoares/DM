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
