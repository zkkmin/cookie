from django.template.defaultfilters import slugify

import factory
import factory.fuzzy

from ..models import Product


class ProductFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))
    price = factory.fuzzy.FuzzyDecimal(90000)
    image = factory.django.ImageField(color='blue')
    
    class Meta:
        model = Product
    