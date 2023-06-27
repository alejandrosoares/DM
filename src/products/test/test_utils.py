from django.test import TestCase


class ProductsUtilsTestCase(TestCase):
    pass
    # def setUp(self):
    #     self.categories = [Mock(), Mock(), Mock()]
    #     self.exclude_id = 1
    #     self.max_items = 4

    # def test_returns_product_list(self):
    #     result = get_products(self.categories, self.exclude_id, self.max_items)
    #     self.assertIsInstance(result, list)
    #     for item in result:
    #         self.assertIsInstance(item, Product)

    # def test_products_not_in_exclude_id(self):
    #     result = get_products(self.categories, self.exclude_id, self.max_items)
    #     for product in result:
    #         self.assertNotEqual(product.id, self.exclude_id)

    # def test_max_items(self):
    #     result = get_products(self.categories, self.exclude_id, self.max_items)
    #     self.assertLessEqual(len(result), self.max_items)

    # def test_empty_categories_returns_empty(self):
    #     result = get_products([], self.exclude_id, self.max_items)
    #     self.assertEqual(result, [])
