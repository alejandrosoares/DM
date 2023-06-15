from django.core.cache import cache


def cache_view(key: str):
    def fn_wrapper(fn):
        def wrapper(*args, **kwargs):
            res = res = cache.get(key)
            if not res:
                res = fn(*args, **kwargs)
                res = cache.set(key, res)
            return res
        return wrapper
    return fn_wrapper
