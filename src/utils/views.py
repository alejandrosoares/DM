from json import loads


def get_data_from(request_body: bytes) -> dict:
    """Deserializes request body. 
    JSONDecodeError is raised if this method cannot deserialize the argument.
    """
    data = loads(request_body)
    return data
