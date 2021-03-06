# Own
from products.models import Product


def get_recommedations_products(categories, exclude_id=None):
    """ Get recommendations products
    @param: products.Category
    @return: list
    """

    initial_list = []
    clean_list = []
    number_of_items = 4

    for c in categories:
        products = c.product_set.all()
        initial_list.extend(products)

    # Clear repeated
    for product in initial_list:
        if product not in clean_list and product.id != exclude_id:
            clean_list.append(product)

    if len(clean_list) > number_of_items:
        clean_list = clean_list[:number_of_items]

    return clean_list
