from decimal import Decimal
import os

from django.test import TestCase

from products.models import upload_to, Product


def create_product(name: str = None, price: Decimal = None) -> Product:
    name = name or 'Toy'
    price = price or Decimal(10)
    product = Product.objects.create(name=name, price=price)
    return product


class ProductsModelTestCase(TestCase):

    def setUp(self) -> None:
        self.product = create_product()

    def test_upload_to(self):
        product_code = 1
        expected_path = os.path.join('img', 'products', f'{product_code}/')
        self.assertEqual(upload_to(product_code), expected_path)

    def test_create_code(self):
        expected_code = 1
        self.assertEqual(self.product.code, expected_code)

    def test_capitalize_name(self):
        name = 'toy'
        product = create_product(name)
        self.assertEqual(product.name, name.upper())
