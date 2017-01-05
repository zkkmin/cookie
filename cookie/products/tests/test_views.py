from django.test import RequestFactory

from test_plus.test import TestCase

from ..views import ProductListView


class TestProductListView(TestCase):
    
    def test_some_view(self):
        # response = self.get_check_200('products:list')
        request = self.factory.get('/products/list/')
        response = ProductListView.as_view(request)
        self.assertEqual(response.status_code, 200)