from django.db.models.query import QuerySet
from django.db.models import Q

from products.models import Product


# TODO: Cache
def get_recommended_products_of(
    product: Product,
    size: int = 4
) -> list[Product]:
    excluded_id = product.id
    categories = product.categories.filter(enable=True)
    recommended = set()
    
    for c in categories:
        recommended.update(c.product_set.all().exclude(id=excluded_id))

    if len(recommended) < size:
        excluded_ids = _get_excluded_ids(recommended, excluded_id)
        amount = size - len(recommended)
        extra_products = _get_extra_products(excluded_ids, amount)
        recommended.update(extra_products)
        
    return list(recommended)[:size]


def _get_extra_products(excluded_ids: list[int], amount: int) -> list[Product]:
    extra_products = Product.objects.filter(~Q(id__in=excluded_ids))
    return extra_products[:amount]


def _get_excluded_ids(recommended: list[Product], excluded_id: int) -> list[int]:
    excluded_ids = [r.id for r in recommended]
    excluded_ids.append(excluded_id)
    return excluded_ids
