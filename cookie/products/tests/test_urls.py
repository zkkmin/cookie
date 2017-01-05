from django.core.urlresolvers import reverse, resolve

from test_plus import TestCase


class TestProductURLs(TestCase):
    """Test URL patterns for products app."""
    
    def test_list_reverse(self):
        """products:list should reverse to '/products/."""
        self.assertEqual(reverse('products:list'), '/products/')
        
    def test_list_resolve(self):
        """/products/ should resolve to 'products:list'."""
        self.assertEqual(resolve('/products/').view_name, 'products:list')
        
    def test_detail_reverse(self):
        """products:detail should reverse to '/products/1/first-product/'."""
        self.assertEqual(reverse('products:detail',
                                    kwargs={'pk': 1, 'slug': 'first-product'}),
                                    '/products/1/first-product/'
                        )
    
    def test_detail_resolve(self):
        """ /products/1/first-product/ should resolve to 'products:detail'."""
        self.assertEqual(resolve('/products/1/first-products/').view_name,
                            'products:detail')
                        