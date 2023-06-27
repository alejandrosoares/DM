from django.test import TestCase, Client
from django.urls import reverse

from products.test.test_models import create_product


class ProductsViewTestCase(TestCase):

    def setUp(self):
        self.product = create_product()
        self.client = Client()
        self.url = reverse("products:product", kwargs={'product_id': self.product.id})

    # TODO: make the mock of product's image
    # def test_get_product(self):
    #     res = self.client.get(self.url)
    #     self.assertEqual(res.status_code, 200)
