# products/urls.py

from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
        url(
            regex=r'^$',
            view=TemplateView.as_view(
                template_name='products/products_list.html'
                ),
            name='list'
        ),
        url(
            regex=r'^(?P<pk>\d+)/(?P<slug>[-_\w]+)/',
            view=TemplateView.as_view(
                template_name='products/product_detail.html'
                ),
            name='detail'
        ),
    ]