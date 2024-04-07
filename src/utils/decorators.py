from functools import wraps


def singleton(callable):
    instances = {}

    @wraps(callable)
    def wrapper(*args, **kwargs):
        if callable not in instances:
            instances[callable] = callable(*args, **kwargs)
        return instances[callable]
    return wrapper
