from test_plus.test import TestCase

from ..models import Product
from .factories import ProductFactory


class TestProduct(TestCase):

    def test__str__(self):
        product = ProductFactory()
        self.assertEqual(
            product.__str__(), 
            product.title
            )