def normalize_text(text):
    """ Normalize text
    Replace accent mark and convert to upper case

    @param: str
    @return: str
    """
    text = text.replace("á", "a").replace("é", "e").replace(
        "í", "i").replace("ó", "o").replace("ú", "u")

    text = text.replace("Á", "A").replace("É", "E").replace(
        "Í", "I").replace("Ó", "O").replace("Ú", "U")

    return text.upper()
